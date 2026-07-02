# -*- coding: utf-8 -*-
from odoo.tests import tagged
from odoo.addons.sale_stock.tests.common import TestSaleStockCommon

@tagged('post_install', '-at_install')
class TestSOStockBalanceCorrector(TestSaleStockCommon):

    def setUp(self):
        super().setUp()
        
        # Create a storable product
        self.product = self.env['product.product'].create({
            'name': 'Test Stock Balancing Product',
            'type': 'consu', # Type 'consu' in modern Odoo handles stock moves if it has routes
            # Note: in Odoo 19 consu behaves similarly to storable in terms of moves creation
            'is_storable': True, 
        })
        
        # Add stock
        self.env['stock.quant']._update_available_quantity(self.product, self.company_data['default_warehouse'].lot_stock_id, 100)

    def test_decrease_so_line_quantity(self):
        """ Test that decreasing SO line quantity updates the picking instead of creating a return """
        
        # Create SO
        so = self.env['sale.order'].create({
            'partner_id': self.partner_a.id,
            'order_line': [(0, 0, {
                'name': self.product.name,
                'product_id': self.product.id,
                'product_uom_qty': 10.0,
                'product_uom': self.product.uom_id.id,
                'price_unit': 50.0,
            })]
        })
        
        # Confirm SO
        so.action_confirm()
        
        # Check that we have 1 picking
        self.assertEqual(len(so.picking_ids), 1)
        picking = so.picking_ids[0]
        self.assertEqual(picking.state, 'assigned')
        
        move = picking.move_ids[0]
        self.assertEqual(move.product_uom_qty, 10.0)
        
        # Decrease SO line quantity to 6
        so.order_line[0].product_uom_qty = 6.0
        
        # There should STILL only be 1 picking (no phantom return generated)
        self.assertEqual(len(so.picking_ids), 1, "A phantom picking was generated instead of updating the existing one.")
        
        # The existing picking's move should be updated to 6
        self.assertEqual(move.product_uom_qty, 6.0, "The pending delivery move quantity was not reduced.")

    def test_decrease_so_line_quantity_to_zero(self):
        """ Test that decreasing SO line quantity to 0 cancels the move instead of creating a return """
        
        # Create SO
        so = self.env['sale.order'].create({
            'partner_id': self.partner_a.id,
            'order_line': [(0, 0, {
                'name': self.product.name,
                'product_id': self.product.id,
                'product_uom_qty': 5.0,
                'product_uom': self.product.uom_id.id,
                'price_unit': 50.0,
            })]
        })
        
        so.action_confirm()
        
        self.assertEqual(len(so.picking_ids), 1)
        picking = so.picking_ids[0]
        move = picking.move_ids[0]
        
        # Decrease to 0
        so.order_line[0].product_uom_qty = 0.0
        
        self.assertEqual(len(so.picking_ids), 1)
        self.assertEqual(move.state, 'cancel', "The move should be cancelled when quantity drops to zero.")

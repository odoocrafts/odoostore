# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools import float_compare

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _action_launch_stock_rule(self, *, previous_product_uom_qty=False):
        """
        Intercept the hook to prevent phantom pickings generation when qty is decreased.
        """
        precision = self.env['decimal.precision'].precision_get('Product Unit')
        
        for line in self:
            line = line.with_company(line.company_id)
            if line.state != 'sale' or line.order_id.locked or line.product_id.type != 'consu':
                continue
                
            qty = line._get_qty_procurement(previous_product_uom_qty)
            if float_compare(qty, line.product_uom_qty, precision_digits=precision) > 0:
                # The quantity has decreased.
                qty_to_reduce = qty - line.product_uom_qty
                
                # Find outgoing moves that are not done or cancelled
                outgoing_moves, _ = line._get_outgoing_incoming_moves(strict=False)
                pending_moves = outgoing_moves.filtered(lambda m: m.state not in ('done', 'cancel'))
                
                for move in pending_moves:
                    if float_compare(qty_to_reduce, 0.0, precision_digits=precision) <= 0:
                        break
                    
                    move_qty = move.product_uom._compute_quantity(move.product_uom_qty, line.product_uom_id)
                    if move_qty > 0:
                        reduce_amount = min(move_qty, qty_to_reduce)
                        new_qty = move_qty - reduce_amount
                        # Convert back to move uom
                        new_move_qty = line.product_uom_id._compute_quantity(new_qty, move.product_uom)
                        
                        if float_compare(new_move_qty, 0.0, precision_digits=precision) <= 0:
                            move._action_cancel()
                        else:
                            move.write({'product_uom_qty': new_move_qty})
                        
                        qty_to_reduce -= reduce_amount
                        
        return super(SaleOrderLine, self)._action_launch_stock_rule(previous_product_uom_qty=previous_product_uom_qty)

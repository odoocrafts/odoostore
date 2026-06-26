from odoo import models, api
from odoo.exceptions import AccessError

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model
    def _check_unlink_permission(self):
        # Allow if the user has the explicit delete permission or is admin
        if self.env.user.has_group('base.group_system') or self.env.user.has_group('website_access_control_pro.group_media_delete_admin'):
            return True
        # If the user is a restricted editor but doesn't have the media delete admin group
        if self.env.user.has_group('website_access_control_pro.group_restricted_editor'):
            raise AccessError("You do not have permission to delete images from the media library.")
        return True

    def unlink(self):
        self._check_unlink_permission()
        return super(IrAttachment, self).unlink()

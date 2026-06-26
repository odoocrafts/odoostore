from odoo import models, api, _
from odoo.exceptions import AccessError

class BlogPost(models.Model):
    _inherit = 'blog.post'

    def write(self, vals):
        if 'is_published' in vals or 'website_published' in vals:
            if self.env.user.has_group('website_access_control_pro.group_blog_writer') and \
               not self.env.user.has_group('website_access_control_pro.group_blog_publisher'):
                if not self.env.user.has_group('base.group_system'):
                    raise AccessError(_("You do not have permission to publish or unpublish blog posts."))
        return super(BlogPost, self).write(vals)

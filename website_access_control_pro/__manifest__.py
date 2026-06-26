{
    'name': 'Website Access Control Pro',
    'version': '1.0.0',
    'category': 'Website',
    'summary': 'Granular permissions for website editing, blogging, snippets, SEO, themes and media.',
    'description': """
Website Access Control Pro
==========================
Odoo Website permissions are very coarse. Once someone gets Website Editor, they can potentially modify any page.
For many companies, that’s far more access than they want to grant.

MVP Features:
1. Page-Level Permissions
2. Menu Permissions
3. Blog Permissions
4. Snippet Restrictions
5. SEO Permissions
6. Theme Lock
7. Media Library Permissions
    """,
    'author': 'Odoocrafts Innovations',
    'website': 'https://odoocrafts.com',
    'depends': ['website', 'website_blog'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/website_templates.xml',
    ],
    'assets': {
        'website.assets_wysiwyg': [
            'website_access_control_pro/static/src/scss/editor_restrictions.scss',
        ],
    },
    'price': 99.0,
    'currency': 'EUR',
    'images': ['static/description/banner.png', 'static/description/screenshot1.png'],
    'installable': True,
    'application': False,
    'license': 'OPL-1',
}

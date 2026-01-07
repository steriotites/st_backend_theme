{
    'name': 'Backend Theme Professional',
    'version': '18.0.1.0.0',
    'summary': 'Modern professional backend UI theme for Odoo 18',
    'description': """
A fully customized backend theme with:
- Custom sidebar
- Enhanced navbar
- Stylish list & kanban views
- Professional color scheme

Free community theme by Steriotites.
    """,
    'author': 'Steriotites',
    'website': '',
    'license': 'LGPL-3',
    'category': 'Themes/Backend',
    'depends': [
        'base',
        'web',
    ],
    'data': [],
    'demo': [],
    'assets': {
        'web.assets_backend': [
            'steriotites_backend_theme/static/src/xml/webClient.xml',
            'steriotites_backend_theme/static/src/xml/navbar.xml',
            'steriotites_backend_theme/static/src/scss/web_client.scss',
            'steriotites_backend_theme/static/src/js/sidebar_menu.js',
        ],
    },
    'images': [
        'static/description/main_screenshot.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,

}

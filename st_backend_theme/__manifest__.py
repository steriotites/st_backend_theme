{
    'name': 'Backend Theme Professional',
    'version': '19.0.1.0.0',
    'summary': 'Modern professional backend UI theme for Odoo 19',
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
            'st_backend_theme/static/src/xml/webClient.xml',
            'st_backend_theme/static/src/xml/navbar.xml',
            'st_backend_theme/static/src/scss/web_client.scss',
            'st_backend_theme/static/src/js/sidebar_menu.js',
        ],
    },
    'images': [
        'static/description/main_screenshot.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
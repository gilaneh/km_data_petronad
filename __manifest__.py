# -*- coding: utf-8 -*-
{
    'name': "km_data_petronad",

    'summary': """
        It will show the jalaali date for most of date fields""",

    'description': """
        
    """,

    'author': "Arash Homayounfar",
    'website': "https://gilaneh.com/",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Service Desk/Service Desk',
    'application': True,
    'version': '1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'km_data', 'sd_visualize', ],

    # always loaded
    'data': [
        ],
    'assets': {
        'web._assets_common_scripts': [
        ],
        'web._assets_common_styles': [
        ],
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
],
        'web.report_assets_common': [
        ],
        },
    'license': 'LGPL-3',
}

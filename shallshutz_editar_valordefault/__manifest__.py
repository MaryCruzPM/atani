# -*- coding: utf-8 -*-
{
    'name': "product editable y default",

    'summary': """editable y default
    """,

    'description': """
        Modulo para fabricacion para que campo sea editable pero lance por dafault un valor
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'mrp',
        'mrp_account',
        ],

 #       'purchase',       
 #       'contacts',
 #       'stock',
  

    # always loaded
	'data': [#'views/fabricacion_editableDview.xml',
                'views/inventario_default.xml',
    
    ],
	'demo':[

	],
    'installable':True,
}

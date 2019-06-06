# -*- coding: utf-8 -*-
{
    'name': "Wizard para agregar autores y editorial a la descripción",

    'summary': """
    Wizard para agregar autores y editorial a la descripción
    """,

    'description': """
        Modulos funcionales
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
        'stock',        
    ],

    # always loaded
	'data': [
	'views/wizard_autor_editorial.xml',
    ],
	'demo':[

	],
    'installable':True,
}

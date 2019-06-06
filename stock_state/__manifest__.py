# -*- coding: utf-8 -*-
{
    'name': "Agrega nuevo estado en la entrega",
    'description': """
        Generar nuevo estado en transferencias
    """,
    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",
    'version': '0.1',
    'depends': ['base','stock'],
    'data': [
        'views/stock_picking_state.xml'
        ],
    'installable':True,
    'auto_install':False,
}

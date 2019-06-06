# -*- coding: utf-8 -*-

from odoo import _
from odoo import api
from odoo import exceptions
from odoo import fields
from odoo import models

class Wizard_Descripcion(models.TransientModel): 
    _name = 'wizard_descripcion'
    
    def _default_descripcion(self):
        return self.env['product.template'].browse(self._context.get('active_ids'))
    
    productos_ids = fields.Many2many('product.template', string='Productos', default=_default_descripcion)

    def descripcion_add(self):
        for record in self.productos_ids:
            editoriales = ""
            authores = ""
            for editorial in record.x_editorial:
                editoriales += editorial.name
            for author in record.x_autor:
                authores += author.name + ", "
            descripcion=record.description_sale
            if descripcion==False:
                record.description_sale=" * Autor(es): "+authores+" Editorial: "+editoriales
            else:
                record.description_sale=descripcion+" * Autor(es): "+authores+" Editorial: "+editoriales
            #record.description_sale+=(" * Autor(es): "+authores+" Editorial: "+editoriales)

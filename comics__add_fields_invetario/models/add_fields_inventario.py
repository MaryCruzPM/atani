# -*- coding:utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models


class add_fields(models.Model):
    """docstring for ClassName"""
    _inherit = 'product.template'


    x_autor = fields.Many2many('res.partner', 
                               string="autor",
                               help="Se agregará automáticamente a la descripción"
                               )
	
    x_editorial = fields.Many2one('res.partner',
                                  string="editorial",
                                  help="Se agregará automáticamente a la descripción"
                                  )

    @api.model
    def create(self, vals):
        producto_creado = super(add_fields, self).create(vals)
        editoriales = ""
        authores = ""
        for editorial in producto_creado.x_editorial:
            editoriales += editorial.name
        for author in producto_creado.x_autor:
            authores += author.name + ", "
        descripcion=producto_creado.description_sale
        if descripcion==False:
            print("ES FALSO")
            producto_creado.description_sale=" * Autor(es): "+authores+" Editorial: "+editoriales
        else:
            lista=producto_creado.description_sale.split("*")
            nueva_descripcion=lista[0]
            nueva_descripcion+=" * Autor(es): "+authores+" Editorial: "+editoriales
            #print(nueva_descripcion)
            producto_creado.description_sale=nueva_descripcion
        return producto_creado
    
    @api.multi
    def write(self, vals):
        self.ensure_one()
        producto_actualizado=super(add_fields, self).write(vals)    
        editoriales = ""
        authores = ""
        nueva_descripcion=""
        for editorial in self.x_editorial:
            editoriales += editorial.name
        for author in self.x_autor:
            authores += author.name + ", "
        descripcion=self.description_sale
        if descripcion==False:
            nueva_descripcion=" * Autor(es): "+authores+" Editorial: "+editoriales
        else:
            lista=descripcion.split("*")
            nueva_descripcion=lista[0]
            nueva_descripcion+=" * Autor(es): "+authores+" Editorial: "+editoriales
        vals['description_sale']=nueva_descripcion
        producto_actualizado=super(add_fields, self).write(vals)

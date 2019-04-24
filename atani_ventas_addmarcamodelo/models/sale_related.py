# - * - coding: utf-8 - * -

from odoo import api
from odoo import fields
from odoo import models

class porcentaje_rapaport(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def _compute_costo_quilate_usd(self):
    	
        id_x= self.env['product.template'].search([('id', '=', self.product_id.product_tmpl_id.id)])
        print(id_x)
        #modelo=self.env['product.product'].search(['product_tmpl_id','=',id_x])
        self.x_xmodelo=id_x.modelo
        self.x_xmarca=id_x.brand_id
        #como se obtuve eb id_x el id de product.template entonces ya podemos accesar con ese id a su modelo y marca de product product porque 
        #estan los cmapos relacionales en product product para product template.

    x_xmodelo = fields.Char(string='Modelo')
    x_xmarca = fields.Many2one('product.brand',string='Marca')
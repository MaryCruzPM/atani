
# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api

class finventario_default(models.Model):
	_inherit='product.template'

	
	x_metros2=fields.Float(string="M2",)
	x_largo=fields.Float(string="Largo",)
	x_ancho=fields.Float(string="Ancho",)
	x_gr_m2=fields.Float(string="Gramaje",)
	x_thicknesstes=fields.Float(string="Prueba de espesor",)
	x_peso=fields.Float(string="Peso",)
	x_turno=fields.Selection(selection=[('Morning','Matutino'),('Vespertino','Evening'),
		('Nocturno','Night')],
		
		)
	x_encargado=fields.Many2one('res.partner',string="Manager",)
	
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api

class editable(models.Model):
	_inherit='mrp.production'


	@api.onchange('product_id')
	def _ca(self):
		id_x= self.env['product.template'].search([('id', '=', self.product_id.product_tmpl_id.id)])
		print(id_x.x_metros2)
		self.m2=id_x.x_metros2
		self.large=id_x.x_largo
		self.wigth=id_x.x_ancho
		self.gr_m2=id_x.x_gr_m2
		self.thicknesstest=id_x.x_thicknesstes
		self.peso=id_x.x_peso
		print(self.turn)
		self.turn=id_x.x_turno
		self.manager=id_x.x_encargado

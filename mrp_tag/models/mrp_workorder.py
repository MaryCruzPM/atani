import re
from odoo import models, fields, api

class MrpWorkorder(models.Model):

    _inherit =  'mrp.workorder'


    def open_tablet_view(self):
        order_id = super(MrpWorkorder, self).open_tablet_view()
        if self.final_lot_id:
            return order_id
        lot_sequence = self.env['ir.sequence']\
                           .next_by_code('mrp.workorder.order')
        pre ="".join(
            re.findall(
                r'-?\d+\.?\d*', self.production_id.name
            )
        )
        product_id = self.production_id.product_id
        lot_id = self.env['stock.production.lot']\
                     .create({
            'name': "{}{}{}".format(
                pre,
                product_id.barcode,
                lot_sequence
            ),
            'product_id': product_id.id
        })
        self.final_lot_id = lot_id.id
        return order_id

    @api.onchange('lot_id')
    def _get_qtyavailable(self):
        self.qty_done = self.component_id.with_context({
            'lot_id':self.lot_id.id,
            'location': self.production_id.location_src_id.id
        }).qty_available

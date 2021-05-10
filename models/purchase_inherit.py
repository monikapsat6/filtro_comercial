# -*- coding: utf-8 -*-
from odoo import models, fields, api


class purchaseorder(models.Model):
    _inherit = 'purchase.order'

    partner_ref_eti = fields.Char()

    @api.multi
    def report_etiqueta_purchase_order(self):
        if 'partner_ref' in self.env['purchase.order']._fields:
            
            self.partner_ref_eti = self.partner_ref

            if self.partner_ref_eti.startswith('#'):

                self.partner_ref_eti = self.partner_ref_eti[1:]

            if len(self.partner_ref_eti) > 17:

                self.partner_ref_eti = self.partner_ref_eti[:17]

        return self.env.ref('filtro_comercial-main.cd_report_etiqueta_purchase_order').report_action(self)

class purchaseorderline(models.Model):
    _inherit = 'purchase.order.line' 

    #move_state = fields.Char(compute='_assign_movement_state')

    @api.multi
    def debug(self):
        print(self.move_ids.state, + "/"*50)

    #@api.depends('move_ids')
    #def _assign_movement_state(self):
    #    self.ensure_one()
    #    #move_state = self.move_ids.state
    #    print(self.move_ids.state)

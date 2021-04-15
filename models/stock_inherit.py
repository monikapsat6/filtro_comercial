# -*- coding: utf-8 -*-
from odoo import models, fields, api

class stockpicking(models.Model):
    _inherit = 'stock.picking'


    orden = None
    @api.multi
    def report_etiqueta_stock_label(self):
        self.orden = self.env['purchase.order'].search([('name','=',self.origin)])
        
        print("//"*15,"ID DE STOCKPICKING: " , self.id)
        print("//"*15,"ID DE ORDEN: " , self.orden.id)
        return self.env.ref('filtro_comercial-main.cd_report_etiqueta_stock').report_action(self)
    
class stockwarehouse(models.Model):
    _inherit = 'stock.warehouse'

    warehouse_type = fields.Char()

class stockpickingtype(models.Model):
    _inherit = 'stock.picking.type'

    warranty = fields.Char()


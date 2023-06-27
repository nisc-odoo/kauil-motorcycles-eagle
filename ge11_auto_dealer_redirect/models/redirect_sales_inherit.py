from odoo import api, models, fields
from odoo.exceptions import ValidationError
import re

class redirectSales(models.Model):
    _inherit = "sale.order"
    
    
    
    
    
    warehouse_id = fields.Many2one(comodel_name="stock.warehouse",compute="_compute_from_address", store=True)
    @api.depends('partner_id')
    def _compute_from_address(self):
        Buffalo = [
                "Alabama",
                "Alaska",
                "Arizona",
                "Arkansas",
                "California",
                "Colorado",
                "Connecticut",
                "Delaware",
                "Florida",
                "Georgia",
                "Hawaii",
                "Idaho",
                "Illinois",
                "Indiana",
                "Iowa",
                "Kansas",
                "Kentucky",
                "Louisiana",
                "Maine",
                "Maryland",
                "Massachusetts",
                "Michigan",
                "Minnesota",
                "Mississippi",
                "Missouri",
                "Montana",]
        sales_with_address = self.filtered(lambda r: r.partner_id)
        for sale in sales_with_address:
            if sale.partner_shipping_id.state_id.name in Buffalo:
                sale.warehouse_id = 3
            else:
                sale.warehouse_id = 4
                
from odoo import api, models, fields
from odoo.exceptions import ValidationError
import re

class RepairEnchance(models.Model):
    _inherit = "repair.order"
    
    vin = fields.Char(string='VIN', required=False)
    current_mileage = fields.Float(string='Current Mileage')
    registry_id = fields.Many2one(comodel_name="motorcycle.registry",compute='_compute_from_vin_repair', required=False, store=True)
    
    @api.depends('vin')
    def _compute_from_vin_repair(self):
        repairs_with_vin = self.filtered(lambda r: r.vin)
        repairs_with_vin._check_vin_pattern_repair()
        for repair in repairs_with_vin:
            reg = self.env['motorcycle.registry'].search_read([('vin','=',repair.vin)])
            if len(reg)>0:
                repair.registry_id = reg[0].get("id")
                repair.partner_id = reg[0].get("owner_id")
            
                prod = self.env['product.template'].search_read([('make','=',reg[0].get('make')),('model','=',reg[0].get('model')),('year','=',reg[0].get('year'))])
                if len(prod) > 0:
                    print(prod)
                    repair.product_id = prod[0].get('id')
                    repair.sale_order_id = self.env['sale.order'].search_read([('product_id','=',prod[0].get('id')),('partner_id','=',reg[0].get("owner_id"))])[0].get('id')

                
            
        for repair in (self - repairs_with_vin):
            repair.registry_id = False
            
            
    @api.constrains('vin')
    def _check_vin_pattern_repair(self):
        pattern = '^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{6}$'
        for registry in self.filtered(lambda r: r.vin):
            match = re.match(pattern, registry.vin)
            if not match:
                raise ValidationError('Odoopsie! Invalid VIN')
            if not registry.vin[0:2] == 'KA':
                raise ValidationError('Odoopsie! Only motorcycles from Kauil Motors are allowed')
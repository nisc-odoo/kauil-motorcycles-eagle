from odoo import api, models, fields
from odoo.exceptions import ValidationError
import re

class Repair_Enchance(models.Model):
    _inherit = "repair.order"
    
    vin = fields.Char(string='VIN', required=True)
    current_mileage = fields.Float(string='Current Mileage')
    registry_id = fields.Char(compute='_compute_from_vin')
    
    @api.depends('vin')
    def _compute_from_vin(self):
        repairs_with_vin = self.filtered(lambda r: r.vin)
        repairs_with_vin._check_vin_pattern()
        for repair in repairs_with_vin:
            repair.registry_id = self.env['motorcycle.registry'].search_read([('registry_number','=',repair.vin)])
        for repair in (self - repairs_with_vin):
            repair.registry_id
            
    @api.constrains('vin')
    def _check_vin_pattern(self):
        pattern = '^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{6}$'
        for registry in self.filtered(lambda r: r.vin):
            match = re.match(pattern, registry.vin)
            if not match:
                raise ValidationError('Odoopsie! Invalid VIN')
            if not registry.vin[0:2] == 'KA':
                raise ValidationError('Odoopsie! Only motorcycles from Kauil Motors are allowed')
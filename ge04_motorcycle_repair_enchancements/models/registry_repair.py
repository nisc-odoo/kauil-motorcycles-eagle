from odoo import api, models, fields
from odoo.exceptions import ValidationError
import re

class registry_repair(models.Model):
    _inherit = "motorcycle.registry"
    repair_count = fields.Integer(compute='compute_count')
    repair_id = fields.One2many(comodel_name='repair.order', inverse_name='registry_id', required=False, store=True)
    def get_repairs(self):
        self.ensure_one()
        return{
            'type':'ir.actions.act_window',
            'name':'repairs',
            'view_mode':'tree',
            'res_model':'repair.order',
            'domain':[('registry_id','=',self.id)],
            'context':"{'create':False}"
        }
    def compute_count(self):
        for record in self:
            record.repair_count = self.env['repair.order'].search_count([('registry_id','=',self.id)])
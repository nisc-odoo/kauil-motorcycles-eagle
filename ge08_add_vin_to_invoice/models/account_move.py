from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = "account.move.line"

    vin = fields.Char(string="VIN", compute="_compute_vin", default="Example VIN data")

    def _compute_vin(self):
        for record in self:
            if (False):
                record.vin = "No VIN assigned yet"
            else:
                record.vin = "Computed VIN"
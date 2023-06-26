from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = "account.move.line"

    vin = fields.Char(string="VIN", compute="_compute_vin", default="Example VIN data")

    def _compute_vin(self):
        for record in self:
            linked_sale_order = self.env["sale.order"].search_read([("name", "=", record.invoice_origin)])
            mrp_id = linked_sale_order[0]["mrp_production_ids"]
            if (len(mrp_id) == 0):
                record.vin = "No MRP found for vehicle"
                return
            linked_mrp = self.env["mrp.production"].search_read([("id", "=", mrp_id[0])])
            print(linked_mrp[0]["lot_producing_id"])
            retrieved_vin = linked_mrp[0]["lot_producing_id"]
            if (retrieved_vin == False):
                record.vin = "No VIN assigned yet"
            else:
                record.vin = retrieved_vin[1]

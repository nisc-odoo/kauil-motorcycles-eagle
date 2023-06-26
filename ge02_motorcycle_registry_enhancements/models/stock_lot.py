from odoo import api, models, fields

class StockLot(models.Model):
	_inherit = "stock.lot"

	
	motorcycle_registry_id = fields.Many2one(comodel_name="motorcycle.registry", ondelete="restrict")
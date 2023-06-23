from odoo import api, models, fields
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
	_inherit = "motorcycle.registry"

	stock_lot_ids = fields.One2many(comodel_name='stock.lot', inverse_name='motorcycle_registry_id', string='Stock Lot Ids')
	stock_lot_id = fields.Many2one(comodel_name='stock.lot', string="Stock Lot", compute="_get_first_lot", store=True, readonly=False)
	
	sale_order_id = fields.Many2one(comodel_name='sale.order.line', string="Related Sale Order", default=False)

	@api.constrains('stock_lot_ids')
	def _check_stock_single(self):
		for record in self:
			if len(record.stock_lot_ids) > 1:
				raise ValidationError("There are more than one stock lot ids to this registry")

	@api.depends('stock_lot_ids')
	def _get_first_lot(self):
		for record in self:
			record.stock_lot_id = record.stock_lot_ids['id']
		return
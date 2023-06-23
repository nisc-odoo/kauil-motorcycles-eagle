from odoo import api, fields, models

class StockLot(models.Model):
    _inherit = "stock.lot"
    _description = "Automates serial number creation"
    
    @api.model
    def _get_next_serial(self, company, product):
        if product.detailed_type == 'motorcycle' and product.tracking != "none":
            if product.make and product.year and product.model:
                temp_serial = product.make + product.model + str(product.year)[2:]
                battery_capacity = 'XX' if not product.battery_capacity else product.battery_capacity
                temp_serial += battery_capacity.upper()
                temp_serial += self.env['ir.sequence'].next_by_code('stock.lot.serial')[1:]
                return temp_serial
        else:
            return self.super(StockLot, self)._get_next_serial(company, product)

    # @api.model
    # def _get_next_serial(self, company, product):
    #     """Return the next serial number to be attributed to the product."""
    #     if product.tracking != "none":
    #         last_serial = self.env['stock.lot'].search(
    #             [('company_id', '=', company.id), ('product_id', '=', product.id)],
    #             limit=1, order='id DESC')
    #         if last_serial:
    #             return self.env['stock.lot'].generate_lot_names(last_serial.name, 2)[1]
    #     return False
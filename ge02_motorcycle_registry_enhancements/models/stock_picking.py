from odoo import api, fields, models

class Picking(models.Model):
    _inherit = "stock.picking"


    def button_validate(self):
        if product['detailed_type'] == 'motorcycle':
            sale_order = self.sale_id
            mrp_order = sale_order['mrp_production_ids']
            product = mrp_order['product_id']
            
            if not self.env['motorcycle.registry'].search_count([('vin', '=', mrp_order['lot_producing_id']['name'])]) > 0:
                print("function called")
                self.env['motorcycle.registry'].create({
                    'vin': mrp_order['lot_producing_id']['name'],
                    'stock_lot_ids': [mrp_order['lot_producing_id'][0]['id']],
                    'sale_order_id': sale_order.id,
                })
        return super(Picking,self).button_validate()

        
from odoo import api, fields, models

class Picking(models.Model):
    _inherit = "stock.picking"


    def button_validate(self):
        
        sale_order = self.sale_id
        try:
            mrp_order = sale_order['mrp_production_ids']
            if sale_order.get('mrp_production_ids'):
                
                product = mrp_order['product_id']
                if product['detailed_type'] == 'motorcycle':
                    if not self.env['motorcycle.registry'].search_count([('vin', '=', mrp_order['lot_producing_id']['name'])]) > 0:
                        self.env['motorcycle.registry'].create({
                            'vin': mrp_order['lot_producing_id']['name'],
                            'stock_lot_ids': [mrp_order['lot_producing_id'][0]['id']],
                            'sale_order_id': sale_order.id,
                        })
        except KeyError:
            pass
        finally:
            return super(Picking,self).button_validate()	

    
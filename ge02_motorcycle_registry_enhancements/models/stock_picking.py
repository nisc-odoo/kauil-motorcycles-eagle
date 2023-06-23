from odoo import api, fields, models

class Picking(models.Model):
    _inherit = "stock.picking"


    def button_validate(self):
        sale_order = self.env['sale.order'].search_read([('id', '=', int(self.origin[1:]))])
        mrp_ids = []

        for sale in sale_order:
            mrp_ids.append(*sale['mrp_production_ids'])
        for mrp in mrp_ids:
            mrp_order = self.env['mrp.production'].search_read([('id', '=', mrp)])
            product = self.env['product.template'].search_read([('name', '=', mrp_order[0]['product_id'][1])])
            print(product)
            if product[0]['detailed_type'] == 'motorcycle':
                if not self.env['motorcycle.registry'].search_count([('vin', '=', mrp_order[0]['lot_producing_id'][1])]) > 0:
                    self.env['motorcycle.registry'].create({
                        'vin': mrp_order[0]['lot_producing_id'][1],
                        'stock_lot_ids': [self.env['stock.lot'].search_read([('name', '=', mrp_order[0]['lot_producing_id'][1])])[0]['id']],
                        'sale_order_id': sale_order[0]['id'],
                    })
        return super(Picking,self).button_validate()

        
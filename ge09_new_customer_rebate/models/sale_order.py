from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Apply new customer discount to appropriate sales"

    is_new_customer = fields.Boolean(string="Is new customer", compute="_compute_is_new_customer")

    @api.depends('partner_id')
    def _compute_is_new_customer(self):
        flag = True
        for record in self:
            customer = record.partner_id
            customer_orders = self.env['sale.order'].search([("partner_id", "=", customer.id)])
            for order in customer_orders:
                if (order.state == "sale" or order.state == "done"):
                    for order_line in order.order_line:
                        if order_line.product_type == "motorcycle":
                            flag = False
            record.is_new_customer = flag

    def apply_discount(self):
        discount_pricelist = self.env["product.pricelist"].search([("name", "=", "New Customer Discount")])[0]
        print(discount_pricelist)
        self.pricelist_id = discount_pricelist
        

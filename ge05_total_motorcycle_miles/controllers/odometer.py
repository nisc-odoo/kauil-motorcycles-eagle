from odoo import http

class Odometer(http.Controller):
    
    @http.route('/odometer/', auth="public", type="json", methods=['POST'])
    def all_miles(self):
        bikes = http.request.env['motorcycle.registry'].search_read([],['current_mileage'])
        return bikes
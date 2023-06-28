from odoo import api, fields, models
from odoo import http
from odoo.addons.portal.controllers import portal
from odoo.exceptions import AccessError, MissingError

class CustomerPortal(portal.CustomerPortal):
    
    #do something here to get registries count
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        partner = http.request.env.user.partner_id

        MotorcycleRegistry = http.request.env['motorcycle.registry']
       
        if 'motorcycle_registry_count' in counters:
            values['motorcycle_registry_count'] = MotorcycleRegistry.search_count([]) \
                if MotorcycleRegistry.check_access_rights('read', raise_exception=False) else 0
        return values

    
    @http.route('/my/registries', auth='user', website=True, sitemap=False)
    def portal_registries_page(self):
        registries = http.request.env['motorcycle.registry'].search([])
        data = {
            'registries': registries
        }
        return http.request.render('ge03_views.motorcycle_registry_list', data)
    @http.route(['/test'], type='http', auth="public", website=True)
    def test(self, report_type=None, access_token=None, message=False, download=False, **kw):
        return "test"

    @http.route(['/my/registries', '/my/registries/<int:registry_id>'], auth="user", website=True)
    def portal_order_page(self, registry_id, access_token=None, **kw):
        print("hello world")
    #     try:
    #         order_sudo = self._document_check_access('motorcycle.registry', registry_id, access_token=access_token)
    #     except (AccessError, MissingError):
    #         return http.request.redirect('/my')

    #     if report_type in ('html', 'pdf', 'text'):
    #         return self._show_report(model=order_sudo, report_type=report_type, report_ref='sale.action_report_saleorder', download=download)

    #     if http.request.env.user.share and access_token:
    #         # If a public/portal user accesses the order with the access token
    #         # Log a note on the chatter.
    #         today = fields.Date.today().isoformat()
    #         session_obj_date = request.session.get('view_quote_%s' % order_sudo.id)
    #         if session_obj_date != today:
    #             # store the date as a string in the session to allow serialization
    #             request.session['view_quote_%s' % order_sudo.id] = today
    #             # The "Quotation viewed by customer" log note is an information
    #             # dedicated to the salesman and shouldn't be translated in the customer/website lgg
    #             context = {'lang': order_sudo.user_id.partner_id.lang or order_sudo.company_id.partner_id.lang}
    #             msg = _('Quotation viewed by customer %s', order_sudo.partner_id.name if request.env.user._is_public() else request.env.user.partner_id.name)
    #             del context
    #             _message_post_helper(
    #                 "sale.order",
    #                 order_sudo.id,
    #                 message=msg,
    #                 token=order_sudo.access_token,
    #                 message_type="notification",
    #                 subtype_xmlid="mail.mt_note",
    #                 partner_ids=order_sudo.user_id.sudo().partner_id.ids,
    #             )

    #     backend_url = f'/web#model={order_sudo._name}'\
    #                   f'&id={order_sudo.id}'\
    #                   f'&action={order_sudo._get_portal_return_action().id}'\
    #                   f'&view_type=form'
    #     values = {
    #         'sale_order': order_sudo,
    #         'message': message,
    #         'report_type': 'html',
    #         'backend_url': backend_url,
    #         'res_company': order_sudo.company_id,  # Used to display correct company logo
    #     }

    #     # Payment values
    #     if order_sudo._has_to_be_paid():
    #         values.update(self._get_payment_values(order_sudo))

    #     if order_sudo.state in ('draft', 'sent', 'cancel'):
    #         history_session_key = 'my_quotations_history'
    #     else:
    #         history_session_key = 'my_orders_history'

    #     values = self._get_page_view_values(
    #         order_sudo, access_token, values, history_session_key, False)
        values = {}
        return http.request.render('ge03_views.registry_portal_content', values)

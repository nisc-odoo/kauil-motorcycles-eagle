# from odoo import http
# from odoo.exceptions import AccessError, MissingError
# from odoo.addons.portal.controllers import portal

# #TODO: add portal class 

# class MotorcycleRegistryController(http.Controller):
# 	@http.route('/my/registries', auth='user', website=True, sitemap=False)
# 	def portal_registries_page(self):
# 		registries = http.request.env['motorcycle.registry'].search([])
# 		data = {
# 			'registries': registries
# 		}
# 		return http.request.render('ge03_views.motorcycle_registry_list', data)



#     #In http.request.session 

# 	# @http.route('/form/<int:registry_id>', auth='user', website=True, sitemap=False) 
# 	# def motorcycle_form(self, registry_id, access_token=None, **kargs):
# 	# 	try:
# 	# 		registry_sudo = self._document_check_access('motorcycle.registry', registry_id, access_token=access_token)
# 	# 	except (AccessError, MissingError):
# 	# 		return http.request.redirect('/list')

# 	# portal serachbar 
	

# 	# 	registries = http.request.env['motorcycle.registry'].search([])
# 	# 	data = {
# 	# 		'registries': registries
# 	# 	}
		
# 	# 	return http.request.render('ge03_views.motorcycle_registry_form', data)

# 	# @http.route('/list', auth='public', website=True, sitemap=False)
# 	# def motorcycle_list(self, **kargs):
# 	# 	registries = http.request.env['motorcycle.registry'].search([])
# 	# 	data = {
# 	# 		'registries': registries
# 	# 	}
		
# 	# 	return http.request.render('ge03_views.motorcycle_registry_list', data)


# 	# @http.route('/test', auth='user', website=True, sitemap=False)
# 	# def test(self, **kargs):
# 	# 	return "test"


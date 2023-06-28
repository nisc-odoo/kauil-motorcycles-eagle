from odoo import api, fields, models

class MotorcycleRegistry(models.Model):
    _inherit = ["motorcycle.registry", "portal.mixin"] 

    is_public = fields.Boolean(string="Is Public", default=False)

    # # # portal.mixin overrides # # #
    # def _compute_access_warning(self):
    #     pass

    
    def _compute_access_url(self):
        super()._compute_access_url()
        for registry in self:
            registry.access_url = f'/form/{registry.id}'

    # def _get_share_url(self):
    #     pass
    # # # portal.mixin overrides # # # 
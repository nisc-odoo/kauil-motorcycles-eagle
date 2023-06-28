from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"
    _description = "Automates motorcycle naming"
    
    # name = fields.Char(compute="_compute_name", inverse="_set_name", store=True, readonly=False)
    name = fields.Char(compute="_compute_name", store=True, readonly=False)
    
    @api.depends('make', 'model', 'year')
    def _compute_name(self):
        for record in self:
            if record.detailed_type == "motorcycle" and record.make and record.model and record.year:
                record.name=f"{record.year} {record.make} {record.model}"
            
    # function that are set to the inverse field run on save. IF you don't want motorcycles to be renamed
    # to anything, use this field. It'll check when saving if it meets requirements.
    # def _set_name(self):
    #     for record in self:
    #         if record.detailed_type == "motorcycle" and record.make and record.model and record.year:
    #             record.name=f"{record.year} {record.make} {record.model}"
        
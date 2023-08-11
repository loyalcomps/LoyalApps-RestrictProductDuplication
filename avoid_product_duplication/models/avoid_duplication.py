from odoo import api, fields, models, exceptions

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, vals):
        company = self.env.company


        if company.avoid_product_name_duplication and 'name' in vals:
            existing_product = self.search([('name', '=', vals['name'])])
            if existing_product:
                raise exceptions.UserError("A product with the same name already exists.")

        if company.avoid_internal_reference_duplication and 'default_code' in vals and isinstance(vals['default_code'], str) and vals['default_code'].strip():
            existing_product = self.search([('default_code', '=', vals['default_code'].strip())])
            if existing_product:
                raise exceptions.UserError("A product with the same Internal Reference already exists.")

        return super(ProductTemplate, self).create(vals)

    def write(self, vals):
        company = self.env.company


        if company.avoid_product_name_duplication and 'name' in vals:
            existing_product = self.search([('name', '=', vals['name'])])
            if existing_product:
                raise exceptions.UserError("A product with the same name already exists.")

        if company.avoid_internal_reference_duplication and 'default_code' in vals and isinstance(vals['default_code'], str) and vals['default_code'].strip():
            existing_product = self.search([('default_code', '=', vals['default_code'].strip())])
            if existing_product:
                raise exceptions.UserError("A product with the same Internal Reference already exists.")

        return super(ProductTemplate, self).write(vals)

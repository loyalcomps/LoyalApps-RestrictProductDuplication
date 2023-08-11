from odoo import models,fields
class ResCompany(models.Model):
    _inherit = 'res.company'

    avoid_product_name_duplication = fields.Boolean(
        string='Restrict Product Name Duplication',
        help='If checked, avoid duplicate product names within .'
    )
    avoid_internal_reference_duplication = fields.Boolean(
        string='Restrict Product Internal Reference Duplication',
        help='If checked, avoid duplicate product reference within .'
    )

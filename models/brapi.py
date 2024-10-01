from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Brapi(models.Model):
    _name = 'investimentoo.brapi'
    _description = 'Brapi Integrator'

    base_url = fields.Char(string='Base URL', required=True)
    api_key = fields.Char(string='API Key', required=True)


    @api.model
    def crete(self, vals):
        if self.search_count([]) >= 1:
            raise ValidationError('Only one record is allowed')

        return super(Brapi, self).create(vals)
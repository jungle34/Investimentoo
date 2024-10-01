from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Fechamentos(models.Model):
    _name = 'investimentoo.fechamentos'
    _description = 'Fechamentos'

    ativo_id = fields.Many2one('investimentoo.ativos', string='Ativo', required=True)
    stock = fields.Char(string='Stock', required=True)
    data = fields.Date(string='Data', required=True)

    close = fields.Float(string='Valor', required=True)
    volume = fields.Float(string='Volume', required=True)
    market_cap = fields.Float(string='Market Cap', required=True)
    change = fields.Float(string='Variacao', required=True)
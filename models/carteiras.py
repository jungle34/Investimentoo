from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Carteira(models.Model):
    _name = 'investimentoo.carteiras'
    _description = 'Carteira de investimentos'

    name = fields.Char(string='Nome', required=True)
    obs = fields.Text(string='Observacoes')

    movimentos = fields.One2many('investimentoo.movimentos', 'carteira_id', string='Movimentos')
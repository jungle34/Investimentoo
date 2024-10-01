from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Movimentos(models.Model):
    _name = 'investimentoo.movimentos'
    _description = 'Movimentos de carteira'
            
    ativo = fields.Many2one('investimentoo.ativos', string='Ativo', required=True)
    carteira_id = fields.Many2one('investimentoo.carteiras', string='Carteira')
    data = fields.Date(string='Data', required=True)
    quantidade = fields.Float(string='Quantidade', required=True)
    valor_unit = fields.Float(string='Valor', required=True)

    carteira_id = fields.Many2one('investimentoo.carteiras', string='Carteira')
    
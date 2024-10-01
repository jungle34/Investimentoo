import logging
import requests

from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class Ativos(models.Model):
    _name = 'investimentoo.ativos'
    _description = 'Gerenciamento de ativos'

    name = fields.Char(string='Nome', required=True)
    ativo = fields.Char(string='Ativo', required=True)
    sector = fields.Char(string='Setor')
    asset_type = fields.Char(string='Tipo')
    logo = fields.Char(string='Logo')

    fechamentos = fields.One2many('investimentoo.fechamentos', 'ativo_id', string='Fechamentos')

    # {
    #     "stock": "PDGR3",
    #     "name": "PDG REALT",
    #     "close": 0.01,
    #     "change": -50,
    #     "volume": 97017500,
    #     "market_cap": 34858586,
    #     "logo": "https://s3-symbol-logo.tradingview.com/pdg-realt--big.svg",
    #     "sector": "Finance",
    #     "type": "stock"
    # }

    # ativo_id = fields.Many2one('investimentoo.ativos', string='Ativo', required=True)
    # data = fields.Date(string='Data', required=True)

    # close = fields.Float(string='Valor', required=True)
    # volume = fields.Float(string='Volume', required=True)
    # market_cap = fields.Float(string='Market Cap', required=True)
    # change = fields.Float(string='Variacao', required=True)

    def import_request(self, request_config):              
        return requests.request("GET", request_config['base_url'] + "/quote/list?token=" + request_config['api_key'])    

    def assets_proccess(self, response):
        for item in response.json()['stocks']:           
            if self.env['investimentoo.ativos'].search_count([('ativo', '=', item['stock'])]) == 0:               
                self.create({
                    'name': item['name'],
                    'ativo': item['stock'],
                    'logo': item['logo'],
                    'sector': item['sector'],
                    'asset_type': item['type']
                })
            
            fechamento_exists = self.env['investimentoo.fechamentos'].search_count([
                ('stock', '=', item['stock']),
                ('data', '=', fields.Date.today())
            ])

            if fechamento_exists == 0:
                _logger.info('Creating fechamento for %s', item['stock'])
                self.env['investimentoo.fechamentos'].create({
                    'ativo_id': self.env['investimentoo.ativos'].search([('ativo', '=', item['stock'])], limit=1).id,
                    'stock': item['stock'],
                    'data': fields.Date.today(),
                    'close': item['close'],
                    'volume': item['volume'],
                    'market_cap': item['market_cap'],
                    'change': item['change']
                })

    @api.model
    def schedule_asset_import(self):
        request_config = self.env['investimentoo.brapi'].search([], limit=1)
        if not request_config:
            _logger.warning('No Brapi configuration found')
            return

        request_config = {'base_url': request_config.base_url, 'api_key': request_config.api_key}
        
        self.assets_proccess(self.import_request(request_config))

        pass
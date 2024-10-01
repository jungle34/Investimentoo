# -*- coding: utf-8 -*-
# from odoo import http


# class Investimentoo(http.Controller):
#     @http.route('/investimentoo/investimentoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/investimentoo/investimentoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('investimentoo.listing', {
#             'root': '/investimentoo/investimentoo',
#             'objects': http.request.env['investimentoo.investimentoo'].search([]),
#         })

#     @http.route('/investimentoo/investimentoo/objects/<model("investimentoo.investimentoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('investimentoo.object', {
#             'object': obj
#         })


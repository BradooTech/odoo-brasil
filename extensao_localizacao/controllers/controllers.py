# -*- coding: utf-8 -*-
from odoo import http

# class ExtensaoLocalizacao(http.Controller):
#     @http.route('/extensao_localizacao/extensao_localizacao/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extensao_localizacao/extensao_localizacao/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extensao_localizacao.listing', {
#             'root': '/extensao_localizacao/extensao_localizacao',
#             'objects': http.request.env['extensao_localizacao.extensao_localizacao'].search([]),
#         })

#     @http.route('/extensao_localizacao/extensao_localizacao/objects/<model("extensao_localizacao.extensao_localizacao"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extensao_localizacao.object', {
#             'object': obj
#         })
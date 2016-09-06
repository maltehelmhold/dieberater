# -*- coding: utf-8 -*-
from openerp import http

# class Dieberater(http.Controller):
#     @http.route('/dieberater/dieberater/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dieberater/dieberater/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dieberater.listing', {
#             'root': '/dieberater/dieberater',
#             'objects': http.request.env['dieberater.dieberater'].search([]),
#         })

#     @http.route('/dieberater/dieberater/objects/<model("dieberater.dieberater"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dieberater.object', {
#             'object': obj
#         })
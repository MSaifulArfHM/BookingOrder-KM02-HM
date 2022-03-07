# -*- coding: utf-8 -*-
# from odoo import http


# class BookingOrderMuhamadSaifulArif(http.Controller):
#     @http.route('/booking_order__muhamad_saiful_arif/booking_order__muhamad_saiful_arif/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order__muhamad_saiful_arif/booking_order__muhamad_saiful_arif/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order__muhamad_saiful_arif.listing', {
#             'root': '/booking_order__muhamad_saiful_arif/booking_order__muhamad_saiful_arif',
#             'objects': http.request.env['booking_order__muhamad_saiful_arif.booking_order__muhamad_saiful_arif'].search([]),
#         })

#     @http.route('/booking_order__muhamad_saiful_arif/booking_order__muhamad_saiful_arif/objects/<model("booking_order__muhamad_saiful_arif.booking_order__muhamad_saiful_arif"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order__muhamad_saiful_arif.object', {
#             'object': obj
#         })

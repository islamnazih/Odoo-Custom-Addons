import logging
from odoo import fields, http, _ , SUPERUSER_ID
# from odoo.addons.purchase_sale_auto_quotation.controllers.auth.common import validate_token
from odoo.http import request

_logger = logging.getLogger(__name__)

class SaleOrderController(http.Controller):

    @http.route('/api/sale/create_from_purchase', type='json', methods=['POST'], auth="public", csrf=False)
    def create_sale_from_purchase(self, **kwargs):
        try:
            data = request.httprequest.get_json()
            customer_id = data.get('vendor_id')

            order_values = {
                'partner_id': customer_id,
            }
            sale_order = request.env['sale.order'].sudo().create(order_values)
            return {'success': True, 'order_id': sale_order.id, 'message': 'Sale Order Created Successfully'}

        except Exception as e:
            return {'error': str(e)}

    # @validate_token
    # @http.route('/api/pos/order/create', type='json', methods=['POST'], auth="none")
    # def create_pos_order(self, **kwargs):
    #     try:
    #         data = request.httprequest.get_json()
    #         session_id = data.get('session_id')
    #         order_lines = data.get('order_lines', [])
    #         payment_lines = data.get('payment_lines', [])
    #         amount_return = data.get('amount_return', 0.0)
    #         user_id = data.get('user_id')
    #
    #         if not session_id:
    #             return {'error': 'Missing field: session_id'}
    #         if not order_lines:
    #             return {'error': 'Order lines cannot be empty'}
    #         if not user_id:
    #             return {'error': 'Missing field: user_id'}
    #
    #         # Validate POS session
    #         pos_session = request.env['pos.session'].sudo().search([('id', '=', session_id)], limit=1)
    #         if not pos_session:
    #             return {'error': 'POS session not found'}
    #
    #         product_lines_values = []
    #         payment_lines_values = []
    #         total_amount = 0.0
    #         total_tax = 0.0
    #         for line in order_lines:
    #             product_id = line.get('product_id')
    #             qty = line.get('quantity', 1)
    #             tax_ids = line.get('tax_ids', [])
    #             price_unit = request.env['product.product'].sudo().browse(product_id).lst_price
    #             price_subtotal = price_unit * qty
    #             price_subtotal_incl = line.get('price_subtotal_incl', price_subtotal)  # You can adjust this calculation if needed
    #
    #             product_lines_values.append((0, 0, {
    #                 'product_id': product_id,
    #                 'full_product_name': request.env['product.product'].sudo().browse(product_id).name,
    #                 'qty': qty,
    #                 'price_unit': price_unit,
    #                 'price_subtotal': price_subtotal,
    #                 'price_subtotal_incl': price_subtotal_incl,
    #                 'tax_ids': [(6, 0, tax_ids)],
    #             }))
    #
    #             total_amount += price_subtotal
    #
    #
    #         for line in payment_lines:
    #             payment_date = line.get('payment_date')
    #             payment_method = line.get('payment_method', 1)
    #             amount_paid = line.get('amount_paid')
    #
    #             payment_lines_values.append((0, 0, {
    #                 'payment_date': payment_date or datetime.now(),
    #                 'payment_method_id': payment_method,
    #                 'amount': amount_paid,
    #             }))
    #
    #         order_values = {
    #             'session_id': pos_session.id,
    #             'name': "New Order",
    #             'user_id': user_id,
    #             'partner_id': False,
    #             'date_order': fields.Datetime.now(),
    #             'amount_total': total_amount,
    #             'amount_tax': total_tax,
    #             'state': 'paid',
    #             'amount_paid': total_amount,
    #             'amount_return': amount_return,
    #             'lines': product_lines_values,
    #             'payment_ids': payment_lines_values
    #         }
    #
    #         pos_order = request.env['pos.order'].sudo().create(order_values)
    #         return {'success': True, 'order_id': pos_order.id, 'message': 'POS order created successfully'}
    #
    #     except Exception as e:
    #         return {'error': str(e)}

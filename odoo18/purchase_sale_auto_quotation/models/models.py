from odoo import api, models, SUPERUSER_ID, _, fields
from odoo.exceptions import AccessDenied
from odoo.http import request
import requests
import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    has_server = fields.Boolean(string="Has Server", default=False)
    server_url = fields.Char(string="Server Url")


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.model_create_multi
    def create(self, vals_list):
        orders = super().create(vals_list)
        for order in orders:
            if order.partner_id.has_server:
                sale_order_data = {
                    "vendor_id": order.partner_id.id
                }
                api_url = order.partner_id.server_url + "/api/sale/create_from_purchase"
                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }
                requests.post(api_url, json=sale_order_data, headers=headers
                              # , timeout=5
                              )
        return orders


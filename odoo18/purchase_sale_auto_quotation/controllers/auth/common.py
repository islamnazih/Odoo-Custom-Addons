import re
import functools
import logging
from odoo import fields,_
from odoo.http import Response, request, SessionExpiredException
from odoo.exceptions import AccessError, AccessDenied, ValidationError
_logger = logging.getLogger(__name__)

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def validate_token(func):
    @functools.wraps(func)
    def wrap(self, *args, **kwargs):
        access_token = request.httprequest.headers.get("Passkey")
        if not access_token:
            raise AccessError("Missing Access Token")
        access_token_data = request.env["smn.api.access.token"].sudo().search([('active', '=', True),("token", "=", access_token),("expiry_date",">=", fields.Datetime.now())], limit=1)
        if access_token_data.find_or_create_token(user_id=access_token_data.user_id.id).token != access_token:
            raise SessionExpiredException(_('Session Expired'))
        request.session.uid = access_token_data.user_id.id
        request.update_env(user=access_token_data.user_id.id)
        return func(self, *args, **kwargs)

    return wrap

# openrouter_integration/controllers/main.py
from odoo import http
from odoo.http import request
import requests
import json

class OpenRouterController(http.Controller):

    @http.route('/openrouter/chat', auth='public', type='json', methods=['POST'], csrf=False)
    def chat_with_openrouter(self, **kwargs):
        api_key = "<OPENROUTER_API_KEY>"  # ضع مفتاحك هنا أو خليه إعداد متغير
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "<YOUR_SITE_URL>",
            "X-Title": "<YOUR_SITE_NAME>",
        }
        payload = {
            "model": "liquid/lfm-7b",
            "messages": [
                {
                    "role": "user",
                    "content": kwargs.get('message', 'Hello!')
                }
            ],
        }

        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

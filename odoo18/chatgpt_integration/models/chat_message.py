from odoo import models, fields, api
from odoo.exceptions import UserError
import requests
import json

class ChatMessage(models.Model):
    _name = 'openrouter.chat.message'
    _description = 'OpenRouter Chat Message'

    message = fields.Text(string='Message', required=True)
    response = fields.Text(string='Response')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('error', 'Error')
    ], default='draft')

    def action_send_message(self):
        api_key = "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"  # ضع المفتاح الحقيقي هنا أو اعمله إعداد لاحقاً
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "<YOUR_SITE_URL>",
            "X-Title": "<YOUR_SITE_NAME>",
        }
        payload = {
            "model": "liquid/lfm-7b",
            "messages": [
                {"role": "user", "content": self.message}
            ],
        }
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            result = response.json()
            self.response = result['choices'][0]['message']['content']
            self.state = 'sent'
        except Exception as e:
            self.response = str(e)
            self.state = 'error'

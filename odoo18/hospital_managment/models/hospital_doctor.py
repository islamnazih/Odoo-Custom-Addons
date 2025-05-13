from odoo import models,fields,api


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'This for Hospital doctor'
    _inherit = ['mail.thread','mail.activity.mixin']
    _log_access = True   # Enable automatic Log tracking fields: (create_uid - create_date - write_uid - write_date)

    name = fields.Char(string='Name')
    specialization = fields.Char()
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    available_from = fields.Float()
    available_to = fields.Float()
    is_available = fields.Boolean(default=True)


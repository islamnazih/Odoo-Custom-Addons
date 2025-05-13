from email.policy import default

from odoo import models,fields,api


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'This for Hospital Patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _log_access = True   # Enable automatic Log tracking fields: (create_uid - create_date - write_uid - write_date)

    name = fields.Char(string='Name')
    gender = fields.Selection([('male','Male'),('female','Female')])
    birth_date = fields.Date(string='Birth Date')
    age = fields.Integer(string='Age')
    mobile = fields.Integer(string='Mobile',default='01')
    address = fields.Char(string='Address')
    blood_type = fields.Selection([('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')])
    image = fields.Binary(string='image')


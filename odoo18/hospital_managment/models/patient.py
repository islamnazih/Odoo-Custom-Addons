from odoo import models,fields,api


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'This for Hospital Patient'
    _log_access = True   # Enable automatic Log tracking fields: (create_uid - create_date - write_uid - write_date)

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male','Male'),('female','Female')])
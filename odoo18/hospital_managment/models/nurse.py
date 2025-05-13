from odoo import models,fields,api


class HospitalNurse(models.Model):
    _name = 'hospital.nurse'
    _description = 'Hospital nurse'

    name = fields.Char(string='Name', required=True)
    department_id = fields.Many2one('hospital.department', required=True)
    shift_start = fields.Many2one('hospital.operation.room', required=True)
    shift_end = fields.Datetime()
    mobile = fields.Char()
    assigned_patients = fields.Selection([('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='scheduled')
    notes = fields.Text()

from odoo import models,fields,api


class HospitalDepartment(models.Model):
    _name = 'hospital.department'
    _description = 'Hospital Department'
    _inherit = ['mail.thread','mail.activity.mixin']
    _log_access = True   # Enable automatic Log tracking fields: (create_uid - create_date - write_uid - write_date)

    name = fields.Char(required=True)
    description = fields.Text()
    responsible_doctor_id = fields.Many2one('hospital.doctor')
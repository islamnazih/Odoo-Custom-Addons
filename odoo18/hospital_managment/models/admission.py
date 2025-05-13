from odoo import models,fields,api


class HospitalAdmission(models.Model):
    _name = 'hospital.admission'
    _description = 'Hospital Admission'

    patient_id = fields.Many2one('hospital.patient', required=True)
    admission_date = fields.Date(default=fields.Date.today)
    discharge_date = fields.Date()
    room_number = fields.Char()
    reason = fields.Text()

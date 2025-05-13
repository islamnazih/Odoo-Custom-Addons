from odoo import models,fields,api


class HospitalMedicalRecord(models.Model):
    _name = 'hospital.medical.record'
    _description = 'Hospital Medical Record'

    patient_id = fields.Many2one('hospital.patient', required=True)
    diagnosis = fields.Text()
    prescription = fields.Text()
    record_date = fields.Date(default=fields.Date.today)
    doctor_id = fields.Many2one('hospital.doctor')
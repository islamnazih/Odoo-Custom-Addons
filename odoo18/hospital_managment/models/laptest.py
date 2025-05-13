from odoo import models,fields,api


class HospitalLabTest(models.Model):
    _name = 'hospital.lab.test'
    _description = 'Hospital Lab Test'

    patient_id = fields.Many2one('hospital.patient', required=True)
    test_type = fields.Char()
    test_date = fields.Date(default=fields.Date.today)
    result = fields.Text()
    doctor_id = fields.Many2one('hospital.doctor')
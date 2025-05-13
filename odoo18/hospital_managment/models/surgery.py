from odoo import models,fields,api


class HospitalSurgery(models.Model):
    _name = 'hospital.surgery'
    _description = 'Hospital Surgery'

    patient_id = fields.Many2one('hospital.patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', required=True)
    room_id = fields.Many2one('hospital.operation.room', required=True)
    scheduled_time = fields.Datetime()
    surgery_type = fields.Char()
    status = fields.Selection([('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='scheduled')
    notes = fields.Text()

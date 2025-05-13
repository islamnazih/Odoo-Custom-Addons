from odoo import models,fields,api


class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'This for Hospital appointment'
    _inherit = ['mail.thread','mail.activity.mixin']
    _log_access = True   # Enable automatic Log tracking fields: (create_uid - create_date - write_uid - write_date)

    patient_id = fields.Many2one('hospital.patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor',)
    appointment_date = fields.Date(required=True)
    appointment_time = fields.Float(required=True)
    status = fields.Selection(
        [
            ('new','New'),
            ('scheduled','Scheduled'),
            ('cancelled','Cancelled'),
        ],string='Status')
    notes = fields.Text()

    def print_test(self):
        for rec in self:
            print(self)
            print(rec.name)
            print(rec.id)
        print("TEST")
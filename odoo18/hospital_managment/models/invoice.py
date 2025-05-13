from odoo import models,fields,api


class HospitalInvoice(models.Model):
    _name = 'hospital.invoice'
    _description = 'Hospital Invoice'

    patient_id = fields.Many2one('hospital.patient', required=True)
    appointment_id = fields.Many2one('hospital.appointment', required=True)
    total_amount = fields.Float()
    paid_amount = fields.Float()
    payment_status = fields.Selection([('paid', 'Paid'), ('unpaid', 'Unpaid'), ('partially_paid', 'Partially Paid')], default='unpaid')
    invoice_date = fields.Date(default=fields.Date.today)
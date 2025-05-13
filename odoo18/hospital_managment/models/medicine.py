from odoo import models,fields,api


class Medicine(models.Model):
    _name = 'hospital.medicine'
    _description = 'This for Hospital medicine'
    _inherit = ['mail.thread','mail.activity.mixin']
    _log_access = True   # Enable automatic Log tracking fields: (create_uid - create_date - write_uid - write_date)

    name = fields.Char(string='Name')
    patient_id = fields.Many2one('hospital.patient',string='patient')
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')
    state = fields.Selection(
        [
            ('new','New'),
            ('scheduled','Scheduled'),
            ('in_progress','In Progress'),
            ('cancelled','Cancelled'),
        ],string='state')


    def print_test(self):
        for rec in self:
            print(self)
            print(rec.name)
            print(rec.id)
        print("TEST")
from odoo import models,fields,api


class HospitalOperationRoom(models.Model):
    _name = 'hospital.operation.room'
    _description = 'Hospital Operation Room'

    name = fields.Char(required=True)
    equipment = fields.Text()
    is_available = fields.Boolean(default=True)
    room_type = fields.Selection([('operation', 'Operation Room'), ('recovery', 'Recovery Room')])
    notes = fields.Text()
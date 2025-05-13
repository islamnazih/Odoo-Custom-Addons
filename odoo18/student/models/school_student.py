from odoo import models, fields, api

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    grade = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ], string="Grade")
    notes = fields.Text(string="Notes")
    user_id = fields.Many2one('res.users', 'Users', ondelete='cascade')
    user_ids = fields.Many2many('res.users', string='Related Users')

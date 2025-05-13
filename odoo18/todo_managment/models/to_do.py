from odoo import models,fields,api
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError, RedirectWarning
from odoo.tools import SQL, Query


class Todo(models.Model):
    _name = "todo.task"
    _description = "Task Managment"

    task_name = fields.Char(string='Task name')
    assign_to = fields.Char(string='Assign')
    description = fields.Text(string = 'description')
    duedate = fields.Date(string='Date')
    status = fields.Selection([('new','New'),('in_progress','In progress'),('completed','Completed')])

    @api.constrains('task_name','assign_to')
    def _check_custom_constraint(self):
        for record in self:
            if not record.task_name or not record.assign_to:
                raise ValidationError("البتاع فاضي")



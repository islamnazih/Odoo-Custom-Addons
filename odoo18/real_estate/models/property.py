import typing

from odoo import api,fields,models
from odoo.api import ValuesType
from odoo.exceptions import ValidationError
from odoo.tools import Query


class Property(models.Model):
    _name = 'property'
    _description = 'Property'

    name = fields.Char(required=1, default='New')
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(digits=(0, 5))
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
        ],
        default='north'
    )

    #
    # @api.constrains('bedrooms','garage')
    # def check_bedrooms(self):
    #     for rec in self:
    #         if rec.bedrooms == 0:
    #             raise ValidationError('Enter the bedrooms')
    #
    #
    #
    #  #CRUD operation    #انا بضيف لوجيك علي الانشاء من خلال هنا
    # @api.model_create_multi
    # def create(self,vals):
    #     res = super(Property, self).create(vals)
    #     print('create Method')
    #     #d
    #     return res
    #
    # def _search(self, domain, offset=0, limit=None, order=None) -> Query:
    #     res = super(Property, self)._search(domain, offset=0, limit=None, order=None)
    #     print('Search Method')
    #     return res
    #
    # def write(self, vals) -> typing.Literal[True]:
    #     res = super(Property, self).write(vals)
    #     print('write Method')
    #     return res
    #
    #
    #
    # def unlink(self):
    #     res = super(Property, self).unlink()
    #     print('unlink Method')
    #     return res

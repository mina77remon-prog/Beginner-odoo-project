from odoo import models, fields


class User(models.Model):
    _name = 'todo.user'
    _description = "To Do Task User"


    name = fields.Char(required=True)
    phone = fields.Char()
    address = fields.Char()

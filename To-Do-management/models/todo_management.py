from odoo import models, fields, api


class TodoManagement(models.Model):
    _name = 'to.do'
    _description = 'To Do Task'
    _inherit = ['mail.thread','mail.activity.mixin']

    task_name = fields.Char(required=True, default='Task', size=10)
    due_date = fields.Date(tracking=True)
    status = fields.Selection([
        ('new','New'),
        ('in_progress', 'In progress'),
        ('complete','Complete'),
    ], default='new',tracking=True)
    description = fields.Text()
    assign_to = fields.Char(related='user_id.name',store=True)

    user_id = fields.Many2one('todo.user')

    _sql_constraints = [
        ('task_name_unique','unique("task_name")','This name already exists!'),
    ]


    @api.onchange('status')
    def _onchange_status(self):
        return{'warning': {'title': 'Warning', 'message': 'You have changed the status!', 'type': 'notification'}}


    def action_new(self):
        for rec in self:
            rec.status = 'new'

    def action_in_progress(self):
        for rec in self:
            rec.status = 'in_progress'

    def action_complete(self):
        for rec in self:
            rec.status = 'complete'

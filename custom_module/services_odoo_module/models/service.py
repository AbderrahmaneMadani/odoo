from odoo import models, fields

class Service(models.Model):
    _name = 'services.service'
    _description = 'Service'

    #TODO other fileds go here.

    name = fields.Char(string='Service Name', required=True)
    description = fields.Text(string='Description')
    category_id = fields.Many2one('services.category', string='Category', required=True)

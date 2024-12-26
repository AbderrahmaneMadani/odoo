from odoo import models, fields

class ServiceCategory(models.Model):
    _name = 'services.category'
    _description = 'Service Category'

    name = fields.Char(string='Category Name', required=True)
    service_ids = fields.One2many('services.service', 'category_id', string='Services')

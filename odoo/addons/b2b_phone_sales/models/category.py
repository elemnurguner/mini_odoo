from odoo import models, fields

class Category(models.Model):
    _name = 'b2b.category'
    _description = 'Product Category'

    name = fields.Char(string="Category Name", required=True)
    description = fields.Text(string="Description")
    created_at = fields.Datetime(string="Created At", default=fields.Datetime.now)

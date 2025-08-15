from odoo import models, fields

class Product(models.Model):
    _name = 'b2b.product'
    _description = 'Product'

    name = fields.Char(string="Product Name", required=True)
    category_id = fields.Many2one('b2b.category', string="Category")
    price = fields.Float(string="Price")
    description = fields.Text(string="Description")
    created_at = fields.Datetime(string="Created At", default=fields.Datetime.now)

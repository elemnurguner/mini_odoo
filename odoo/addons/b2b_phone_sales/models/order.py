from odoo import models, fields

class Order(models.Model):
    _name = 'b2b.order'
    _description = 'Order'

    name = fields.Char(string="Order Reference", required=True)
    customer_id = fields.Many2one('b2b.customer', string="Customer")
    order_date = fields.Datetime(string="Order Date", default=fields.Datetime.now)
    product_ids = fields.Many2many('b2b.product', string="Products")
    total_amount = fields.Float(string="Total Amount")

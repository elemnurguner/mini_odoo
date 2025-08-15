from odoo import models, fields

class Customer(models.Model):
    _name = 'b2b.customer'
    _description = 'Customer'

    name = fields.Char(string="Customer Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    created_at = fields.Datetime(string="Created At", default=fields.Datetime.now)

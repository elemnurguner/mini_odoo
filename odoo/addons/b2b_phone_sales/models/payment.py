from odoo import models, fields

class Payment(models.Model):
    _name = 'b2b.payment'
    _description = 'Payment'

    order_id = fields.Many2one('b2b.order', string="Order")
    payment_date = fields.Datetime(string="Payment Date", default=fields.Datetime.now)
    amount = fields.Float(string="Amount")
    payment_type = fields.Selection([('cash', 'Cash'), ('bank', 'Bank')], string="Payment Type")

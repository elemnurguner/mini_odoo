from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    phone_extension = fields.Char(string="Phone Extension")

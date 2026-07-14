from odoo import fields, models


class FaultLog(models.Model):
    _name = 'fault.log'
    _description = 'Equipment Fault Log'
    _order = 'date_reported desc'

    name = fields.Char(string='Fault Title', required=True)
    product_id = fields.Many2one('product.product', string='Product/Machine')
    severity = fields.Selection(
        [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        string='Severity', default='low', required=True,
    )
    description = fields.Text(string='Description')
    date_reported = fields.Date(string='Date Reported', default=fields.Date.context_today)
    state = fields.Selection(
        [('new', 'New'), ('investigating', 'Investigating'), ('resolved', 'Resolved')],
        string='Status', default='new', required=True,
    )

from odoo import fields, models


class FootballTeam(models.Model):
    _name = 'football.team'
    _description = 'Football Team'

    name = fields.Char(required=True)
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one(
        'res.country.state', string='State',
        domain="[('country_id', '=?', country_id)]",
    )
    founded_year = fields.Integer(string='Founded Year')
    player_ids = fields.One2many('football.player', 'team_id', string='Players')

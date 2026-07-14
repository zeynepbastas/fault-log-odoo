from odoo import fields, models


class FootballPlayer(models.Model):
    _name = 'football.player'
    _description = 'Football Player'

    name = fields.Char(required=True)
    team_id = fields.Many2one('football.team', string='Team')
    position = fields.Selection(
        [
            ('goalkeeper', 'Goalkeeper'),
            ('defender', 'Defender'),
            ('midfielder', 'Midfielder'),
            ('forward', 'Forward'),
        ],
        string='Position',
    )
    jersey_number = fields.Integer(string='Jersey Number')
    age = fields.Integer()
    market_value = fields.Float(string='Market Value')
    photo = fields.Binary(string='Photo', attachment=True)

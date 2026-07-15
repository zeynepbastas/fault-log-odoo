{
    'name': 'Football Manager',
    'version': '19.0.1.0.0',
    'summary': 'Manage football teams and their players',
    'description': """
Football Manager
================
A small practice module for Many2one/One2many relationships:
teams have many players, each player belongs to one team.
""",
    'category': 'Sports',
    'author': 'Zeynep Bastas',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/football_team_views.xml',
        'views/football_player_views.xml',
        'views/football_manager_menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

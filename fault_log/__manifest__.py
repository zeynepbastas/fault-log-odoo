{
    'name': 'Fault Log',
    'version': '19.0.1.0.0',
    'summary': 'Log and track recurring equipment faults by product and severity',
    'description': """
Fault Log
=========
Track equipment/machine faults: what broke, how severe, and its resolution state.
""",
    'category': 'Manufacturing',
    'author': 'Zeynep Bastas',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/fault_log_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

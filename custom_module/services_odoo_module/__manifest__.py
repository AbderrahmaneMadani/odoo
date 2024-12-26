{
    'name': 'Services Management',
    'version': '1.0',
    'summary': 'Module to manage services and their categories',
    'category': 'Services',
    'author': 'Madani',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/services_data.xml',
        'views/service_views.xml',
    ],
    'installable': True,
    'application': True,
}

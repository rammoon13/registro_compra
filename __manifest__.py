# registro_compra/__manifest__.py
{
    'name': 'Registro de Compra',
    'version': '1.0',
    'summary': 'Módulo para gestionar el registro de compras realizadas por empleados',
    'category': 'Sales',
    'author': 'Tu Nombre',
    'website': 'https://tuweb.com',
    'license': 'LGPL-3',
    'depends': ['base', 'hr', 'product'],
    'icon': '/registro_compra/static/description/icon.png',
    'data': [
        'security/ir.model.access.csv',
        'views/registro_compra_views.xml',
    ],
    'application': True,
    'installable': True,
}

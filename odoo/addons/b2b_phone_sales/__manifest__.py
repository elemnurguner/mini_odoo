{
    'name': 'B2B Phone Sales',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': 'B2B Sales Module',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/category_views.xml',
        'views/product_views.xml',
        'views/customer_views.xml',
        'views/order_views.xml',
        'views/payment_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}

# -*- coding: utf-8 -*-
{
    'name': "Investimentoo",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",    
    'category': 'Sales/Investimentos',
    'version': '0.1',
    'application': True,
    'installable': True,    
    'depends': ['base', 'web'],    
    'data': [
        # 'security/ir.model.access.csv',
        'views/brapi.xml',
        'views/carteiras.xml',
        'views/ativos.xml',
        'views/fechamentos.xml',        
        'views/views.xml',        
    ]
}


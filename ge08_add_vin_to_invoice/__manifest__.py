{
    "name": "GE8 Add VIN to Invoice",
    
    "summary": "Automatically adds the VIN to each invoice",
    
    "description": """
    Motorcycle Registry
====================
This Module is used to add VIN information to customer invoices.
    """,
    
    "version": "0.1",
    
    "category": "Kauil/Registry",
    
    "license": "OPL-1",
    
    "depends": ["base", "motorcycle_registry", "account", "purchase", "sale"],
    
    "data": [
        "views/account_move_form_views.xml"
    ],
    
    "demo": [
        
    ],
    
    "author": "kauil-motors",
    
    "website": "www.odoo.com",

    "installable": True,
    
    "application": True,
    
}
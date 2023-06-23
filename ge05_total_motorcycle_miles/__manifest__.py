{
    "name": "Odometer",
    
    "summary": "Total motorcycle miles",
    
    "description": 'distance calculator widget',
    
    "version": "0.1",
    
    "category": "Kauil/Registry",
    
    "license": "OPL-1",
    
    "depends": ["motorcycle_registry","website"],
    
    "data": [
        "views/snippets/s_odometer.xml",
        "views/snippets/snippets.xml",
        
    ],
    
    "demo": [

    ],
    
    'assets':{
        'web.assets_frontend':[
            "ge05_total_motorcycle_miles/static/src/snippets/s_odometer/odometer.js",
            "ge05_total_motorcycle_miles/static/src/snippets/s_odometer/odometer-options.js",
        ]
    },
    
    "author": "kauil-motors",
    
    "website": "www.odoo.com",
    
    "application": True,
    
}
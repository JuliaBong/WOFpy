from flask import Flask

import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)
    
    from wofpy_flask.views.rest import rest
    app.register_module(rest)
    
    from wofpy_flask.views.wsdl import wsdl
    app.register_module(wsdl)
    
    return app

#app = Flask(__name__)
#app.config.from_object(config.Config)

#import views
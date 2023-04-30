from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

# create the extension
db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    #Configuracion del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRETE_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///todolist.db"

    )

    # initialize the app with the extension
    db.init_app(app)

    # Registrar  Blueprint
    from . import todo
    app.register_blueprint(todo.bp)

    # Registrar Auth
    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()
    
    return app
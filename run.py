from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'rfe2fcdfdafdf/fdfd'

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from main import main as main_blueprint

app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)

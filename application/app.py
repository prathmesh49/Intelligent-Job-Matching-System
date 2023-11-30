from flask import Flask
from flask_migrate import Migrate
from myapp.models import db

app = Flask(__name__)
app.debug = True

# Replace 'mysql+mysql connector' with the appropriate MySQL dialect for your setup.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:4355@localhost/jobposting'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Migrate
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/home")
def hello_world():
    return "hello world"


if __name__ == '__main__':
    app.run()

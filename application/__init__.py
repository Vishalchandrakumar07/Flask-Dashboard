from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Corrected configuration key
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expensesDB.db"
app.config["SECRET_KEY"] = (
    "drvuurrtduyfdvgnfrdvbfdbvcsyjgvtfhtcjhvtdrfdgjfthhhftd234567"
)


db = SQLAlchemy(app)

from application import routes

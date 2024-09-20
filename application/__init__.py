from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Corrected configuration key
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://default:3RPk1VeSxaCJ@ep-shy-glade-a4o8y8my-pooler.us-east-1.aws.neon.tech:5432/verceldb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "drvuurrtduyfdvgnfrdvbfdbvcsyjgvtfhtcjhvtdrfdgjfthhhftd234567"



db = SQLAlchemy(app)

from application import routes

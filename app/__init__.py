from flask import Flask
from .config import config
from .models import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app) 

with app.app_context():
    print("start create_all...")
    db.create_all()
    print("end create_all...")

#with app:
#    db.create_all()
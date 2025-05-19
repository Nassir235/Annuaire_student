from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, models, routes, db


print('in run.py...') 

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print('db.create_all()...finished') 

    print('running....') 
    app.run(debug=True)

#FLASK_APP=run.py flask run --host=0.0.0.0
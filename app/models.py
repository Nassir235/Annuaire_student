from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(80), nullable=False)
    last_name=db.Column(db.String(80), nullable=False)
    phone=db.Column(db.String(80), nullable=False) # on vient d'ajouter
    departement=db.Column(db.String(80), nullable=False) # on vient d'ajouter
    filiere=db.Column(db.String(80), nullable=False)# on vient d'ajouter
    Level=db.Column(db.String(80), nullable=False) # on vient d'ajouter
    academic_year=db.Column(db.String(80), nullable=False) #on vient d'ajouter
    #mdp=db.Column(db.String(120), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Student %r>' % self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


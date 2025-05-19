import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    
    #config mysql installation locale 
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:266139@db/annuaire_student'
    
    #config mariadb installation locale 
    #SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://root:266139@localhost/annuaire_student'
    
    #config contenaire mariadb nom:db
    SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://root:266139@db/annuaire_student'


    #config sqlite installation locale or via contenaire 
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///annuaire_student.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = Config()
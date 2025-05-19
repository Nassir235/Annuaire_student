from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    first_name = StringField('Prénom', validators=[DataRequired()])
    last_name = StringField('Nom', validators=[DataRequired()])
    id = IntegerField('Numéro d\'étudiant',validators=[DataRequired()])
    phone = StringField('Telephone', validators=[DataRequired()])
    departement = StringField('Departement', validators=[DataRequired()])
    filiere = StringField('Filiere', validators=[DataRequired()])
    Level = StringField('Niveau de etudiant', validators=[DataRequired()])
    academic_year = StringField('annee academique', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    #mdp =  PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Enregistrer')


class LoginForm(FlaskForm):
    last_name = StringField('Nom', validators=[DataRequired()])

    mdp = PasswordField('password', validators=[DataRequired()])

    submit = SubmitField('Login')

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, NumberRange, URL, Optional


class AddCupcakeForm(FlaskForm):
    """Form for adding pets to the database"""

    flavor = StringField('Flavor', validators=[InputRequired(message="Flavor cannot be blank")])
    size = SelectField('Size', validators=[InputRequired(message="Size cannot be blank")], choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])
    rating = FloatField('Rating', validators=[Optional(), NumberRange(min=1, max=10, message='The rating must be between %(min)s and %(max)s')])
    image = StringField('Image', validators=[Optional(), URL(require_tld=True, message='Please provide a valid URL address or leave the field empty')] )
    
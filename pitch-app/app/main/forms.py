from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    category = StringField('Pitchcategory',validators=[Required()])
    pitches_destription= TextAreaField('User pitch')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):

    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
   
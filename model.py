from wtforms import Form, IntegerField, TextAreaField, validators

class InputForm(Form):
    text_input = TextAreaField(
        label='Input text',
        default="""
In 1884,  meridian time personnel met
in Washington to change Earth time.
First words said was that only 1 day
could be used on Earth to not change
the 1 day bible. So they applied the 1
day  and  ignored  the  other  3 days.
The bible time was wrong then and it
proved wrong today. This a major lie
has so much evil feed from it's wrong.
No man on Earth has no belly-button,
it proves every believer on Earth a liar.""",
        validators=[validators.InputRequired()])

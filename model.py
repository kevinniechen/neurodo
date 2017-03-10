from wtforms import Form, TextAreaField, validators


class InputForm(Form):
    text_input = TextAreaField(
        label='Input text',
        default="""""",
        validators=[validators.InputRequired()])

from model import InputForm
from flask import Flask, render_template, request, Response
from compute import unpack_data, unpack_to_set, number_of_words, calc_delusions
import csv, io, os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result_delusions = calc_delusions(unpack_data(form.text_input))
        return render_template('results.html', form=form, result_delusions=result_delusions)
    else:
        return render_template('view.html', form=form)

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
     app.debug = True
     port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=port)

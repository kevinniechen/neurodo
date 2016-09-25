from model import InputForm
from flask import Flask, render_template, request, Response
from compute import unpack_data, unpack_to_set, number_of_words, calc_delusions, calc_ml, calc_basics, calc_coherence, calc_phrase_len, calc_determiners
import csv, io, os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result_coherence = calc_coherence(unpack_data(form.text_input))
        result_determiners = calc_determiners(unpack_data(form.text_input))
        result_phrase_length = calc_phrase_len(unpack_data(form.text_input))
        result_delusion_dict = calc_delusions(unpack_data(form.text_input))
        result_a1 = result_delusion_dict['time']
        result_a2 = result_delusion_dict['self']
        result_a3 = result_delusion_dict['surveillance']
        result_a4 = result_delusion_dict['unfair']
        result_a5 = result_delusion_dict['mind_control']
        result_a6 = result_delusion_dict['alien']
        result_ml = calc_ml(result_coherence, result_determiners,
            result_phrase_length,
            result_a1, result_a2, result_a3, result_a4, result_a5, result_a6)
        return render_template('results.html', form=form, result_ml=result_ml)
    else:
        return render_template('view.html', form=form)

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
     app.debug = True
     port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=port)

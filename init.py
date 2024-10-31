import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template
from flask import request
from days_calculator import gen_days
from included_dial import gen_sundial
from Planets import planet_data 

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/get_plot', methods= ['GET', 'POST'])
def get_plot():
    if request.method == "POST":
        year_1 = int(request.form['year_1'])
        month_1 = int(request.form['month_1'])
        day_1 = int(request.form['day_1'])
        lat = float(request.form['lat'])
        height = float(request.form['height']) / 10
        time = gen_days(day_1, month_1, year_1)
        planet = str(request.form['planet_name'])
        obl, per = planet_data(planet)
        gen_sundial(obl, per, lat, time, height)
        return render_template('index.html', plot_url = "static/my_plot.png")
        
    else:
        return render_template('index.html')

app.secret_key = "Honeycombs"

if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
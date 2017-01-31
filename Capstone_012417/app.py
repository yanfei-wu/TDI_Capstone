from flask import Flask,render_template, redirect
import pandas as pd
from pandas import DataFrame
from bokeh.plotting import figure, output_file, show
from bokeh.io import vform
from bokeh.models.widgets import RadioButtonGroup
from bokeh.embed import components
#from bokeh.sampledata import us_states

app = Flask(__name__)
selector = {}

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')

def simpleLine():
    fig=figure(title="Sensor data")
    fig.line([1,2,3,4],[2,4,6,8])
    script,div=components(fig)
    return render_template('index.html',div=div,script=script)
    output_file("index.html")
    #show(fig)

fig=figure(title="Sensor data")
fig.line([1,2,3,4],[2,4,6,8])
script,div=components(fig)

if __name__ == "__main__":
    app.run(debug=True)

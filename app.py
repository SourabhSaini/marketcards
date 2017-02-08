from flask import Flask, redirect, url_for, request, render_template
from nsetools import Nse
import ast

app = Flask(__name__)

@app.route('/')
def index():
    nse = Nse()
    top_gainers = nse.get_top_gainers()
    top_losers = nse.get_top_losers()
    return render_template('marketcards.html', gainers=top_gainers, losers=top_losers)

@app.route('/all_data.html', methods=['POST','GET'])
def all_data():
    all = ast.literal_eval(request.args.get('sym'))
    return render_template('all_data.html', data=all)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, url_for
import back.db as db
import json

app = Flask(__name__, template_folder='templates')
with app.test_request_context():
    url_for('static', filename='static')

graph = db.connect_to_db()

@app.route('/')
def index():
    user = 'You'
    return render_template('index.html', user=user)


@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/receiver', methods= ['POST'])
def get_histogram():
    #data = db.get_histogram_of_relation(graph)
    return '"data": 4'




if __name__ == "__main__":

    app.run(debug=True)

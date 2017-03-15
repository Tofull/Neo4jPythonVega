from flask import Flask, render_template, url_for


app = Flask(__name__, template_folder='templates')
with app.test_request_context():
    url_for('static', filename='static')


#Bootstrap(app)

@app.route('/')
def index():
    user = 'You'
    return render_template('index.html', user=user)


if __name__ == "__main__":
    app.run(debug=True)

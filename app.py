from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello Safi Khan!</h1>'


@app.route('/about')
def about_page():
    return render_template('about.html', name="Aleena") # name is acting as a variable

@app.route('/age')
def age_page():
    return "You are 10 years old"

@app.route('/location')
def location_page():
    return "Location is changed!"


if __name__ == '__main__':
    app.run(debug=True) # Because Server does not reload on change

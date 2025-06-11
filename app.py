from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello Safi Khan!</h1>'


@app.route('/about')
def about_page():
    return render_template('about.html', name="Aleena")


if __name__ == '__main__':
    app.run(debug=True)

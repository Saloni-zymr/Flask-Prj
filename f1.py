from flask import Flask, render_template

app = Flask(__name__)


# / -> endpoint
@app.route("/")
def hello():
    # return 'Hello !'
    return render_template('index.html')


@app.route("/about")
def about():
    name = "Saloni"
    return render_template('about.html', name=name)


app.run(debug=True)


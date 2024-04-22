from flask import Flask, render_template


app = Flask("website")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("api/v1/<station>/<date>")
def api(station, date):
    pass


app.run(debug=True)
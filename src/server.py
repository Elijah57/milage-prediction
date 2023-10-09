from flask import Flask, render_template, request, url_for
from datetime import datetime
from joblib import load

app = Flask(__name__)

@app.route("/")
def home():
    year = datetime.now().year
    return render_template("main.html", current_year=year)

@app.route("/about-us")
def about_page():
    year = datetime.now().year
    return render_template("about.html", current_year=year)

@app.route("/predict_milage", methods=["GET", "POST"])
def predict_data():

    year = datetime.now().year
    model = load("model/carModel.joblib")
    results_predict = None
    if request.method == "POST":

        cylinders = int(request.form["cylinders"])
        displacement = float(request.form["displacement"])
        hp = float(request.form["hp"])
        weight = float(request.form["weight"])
        acceleration = float(request.form["acceleration"])
        
        data = [cylinders, displacement, hp, weight, acceleration]
        results_predict = model.predict([data])

    return render_template("form.html", current_year=year, results=results_predict)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/recommendation")
def recommendation():
    return render_template("recommendation.html")

@app.route("/review")
def review():
    return render_template("review.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()
    app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))
from flask import Flask, request, render_template

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

if __name__ == "__main__":
    app.run()
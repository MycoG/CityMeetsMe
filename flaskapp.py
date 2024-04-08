from flask import Flask, request, render_template, url_for
from formula import setData, findRecc, outputRecc

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/recommendation", methods=["GET","POST"])
def recommendation():
    if request.method == "POST":
        if request.form['submit'] != "reset":
            a = request.values.get('attr1')
            b = request.values.get('attr2')
            c = request.values.get('attr3')
            print(a, b, c)
            return render_template("recommendation.html", val1=a, val2=b, val3=c)
        else:
            #reset the template
            return render_template("recommendation.html", val1=0.5, val2=0.5, val3=0.5)
    return render_template("recommendation.html", val1=0.5, val2=0.5, val3=0.5)

@app.route("/review")
def review():
    return render_template("review.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()
    app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))
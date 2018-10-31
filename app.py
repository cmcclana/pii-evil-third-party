from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/', methods=["POST", "GET"]) 
def pii():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        return render_template('index.html', first_name=first_name, last_name=last_name)
    return render_template('index.html', first_name="", last_name="")


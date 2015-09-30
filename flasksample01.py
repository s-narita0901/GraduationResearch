from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def todb():
    return render_template("todb.html")

app.debug=True
app.run()

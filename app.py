from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def anil():
    return render_template("index.html")
app.run()
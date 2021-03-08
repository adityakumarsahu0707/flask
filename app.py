from flask import Flask, render_template
app=Flask('test')

@app.route('/')
def index():
    return "Flask Model"
    #return("Index page!!")
@app.route("/test")
def test():
    return render_template("test.html")

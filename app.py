from flask import Flask
app=Flask('test')

@app.route('/')
def index():
    return "Flask Model"
    #return("Index page!!")

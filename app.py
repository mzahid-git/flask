from flask import Flask
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application
'''

app=Flask(__name__)

@app.route("/") # "/" is just the home page
def welcome():
    return "I can't wait for witcher 4"

@app.route("/index") # "/" is just the home page
def index():
    return "This is the index page"

if __name__=='__main__':
    app.run(debug=True) # debug=True is used so that everytime a change occurs in .py, the server will
    # automatically get restarted
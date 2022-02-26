# Create a virtual environment
# import Flask from flask module
# Then initialize our app instance using the imported Flask
from distutils.log import debug
from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)


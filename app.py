import sqlalchemy
from flask import Flask, render_template, redirect

#### Setup Flask ####
app = Flask(__name__)

# Use PyMongo to establish Mongo connection

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

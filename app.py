import sqlalchemy
from flask import Flask, render_template, redirect
import load as l

#### Setup Flask ####
app = Flask(__name__)

# Use PyMongo to establish Mongo connection

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Run this to generate the parks.json file
    # l.process()

    # Load parks.json into POSTGRES

    # Return template and data
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

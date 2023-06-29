from flask import Flask,render_template,request
from flask_cors import CORS,cross_origin

from aaroh import *
from avroh import *

app = Flask(__name__)

@app.route("/", methods = ['GET'])
@cross_origin()

def homepage():
    return render_template("homepage.html")


@app.route("/generate_sargam",methods = ["POST"])
@cross_origin()

def generate_sargam():
    if request.method == "POST":
        try:
            pattern = request.form['content'].split(" ")
            aaroh = get_aaroh(pattern)
            aaroh= aaroh.tolist()
            avroh = get_avroh(pattern)
            avroh = avroh.tolist()
            return render_template("result.html",aaroh = aaroh,avroh=avroh)
        except:
            return "OOPS ! Something went wrong. Kindly check your swaras"
    else:
        return render_template("homepage.html")

if __name__ == "__main__":
    app.run()


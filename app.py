from flask import *
import pymysql
# intialize the application
app=Flask(__name__)


# define the route/endpoint
@app.route("/api/signup",methods=["post"])
# define the function
def signup():
    # get user inputs from the form
    username= request.form["username"]
    email=request.form["email"]
    password=request.form["password"]
    phone=request.form["phone"]

    # connection to database 
    connection= pymysql.connect(
        host="root",
        user="localhost",
        password="",
        database="modcomfrancis",

    )


# run the application
app.run(debug=True)
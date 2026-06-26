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
        host="localhost",
        user="root",
        password="",
        database="modcomfrancis",

    )
    # define the cursor
    cursor=connection.cursor()
    
    # define sql to insert users
    sql="insert into users(username,password,email,phone) values(%s,%s,%s,%s)"
    # define your data
    # NB:coming from step 3
    data=(username,password,email,phone)
    # execute/run query
    cursor.execute(sql,data)
    # commtit/save changes
    connection.commit()
    return jsonify({"message":"user registration successfully"})


# member signin/login
 # define route/endpoint
@app.route("/api/signin",methods=["POST"])
# define the function
def signin():
    # get user inputs from the form
    email= request.form["email"]
    password=request.form["password"]

    # connection to database
    connection= pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="modcomfrancis",
    )
    # define the cursor
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    # define sql to select users
    sql="select * from users where email =%s and password=%s"
    # define your data
    # NB: its coming from step 3
    data = (email , password)
    # execute/run query
    cursor.execute(sql,data)
    # wrong email and password
    if cursor.rowcount==0 :
        return jsonify({"message":"invalid email or password"
        })
    # correct email and password
    if cursor.rowcount==1 :
        # fetch the user,
        user = cursor.fetchone()
        return jsonify ({"message":"login successful",
                         "user":user})


















# run the application
app.run(debug=True)
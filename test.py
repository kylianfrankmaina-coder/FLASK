from flask import *
# intialize the application
app=Flask(__name__)
# define route/end point
@app.route("/api/home")
# define function
def home():
    return jsonify({"message":"welcome home"})


@app.route("/api/services")
def services():
    return jsonify({"message":"welcome to services"})


@app.route("/api/about")
def about():
    return jsonify({"message":"welcome to about"})

@app.route("/api/contact")
def contact():
    return jsonify({"message":"contact us for more information"})

@app.route("/api/products")
def products():
    return jsonify({"message":"products available"})

@app.route("/api/students")
def students():
    return jsonify({"message":"list of students"})

@app.route("/api/courses")
def courses():
    return jsonify({"message":"courses offered"})

@app.route("/api/teachers")
def teachers():
    return jsonify({"message":"list of teachers"})

@app.route("/api/news")
def news():
    return jsonify({"message":"latest news update"})

@app.route("/api/gallery")
def gallery():
    return jsonify({"message":"gallery images"})

@app.route("/api/faq")
def faq():
    return jsonify({"message":"Frequently asked questions"})

@app.route("/api/profile")
def profile():
    return jsonify({"message":"student profile information"})

@app.route("/api/events")
def events():
    return jsonify({"message":"upcoming events"})

@app.route("/api/library")
def library():
    return jsonify({"message":"library resources available"})

@app.route("/api/addition",methods=["POST"] )
def addition():
    number1=request.form["number1"]
    number2=request.form["number2"]
    answer=int(number1)+int(number2)
    return jsonify({"Answer":answer})

@app.route("/api/subtract",methods=["POST"])
def subtract():
    number1=request.form["number1"]
    number2=request.form["number2"]
    answer=int(number1)-int(number2)
    return jsonify({"Answer":answer})

@app.route("/api/multiplication",methods=["POST"])
def multiplication():
    number1=request.form["number1"]
    number2=request.form["number2"]
    answer=int(number1)*int(number2)
    return jsonify({"Answer":answer})

@app.route("/api/division",methods=["POST"])
def division():
    number1=request.form["number1"]
    number2=request.form["number2"]
    answer=int(number1)/int(number2)
    return jsonify({"Answer":answer})







# run the application
app.run(debug=True)
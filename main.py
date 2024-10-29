#import the flask library for usage!
from flask import Flask, request

#create an instance of the flask server
# as the root director within 'main.py'
app = Flask(__name__)

#create some routes
#when working with Flask, we will be using decorators '@'
@app.route('/')
def displayHomepage(): 
    return"<h1>Welcome to your first website!</h1>"

@app.route('/route1')
def route1Info():
    return "<h3> congrats on making route 1! </h3>"

#WHY = we need to be able to collect data from users!
#Module 1.5
#1. Utilize route variables to GET request data from the URL
#2. Utilize form data to collect large swaths of info at once!

#<> denote a route variable! meaning it is a placeholder for some valuble in the URL
# @app.route('/profile/<users_name>')
# def profile(users_name):
#     return "<h2> Hello " + users_name + "!</h2>"
#every route needs to have a function like above^^.

#retry with cleaner way:
@app.route('/profile/<users_name>')
def profile(users_name):
    return f"Why hello there {users_name}!"

#cleaner way:
@app.route('/date/<month>/<day>/<year>')
def display_given_date(month, day, year):
    return f"{month} / {day} / {year}"

# creating a <form>!
# all forms require a submission button.
form_data = f"""
    <form action="/results" method="GET">
        What's your favorite pizza flavor?
        <input type = "text" name = "pizza_flavor">
        <br>
        What's your favorite crust type?
        <input type = "text" name = "crust">
        <input type = "submit" value = "submit pizza!">
    </form>
""" 

@app.route('/form_example')
def first_form():
    return form_data

@app.route('/results', methods=['GET'])
def simple_pizza_results():
    pizza_flavor = request.args.get("pizza_flavor")
    crust = request.args.get("crust")
    return f"<h3> A {crust}-crust {pizza_flavor} pizza hass been ordered!</h3>"

# #Module 1.5 Question:
# plane_data = f"""
#     <form>
#         Departure
#         <input type="text" name="departure">
#         <br>
#         Destination
#         <input type="text" name="destination">
#         <br>
#         Class
#         <input type="text" name="class_type">
#         <input type = "submit" value = "submit">
#     </form>
# """

# @app.route('/plane_data')
# def plane_info():
#     return plane_data

#turn the server on for serving!



user_login = f"""
    <form action="/result" method="POST">
        <label>
            Username:
            <input type="text" name="user_name">
        </label>
        <label>
            Password: 
            <input type="password" name="user_password">
        </label>

        <input type = "submit" name="Login!">
    </form>
""" 

@app.route('/login')
def login():
    return user_login

@app.route("/result", methods=["GET","POST"])
def user_account():
    user_name = request.form.get("user_name")
    password = request.form.get("user_password")
    if user_name == password:
        return f'thanks for logging in {user_name}!'
    else:
        return  "Invalid username or password, please try again."



if __name__ == "__main__":
    app.run(debug=True, port=3000)

#thanks for logging in user_name

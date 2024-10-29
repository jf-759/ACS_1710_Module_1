# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/')
# def displayHomepage(): 
#     return"<h1>Welcome to your first website!</h1>"

# user_login = f"""
#     <form action="/result" method="POST">
#         <label>
#             Username:
#             <input type="text" name="user_name">
#         </label>
#         <label>
#             Password: 
#             <input type="password" name="user_password">
#         </label>

#         <input type = "submit" name="Login!">
#     </form>
# """ 

# @app.route('/login')
# def login():
#     return user_login

# @app.route("/result", methods=["GET","POST"])
# def user_account():
#     user_name = request.form.get("user_name")
#     password = request.form.get("user_password")
#     if user_name == password:
#         return f'thanks for logging in {user_name}!'
#     else:
#         return  "Invalid username or password, please try again."



# if __name__ == "__main__":
#     app.run(debug=True, port=3000)

def make_pizza(size, toppings, name):
    print(f"{name} ordered a {size} pizza with {toppings}.")

# Example usage
make_pizza(size="large", toppings="chicken, chopped garlic, onions, olives, and cheese", name="Jane")


def find_smallest_number(*args):
    return min(args)

# Calling the function with the specified values
smallest_number = find_smallest_number(11, 5, 21, 67, 3, 9)
print(f"The smallest number is: {smallest_number}")



def order_milk_tea(**kwargs):
    size = kwargs.get('size', 'medium')  
    has_milk = kwargs.get('has_milk', True)  
    has_boba = kwargs.get('has_boba', True)
    flavor = kwargs.get('flavor', 'original')  

    milk_option = "with milk" if has_milk else "without milk"
    boba_option = "with boba" if has_boba else "without boba"

    print(f"Ordered a {size} {flavor} iced milk tea {milk_option} and {boba_option}.")

# Calling the function with some example values
order_milk_tea(size="medium", has_milk=True, has_boba=False, flavor="strawberry")


#Named Parameters:

def divide(numerator, denominator):
    return numerator / denominator

answer = divide (12, 6)
print(answer)


def really_long_function(
        num_times,
        greeting,
        outro,
        age,
        show_greeting,
        show_outro):
    pass

really_long_function(
    num_times=10,
    greeting='hello',
    outro='goodbye',
    age=25,
    show_greeting=True,
    show_outro=False
)


#*args

#* it can hold a list a numbers without using []
# it can also be *nums
#works if it's all the same data
def add_all_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

answer = add_all_numbers(1, 2, 3, 4, 5)
print(answer)




#**kwargs
#works with all different types of data.
#key value pairs inputs

def print_user_attributes(**kwargs):
   for key, value in kwargs.items():
       print(key + ": " + str(value))

print_user_attributes(
    first_name='Meredith',
    last_name='Teo',
    name= 30
)
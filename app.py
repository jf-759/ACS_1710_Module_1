from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """ Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f"How did you know I liked {users_dessert}?"

@app.route('/madlibs/<adjective>/<noun>')
def madlibs_answer(adjective, noun):
    """Display a madlib that includes an adjective and a noun that the user provided."""
    return f"The {adjective} goose tried to tell a funny joke but the {noun} did not laugh."

@app.route('/multiply/<int:number1>/<int:number2>')
def multiply(number1, number2):
    """Display the two numbers given by the user, multiply them, and show the answer."""
    total = number1 * number2
    return f"The result of {number1} multiplied by {number2} is {total}."

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Repeat the word a given number of times, or show an error if the input is not valid."""
    try:
        n = int(n)
        result = ""

        for _ in range(n):
            result += word + " "

        return result.strip()

    except ValueError:
        return "Invalid input. Please try again by entering a word and a number. Thank you!"

@app.route('/dicegame')
def dicegame():
    """Roll a die and determine if the user wins or loses."""
    roll = random.randint(1, 6)

    if roll == 6:
        result = f"You rolled a {roll}. You won! Yay!"
    
    else:
        result = f"You rolled a {roll}. Sorry, you lost."

    return result


if __name__ == '__main__':
    app.run(debug=True)


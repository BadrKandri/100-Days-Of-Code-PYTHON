from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return """
    <div style="text-align: center;">
        <h1>Guess a number between 0 and 9</h1>
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" style="display: block; margin: auto;">
    </div>
"""

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return """
    <div style="text-align: center;">
        <h1 style="color: purple;">Too high, try again!</h1>
        <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" style="display: block; margin: auto;">
    </div>
"""

    elif guess < random_number:
        return """
    <div style="text-align: center;">
        <h1 style="color: red;">Too low, try again!</h1>
        <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" style="display: block; margin: auto;">
    </div>
"""
    else:
        return """
    <div style="text-align: center;">
        <h1 style="color: green;">You found me!</h1>
        <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" style="display: block; margin: auto;">
    </div>
"""


if __name__ == "__main__":
    app.run(debug=True)
    
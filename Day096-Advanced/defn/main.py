from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_character_fact')
def get_character_fact():
    response = requests.get("https://hp-api.com/characters/random")
    data = response.json()
    # Assuming the API returns a dictionary with a 'name' key for the character's name.
    # Adjust this line according to the actual API response structure.
    fact = f"{data['name']} is a character in Harry Potter."
    return fact

if __name__ == '__main__':
    app.run(debug=True)

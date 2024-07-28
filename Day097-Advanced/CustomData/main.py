from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_food_facts')
def get_food_facts():
    response = requests.get("https://food-facts-api.herokuapp.com/api/food/facts?limit=10")
    data = response.json()
    # Convert the list of dictionaries into a single dictionary for easier management
    facts_dict = {}
    for fact in data:
        # Assuming each fact has a unique identifier (id) for easy lookup
        facts_dict[fact['id']] = fact
    return facts_dict

if __name__ == '__main__':
    app.run(debug=True)

# `Day 66 - Advanced`

# What is a REST API?

A REST (Representational State Transfer) API is an architectural style for designing networked applications. It uses HTTP requests to access and use data. REST APIs allow different software systems to communicate with each other over the web without needing to know details about the underlying platform or system architecture. They rely on standard HTTP methods like GET, POST, PUT, DELETE, etc., to perform operations on resources identified by URLs.

## Key Characteristics of REST APIs:

- **Stateless**: Each request from a client to a server must contain all the information needed to understand and process the request. The server should not store anything about the latest HTTP request the client made. Each request is processed independently.

- **Client-Server Architecture**: The client and server are separate entities. This separation allows for independent evolution of the client and server.

- **Cacheable**: Responses from the server may be cached by the client to improve performance.

- **Uniform Interface**: The method of communication between the client and the server is uniform and does not vary between servers. This simplifies and decouples the architecture, allowing each part to evolve independently.

# How REST APIs Relate to Python

Python is a versatile programming language widely used for web development, including creating and consuming REST APIs. Libraries such as `requests` make it easy to send HTTP requests to REST endpoints, and frameworks like Flask and Django simplify the process of building RESTful services.

## Key Points When Working with REST APIs in Python:

### Using the Requests Library

The `requests` library is one of the most popular libraries for making HTTP requests in Python. It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application.

Example of using `requests` to consume a REST API:

```
import requests

response = requests.get('https://api.example.com/data') data = response.json()

print(data)
```


### Building RESTful Services with Flask

Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. Flask provides tools, libraries, and technologies that allow you to build RESTful APIs easily.

Example of a simple Flask app serving a REST API:

```
from flask import Flask, jsonify

app = Flask(name)

@app.route('/api/data', methods=['GET']) def get_data(): return jsonify({'message': 'Hello, World!'})

if name == 'main': app.run(debug=True)
```

In this example, we define a route `/api/data` that responds to GET requests with a JSON message.

# `Practice` Example

```
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database
books = {
    'book1': {'title': 'Book One', 'author': 'Author One'},
    'book2': {'title': 'Book Two', 'author': 'Author Two'}
}

# Route for getting all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Route for getting a book by ID
@app.route('/api/books/<string:book_id>', methods=['GET'])
def get_book(book_id):
    return jsonify(books[book_id])

# Route for adding a new book
@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = request.json
    books[new_book['id']] = new_book
    return jsonify(new_book), 201

# Route for updating a book
@app.route('/api/books/<string:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_book = request.json
    books[book_id] = updated_book
    return jsonify(updated_book)

# Route for deleting a book
@app.route('/api/books/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    del books[book_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

```

## Testing the Endpoints:
Here are some cURL commands to test the endpoints:

1. Get all books: curl http://127.0.0.1:5000/api/books
2. Add a new book: curl -X POST -H "Content-Type: application/json" -d '{"id":"book3","title":"Book Three","author":"Author Three"}' http://127.0.0.1:5000/api/books
3. Get a specific book: curl http://127.0.0.1:5000/api/books/book3
4. Update a book: curl -X PUT -H "Content-Type: application/json" -d '{"title":"Updated Book Title","author":"Updated Author Name"}' http://127.0.0.1:5000/api/books/book3
5. Delete a book: curl -X DELETE http://127.0.0.1:5000/api/books/book3

# Summary

REST APIs are a fundamental part of modern web development, enabling different software systems to communicate over the web. Python, with its simplicity and powerful libraries, is an excellent choice for both consuming and building RESTful services. Whether you're sending requests to external APIs or developing your own RESTful web services, Python offers the tools necessary to achieve these tasks efficiently.



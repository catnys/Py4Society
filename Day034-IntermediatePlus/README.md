# `Day 34 - Intermediate+`

# Understanding REST APIs and Their Role in Python Development

## What are REST APIs?

REST (Representational State Transfer) APIs are a set of architectural principles designed around HTTP protocols. They allow client applications to interact with server-side resources over the internet. RESTful services are stateless, meaning each request from a client to a server must contain all the necessary information to understand and respond to the request.

### Key Characteristics of REST APIs:

- **Stateless Operations**: Each request is independent and does not rely on any previous requests.
- **Client-Server Architecture**: Separation of concerns between client and server, allowing each to evolve independently.
- **Cacheable Responses**: Responses may be cached to improve performance.
- **Uniform Interface**: Simplifies architecture by providing a consistent way of interacting with resources.
- **Layered System**: Client cannot usually tell whether it is connected directly to the end server or to an intermediary along the way.

## REST API Methods

REST APIs utilize standard HTTP methods to perform CRUD (Create, Read, Update, Delete) operations:

- **GET**: Retrieve information about a resource.
- **POST**: Create a new resource.
- **PUT/PATCH**: Update an existing resource.
- **DELETE**: Remove a resource.

## Python and REST APIs

In Python, REST APIs can be consumed using various libraries, most notably `requests`, which simplifies making HTTP requests. Additionally, Python frameworks like Flask and Django can be used to build RESTful services.

### Consuming REST APIs in Python

Here's how you might use the `requests` library to interact with a REST API:

### Make a GET Request

```
response = requests.get('https://api.example.com/items') data = response.json()
```

### Make a POST Request
```
payload = {'name': 'New Item', 'description': 'Item description'} response = requests.post('https://api.example.com/items', json=payload)
```


### Building REST APIs in Python

Frameworks like Flask and Django provide tools to easily build RESTful services.

#### Flask Example

Flask is a lightweight framework suitable for building small to medium-sized applications.

```
app = Flask(name)

items = [{'id': 1, 'name': 'Item 1'}, {'id': 2, 'name': 'Item 2'}]

@app.route('/items', methods=['GET']) def get_items(): return jsonify(items)

@app.route('/items', methods=['POST']) def add_item(): items.append(request.json) return jsonify(request.json), 201

if name == 'main': app.run(debug=True)
```


#### Django Example

Django is a high-level framework that encourages rapid development and clean design.

```
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=20)

    def __str__(self):
        return self.title

```


## Conclusion

REST APIs play a crucial role in modern web development, enabling 'seamless' - probably not as seamless as thay 'seamless' :D but anyway - communication between clients and servers over the internet. Python, with its rich ecosystem of libraries and frameworks, provides robust tools for both consuming existing REST APIs and building new ones. Whether you're fetching data from a third-party service or creating your own API-driven application, understanding and utilizing REST principles is essential in today's interconnected world.


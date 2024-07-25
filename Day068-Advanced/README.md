# `Day 68 - Advanced`

# Authentication in Flask

This document provides an overview of implementing user authentication in Flask applications using Flask-Login. Flask-Login extends Flask to simplify the login process and manage user sessions.

## Prerequisites

Before starting, ensure you have Python installed on your system. You'll also need to install Flask and Flask-Login:

```
pip install Flask Flask-Login
```

## Setting Up Flask-Login

To use Flask-Login, you need to integrate it into your Flask application. Here's how to do it:

Flask is a micro web framework written in Python. It does not require particular tools or libraries, making it simple and easy to deploy. Flask provides mechanisms for routing HTTP requests to Python functions easily and allows developers to build web applications quickly.

### Flask: The core Flask package.
render_template: Used to render HTML templates from .html files stored in templates folder.
request: An object containing all incoming request data.
url_for: Generates URLs for endpoints.
redirect: Helper function to redirect to another endpoint.
flash: Provides a way to store temporary messages between requests.
send_from_directory: Sends a file from a given directory.

### Werkzeug
Werkzeug is a comprehensive WSGI utility library for Python. It is often used alongside Flask but can be used independently. Werkzeug provides utilities for secure password hashing.

generate_password_hash: Generates a hash value of a password for storage.
check_password_hash: Checks a password against a hashed version of it.
Flask-SQLAlchemy
Flask-SQLAlchemy is an extension for Flask that simplifies the use of SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.

### SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) system for Python, providing full suite of well known enterprise-level persistence patterns.
SQLAlchemy ORM: Allows you to interact with your database like you would with SQL. In other words, it’s a way to create, retrieve, update and delete records in your database using Python classes.
DeclarativeBase, Mapped, mapped_column: Tools for defining models in SQLAlchemy ORM.
Integer, String: Data types used when defining columns in SQLAlchemy models.
Flask-Login
Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering users' sessions over extended periods of time.

### UserMixin: A mixin class that adds default implementations for the methods that Flask-Login expects user objects to have.
login_user: Logs a user in.
LoginManager: Manages user sessions.
login_required: Decorator which redirects to the login page if the user is not logged in.
current_user: Represents the user currently interacting with the application.
logout_user: Logs a user out.


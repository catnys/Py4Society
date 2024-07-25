# Day 61 - Advanced

# WTForms

WTForms is a flexible forms validation and rendering library for Python web development. It allows developers to create form classes that can validate input data against various criteria before processing it. WTForms supports both simple and complex form structures and integrates well with popular web frameworks like Flask and Django.

## Features

- **Flexible Validation**: Easily define custom validation rules for your form fields.
- **Rendering**: Supports automatic rendering of form fields to HTML, including support for Bootstrap and other CSS frameworks.
- **Integration**: Seamlessly integrates with Flask, Django, and other Python web frameworks.
- **Security**: Helps prevent common security vulnerabilities such as SQL injection and cross-site scripting (XSS).

## Installation

To install WTForms, use pip:

```
pip install WTForms
```


## Usage

Here's a simple example of how to create a form using WTForms:

### Step 1: Import WTForms

First, import the necessary components from WTForms:

```
from wtforms import Form, StringField, validators
```


### Step 2: Define Your Form Class

Next, define your form class by inheriting from `Form`. Add fields as class variables:


```
class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20)])
    password = StringField('Password', [validators.DataRequired()])

```

### Step 3: Validate Input

Use the form instance to validate input data:

```
form = RegistrationForm(request.form)

if request.method == 'POST' and form.validate():
    # Process the form data
    pass

```

### Rendering the Form

To render the form in a template, pass the form instance to your template context:


```
<form method="post">
    {{ form.hidden_tag() }}
    <p>{{ form.username.label }} {{ form.username() }}</p>
    <p>{{ form.password.label }} {{ form.password() }}</p>
    <p><input type="submit" value="Register"></p>
</form>

```
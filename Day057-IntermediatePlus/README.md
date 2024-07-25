# `Day 57 - Intermediate+`

# Jinja Templates Overview

Jinja is a modern and designer-friendly templating language for Python, modelled after Django’s templates. It provides a simple way to generate text output from templates and variables. Jinja templates are used extensively in web development frameworks like Flask and Pyramid to create dynamic web pages.

## What is Jinja?

Jinja combines clear separation of logic and presentation concerns with a simple yet powerful template language. It allows you to build semantic templates effectively with the right balance between flexibility and power.

## Features of Jinja

- **Powerful Template Language**: Jinja offers a rich set of features including inheritance, filters, tests, macros, and more, making it highly expressive.
- **Fast Compilation**: Jinja compiles templates into Python functions, resulting in fast rendering times.
- **Automatic Escaping**: By default, Jinja escapes variables to prevent XSS attacks, enhancing security.
- **Extensibility**: Jinja can be extended with custom filters, tests, and global variables.

## Basic Syntax

Jinja uses a combination of curly braces `{}` and double curly braces `{{}}` for variable interpolation. Here are some basic examples:

### Variables

To display a variable, wrap it in double curly braces:

```jinja Hello, {{ name }}!```


This would render as "Hello, John!" if `name` was passed as "John".

### Control Structures

Jinja supports control structures like `if`, `elif`, `else`, `for`, and `with` statements, allowing you to add logic to your templates.

#### If Statement

```
jinja {% if user.is_authenticated %} Welcome back, {{ user.username }}! {% else %} Please log in. {% endif %}
```


### Filters

Filters transform the data before displaying it. They are applied inside the double curly braces.
```
jinja The price is {{ product.price|currency }}
```

This applies the `currency` filter to the `product.price` variable, formatting it as currency.

## Getting Started with Jinja

To get started with Jinja, you'll need to install it via pip:


```
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.')) 
template = env.get_template('example.html')
output = template.render(name='John Doe') 
print(output)
```


This script loads a template named `example.html` from the current directory, renders it with a context containing a single variable `name`, and prints the result.

## Conclusion

Jinja is a powerful tool for generating dynamic content in Python applications. Its simplicity and expressiveness make it a favorite among developers for creating web pages, emails, configuration files, and more.



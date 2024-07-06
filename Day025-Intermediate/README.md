# `Day 25 - Intermediate`

# Working with CSV Files in Python

This README provides an overview of handling CSV (Comma-Separated Values) files in Python. It includes examples of reading, writing, and manipulating CSV data using the built-in `csv` module and the `pandas` library.

## What is a CSV File?

A CSV file is a plain text file that contains data separated by commas. Each line in the file represents a row of data, and each comma-separated value represents a column.

### Example CSV Content

```
Name,Age,Occupation
John Doe,30,Software Engineer
Jane Smith,25,Data Scientist
```

## Using the `csv` Module

The `csv` module in Python's standard library provides functionality to both read from and write to CSV files.

### Reading a CSV File

```python
import csv

file_path = 'example.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row
    for row in csv_reader:
        print(row)
```

### Writing to a CSV File

```python
import csv

file_path = 'output.csv'

data = [
    ['Name', 'Age', 'Occupation'],
    ['John Doe', '30', 'Software Engineer'],
    ['Jane Smith', '25', 'Data Scientist']
]

with open(file_path, mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
```

### Reading a CSV File with a Header

```python
import csv

file_path = 'example.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
```

### Writing to a CSV File with a Header

```python
import csv

file_path = 'output.csv'

data = [
    {'Name': 'John Doe', 'Age': 30, 'Occupation': 'Software Engineer'},
    {'Name': 'Jane Smith', 'Age': 25, 'Occupation': 'Data Scientist'}
]

header = data[0].keys()

with open(file_path, mode='w', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=header)
    csv_writer.writeheader()
    csv_writer.writerows(data)
```

## Using the `pandas` Library

`pandas` is a powerful library for data manipulation and analysis. It provides easy-to-use functions to handle CSV files.

### Reading a CSV File

```python
import pandas as pd

file_path = 'example.csv'
df = pd.read_csv(file_path)
print(df)
```

### Writing to a CSV File

```python
import pandas as pd

file_path = 'output.csv'

data = {
    'Name': ['John Doe', 'Jane Smith'],
    'Age': [30, 25],
    'Occupation': ['Software Engineer', 'Data Scientist']
}

df = pd.DataFrame(data)
df.to_csv(file_path, index=False)
```

## Conclusion

Python provides multiple ways to handle CSV files, from the built-in `csv` module to the more advanced `pandas` library. Choose the method that best fits your needs based on the complexity of your tasks and the size of your datasets.

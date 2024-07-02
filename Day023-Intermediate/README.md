# `Day 23 - Intermediate`

# Step-by-Step Guide: Reading Information from a File and Storing in Dictionaries

This guide will walk you through the process of reading information from a file, storing it into dictionaries, and then creating a list of those dictionaries using Python. 

## Prerequisites

- Python installed on your system
- Basic understanding of Python programming

## Steps

### 1. Prepare Your File

Ensure you have a file with the information you want to read. For this guide, we'll assume a CSV file named `data.csv` with the following content:

```
name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
```

### 2. Import Necessary Libraries

You'll need the `csv` library to handle the file reading. 

```python
import csv
```

### 3. Read the File and Store Data in Dictionaries

We'll read the file line by line and store each line as a dictionary. 

```python
# Define the file name
file_name = 'data.csv'

# Create an empty list to store the dictionaries
data_list = []

# Open the file for reading
with open(file_name, mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Convert the row into a dictionary and add it to the list
        data_list.append(dict(row))

# Print the list of dictionaries
print(data_list)
```

### 4. Explanation of the Code

- **Import the csv library**: This library provides functionality to read from and write to CSV files.
- **Define the file name**: Specify the name of the file you want to read.
- **Create an empty list**: This list will store the dictionaries created from each row of the CSV file.
- **Open the file**: Use the `open()` function to open the file in read mode.
- **Create a CSV reader object**: The `csv.DictReader` class reads each row in the CSV file as a dictionary.
- **Iterate over each row**: Use a for loop to iterate over each row in the CSV file.
- **Convert each row into a dictionary and add to the list**: The `dict(row)` converts the row into a dictionary and the `append()` method adds it to the list.

### 5. Complete Code

Here is the complete code combined for your reference:

```python
import csv

# Define the file name
file_name = 'data.csv'

# Create an empty list to store the dictionaries
data_list = []

# Open the file for reading
with open(file_name, mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Convert the row into a dictionary and add it to the list
        data_list.append(dict(row))

# Print the list of dictionaries
print(data_list)
```

### 6. Running the Code

1. Save the CSV content in a file named `data.csv`.
2. Save the complete code in a Python file, e.g., `read_file.py`.
3. Run the Python file using the command:

```
python read_file.py
```

You should see the following output:

```
[{'name': 'Alice', 'age': '30', 'city': 'New York'}, {'name': 'Bob', 'age': '25', 'city': 'Los Angeles'}, {'name': 'Charlie', 'age': '35', 'city': 'Chicago'}]
```

## Conclusion

By following these steps, you can read data from a file, store it in dictionaries, and create a list of those dictionaries in Python. This method is versatile and can be adapted for different file formats and data structures.

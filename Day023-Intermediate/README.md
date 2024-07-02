# `Day 23 - Intermediate`

# Step-by-Step Guide: Reading Information from a CSV File and Storing in Dictionaries (Without Using `csv` Library)

This guide will walk you through the process of reading information from a CSV file, storing it into dictionaries, and then creating a list of those dictionaries using Python without using the `csv` library.

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

### 2. Read the File and Store Data in Dictionaries

We'll read the file line by line, manually extract the header, and then store each subsequent line as a dictionary.

```python
# Define the file name
file_name = 'data.csv'

# Create an empty list to store the dictionaries
data_list = []

# Open the file for reading
with open(file_name, mode='r') as file:
    # Read all lines from the file
    lines = file.readlines()

    # Extract the header from the first line and split by comma
    header = lines[0].strip().split(',')

    # Iterate over each remaining line in the file
    for line in lines[1:]:
        # Split the line by comma to get the values
        values = line.strip().split(',')
        
        # Convert the line into a dictionary using the header
        row_dict = {header[i]: values[i] for i in range(len(header))}
        
        # Add the dictionary to the list
        data_list.append(row_dict)

# Print the list of dictionaries
print(data_list)
```

### 3. Explanation of the Code

- **Define the file name**: Specify the name of the file you want to read.
- **Create an empty list**: This list will store the dictionaries created from each row of the CSV file.
- **Open the file**: Use the `open()` function to open the file in read mode.
- **Read all lines from the file**: Use the `readlines()` method to read all lines from the file into a list.
- **Extract the header**: The first line of the file contains the column names, which are split by comma and stored in the `header` list.
- **Iterate over each remaining line**: Use a for loop to iterate over each remaining line in the file.
- **Split the line by comma**: The `strip()` method removes any leading/trailing whitespace, and the `split(',')` method splits the line by comma to get the values.
- **Convert each line into a dictionary using the header**: Create a dictionary where the keys are the column names from the header and the values are the corresponding data from the line.
- **Add the dictionary to the list**: Use the `append()` method to add the dictionary to the list.

### 4. Complete Code

Here is the complete code combined for your reference:

```python
# Define the file name
file_name = 'data.csv'

# Create an empty list to store the dictionaries
data_list = []

# Open the file for reading
with open(file_name, mode='r') as file:
    # Read all lines from the file
    lines = file.readlines()

    # Extract the header from the first line and split by comma
    header = lines[0].strip().split(',')

    # Iterate over each remaining line in the file
    for line in lines[1:]:
        # Split the line by comma to get the values
        values = line.strip().split(',')
        
        # Convert the line into a dictionary using the header
        row_dict = {header[i]: values[i] for i in range(len(header))}
        
        # Add the dictionary to the list
        data_list.append(row_dict)

# Print the list of dictionaries
print(data_list)
```

### 5. Running the Code

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

By following these steps, you can read data from a CSV file, store it in dictionaries, and create a list of those dictionaries in Python without using the `csv` library. This method is versatile and can be adapted for different file formats and data structures.

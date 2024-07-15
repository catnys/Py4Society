# `Day 32 - Intermediate+`

# CSV to Dictionary List in Python

This guide explains how to read data from a CSV file and convert it into a list of dictionaries in Python. The `csv` module in Python makes it easy to work with CSV files.

## Prerequisites

- Python 3.x

## Steps

### 1. Import Required Libraries

First, import the necessary libraries. The `csv` module is part of the Python standard library, so you don't need to install anything extra.

```python
import csv
```

### 2. Define the Function to Read CSV and Create Dictionary List

Create a function that reads the CSV file and converts it into a list of dictionaries. Each row in the CSV file will be converted into a dictionary where the keys are the column headers.

```python
def read_csv_to_dict_list(csv_file):
    dict_list = []
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            dict_list.append(row)
    return dict_list
```

### 3. Sample CSV File

Consider a sample CSV file named `data.csv` with the following content:

```csv
name,email,subject,body
John Doe,john@example.com,Hello,This is a test email.
Jane Smith,jane@example.com,Greetings,This is another test email.
```

### 4. Reading the CSV File

Use the `read_csv_to_dict_list` function to read the CSV file and print the resulting list of dictionaries.

```python
csv_file = 'data.csv'
email_data = read_csv_to_dict_list(csv_file)
print(email_data)
```

### 5. Detailed Breakdown of Operations

#### 5.1 Open the CSV File

Use the `open` function to open the CSV file. The `mode='r'` parameter indicates that the file is opened in read mode.

```python
with open(csv_file, mode='r') as file:
```

#### 5.2 Create a CSV Reader

Use `csv.DictReader` to read the CSV file. This reader object maps the information in each row to a dictionary whose keys are the column headers.

```python
csv_reader = csv.DictReader(file)
```

#### 5.3 Iterate Over Rows

Iterate over each row in the CSV reader object and append the row (which is a dictionary) to the `dict_list`.

```python
for row in csv_reader:
    dict_list.append(row)
```

### 6. Full Example Script

Here is the complete script to read data from a CSV file and convert it into a list of dictionaries.

```python
import csv

def read_csv_to_dict_list(csv_file):
    dict_list = []
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            dict_list.append(row)
    return dict_list

# Example usage
csv_file = 'data.csv'
email_data = read_csv_to_dict_list(csv_file)
print(email_data)
```

### 7. Additional Operations

#### 7.1 Handling Different Delimiters

If your CSV file uses a delimiter other than a comma (e.g., a tab or semicolon), specify the delimiter when creating the `DictReader` object.

```python
csv_reader = csv.DictReader(file, delimiter=';')
```

#### 7.2 Handling Missing Values

If your CSV file has missing values, you can handle them by checking for missing keys in each row dictionary.

```python
for row in csv_reader:
    if 'name' not in row:
        row['name'] = 'Unknown'
    dict_list.append(row)
```

### 8. Integration with Other Code

You can integrate this functionality into larger applications. For example, if you are sending emails, you can use the list of dictionaries to customize and send emails to multiple recipients.



---

# ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 ⭐️✨🌸 

---


# Python Email Sender

This project is a simple Python script that sends an email using the `smtplib` library. The script allows you to send an email with a subject and body to a specified recipient.

## Files

- `main.py`: The main script that sends the email.
- `emailObj.py`: Contains the `Email` class to manage email attributes.


## Setup

1. Clone the repository or download the files.

2. Create a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install required packages (if any):

```sh
pip install -r requirements.txt  # This example does not require external packages
```

## Configuration

1. Update the email credentials and recipient in `main.py`:

```python
sender = "your_email@example.com"
receiver = "receiver_email@example.com"
password = "your_password"
```

2. Make sure the `emailObj.py` is correctly named and placed in the same directory as `main.py`.

## Running the Script

Run the script using:

```sh
python main.py
```

## Reading Data from CSV and Creating a Dictionary List

To read data from a CSV file and create a list of dictionaries, you can use the `csv` module. Below is an example of how to do this:

### Example CSV File: `data.csv`

```csv
name,email,subject,body
John Doe,john@example.com,Hello,This is a test email.
Jane Smith,jane@example.com,Greetings,This is another test email.
```

### Script to Read CSV and Create Dictionary List

```python
import csv

def read_csv_to_dict_list(csv_file):
    dict_list = []
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            dict_list.append(row)
    return dict_list

csv_file = 'data.csv'
email_data = read_csv_to_dict_list(csv_file)
print(email_data)
```

This script reads `data.csv` and creates a list of dictionaries where each dictionary represents a row in the CSV file.

### Integration with Email Script

You can integrate this CSV reading functionality into your email script to send emails to multiple recipients. 

Here's an example:

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

def createMessage(sender, receiver, subject, body):
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    return message

def read_csv_to_dict_list(csv_file):
    dict_list = []
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            dict_list.append(row)
    return dict_list

def main():
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    sender = "your_email@example.com"
    password = "your_password"
    csv_file = 'data.csv'
    
    email_data = read_csv_to_dict_list(csv_file)

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, password)
        
        for data in email_data:
            receiver = data['email']
            subject = data['subject']
            body = data['body']
            message = createMessage(sender, receiver, subject, body)
            server.sendmail(sender, receiver, message.as_string())
            print(f"Email sent to {receiver} successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    main()
```

This integration allows you to send personalized emails to multiple recipients listed in a CSV file.


## Conclusion

This guide provides a comprehensive overview of reading a CSV file and converting it into a list of dictionaries in Python. By following these steps, you can easily handle CSV data and integrate it into your applications.


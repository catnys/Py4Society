# `Day 40 - Intermediate+`

# Flight Deal Notification System

## Overview

This project aims to automate the process of finding and notifying customers about flight deals. It leverages Google Forms for collecting customer data and integrates with Google Sheets for storing this data. Additionally, it utilizes the Amadeus API to search for both direct and indirect flights based on customer preferences. This document outlines the steps to configure the system, including setting up a Google Form, integrating it with Google Sheets, configuring Sheety for user data synchronization, and modifying the Python scripts to handle flight searches and notifications.

## Step 1 - Create a Sharable Form Linked to Your Sheet

### Configure a Google Form Write to Your Existing Sheet

1. **Create a New Google Form**: Navigate to Google Drive, right-click, and select "New" > "More" > "Google Forms".
2. **Disable Email Collection and Limit Responses**: Ensure that the option to collect emails is disabled, and there is no limit on the number of responses. This allows for easy testing with dummy data.
3. **Add Questions**: Include three questions to collect the customer's first name, last name, and email address.
4. **Link to Your Sheet**: Connect your Google Form to the existing "Flight Deals" Google Sheet.
5. **Rename Responses Sheet**: Change the name of the responses sheet to "users".
6. **Test the Form**: Submit some dummy data through the form and verify that it appears in your "users" sheet.

### Configure Sheety for User Data

1. **Sync the New Sheet in Sheety**: After logging in, sync the "users" sheet in Sheety. It should appear below the "prices" sheet.
2. **Enable PUT and POST Requests**: For the "users" tab, ensure that both PUT and POST requests are enabled. Specifically, enable POST requests for the users endpoint.

## Why Google Form?

Due to limitations on sharing terminal-style programs on Replit, a Google Form serves as a practical alternative for collecting customer data.

## Step 3 - Handling Destinations Without Direct Flights

The system requires modifications to accommodate destinations without direct flights. Specifically, it should search for indirect flights (with 1 or 2 stops) if no direct flights are available and capture the cheapest price among these options.

### Technical Specifications

- **Modify `main.py`, `flight_search.py`, and `flight_data.py`**:
  - Adjust the `check_flights()` function to include an `is_direct` parameter with a default value of `True`.
  - In `flight_search.py`, utilize the Amadeus API's "nonStop" query parameter to filter flights based on whether they are direct or indirect.
  - Update `flight_data.py` to include a `stops` variable in the `__init__()` method, which tracks the number of stops in a flight.
  - Ensure that the destination is correctly identified from the final destination rather than a stopover, considering that an itinerary with a single segment is considered a direct flight in the Amadeus API context.

## `Objective`

Retrieve the emails from your Google Sheet as a Python list inside your `main.py`.

## Technical Requirements

You should make changes to your `data_manager.py`, `main.py`, and `.env` file.

### Steps:

1. **Make a Note of the Column Name That Contains the Email Addresses**

   - The name comes from what you used in the Google Form.

2. **Update Your `.env` File**

   - Add your endpoints for your "prices" and your "users" sheets to your `.env` file.

3. **Modify `data_manager.py`**

   - Add a method called `get_customer_emails()` to your `data_manager.py`. This should return the data on your "users" spreadsheet.

4. **Update the `__init__()` Method**

   - So that you retrieve all the environment variables in one place. This should include things like your `SHEETY_USERNAME`, your password, but also your endpoints.

### Next Step

In the next step, we'll send out emails to all our customers that we've retrieved from the Google sheet!


# `Objective`

Send all our customers in the "users" sheet from Google Sheets an email that contains the flight deal.

## Technical Requirements

1. **Update Your `.env` File**

   - With your SMTP address, your email, and your app password.

2. **Modify `notification_manager.py`**

   - Update your `__init__()` method so that you retrieve all the environment variables in one place.

   - Create a method in the `NotificationManager` called `send_emails()`.

   - NOTE: When sending emails, it won't like the "£" symbol, you might get an error. Use "GBP" instead of the "£" symbol. You can also solve this by encoding the message with UTF-8. Refer to [this Stack Overflow post](https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20#answer-9942885) for details.

3. **Craft Different Messages in `main.py`**

   - Depending on whether the flight is direct or has a stopover.

### Finalizing the Project

With these steps completed, your program will be fully functional, capable of notifying customers about flight deals directly from the "users" sheet in Google Sheets. This concludes the project, showcasing a comprehensive solution for automating flight deal notifications.


## Conclusion

By following these steps, you can set up a comprehensive system for collecting customer data, searching for flight deals, and notifying customers about relevant offers. This setup ensures efficient data management and personalized communication, enhancing the overall customer experience.

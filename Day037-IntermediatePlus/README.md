# `Day 37 - Intermediate+`

# Pixela Integration Script

## Before We Start
APIs, or Application Programming Interfaces, allow software applications to communicate with each other. They define methods and data formats that a program can use to perform tasks, access databases, or interact with external systems.

Moreover, APIs enable developers to leverage existing services and data sources, reducing the need to build everything from scratch. They facilitate integration between different software components and platforms, enabling the creation of complex applications through simple interfaces.

This script demonstrates how to interact with the Pixela API to create a user, create a graph, post pixels to the graph, update pixel quantities, and delete pixels. It uses the `requests` library to make HTTP requests and the `datetime` module to work with dates.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Functions Explained](#functions-explained)
- [Best Practices](#best-practices)

## Setup

Before running this script, ensure you have the `requests` library installed.
```
bash pip install requests
```

Replace `<KEY>`, `<TOKEN>`, and `<GRAPH_ID>` with your actual Pixela API key, token, and desired graph ID.

## Usage

This script is structured to perform several operations with the Pixela API:

1. **Create a User**: Uncomment the `requests.post(url=PIXELA_ENDPOINT, json=Parameters)` line to create a new user on Pixela. Note that this operation is idempotent; attempting to create the same user again will return a success message without creating a duplicate.

2. **Create a Graph**: Uncomment the `requests.post(PIXELA_GRAPH_ENDPOINT, json=graphConfig, headers=headers)` line to create a new graph for the specified user. This graph will track sports activities measured in kilometers.

3. **Post Pixels to the Graph**: Uncomment the `requests.post(url=PIXELA_CREATE_PIXEL_ENDPOINT,json=pixelData, headers=headers)` line to post a pixel to the graph, indicating an activity performed on a specific date.

4. **Update Pixel Quantity**: Uncomment the `requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)` line to update the quantity of pixels for a specific date, reflecting changes in the tracked activity.

5. **Delete Pixels**: Uncomment the `requests.delete(url=delete_endpoint, headers=headers)` line to delete a pixel from the graph for a specific date.

## Functions Explained

- **Create User**: Sends a POST request to the Pixela API to create a new user with the specified username and agreement to terms of service.
- **Create Graph**: Sends a POST request to create a new graph for tracking sports activities, specifying details such as the unit of measurement and color.
- **Post Pixels**: Adds a new pixel to the graph, representing an activity performed on a specific date.
- **Update Pixel Quantity**: Updates the quantity of pixels for a given date, allowing for adjustments to the recorded activity level.
- **Delete Pixels**: Removes a pixel from the graph for a specific date, useful for correcting entries.

## Best Practices

- **Security**: Keep your API keys and tokens secure. Do not hardcode them directly into your scripts; consider using environment variables or secure vault services.
- **Error Handling**: Implement error handling for HTTP requests to gracefully handle failures and provide informative feedback.
- **Idempotency**: Be aware of idempotent operations (like creating a user or a graph) and handle cases where repeating the operation would have no effect.
- **Documentation**: Document your code thoroughly, especially when interacting with external APIs, to make maintenance easier for yourself and others.

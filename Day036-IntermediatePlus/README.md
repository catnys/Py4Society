# `DAY 36 - Intermediate+`

# `REVISION` Understanding APIs: Types and RESTful APIs

APIs (Application Programming Interfaces) are essential components in modern software development, allowing different applications to communicate and share data efficiently. There are several types of APIs, each designed for specific use cases and communication protocols. This document provides an overview of common API types and delves into the concept of RESTful APIs.

## Types of APIs

APIs can be categorized based on their architectural style, scope, and protocol. Here are some common types:

### 1. Web APIs
Web APIs facilitate communication between web applications through HTTP protocols. They are further divided into SOAP and REST APIs.

#### SOAP (Simple Object Access Protocol)
SOAP is a protocol specification for exchanging structured information in web services using XML. It's highly standardized and offers extensive security features but can be complex and verbose.

#### REST (Representational State Transfer)
REST is an architectural style for designing networked applications. It uses HTTP requests to access and manipulate web resources. RESTful APIs are more flexible and easier to use compared to SOAP.

### 2. GraphQL APIs
GraphQL is a query language for APIs and a runtime for executing those queries against your existing data. It allows clients to request exactly the data they need, making it efficient and flexible.

### 3. gRPC APIs
gRPC is a high-performance, open-source framework developed by Google. It uses Protocol Buffers as its interface definition language, enabling the development of highly efficient APIs that can run in any environment.

## What is a RESTful API?

A RESTful API adheres to the principles of Representational State Transfer (REST), an architectural style for designing networked applications. Here are some key characteristics:

- **Stateless**: Each request from client to server must contain all the information needed to understand and process the request. The server does not store anything about the latest HTTP request the client made.
  
- **Client-Server Architecture**: RESTful APIs separate concerns between client and server. This separation allows independent evolution of the client and server components.

- **Cacheable**: Responses define themselves as cacheable or non-cacheable. Caching can significantly improve performance by reducing the load on servers and network traffic.

- **Layered System**: A client cannot usually tell whether it is connected directly to the end server or to an intermediary along the way. This allows for greater scalability and flexibility.

- **Uniform Interface**: RESTful APIs have a uniform interface, simplifying and decoupling the architecture, which allows each part to evolve independently.

RESTful APIs use standard HTTP methods like GET, POST, PUT, DELETE to perform operations on resources identified by URLs. They typically exchange data formatted as JSON or XML.


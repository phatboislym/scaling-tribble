# Token Authentication System

## Objective

Create a token authentication system with properly documented code.

This system should have at least two endpoints

- one for GET endpoints
- one for POST endpoints

Each endpoint should require authentication using a token provided by the user.

## Requirements:

### Authentication Flow:

Users should be able to obtain an authentication token, possibly by sending
their username and password or other means of identification.

Users should then include this token in the request header when making requests
to either the POST or GET endpoints.

### Endpoint Functionality

Implement two endpoints:

- GET endpoint
- POST endpoint

Both endpoints should perform specific operations and return a response.

### Proper Response Handling

Ensure that each response returned has an appropriate HTTP response code.
Implement validation for user inputs and data received.
Proper response objects (e.g., validation messages, status codes, etc.) must
be returned for all endpoints.

### Error Handling

Implement try-catch blocks to handle exceptions gracefully.
Your code must not break, and it should return meaningful error responses.

### Code Deployment

Deploy your code on a free hosting platform (e.g. Heroku, Netlify, Vercel, etc.)

## Documentation

- Document your code thoroughly, including instructions on how to use your authentication system.
- Host your documentation on a publicly available platform ( GitHub repo).
- Test Credentials
  Provide a test username and password or other means of identification to
  demonstrate how users can obtain an authentication token.

### Submission Links

Please submit the following links:

- GitHub Repository URL.
- URLs for the hosted GET and POST endpoints.
- URL for your hosted documentation.
- Test username and password or other identification means.

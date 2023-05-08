### NOTES REST API
This project is a Django REST Framework API that allows users to create and manage notes.

## Features
Create, read, update, and delete notes
Users can only modify their own notes
Users can only view their own notes
Supports token-based authentication

## Requirements
Python 3.6 or higher
Django 3.2 or higher
Django REST Framework 3.12 or higher

## Installation
Clone the repository: git clone https://github.com/yourusername/yourproject.git

On you terminal run the following commands
```
./initialize_repo.sh
./run_server.sh
```

Usage
Authentication
To authenticate, send a POST request to http://127.0.0.1:8000/login/ with your username and password as JSON:
```
{
    "username": "yourusername",
    "password": "yourpassword"
}
```
The response will contain True or the error


## Endpoints
Notes
```
GET /notes/ - List all notes
POST /notes/ - Create a new note
GET /notes/{id}/ - Retrieve a note by ID
PUT /notes/{id}/ - Update a note by ID
DELETE /notes/{id}/ - Delete a note by ID

User
POST /users/ create a new user
POST /login/ log in
```

## Permissions
The API has the following permissions:

IsAuthenticated - Allows authenticated users to access the view
IsOwnerOrReadOnly - Allows only the owner of an object to edit it. Other users can only read it.
## Documentation
API documentation is available at /notes/ and /users/.
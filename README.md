# TODOAPP
The TODOAPP API is a RESTful web service built with Flask and SQLAlchemy, allowing users to add username and email. It provides endpoints for task, edit task, delete, check completed and uncompleted task, user accounts

## Files
- main.py: Main file containing the application's routes and controllers.
- Models.py Contains database models for the application.
- task.py: Handles user-setting task functionalities
- User.py - Handles user-related functionalities.

## Setup
1. Set up the database by running: python models.py
2. Start the application: python app.py

## Features
*User Authentication*: Users can create username and email , and delete their accounts.
*Task Management*: add, update, and delete task. Each task includes viewing completed or uncompleted task. 
*RESTful API*: Follows RESTful principles for resource naming and HTTP methods.

## Installation

#### Clone the repository: 
git clone https://github.com/your-username/todoapp.git

#### Install dependencies:

pip install -r requirements.txt



### Set up environment variables:

Create a .env file in the project root directory.

 ### Define the following environment variables:

*from dotenv import load_dotenv and import os to be able to load it from the .env*

HOSTNAME=os.getenv("your_database_hostname")

DATABASE=os.getenv("your_database_name")

USER=os.getenv("your_database_username")

PASSWORD=os.getenv("your_database_password")

PORT_ID=os.getenv("your_database_port")

SECURITY=os.getenv("your_flask_secret_key")


### Run the Flask application:

flask run


## API Documentation

#### API Reference: Detailed documentation for all available endpoints and their usage.

### Usage

 *Tested the endpoints using the RESTFUL API Extension*


*Adding a User* : Use the POST /add_user endpoint with a JSON payload containing the username and email fields. Example:
`{
  "username": "Simon",
  "email": "simon@example.com"
}`

*Adding a Task*: Use the POST /add_task endpoint with a JSON payload containing the title, description, and user_id fields. Example:
`{
  "title": "Day 1",
  "description": "Running",
  "user_id": 1
}`


*Marking a Task as Complete* : Use the PUT /mark_complete/<int:id> endpoint to mark a task as complete.
Viewing Tasks: Use the GET /tasks endpoint to view all tasks or filter by status (completed or uncompleted). Example:
GET http://127.0.0.1:5000/tasks?status=completed

Viewing Users: Use the GET /users endpoint to view all users.
Updating a User: Use the PUT /update_user/<int:id> endpoint with a JSON payload containing the username field to update a user's username. Example:

`{
  "username": "Ama"
}`
*Deleting a User* : Use the DELETE /user/<int:user_id> endpoint to delete a user.


## Technologies Used

- Python
  
- Flask
  
- SQLAlchemy


### Security
Make sure to keep your .env file containing sensitive information such as database credentials and secret keys private and not to include it in version control.


## Contributing

Contributions are welcome! If you would like to contribute to the development of the Task API, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them with descriptive messages.

3. Push your changes to your fork.

4. Submit a pull request to the main repository's develop branch. 





# Shorten My Link

This is a web application that allows you to shorten long URLs, creating custom short links.

## Installation and Setup

### Install Dependencies

1. Ensure you have Python and PostgreSQL installed.

2. Create a virtual environment (recommended) and activate it:

   ```
   python -m venv venv
   source venv/bin/activate
   
   # For Windows, use
   venv\Scripts\activate
   ```
   
3. Install dependencies for the Flask server:
   ```pip install flask flask_sqlalchemy validators shortuuid```

4. Install dependencies for the React app. Navigate to the frontend folder:
```
cd react_app
npm install
```

## Configure the Database

1. Create a PostgreSQL database named flask.

2. In the app.py file:
Replace 'postgresql://postgres:postgres@localhost/flask' with your database connection string in the app.py ['SQLALCHEMY_DATABASE_URI'] variable.

3. In the init.sql replace 'flask' with your database name

## Run the Server

Start the Flask server:
```
flask run
```
Flask will be running at http://localhost:5000.

## Run the React

Go back to the project's root folder if you are inside the backend folder.

Start the React app:
```
npm start
```
React will be running at http://localhost:3000.

## Running the Project Using Docker
To run this project using Docker, follow these steps:

1. Make sure you have Docker installed on your computer. If Docker is not already installed, you can download it from the [official Docker website](https://docs.docker.com/get-docker/).
   
2. Clone the project repository to your computer if you haven't already:

   ```
   git clone <repository-url>
   cd <project-directory>
   ```

3. Make database-related changes as it is written in the 'Configure the Database' instructions if necessary 

4. Now, you can start the Docker containers for your project using the following command:
   ```
   docker-compose up --build
   ```

5. After successfully starting the containers, your project will be accessible in a web browser at the following addresses:
- React frontend: http://localhost:3000
- Flask backend: http://localhost:5000

6. You can stop the Docker containers using the following command:
   ```
   docker-compose down
   ```
## Usage

To shorten a long URL:

1. Open the application in your browser by going to http://localhost:3000.

2. Enter the long URL you want to shorten in the input field.

3. Click the "Create" button to generate a short link.

4. The short link will be displayed below. Click the "Copy" button to copy it to your clipboard.

To custom a long URL:

1. Enter the long URL you want to shorten into the input field.
   
2. Click the "Send" button to generate a short link.
   
3. To create a custom short link
   
4. Enter the desired custom short link in the "Enter custom short link" field.
   
5. Click the "Save" button to save the custom short link.
    
6. The generated short link will be displayed below. To copy it to your clipboard, click the "Copy" button.

You can use the short link (either the automatically generated one or the custom one you saved) to navigate to the corresponding long URL.

## API

### POST /shorten
Creates a short link based on the provided long URL.

Request Body
```
{
  "long_url": "https://example.com/very/long/url"
}
```
Response
```
{
  "short_url": "http://localhost:5000/abcdefg"
}
```

### POST & GET /custom

Creates a short custom link based on the provided long URL.

Request Body:
```
{
  "long_url": "https://example.com/very/long/url"
}
```
Response:
```
{
  "custom_link": "http://localhost:5000/custom/unique-short-url"
}
```


### GET /<short_id>
Redirects the user to the corresponding long URL for a given short link if it exists.

## React Components

### InputLink
Component for creating short links.
### CustomLink
Component for creating short custom links.
### App
Main application component.

## Backend Modules
### app.py
Main application module.
### test_app.py
Module containing tests of the main application


## Tests
These tests cover various aspects of my Flask application, including URL validation, database operations, URL redirection, and the generation of short links. They help ensure that my application functions correctly and handles different scenarios appropriately.

1. **test_get_long_url**:
   - Sends a POST request with a valid long URL.
   - Checks if the response status code is 200 (OK).

2. **test_validate_url**:
   - Sends a POST request with an invalid long URL.
   - Checks if the response status code is 400 (Bad Request).
   - Checks if the response data contains the message "Invalid Url."

3. **test_create_db**:
   - Checks that the 'link' table has been created in the database.

4. **test_existing_db**:
   - Checks that the 'link' table exists before creating a short link.
   - Sends a POST request to create a short link.
   - Checks that the 'link' table is still created after creating the short link.

5. **test_existing_link_in_db**:
   - Adds a link to the database.
   - Sends a POST request with a long link that already exists in the database.
   - Checks if the response status code is 200 (OK).

6. **test_correct_short_url**:
   - Sends a POST request to create a short link.
   - Checks if the short link in the response matches the expected format (starts with "http://localhost:5000/").

7. **test_data_in_db**:
   - Sends a POST request to create a short link.
   - Gets the short link from the response.
   - Searches for a database entry corresponding to the short link.
   - Checks if the entry exists in the database.

8. **test_redirect_to_long_url**:
   - Sends a POST request to create a short link.
   - Gets the short link from the response.
   - Sends a GET request to the short link and checks if it is redirected to the long link.

9. **test_get_custom_url**:
   - Sends a POST request to save a custom and original URL.
   - Checks if the response status code is 200 (OK).

10. **test_save_custom_url**:
    - Sends a POST request to create a short link with a custom short URL.
    - Checks if the response status code is 200 (OK).
    - Gets the custom link from the response.
    - Searches for a database entry corresponding to the custom short link.
    - Checks if the entry exists in the database.

11. **test_redirect_from_custom_to_long_url**:
    - Sends a POST request to save a custom URL.
    - Gets the custom link from the response.
    - Sends a GET request to the custom link and checks if it is redirected to the long link.

12. **test_generate_different_short_links**:
    - Sends a POST request to create the first short link.
    - Gets the short link from the response.
    - Sends a POST request to create the second short link with a different long URL.
    - Gets the short link from the response.
    - Checks that the generated short links are different.

## Running Locust for Load Testing
To perform load testing on your application using Locust, follow these steps:

1. Open your web browser and go to http://localhost:8089 to access the Locust web interface running in the Docker container.

2. Configure the number of users, spawn rate, and other parameters for your load test.
- Host by default:
```
http://flask-backend:5000
```

3. Start the load test, and Locust will simulate user behavior to test the performance of your application.

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
Replace 'postgresql://postgres:postgres@localhost/flask' with your database connection string in the app.config['SQLALCHEMY_DATABASE_URI'] variable.

## Run the Server

Start the Flask server:
```python app.py```
Flask will be running at http://localhost:5000.

## Run the React

Go back to the project's root folder if you are inside the backend folder.

Start the React app:
```npm start```
React will be running at http://localhost:3000.

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
Request Body
```
{
  "long_url": "https://example.com/very/long/url"
}
```
```
{
  "short_url": "custom"
}
```
Response
```
{
  "short_url": "http://localhost:5000/custom"
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




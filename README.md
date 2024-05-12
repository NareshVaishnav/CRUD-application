# Backend Application for Managing Users

This backend application provides CRUD (Create, Read, Update, Delete) APIs for managing users. It allows users to perform operations such as adding new users, retrieving user details, updating user information, and deleting users.

## Technology Stack

- Programming Language: Python
- Framework: Flask
- Database: MySQL
- Postman: Postman Collection (See below)

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the MySQL database:**
   
   - Create a MySQL database.
   - Update the database URI in the Flask application configuration (`app.py` or your Flask application file) with your MySQL database credentials.

4. **Run the Flask application:**

    ```bash
    python app.py
    ```

## API Endpoints

- `POST /user`: Creates a new user record.
- `GET /user/<user_id>`: Retrieves details of the user with the specified ID.
- `PUT /user/<user_id>`: Updates details of the user with the specified ID.
- `DELETE /user/<user_id>`: Deletes the record of the user with the specified ID.

## Postman Collection

The Postman Collection (`API Test.postman_collection.json`) contains requests for testing the implemented API endpoints. Follow the steps below to use it:

1. **Import the provided Postman Collection into Postman:**
   
   - Open Postman.
   - Click on "Import" button in the top left corner.
   - Choose the `API Test.postman_collection.json` file and import it into Postman.

2. **Send requests to the API endpoints:**
   
   - Once imported, you'll see a collection named "Backend Application for Managing Users" in Postman.
   - Click on the collection to view the included requests.
   - Select a request and click on "Send" to execute it against the corresponding API endpoint.

3. **Handle responses and errors appropriately:**
   
   - Verify the responses returned by the API requests.
   - Handle any errors or unexpected behavior as needed.

## Usage

1. **Send requests using Postman:**

    - Use Postman to interact with the API endpoints and perform CRUD operations on users.
    - Ensure to include necessary request parameters and handle responses properly.

## Contributor

- Naresh Vaishnav (nareshvaishnavrko11@gmail.com)


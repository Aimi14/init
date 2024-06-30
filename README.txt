# Fund Management System

## Overview

The Fund Management System is a web application designed to manage investment funds. 
It provides functionalities to create, read, update, and delete (CRUD) fund records via a RESTful API. 
The system uses Flask for the web framework and PostgreSQL for data persistence.

## Project Structure
FundSystem/
├── app/
│ ├── init.py
│ ├── database.py
│ ├── models.py
│ ├── routes.py
├── tests/
│ ├── init.py
│ └── test_api.py
├── venv/
├── funds.db
├── initialize_sqlite_db.py
├── main.py
├── migrate_data.py
├── schema.sql
├── verify_db.py



## Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine:

### 2. Set Up Virtual Environment
Create and activate a virtual environment:

#### Windows
### 3. Install Dependencies
Install the required Python packages using `pip`:

### 4. Initialize SQLite Database (for initial setup)
Run the script to initialize the SQLite database and populate it with initial data:

### 5. Migrate Data to PostgreSQL
Ensure PostgreSQL is running and configured properly, then run the migration script:

## Running the Application
Start the Flask application:

The application will be accessible at `http://127.0.0.1:5000`.
## API Endpoints
### GET /funds
Retrieve a list of all funds.
### POST /funds
Create a new fund.
### GET /funds/{fund_id}
Retrieve details of a specific fund by ID.
### PUT /funds/{fund_id}
Update the performance of a specific fund by ID.
### DELETE /funds/{fund_id}
Delete a specific fund by ID.


## Running Tests
To run the unit tests, use the following command:


## Additional Information
- Ensure PostgreSQL is installed and running on your machine.
- Update the PostgreSQL connection details in `app/database.py` as needed.
- Use the provided `schema.sql` to create necessary tables in PostgreSQL.

## Troubleshooting
If you encounter any issues, ensure all dependencies are installed and the virtual environment is activated. For database-related issues, verify the connection details and ensure the PostgreSQL service is running.

---

By following these instructions, you should be able to set up, run, and test the Fund Management System. For any further assistance, please refer to the project documentation or contact the project maintainer.

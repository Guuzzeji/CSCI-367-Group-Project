<p align="center">
    <img width="300px" src="./meme_readme.png">
</p>

# Backend (Python+Flask) Web Server

This web server is designed to act as an intermediary between the frontend and MySQL database. It provides API endpoints that allow the frontend to access data from the database in a structured manner. The web server runs on port `3030`.

## API Documentation 

### GET: `/API/manga/<int:book_id>`

**Example:** `/API/manga/69`

**Response:**

> Need to implement

This endpoint retrieves more information about a specific manga based on its `book_id`, which corresponds to an ID within the MySQL database.

---

### GET: `/API/search`

**Example:** `/API/search?query=helloworld&type=author&lastbookid=10`

**Response:**

> Need to implement

This endpoint is a query URL used to search for manga in the database based on given parameters:
- **type**: title | author | theme | genre (default is title)
- **lastbookid**: an integer (default is 1)
- **query**: user search term (required)

---

### GET: `/TEST/ping`

### Response

```text
pong
```

Use this to test connection of web server.

# Setup Backend 

## Setting Up a Virtual Environment (venv)

It's recommended to use a virtual environment to manage project dependencies and isolate them from the global Python environment.

### 1. Create a virtual environment named `venv`:

```bash
python -m venv venv
```

### 2. Activate the virtual environment:

**On Windows:**

```bash
venv\Scripts\activate
```

**MacOS / Linux:**

```bash
source venv/bin/activate
```

## Installing Dependencies

After activating the virtual environment, install the required packages using the requirements.txt file:

```bash
pip install -r requirements.txt
```

## How to Run the Web Server

Create a .env file at the root of the folder and define the following variables. These variables should match those defined for the MySQL Docker image or the username and password you've set for the MYSQL_DATABASE.

```env
MYSQL_USERNAME=exampleUser
MYSQL_PASSWORD=pwd12345
MYSQL_HOST=localhost
MYSQL_DATABASE=manga_db
MYSQL_PORT=3306
FLASK_DEBUG=true
```

**Note**: 
- Avoid changing MYSQL_DATABASE unless you know what you're doing.
- Set `FLASK_DEBUG` to true if you are making changes to the web server

## Run / Start Server

Execute the following command to start the server and will run on `localhost:3030`:

```bash
python app.py
```
<p align="center">
    <img width="300px" src="./meme_readme.png">
</p>

# Backend (Python+Flask) Web Server

This web server is designed to act as an intermediary between the frontend and MySQL database. It provides API endpoints that allow the frontend to access data from the database in a structured manner. The web server runs on port `3030`.

## API Documentation 

### GET: `/API/manga/<int:book_id>`

**Example:** `/API/manga/69`

**Response:**

```txt
[
    {
        imgurl: "string",
        title: "string",
        genres: "string",
        author: "string",
        published_end: "string",
        published_start: "string",
        themes: "string" | "null",
        synopsis: "string",
        imgurl: "string",
        myanimelisturl: "string",
    }
]
```

This endpoint retrieves more information about a specific manga based on its `book_id`, which corresponds to an ID within the MySQL database.

---

### GET: `/API/search`

**Example:** `/API/search?query=helloworld&type=author`

**Response: JSON**

```txt
[
    {
        bookid: 0,
        imgurl: "string",
        title: "string",
        type: "string" | undefined,
        author: "string" | undefined
    }
    ...
]
```


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

## Run / Start Server

Execute the following command to start the server and will run on `localhost:3030`:

```bash
python app.py
```
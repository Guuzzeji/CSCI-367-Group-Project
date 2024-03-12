<p align="center">
    <img width="600px" src="./memeimage.gif">
</p>

<h1 align="center">
    DB-Creater
</h1>

## Overview
Create a database in CSV format by fetching data from the Jikan API (https://jikan.moe/). The generated CSV files will contain information about manga, including details such as titles, authors, demographics, genres, themes, reviews, and more.

## Notes
- Program may take some time to create a db, need to sleep for 4 seconds after every request to not hit rate limit of API
- Already created 100 row table with everything, can just load that into db


## API Documentation
- Manga Reviews: [API Documentation](https://docs.api.jikan.moe/#tag/manga/operation/getMangaReviews)
- Manga Search: [API Documentation](https://docs.api.jikan.moe/#tag/manga/operation/getMangaSearch)

## Created Tables

### Manga Table
- `bookid`: Integer
- `myanimelisturl`: String/VARCHAR
- `title`: String/VARCHAR
- `imgurl`: String/VARCHAR
- `chapters`: Integer (can be NULL, if not in found myanimelist)
- `volumes`: Integer (can be NULL, if not in found myanimelist)
- `publishedstart`: String/Datetime
- `publishedend`: String/Datetime (or NULL if ongoing)
- `synopsis`: String/VARCHAR
- `background`: String/VARCHAR

### Author Table
- `bookid`: Integer (reference to Manga Table)
- `Name`: String/VARCHAR

### Demographic Table
- `bookid`: Integer (reference to Manga Table)
- `Name`: String/VARCHAR

### Genre Table
- `bookid`: Integer (reference to Manga Table)
- `type`: String/VARCHAR

### Theme Table
- `bookid`: Integer (reference to Manga Table)
- `type`: String/VARCHAR

### Review Table
- Note: Some books may not have a review
- `bookid`: Integer (reference to Manga Table)
- `username`: String/VARCHAR
- `score`: Integer
- `datecreated`: String/Datetime
- `myanimeurl`: String/VARCHAR

## How to setup
Creating a virtual environment (venv) in Python allows you to isolate your project's dependencies and avoid conflicts with other projects. Here's how to create a venv using Python:

1. **Open a Terminal or Command Prompt**: Depending on your operating system, open a terminal or command prompt window. On Windows, you can press `Win + R`, type `cmd`, and press Enter. On macOS or Linux, you can use the built-in Terminal application.

2. **Navigate to Your Project Directory**: Use the `cd` command to navigate to the directory where you want to create your virtual environment. For example:
   
   ```
   cd path/to/your/project/directory
   ```

3. **Create the Virtual Environment**: Run the following command to create a virtual environment named `venv`:

   ```
   python -m venv venv
   ```

   This command creates a directory named `venv` in your project directory, which contains all the necessary files for the virtual environment.

4. **Activate the Virtual Environment**: To start using the virtual environment, you need to activate it. Run the appropriate command based on your operating system:

   - **Windows**:
     ```
     venv\Scripts\activate
     ```

   - **macOS and Linux**:
     ```
     source venv/bin/activate
     ```

   Once activated, you should see `(venv)` in front of your command prompt, indicating that the virtual environment is active.

5. **Install Dependencies**: Now that the virtual environment is active, you can install Python packages and dependencies using `pip` without affecting the global Python installation. For example:
   
   ```
   pip install -r ./requirements.txt
   ```

6. **Deactivate the Virtual Environment**: When you're done working on your project, you can deactivate the virtual environment by running the following command:

   ```
   deactivate
   ```

   This will return you to the global Python environment. Remember to activate the virtual environment whenever you work on your project to ensure that you're using the correct dependencies.

7. **Run**: Will give you a prompt on how many rows of manga you want to create, just type after number greater than 0 and below 100000 (or some crazy big number)

   ```
   python db-creator.py
   ```

That's it! You've successfully created an anime db. 

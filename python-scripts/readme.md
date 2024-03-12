<p align="center">
    <img src="./memeimage.gif">
</p>

<h1 style="text-align: center;">
    Cool/DB
</h1>

## About
Create db as .csv from https://api.jikan.moe/v4/manga

Docs from API https://jikan.moe/
- https://docs.api.jikan.moe/#tag/manga/operation/getMangaReviews
- https://docs.api.jikan.moe/#tag/manga/operation/getMangaSearch 

**Create these tables**
- Manga Table 
    - bookid = int
    - myanimelisturl = string/varchar
    - title = string/varchar
    - imgurl = string/varchar
    - chapters = int
    - volumes = int
    - publishedstart = string/datetime
    - publishedend = string/datetime or null if still running
    - synopsis = string/varchar
    - background = string/varchar

- Author Table
    - bookid = int, referance to managa table
    - Name = string/varchar

- Demographic Table
    - bookid = int, referance to managa table
    - Name = string/varchar
  
- Genre Table
    - bookid = int, referance to managa table
    - type = string/varchar

- Theme Table
    - bookid = int, referance to managa table
    - type = string/varchar

- Review Table
    - bookid = int, referance to managa table
    - username = string/varchar
    - score = int
    - datecreated = string/datetime
    - myanimeurl = string/varchar

## How to setup
Creating a virtual environment (venv) in Python allows you to isolate your project's dependencies and avoid conflicts with other projects. Here's how to create a venv using Python:

1. **Open a Terminal or Command Prompt**: Depending on your operating system, open a terminal or command prompt window. On Windows, you can press `Win + R`, type `cmd`, and press Enter. On macOS or Linux, you can use the built-in Terminal application.

2. **Navigate to Your Project Directory**: Use the `cd` command to navigate to the directory where you want to create your virtual environment. For example:
   
   ```
   cd path/to/your/project/directory
   ```

3. **Create the Virtual Environment**: Run the following command to create a virtual environment named `venv`:

   ```
   python -m venv lib
   ```

   This command creates a directory named `venv` in your project directory, which contains all the necessary files for the virtual environment.

4. **Activate the Virtual Environment**: To start using the virtual environment, you need to activate it. Run the appropriate command based on your operating system:

   - **Windows**:
     ```
     lib\Scripts\activate
     ```

   - **macOS and Linux**:
     ```
     source lib/bin/activate
     ```

   Once activated, you should see `(venv)` in front of your command prompt, indicating that the virtual environment is active.

5. **Install Dependencies**: Now that the virtual environment is active, you can install Python packages and dependencies using `pip` without affecting the global Python installation. For example:
   
   ```
   pip install ./requirements.txt
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
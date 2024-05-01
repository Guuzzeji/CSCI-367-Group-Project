<p align="center">
    <img width="300px" src="./totoro.gif">
</p>

# CSCI-367-Group-Project (OtakuOracle)

CSCI 367 Group Project For Class Spring 2024

**By. Gabe, Wasif, Bryant**

----------------------------------------------------------------

## 🗯 Overview of Project

OtakuOracle is a specialized manga search engine designed to cater to the needs of manga enthusiasts worldwide. With its intuitive interface and extensive database, users can easily search for manga titles based on various criteria such as title, author, genre, and theme. Whether you're looking for the latest releases or exploring classic titles, OtakuOracle provides a comprehensive platform to discover and explore a vast collection of manga.

### ❤️ Project Inspiration

The inspiration behind OtakuOracle stems from our shared passion for manga and anime. As avid readers and fans ourselves, we often found it challenging to keep track of new releases, discover hidden gems, and explore titles based on specific themes or genres. This gap in the market led us to conceptualize OtakuOracle, aiming to create a user-friendly platform that simplifies the manga search process and enhances the overall reading experience for manga enthusiasts.

Our project draws inspiration from popular platforms like "MyAnimeList", which has revolutionized the way anime fans discover and track their favorite series. We recognized the need for a similar platform dedicated exclusively to manga, offering a more tailored and focused experience for manga readers. By leveraging the best features of existing platforms and incorporating innovative search functionalities, OtakuOracle aims to become the go-to resource for manga enthusiasts seeking to expand their reading horizons.

## ❗️ Main Features ❗️

The main features of OtakuOracle are:

- Simple search interface
- Clear and concise search results
- Highly detailed pages for specific books that are dynamically generated
- Clean and highly stylized user interface
- Modular development stack and system design

These main features of our project allowed us to create not only a wonderful product for manga enthusiasts that allow them to quickly search and explore new types of books, but also allowed us as developers to test our programming and design capabilities. These features were essential to implement as they were the foundation of our project, wanting to have a website to allow users to easily search different mangas. Likewise, we also wanted to develop our project in a way that allowed it to be quickly interacted with without too much complexity slowing down our creative ideas. Having a stylized and clean interface will differentiate us from dull looking websites that are convoluted with extra things. This also allows the user to have a fun time searching for their favorite manga without having to manage through the extra garbage. Our simple search engine will allow users to find things easily through things like our advance search for titles and authors. With our search engine as well, users will be able to find new manga based on their favorite themes, genres, or authors.

## 💾 Technology Stack

The development framework and tool set we used to develop the project:

- **MySQL & Docker**: Containerized the database.
- **Python & Flask**: Developed the API web server.
- **React**: Built frontend functionality.
- **Chakra UI**: Crafted UI components.
- **React-router-dom**: Managed webpage routing.
- **GitHub**: Controlled source code.
- **Markdown**: Documenting features and API design.

We used all of these frameworks and toolsets to help develop the final product of our project, along with helping us manage our codebase as a team. All of these tools were used in some shape or form to help develop our project and create our rich feature set for our project. We used MySQL to create the queries to search through our database. We used python as our main language throughout the project. React was used to style our pages and GitHub was used for communication and sharing code to ensure all of us were up to date.

## 🕹 How to Run Project

### Install Prerequisites

- Docker Desktop: [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Node.js: [Download Node.js](https://nodejs.org/en)
- Python: [Download Python](https://www.python.org/)

### Start up Docker MySQL Database

Navigate to the project folder and then into the `db` folder:

```bash
cd db
```

Run the following Docker Compose command to start the MySQL server:

```bash
docker-compose up
```

The server will be running on `localhost:4040`.

Then navigate to the `db-populate` folder and run `DatabaseWriter.py` to download .csv files containing all the table data. Afterward, run `InsertIntoSql.py` to insert all .csv files into the MySQL database.

### Running Backend Web Server

Navigate to the `Backend` folder and execute the following commands:

To install the required packages for the server:

```bash
pip install -r requirements.txt
```

To run the server on port 3030:

```bash
python app.py
```

>[!NOTE]
>If you encounter an error stating that the MySQL server is not running, ensure that you have the Docker MySQL server running on port 4040. If you want to run it on a different port, modify the port and host information in `Backend/db/connection.py` accordingly.

### Running Frontend Web Server

Navigate to the `Frontend/anime-search-app` folder and execute the following commands:

To install all necessary packages:

```bash
npm install
```

To run the frontend server, which will default to port 3000 if no conflicting ports are in use:

```bash
npm start
```
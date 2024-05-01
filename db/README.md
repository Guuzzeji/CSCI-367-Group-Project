# MySQL Database

This is MySQL database used to store manga information that was previously stored in .csv files. The database is running on port 4040.

## Setup Instructions

### Prerequisites

Before you begin, ensure you have Docker Desktop installed on your machine. Follow the steps below to download and set up Docker Desktop:

 **Download Docker Desktop:**
- Navigate to the [Docker Desktop download page](https://www.docker.com/products/docker-desktop).
- Choose the appropriate version for your operating system (Windows/Mac) and download the installer.
- Run the installer and follow the on-screen instructions to complete the installation process.

### Setting Up the MySQL Database

**Run the Server:**

- Open a terminal and navigate to the root directory of this repository.
- Run the following command to start the MySQL server using Docker Compose:
- This will have the server running on `localhost:4040`

```sh
docker-compose up
```

## Database Password & Username

**We know this is bad, but have to do this for easy of development**

```text
MYSQL_USER=exampleUser
MYSQL_PASSWORD=pwd12345
MYSQL_ROOT_PASSWORD=rootpassword
```

## Created Tables

```SQL
-- Create Manga Table
CREATE TABLE Manga (
    bookid INT PRIMARY KEY,
    myanimelisturl VARCHAR(255),
    title VARCHAR(255),
    imgurl VARCHAR(255),
    chapters INT,
    volumes INT,
    `status` varchar(50),
    publishedstart DATETIME,
    publishedend DATETIME,
    synopsis VARCHAR(3000),
    background VARCHAR(2000)
);

-- Create Author Table
CREATE TABLE Author (
    bookid INT,
    Name VARCHAR(255),
    authorurl varchar(250),
    FOREIGN KEY (bookid) REFERENCES Manga(bookid)
);

-- Create Demographic Table
CREATE TABLE Demographic (
    bookid INT,
    Name VARCHAR(255),
    FOREIGN KEY (bookid) REFERENCES Manga(bookid)
);

-- Create Genre Table
CREATE TABLE Genre (
    bookid INT,
    type VARCHAR(255),
    FOREIGN KEY (bookid) REFERENCES Manga(bookid)
);

-- Create Theme Table
CREATE TABLE Theme (
    bookid INT,
    type VARCHAR(255),
    FOREIGN KEY (bookid) REFERENCES Manga(bookid)
);

/*Do we really need this one?*/
-- NOTE: NOT USING THIS TABLE
-- Create Review Table
CREATE TABLE Review (
    bookid INT,
    username VARCHAR(255),
    score INT,
    datecreated DATETIME,
    myanimeurl VARCHAR(255),
    FOREIGN KEY (bookid) REFERENCES Manga(bookid)
); 

CREATE table Ratings (
	bookid int,
    score DECIMAL(10,2),
    FOREIGN KEY (bookid) REFERENCES Manga(bookid)
);
```

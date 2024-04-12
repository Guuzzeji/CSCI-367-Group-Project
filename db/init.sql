USE manga_db;

-- Create table stuff here

-- Manga Table
CREATE TABLE Manga (
    bookid INT PRIMARY KEY,
    myanimelisturl VARCHAR(255),
    title VARCHAR(255),
    imgurl VARCHAR(255),
    chapters INT,
    volumes INT,
    publishedstart DATETIME,
    publishedend DATETIME,
    synopsis VARCHAR(255),
    background VARCHAR(255)
);

-- Author Table
CREATE TABLE Author (
    bookid INT,
    Name VARCHAR(255),
    FOREIGN KEY (bookid) REFERENCES Manga(bookid)
);

-- Demographic Table
CREATE TABLE Demographic (
    bookid INT,
    Name VARCHAR(255),
    FOREIGN KEY (bookid) REFERENCES Manga(bookid)
);

-- Genre Table
CREATE TABLE Genre (
    bookid INT,
    type VARCHAR(255),
    FOREIGN KEY (bookid) REFERENCES Manga(bookid)
);

-- Theme Table
CREATE TABLE Theme (
    bookid INT,
    type VARCHAR(255),
    FOREIGN KEY (bookid) REFERENCES Manga(bookid)
);

-- Review Table
CREATE TABLE Review (
    bookid INT,
    username VARCHAR(255),
    score INT,
    datecreated DATETIME,
    myanimeurl VARCHAR(255),
    FOREIGN KEY (bookid) REFERENCES Manga(bookid)
);
#database

## 1
Make sure you create a schema for this project and add these tables:

```
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

## 2
To run the DatabaseWriter, you need to install python (obv) and in case you need other libraries like requests or datetime, in cmd prompt, write: 
pip install whatever or if that doesnt work python -m pip install whatever
Create a folder to put it in and run. EZ


## 3
To run the insertIntoSql file, make sure you've done the previous steps. If need be, change the paths to the csv files in the code. 
Also make sure you change the connections to your own specific instances. 


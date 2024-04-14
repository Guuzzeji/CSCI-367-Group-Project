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

1. **Create .env File:**
    - Inside the `db` folder, create a file named `.env`.
    - Add the following environment variables to the `.env` file:
    ```plaintext
    MYSQL_PASSWORD=pwd12345
    MYSQL_USER=exampleUser
    MYSQL_ROOT_PASSWORD=rootpassword
    ```

2. **Run the Server:**
    - Open a terminal and navigate to the root directory of this repository.
    - Run the following command to start the MySQL server using Docker Compose:
    - This will have the server running on `localhost:4040`
    ```sh
    docker-compose --env-file path/to/.env up
    ```
    Replace `path/to/.env` with the actual path to your `.env` file.


# Frontend

## Introduction

Welcome to the frontend section of the anime-search-engine app! This markdown provides instructions for running the frontend in production mode and guidelines for contributing to the frontend codebase.

## Running Frontend in Production Mode

To run the frontend in production mode, follow these steps:

1. Ensure that Docker is installed on your machine. If not, you can download and install Docker from the official website: [Docker](https://www.docker.com/).

2. Navigate to the root directory of the frontend project.

3. Open the `docker-compose.yml` file located in the root directory of the frontend project.

4. Optionally, you can modify the port number in the `docker-compose.yml` file. By default, the frontend is configured to run on port 8080.

5. Run the following command in your terminal to start the frontend application:

```bash
docker-compose up
```

This command will build the Docker image and start the container, making the frontend accessible at http://localhost:8080 in your web browser.

## Editing Frontend

If you're interested in contributing to the frontend codebase, here are the steps to get started:

Clone the repository to your local machine using Git:

Navigate to the anime-search-app directory, which contains the frontend code.

Read the README.md file in the anime-search-app directory to understand the project structure and how to set up the development environment.

Start working on the frontend codebase by creating new features, fixing bugs, or improving existing functionality.

Happy coding!
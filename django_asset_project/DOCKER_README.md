# Docker Setup for Asset Management API

This document provides instructions on how to run the Asset Management API using Docker.

## Prerequisites

- Docker and Docker Compose installed on your system
- Docker daemon running

## Running the Application

1. Make sure Docker is running on your system.

2. Build the Docker images:
   ```
   docker-compose build
   ```

3. Start the containers:
   ```
   docker-compose up
   ```

4. Access the API:
   - The API will be available at http://localhost:8000/api/assets/1/
   - Admin interface: http://localhost:8000/admin/
   - Default superuser credentials: username: `admin`, password: `admin123`

5. To run in detached mode (background):
   ```
   docker-compose up -d
   ```

6. To stop the containers:
   ```
   docker-compose down
   ```

## Environment Variables

The following environment variables can be configured in the `docker-compose.yml` file:

- `DB_NAME`: PostgreSQL database name
- `DB_USER`: PostgreSQL username
- `DB_PASSWORD`: PostgreSQL password
- `DB_HOST`: PostgreSQL host
- `DB_PORT`: PostgreSQL port
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to 'True' for development, 'False' for production

## Useful Docker Commands

- View running containers:
  ```
  docker ps
  ```

- View logs for a specific container:
  ```
  docker-compose logs web
  ```

- Execute commands in the running container:
  ```
  docker-compose exec web python manage.py shell
  ```

- Create a superuser:
  ```
  docker-compose exec web python manage.py createsuperuser
  ```

- Run migrations:
  ```
  docker-compose exec web python manage.py migrate
  ```

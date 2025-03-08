# Asset Management API

A Django project with a REST API endpoint to fetch specific assets from a PostgreSQL database.

## Setup Instructions

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your PostgreSQL database credentials:
   ```
   DB_NAME=asset_db
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   SECRET_KEY=your_django_secret_key
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

- `GET /api/assets/<id>/`: Retrieve a specific asset by ID

# Movie Stills Server

This Django project serves as a backend for managing and serving movie stills.

# API Endpoints

## Main Resources
| Endpoint          | Method        | Description                                      |
|-------------------|---------------|--------------------------------------------------|
| `/movies/`        | GET           | List all movies or create a new movie            |
| `/movies/<id>/`   | GET           | Retrieve a movie         |
| `/stills/`        | GET           | List all movie stills or create a new still      |
| `/stills/<id>/`   | GET           | Retrieve a movie still   |


## Single Field Endpoints
These endpoints return lists of unique values for the specified field:
| Endpoint | Method | Description |
|--------------|--------|---------------------------------|
| `/only/directors` | GET | List all unique directors |
| `/only/titles` | GET | List all unique movie titles |
| `/only/genres` | GET | List all unique genres |
| `/only/countries` | GET | List all unique countries |
| `/only/years` | GET | List all unique years |
| `/only/imdb` | GET | List all unique IMDb IDs |

## Filtered Movie Lists
The following endpoints return movies filtered by the specified parameter:
| Endpoint | Method | Description |
|---------------------------|--------|--------------------------------------------|
| `/titles/<title-name>/` | GET | List movies with the specified title |
| `/directors/<director-name>/` | GET | List movies by the specified director |
| `/genres/<genre-name>/` | GET | List movies in the specified genre |
| `/countries/<country-name>/` | GET | List movies from the specified country |
| `/years/<year-number>/` | GET | List movies released in the specified year |

## Setup

## Prerequisites 
Ensure these tools are installed:

- Python 3
- PostgresSQL

 ## Step 1: Clone the Project
```bash
git clone https://github.com/your-username/movies_server.git
cd movies_server
```
—
 ## Step 2: Create and Activate a Virtual Environment
```bash
python3 -m venv movie_stills_env
source movie_stills_env/bin/activate
```
—
 ## Step 3: Install Python Dependencies
```bash
pip install -r requirements.txt
This installs Django and any other required libraries defined in requirements.txt.
```
—
 ## Step 4: Create PostgreSQL Database and User

Start the PostgreSQL shell:
```bash
psql -U your_postgres_user
```
Then run the following commands inside the psql shell:

```sql
CREATE DATABASE mise_en_scene;
CREATE USER mise_en_scene_admin WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE mise_en_scene TO mise_en_scene_admin;
\q
```
—
## Step 5: Configure Django to Use the Database

Open movies_server/settings.py, and edit the DATABASES section:

``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mise_en_scene',
        'USER': 'mise_en_scene_admin',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
—
## Step 6: Create the Database Tables (Run Migrations)

```python
python manage.py makemigrations
python manage.py migrate
```

—-
## Step 7: Seed the Database With Initial Data

```bash
python manage.py seed json/master.json
```

## Step 8: Run the Server
 If connecting to a movie_stills client app - https://github.com/alantothe/movie_stills
```bash
 python3 manage.py runserver 8081 
```
Otherwise 
```bash
  python3 manage.py runserver
```

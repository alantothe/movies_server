# Movie Stills Server

This Django project serves as a backend for managing and serving movie stills.


## Setup

1. Clone the repository:
   ```
   git clone https://github.com/alantothe/movies_server.git
   cd movie_stills
   ```

2. Create a virtual environment:
   ```
   python3 -m venv movie_stills_env
   ```

3. Activate the virtual environment:
   ```
   source movie_stills_env/bin/activate  # On Unix or MacOS
   # movie_stills_env\Scripts\activate.bat  # On Windows
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```
   python3 manage.py migrate
   ```

6. Run the development server:
   ```
   python3 manage.py runserver
   ```

The API will be available at http://localhost:8000/.

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
| `/directors` | GET | List all unique directors |
| `/titles` | GET | List all unique movie titles |
| `/genres` | GET | List all unique genres |
| `/countries` | GET | List all unique countries |
| `/years` | GET | List all unique years |
| `/imdb` | GET | List all unique IMDb IDs |

## Filtered Movie Lists
The following endpoints return movies filtered by the specified parameter:
| Endpoint | Method | Description |
|---------------------------|--------|--------------------------------------------|
| `/titles/<title_name>/` | GET | List movies with the specified title |
| `/directors/<director_name>/` | GET | List movies by the specified director |
| `/genres/<genre_name>/` | GET | List movies in the specified genre |
| `/countries/<country_name>/` | GET | List movies from the specified country |
| `/years/<year_number>/` | GET | List movies released in the specified year |
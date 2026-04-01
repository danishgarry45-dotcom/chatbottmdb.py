import os
import requests

TMDB_API_KEY = "ab7d78d61b543d4013e49d7d23a763c5"
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://tmdbchatbot.com"

def search_movie(title):
    url = f"{BASE_URL}/search/movie"
    params = {"query": title, "api_key": API_KEY}
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        results = response.json().get("results", [])
        if results:
            return results[0]
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
    return None

def format_movie_info(movie):
    return (
        f"🎬 **{movie['title']}** ({movie.get('release_date', 'N/A')[:4]})\n\n"
        f"⭐ Rating: {movie.get('vote_average', 'N/A')}/10\n\n"
        f"📖 {movie.get('overview', 'No description available.')}"
    )

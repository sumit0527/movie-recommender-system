import requests


# ------------------------------------------------------------
# 🧩 POSTER FETCHING MODULE
# ------------------------------------------------------------
# This module retrieves movie posters from the TMDb API
# using the provided movie ID.
# ------------------------------------------------------------

def fetch_poster(movie_id):
    """
    Fetch the movie poster URL from the TMDb API for a given movie ID.

    Args:
        movie_id (int): The unique identifier of the movie in TMDb.

    Returns:
        str: A complete URL to the movie's poster image.
    """

    # --------------------------------------------------------
    # Step 1️⃣ — Construct API request URL
    # --------------------------------------------------------
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=12fd4aee4b51f241f3108707b3e9984d&language=en-US"

    # --------------------------------------------------------
    # Step 2️⃣ — Send request to TMDb API
    # --------------------------------------------------------
    response = requests.get(url)
    data = response.json()

    # --------------------------------------------------------
    # Step 3️⃣ — Extract poster path and construct full image URL
    # --------------------------------------------------------
    poster_path = data['poster_path']
    full_poster_url = "https://image.tmdb.org/t/p/w500/" + poster_path

    # --------------------------------------------------------
    # Step 4️⃣ — Return poster URL
    # --------------------------------------------------------
    return full_poster_url

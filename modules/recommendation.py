from modules.fetch_posters import fetch_poster

# ------------------------------------------------------------
# 🎬 RECOMMENDATION LOGIC MODULE
# ------------------------------------------------------------
# This module handles the logic to recommend top 5 similar movies
# based on cosine similarity scores.
# ------------------------------------------------------------
def recommend(movie, movies, similarity):
    """
    Generate top 5 movie recommendations based on similarity scores.

    Args:
        movie_name (str): The name of the movie selected by the user.

    Returns:
        list: A list containing the titles of the top 5 recommended movies.
    """

    # --------------------------------------------------------
    # Step 1️⃣ — Get index of the selected movie
    # --------------------------------------------------------
    movie_index = movies[movies['title'] == movie].index[0]

    # --------------------------------------------------------
    # Step 2️⃣ — Retrieve similarity scores for the selected movie
    # --------------------------------------------------------
    distances = similarity[movie_index]

    # --------------------------------------------------------
    # Step 3️⃣ — Sort movies by similarity score (descending)
    # and pick top 5 recommendations (excluding the movie itself)
    # --------------------------------------------------------
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # --------------------------------------------------------
    # Step 4️⃣ — Fetch movie titles and posters
    # --------------------------------------------------------
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)

        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))

    # --------------------------------------------------------
    # Step 5️⃣ — Return the top 5 recommended movies with posters
    # --------------------------------------------------------
    return recommended_movies,recommended_movies_posters

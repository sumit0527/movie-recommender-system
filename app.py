import streamlit as st
import pickle
import pandas as pd
from modules.recommendation import recommend

# ------------------------------------------------------------
# 🎬 MOVIE RECOMMENDER SYSTEM - MAIN APPLICATION
# ------------------------------------------------------------
# This Streamlit application allows users to select a movie
# and get top 5 similar movies with their posters displayed.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 🧱 APP TITLE AND DESCRIPTION
# ------------------------------------------------------------
st.title("🎬 Movie Recommender System")
st.markdown("Select a movie from the dropdown below and discover top 5 similar movies!")

# Load pre-trained data (movies and similarity matrix)
movies_dict = pickle.load(open("data/movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
movies_list = movies['title'].values
similarity = pickle.load(open("data/similarity.pkl", "rb"))

# ------------------------------------------------------------
# 🧭 STREAMLIT PAGE CONFIGURATION
# ------------------------------------------------------------
st.set_page_config(
    page_title="Movie Recommender System 🎥", page_icon="🎬"
)

# ------------------------------------------------------------
# 🎞️ MOVIE SELECTION SECTION
# ------------------------------------------------------------
selected_movie_name = st.selectbox("Choose Movie:", movies_list)

# ------------------------------------------------------------
# 🔘 RECOMMENDATION BUTTON
# ------------------------------------------------------------
if st.button(label="Recommend"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name, movies, similarity)

    # Display 5 movies in columns
    col1, col2, col3, col4, col5 = st.columns(5)

    # Show movie poster &  Display movie title
    with col1:
        st.image(
            recommended_movie_posters[0],
            caption=recommended_movie_names[0],
            use_container_width=True,
        )
    with col2:
        st.image(
            recommended_movie_posters[1],
            caption=recommended_movie_names[1],
            use_container_width=True,
        )
    with col3:
        st.image(
            recommended_movie_posters[2],
            caption=recommended_movie_names[2],
            use_container_width=True,
        )
    with col4:
        st.image(
            recommended_movie_posters[3],
            caption=recommended_movie_names[3],
            use_container_width=True,
        )
    with col5:
        st.image(
            recommended_movie_posters[4],
            caption=recommended_movie_names[4],
            use_container_width=True,
        )

# ------------------------------------------------------------
# ⚙️ END OF APPLICATION
# ------------------------------------------------------------
# Tip: The app layout is responsive and will adjust automatically
# on desktop and mobile screens.


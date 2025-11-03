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

movies_dict = pickle.load(open("data/movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
movies_list = movies['title'].values
similarity = pickle.load(open("data/similarity.pkl", "rb"))

# ------------------------------------------------------------
# 🎞️ MOVIE SELECTION SECTION
# ------------------------------------------------------------
selected_movie_name = st.selectbox("Choose Movie:", movies_list)

# ------------------------------------------------------------
# 🔘 RECOMMENDATION BUTTON
# ------------------------------------------------------------
if st.button(label="Recommend"):
    recommendations = recommend(selected_movie_name, movies, similarity)
    for i in recommendations:
        st.write(i)

import streamlit as st

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

# ------------------------------------------------------------
# 🎞️ MOVIE SELECTION SECTION
# ------------------------------------------------------------
selected_movie_name = st.selectbox("Choose Movie:", ("Superman","Batman","Ironman"))

# ------------------------------------------------------------
# 🔘 RECOMMENDATION BUTTON
# ------------------------------------------------------------
if st.button(label="Recommend"):
    st.write(selected_movie_name)






import streamlit as st
import pickle
import pandas as pd
from modules.recommendation import recommend
import os

try:
    import gdown
except ModuleNotFoundError:
    import subprocess
    subprocess.run(["pip", "install", "gdown"], check=True)
    import gdown


# ------------------------------------------------------------
# 🎬 MOVIE RECOMMENDER SYSTEM - STREAMLIT APP
# ------------------------------------------------------------
# This app lets users select a movie and get top 5 similar
# recommendations using pre-trained similarity data.
# ------------------------------------------------------------


# ------------------------------------------------------------
# ⚙️ HELPER FUNCTION: LOAD PICKLE FROM GOOGLE DRIVE
# ------------------------------------------------------------
@st.cache_resource
def load_pickle_from_drive(file_id, filename):
    """Download and load pickle files from Google Drive (cached)."""
    os.makedirs("data", exist_ok=True)
    output_path = os.path.join("data", filename)

    # Download only if not already present
    if not os.path.exists(output_path):
        gdown.download(f"https://drive.google.com/uc?id={file_id}", output_path, quiet=False)

    with open(output_path, "rb") as f:
        return pickle.load(f)


# ------------------------------------------------------------
# 🧭 STREAMLIT CONFIGURATION
# ------------------------------------------------------------
st.set_page_config(
    page_title="Movie Recommender System 🎥",
    page_icon="🎬",
    layout="wide",
)

# ------------------------------------------------------------
# 🧱 PAGE TITLE
# ------------------------------------------------------------
st.title("🎬 Movie Recommender System")
st.markdown("### Discover top 5 similar movies based on your favorite film!")

# ------------------------------------------------------------
# 📦 LOAD DATA
# ------------------------------------------------------------
try:
    movies_dict = load_pickle_from_drive("1gDlygvY0eBPjk23W3VQPgJTkPqdNaXfe", "movies_dict.pkl")
    similarity = load_pickle_from_drive("1JeBho71-k_5KhCal3qeGJdQ_U1361_Hp", "similarity.pkl")
    movies = pd.DataFrame(movies_dict)
    movies_list = movies['title'].values
except Exception as e:
    st.error(f"❌ Failed to load model files: {e}")
    st.stop()

# ------------------------------------------------------------
# 🎞️ MOVIE SELECTION SECTION
# ------------------------------------------------------------
selected_movie_name = st.selectbox("🎥 Choose a movie to get recommendations:", movies_list)

# ------------------------------------------------------------
# 🔘 RECOMMENDATION BUTTON
# ------------------------------------------------------------
if st.button("Recommend 🎯"):
    try:
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name, movies, similarity)

        # Display results in 5 columns
        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.image(
                    recommended_movie_posters[i],
                    caption=recommended_movie_names[i],
                    use_container_width=True
                )
    except Exception as e:
        st.error(f"⚠️ Error while generating recommendations: {e}")

# ------------------------------------------------------------
# 🧾 FOOTER
# ------------------------------------------------------------
st.markdown("---")
st.caption("Developed by **Sumit Patil** | Powered by Streamlit 🚀")

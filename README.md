# 🎬 Movie Recommender System

A content-based recommendation system that suggests movies similar to a selected title using cosine similarity.  
Built with **Python**, **scikit-learn**, and **Streamlit**.

---

## 🚀 Features
- Search and select a movie from the dropdown list
- Instantly get 5 similar movie recommendations
- Displays each movie with its poster
- Clean, responsive, and user-friendly layout

---

## 🧰 Tech Stack
- **Python 3.10+**
- **Streamlit** — Web app framework  
- **scikit-learn** — Similarity calculation  
- **Pandas / NumPy** — Data handling  
- **TMDb API** — Poster retrieval

---

## 📂 Folder Structure
movie-recommender-system/
│
├── app.py # Main Streamlit app
├── modules/
│ ├── recommend.py # Movie recommendation logic
│ ├── fetch_poster.py # Poster retrieval function
│
├── data/
│ ├── tmdb_5000_movies.csv
│ ├── tmdb_5000_credits.csv
│
├── similarity.pkl
├── movies_dict.pkl
├── README.md
└── movie-recommender-system.ipynb # Notebook version


---

## ⚙️ Setup Instructions
```bash
# Clone the repo
git clone "https://github.com/sumit0527/movie-recommender-system.git"

# Navigate to the folder
cd movie-recommender-system

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```
```     
👨‍💻 Author
Sumit Patil
```




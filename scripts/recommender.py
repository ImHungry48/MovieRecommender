import sqlite3
from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "girly_recommender.db"


def load_movies():
    conn = sqlite3.connect(DB_PATH)
    query = """
        SELECT id, film, plot
        FROM movies
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def build_tfidf_matrix(df):
    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        max_df=0.85,
        sublinear_tf=True
    )
    tfidf_matrix = vectorizer.fit_transform(df["plot"])
    return vectorizer, tfidf_matrix


def compute_similarity(tfidf_matrix):
    return cosine_similarity(tfidf_matrix, tfidf_matrix)


def suggest_titles(title, df, n=3):
    titles = df["film"].tolist()
    return get_close_matches(title, titles, n=n, cutoff=0.6)

def recommend_movies(title, df, similarity_matrix, top_n=5):
    cleaned_title = title.strip().lower()
    matches = df[df["film"].str.lower() == cleaned_title]

    if matches.empty:
        return None, []

    movie_index = matches.index[0]
    matched_title = df.iloc[movie_index]["film"]

    similarity_scores = list(enumerate(similarity_matrix[movie_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for index, score in similarity_scores[1:top_n + 1]:
        recommendations.append((df.iloc[index]["film"], score))

    return matched_title, recommendations
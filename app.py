from flask import Flask, request, jsonify, render_template
from scripts.recommender import (
    load_movies,
    build_tfidf_matrix,
    compute_similarity,
    recommend_movies,
    suggest_titles,
)

app = Flask(__name__)

# Load data and build the model once when the server starts
df = load_movies()
_, tfidf_matrix = build_tfidf_matrix(df)
similarity_matrix = compute_similarity(tfidf_matrix)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    user_input = data.get("movie", "").strip()

    if not user_input:
        return jsonify({
            "matched": None,
            "recommendations": [],
            "suggestions": [],
            "error": "Please enter a movie."
        }), 400

    matched_title, recs = recommend_movies(user_input, df, similarity_matrix)

    if recs:
        return jsonify({
            "matched": matched_title,
            "recommendations": [
                {"title": film, "score": score}
                for film, score in recs
            ],
            "suggestions": [],
            "error": None
        })

    suggestions = suggest_titles(user_input, df)
    return jsonify({
        "matched": None,
        "recommendations": [],
        "suggestions": suggestions,
        "error": None
    })


if __name__ == "__main__":
    app.run(debug=True)
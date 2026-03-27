<h1 align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Bitcount+Prop+Single+Ink&size=30&pause=1000&color=F748F3&center=true&vCenter=true&width=435&lines=Girly+Movie+Recommender" alt="Typing SVG" />
</h1>

<p align="center">
  A content-based movie recommendation web app that uses TF-IDF and cosine similarity to suggest similar films from the Barbie, Bratz, and Monster High franchises.
</p>

<p align="center">
  <img src="bibble-hip-hop.gif" width="600"/>
</p>

<p align="center">
  <a href="https://img.shields.io/badge/Python-3.12-pink"><img src="https://img.shields.io/badge/Python-3.12-pink" /></a>
  <a href="https://img.shields.io/badge/Flask-Web%20App-f7c6d9"><img src="https://img.shields.io/badge/Flask-Web%20App-f7c6d9" /></a>
  <a href="https://img.shields.io/badge/SQLite-Database-d8bfce"><img src="https://img.shields.io/badge/SQLite-Database-d8bfce" /></a>
  <a href="https://img.shields.io/badge/TF--IDF-Recommender-c9e6ee"><img src="https://img.shields.io/badge/TF--IDF-Recommender-c9e6ee" /></a>
  <a href="https://img.shields.io/badge/Dataset-Self--Curated-a047df"><img src="https://img.shields.io/badge/Dataset-Self--Curated-a047df" /></a>
</p>

---

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Future Improvements](#future-improvements)

---

## Overview

Girly Movie Recommender is a content-based movie recommendation system built with Python, Flask, and SQLite. It uses TF-IDF vectorization and cosine similarity to analyze movie plot descriptions and recommend films that are similar in story, themes, and overall feel.

This project focuses on movies from the Barbie, Bratz, and Monster High franchises using a self-curated dataset compiled specifically for this recommender. The recommendation engine is connected to a simple frontend interface, allowing users to enter a movie title and receive similar movie suggestions.

---

## How It Works

1. Movie data is collected and stored in a custom dataset.
2. The dataset is loaded into a SQLite database.
3. Plot descriptions are transformed into numerical text vectors using **TF-IDF**.
4. **Cosine similarity** is used to compare movie plots and measure how similar they are.
5. A Flask backend serves recommendations to a simple HTML frontend.

When a user enters a movie title, the app finds the matching film in the dataset and returns the top most similar movies based on plot similarity.

---

## Dataset

- **Source Type**: Self-curated dataset
- **Content**: Movies from the Barbie, Bratz, and Monster High franchises
- **Sources Used**:
  - Wikipedia
  - Barbie Wiki
  - Bratz Wiki – Movies
  - Monster High Wiki
- **Collection Method**: Movie metadata and plot summaries were manually compiled and organized into a custom CSV dataset.
- **Fields Included**:
  - `Id`
  - `Film`
  - `Release Date`
  - `Release Year`
  - `Era`
  - `Type`
  - `Plot`

Each row represents one film and includes its title, release information, franchise type, era classification, and plot summary.

**Note**: This dataset was created for educational and portfolio purposes only.

---

## Project Structure

```text
GirlyMovieRecommender/
├── app.py
├── templates/
│   └── index.html
├── scripts/
│   ├── recommender.py
│   ├── create_database.py
│   └── test_database.py
├── database/
│   └── girly_recommender.db
├── data/
│   └── girly_movies.csv
├── README.md
└── requirements.txt
```
---
## How to Run

1. Clone the repository
2. Install the required dependencies
   ```Bash
   pip install -r requirements.txt
   ```
3. Start the Flask server:
   ```Bash
   python app.py
   ```
4. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```
5. Enter a movie title to receive recommendations.
---
## Future Improvements
- Expand the dataset with more franchises or additional text fields such as reviews
- Experiment with combining plot-based recommendations with metadata-based filtering
- Improve title matching with better suggestion handling

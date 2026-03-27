import sqlite3
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "girly_recommender.db"

def run_query(conn, query, description):
    cursor = conn.cursor()
    print(f"\n--- {description} ---")
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    conn = sqlite3.connect(DB_PATH)

    try:
        # 1. Show tables
        run_query(
            conn,
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table';
            """,
            "Tables in database"
        )

        # 2. Count rows
        run_query(
            conn,
            """
            SELECT COUNT(*) AS total_rows
            FROM movies;
            """,
            "Total rows in movies table"
        )

        # 3. Preview data
        run_query(
            conn,
            """
            SELECT *
            FROM movies
            LIMIT 10;
            """,
            "First 10 rows"
        )

        # 4. Distinct types
        run_query(
            conn,
            """
            SELECT DISTINCT type
            FROM movies
            ORDER BY type;
            """,
            "Distinct movie types"
        )

        # 5. Distinct eras
        run_query(
            conn,
            """
            SELECT DISTINCT era
            FROM movies
            ORDER BY era;
            """,
            "Distinct eras"
        )

        # 6. Count by type and era
        run_query(
            conn,
            """
            SELECT type, era, COUNT(*) AS count
            FROM movies
            GROUP BY type, era
            ORDER BY type, era;
            """,
            "Counts by type and era"
        )

        # 7. Check for missing values
        run_query(
            conn,
            """
            SELECT *
            FROM movies
            WHERE id IS NULL
               OR film IS NULL OR TRIM(film) = ''
               OR era IS NULL OR TRIM(era) = ''
               OR type IS NULL OR TRIM(type) = ''
               OR plot IS NULL OR TRIM(plot) = '';
            """,
            "Rows with missing important values"
        )

        # 8. Check for duplicate film titles
        run_query(
            conn,
            """
            SELECT film, COUNT(*) AS count
            FROM movies
            GROUP BY film
            HAVING COUNT(*) > 1;
            """,
            "Duplicate film titles"
        )

    finally:
        conn.close()

if __name__ == "__main__":
    main()
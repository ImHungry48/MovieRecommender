import sqlite3
import csv
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "girly_movies.csv"
DB_PATH = BASE_DIR / "database" / "girly_recommender.db"

def create_connection():
    return sqlite3.connect(DB_PATH)

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            film TEXT NOT NULL,
            year TEXT NOT NULL,
            era TEXT NOT NULL,
            type TEXT NOT NULL,
            plot TEXT NOT NULL
        )
    """)
    conn.commit()

def load_csv_data():
    rows = []
    with open(DATA_PATH, "r", encoding="cp1252") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
            rows.append({
                "id": int(row["Id"]),
                "film": row["Film"].strip(),
                "year": row["Release Year"].strip(),
                "era": row["Era"].strip(),
                "type": row["Type"].strip(),
                "plot": row["Plot"].strip()
            })
    return rows

def insert_data(conn, rows):
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT OR REPLACE INTO movies (id, film, year, era, type, plot)
        VALUES (:id, :film, :year, :era, :type, :plot)
    """, rows)
    conn.commit()

def verify_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM movies")
    count = cursor.fetchone()[0]
    print(f"Total rows in movies table: {count}")

    cursor.execute("SELECT id, film, type FROM movies LIMIT 5")
    sample_rows = cursor.fetchall()
    print("\nSample rows:")
    for row in sample_rows:
        print(row)

def main():
    conn = create_connection()
    try:
        create_table(conn)
        rows = load_csv_data()
        insert_data(conn, rows)
        verify_data(conn)
        print("\nDatabase created and populated successfully.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
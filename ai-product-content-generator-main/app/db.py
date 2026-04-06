import sqlite3
import os

"""
    This module handles database operations for saving generated SEO descriptions to a MySQL database.
"""

DB_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
DB_PATH = os.path.join(DB_FOLDER, "youtube_articles.db")

def get_connection():
    os.makedirs(DB_FOLDER, exist_ok=True)
    return sqlite3.connect(DB_PATH)

def save_to_mysql(product_name, description):
    conn = get_connection()
    cursor = conn.cursor()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product_descriptions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_name TEXT,
            description TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO product_descriptions (product_name, description)
        VALUES (?, ?)
    """, (product_name, description))

    conn.commit()
    conn.close()

def drop_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS product_descriptions
    """)
    
    conn.commit()
    conn.close()
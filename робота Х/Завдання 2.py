import json
import psycopg2

# Налаштування підключення до PostgreSQL
conn_params = {
    "dbname": "test2",
    "user": "postgres",
    "password": "2281488",
    "host": "localhost",
    "port": 5432
}

# Шлях до JSON-файлу
file_path = r"C:\Users\Denis\Downloads\random_books.json"

# Створення таблиці для збереження даних
create_table_query = """
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    publication_year INTEGER NOT NULL
);
"""

# Читання даних з JSON-файлу
with open(file_path, "r", encoding="utf-8") as file:
    books = json.load(file)

# Підключення до бази даних та імпорт даних
try:
    # Підключення
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()
    
    # Створення таблиці
    cursor.execute(create_table_query)
    conn.commit()
    
    # Вставка даних у таблицю
    insert_query = """
    INSERT INTO books (title, author, publication_year)
    VALUES (%s, %s, %s);
    """
    for book in books:
        cursor.execute(insert_query, (book["назва"], book["автор"], book["рік видання"]))
    conn.commit()
    
    print("Дані успішно імпортовано!")
    
except Exception as e:
    print("Виникла помилка:", e)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

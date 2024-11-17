import psycopg2
from psycopg2 import sql

# Параметри підключення до бази даних
db_config = {
    'dbname': 'test',
    'user': 'postgres',
    'password': '2281488',
    'host': 'localhost',  # або інший хост
    'port': '5432'        # стандартний порт PostgreSQL
}

# Підключення до бази даних
try:
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()

    create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    "ім'я" VARCHAR(100) NOT NULL,
    вік INTEGER NOT NULL,
    адресса VARCHAR(255) NOT NULL
);
'''              

    # Виконання запиту
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблиця 'users' була успішно створена.")

except Exception as e:
    print(f"Виникла помилка: {e}")

finally:
    # Закриття курсора та з'єднання
    if cursor:
        cursor.close()
    if connection:
        connection.close()
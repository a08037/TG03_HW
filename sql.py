import sqlite3

def init_db():
    # Подключение к базе данных (создаст файл, если его еще нет)
    conn = sqlite3.connect('school_data.db')
    cur = conn.cursor()

    # Создание таблицы students
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL
        )
    ''')

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

# Запуск функции для инициализации базы данных
init_db()

import sqlite3

with sqlite3.connect('toy_shop.db') as db:
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS toys (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT,
            price REAL,
            stock_quantity INTEGER
        )
    ''')

    cursor.execute("INSERT INTO toys (name, type, price, stock_quantity) VALUES (?, ?, ?, ?)",
                   ("М'яка ведмедиця", "Плюшева іграшка", 19.99, 50))

    cursor.execute("INSERT INTO toys (name, type, price, stock_quantity) VALUES (?, ?, ?, ?)",
                   ("М'яка кішка", "Плюшева іграшка", 10.99, 25))

    cursor.execute("INSERT INTO toys (name, type, price, stock_quantity) VALUES (?, ?, ?, ?)",
                   ("М'який пес", "Плюшева іграшка", 12.99, 7))

    cursor.execute("DELETE FROM toys WHERE stock_quantity <= 0")
    cursor.execute("UPDATE toys SET stock_quantity = stock_quantity + 5")

    cursor.execute("SELECT name FROM toys")
    rows = cursor.fetchall()

    for row in rows:
        print(row[0])

    cursor.execute("SELECT name, price FROM toys WHERE price < 20")
    rows = cursor.fetchall()

    for row in rows:
        print("Ім'я:", row[0])
        print("Ціна:", row[1])

    cursor.execute("SELECT type, SUM(stock_quantity) FROM toys GROUP BY type")
    rows = cursor.fetchall()

    for row in rows:
        print("Тип:", row[0])
        print("Загальна кількість:", row[1])

    cursor.execute("SELECT name, stock_quantity FROM toys WHERE stock_quantity < 10")
    rows = cursor.fetchall()

    for row in rows:
        print("Ім'я:", row[0])
        print("Кількість на складі:", row[1])

    cursor.execute("SELECT name, stock_quantity FROM toys")
    rows = cursor.fetchall()

    for row in rows:
        print("Ім'я:", row[0])
        print("Кількість на складі:", row[1])

    cursor.execute("SELECT name, price FROM toys WHERE price < 20")
    rows = cursor.fetchall()

    for row in rows:
        print("Ім'я:", row[0])
        print("Ціна:", row[1])

    cursor.execute("SELECT name, stock_quantity FROM toys WHERE stock_quantity < 10")
    rows = cursor.fetchall()

    for row in rows:
        print("Ім'я:", row[0])
        print("Кількість на складі:", row[1])

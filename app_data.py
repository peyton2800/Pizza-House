# app_data.py

import sqlite3


def establish_menu_items_connection():
    return sqlite3.connect('menu_items.db')


def close_menu_items_connection(conn):
    conn.close()


def create_orders_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        menu_item_id INTEGER,
        num_items INTEGER,
        FOREIGN KEY(menu_item_id) REFERENCES menu_items(id)
    );
    ''')
    conn.commit()


def insert_menu_item(item_name, price):
    conn = establish_menu_items_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO menu_items (item_name, price) VALUES (?, ?)', (item_name, price))
    conn.commit()
    close_menu_items_connection(conn)


# Inserting menu items
insert_menu_item('Cheese Pizza', 10,)
insert_menu_item('Burger', 8)
insert_menu_item('Pasta', 12)
insert_menu_item('Salad', 6)

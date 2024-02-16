from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Define the order list
order = []


# Function to fetch menu items from the database
def fetch_menu_items():
    connect = sqlite3.connect('menu_items.db')
    cursor = connect.cursor()
    cursor.execute('SELECT item_name, price FROM menu_items')
    menu_items = dict(cursor.fetchall())
    connect.close()
    return menu_items


# Function to fetch menu item by ID from the database
def fetch_menu_item_by_id(menu_item_id):
    connect = sqlite3.connect('menu_items.db')
    cursor = connect.cursor()
    cursor.execute('SELECT item_name, price, description FROM menu_items WHERE id = ?', (menu_item_id,))
    menu_item = cursor.fetchone()
    connect.close()
    return menu_item


# Route to display the menu
@app.route('/')
def menu():
    menu_items = fetch_menu_items()
    return render_template('menu.html', menu_items=menu_items, current_page='menu')


# Route to add an item to the order
@app.route('/add_to_order', methods=['POST'])
def add_to_order():
    item = request.form['item']
    menu_items = fetch_menu_items()
    connect = sqlite3.connect('menu_items.db')
    cursor = connect.cursor()
    cursor.execute('SELECT id, price FROM menu_items WHERE item_name = ?', (item,))
    item_id, price = cursor.fetchone()
    connect.close()
    if (item_id, price):
        order.append({'item_id': item_id, 'item': item, 'price': price})
        return redirect(url_for('menu'))
    else:
        return "Item not found in menu!"


# Route to remove an item from the order
@app.route('/remove_from_order/<int:item_index>', methods=['POST'])
def remove_from_order(item_index):
    if 0 <= item_index < len(order):
        del order[item_index]
    return redirect(url_for('view_order'))


# Route to view the order
@app.route('/view_order')
def view_order():
    total = sum(item['price'] for item in order)
    items_with_details = [
        {'index': index, 'item_name': fetch_menu_item_by_id(item['item_id'])[0], 'price': item['price']} for index, item
        in enumerate(order)]
    return render_template('view_order.html', items=items_with_details, total=total, current_page='view_order')


# Route to check out and save the order to orders.db
@app.route('/checkout')
def checkout():
    connect_orders = sqlite3.connect('orders.db')
    cursor_orders = connect_orders.cursor()

    for item in order:
        cursor_orders.execute("INSERT INTO orders (menu_item_id, num_items) VALUES (?, ?)",
                              (item['item_id'], 1))  # Assuming num_items is 1 for simplicity

    connect_orders.commit()
    connect_orders.close()

    total = sum(item['price'] for item in order)
    return render_template('checkout.html', order=order, total=total)


if __name__ == '__main__':
    app.run(debug=True)

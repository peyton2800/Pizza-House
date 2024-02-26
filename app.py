#app.py
from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
# Set a secret key for session management.
app.secret_key = 'your_secret_key'

# Define default customization options for different types of pizzas.
default_customizations = {
    "Cheese Pizza": {
        "Size": "Large",
        "Pizza Sauce": "Original",
        "Crust": "Original Crust",
        "Cheese": "3 Cheese Blend",
        "Meats": None,
        "Veggies": None
    },
    "Pepperoni Pizza": {
        "Size": "Large",
        "Pizza Sauce": "Original",
        "Crust": "Original Crust",
        "Cheese": "3 Cheese Blend",
        "Meats": "Pepperoni",
        "Veggies": None
    },
    "Sausage Pizza": {
        "Size": "Large",
        "Pizza Sauce": "Original",
        "Crust": "Original Crust",
        "Cheese": "3 Cheese Blend",
        "Meats": "Sausage",
        "Veggies": None
    }
}

# Predefined deals to be shown on the home page.
deals = [
    {"title": "Family Meal Deal", "description": "Two large pizzas, two sides, and a 2-liter soda for $24.99."},
    {"title": "Weekday Lunch Special",
     "description": "Personal pizza and a soft drink for $5.99. Available from 11 AM to 3 PM on weekdays."},
    {"title": "Buy One Get One Free",
     "description": "Buy any large pizza at regular price and get a second large pizza of equal or lesser value for free."},
]


def get_item_price(item_name):
    """
        Retrieve the price of a specific menu item from the database.

        Parameters:
            item_name (str): The name of the item.

        Returns:
            float: The price of the item.
        """
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM menu_items WHERE item_name=?", (item_name,))
    price = cursor.fetchone()[0]
    conn.close()
    return price


def get_customization_price(option_type, option_name):
    """
        Retrieve the additional cost for a specific customization option.

        Parameters:
            option_type (str): The type of customization.
            option_name (str): The name of the customization option.

        Returns:
            float: The additional cost of the customization option.
        """
    if option_name == 'None' or option_name in default_customizations.get(option_type, {}).get('defaults', []):
        return 0  # No additional cost for default or 'None' options

    # Check the database for additional price
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()
    cursor.execute("SELECT additional_price FROM customization_options WHERE option_name=?", (option_name,))
    additional_price = cursor.fetchone()
    conn.close()
    return additional_price[0] if additional_price else 0


@app.route('/')
def home():
    """
        Render the homepage with the current deals.

        Returns:
            Template: The home page template populated with deals.
        """
    return render_template('home.html', deals=deals)


@app.route('/menu')
def menu():
    """
        Display the menu with items and customizable options.

        Returns:
            Template: The menu page template populated with menu items and customization options.
        """
    conn = sqlite3.connect('tables.db')
    cursor = conn.cursor()

    # SQL query to select all items from the 'menu_items' table.
    cursor.execute("SELECT item_name, price, description, category FROM menu_items")
    menu_items = cursor.fetchall()  # Fetch all results from the executed query and store them in 'menu_items'.

    # SQL query to select all customization options from the 'customization_options' table.
    cursor.execute("SELECT option_type, option_name, additional_price, category FROM customization_options")
    customization_options = cursor.fetchall()

    options_by_category = {}
    # Loop through each customization option fetched from the database.
    for option_type, option_name, additional_price, category in customization_options:
        if category not in options_by_category:
            options_by_category[category] = {}
        if option_type not in options_by_category[category]:
            options_by_category[category][option_type] = []
        # Append the current customization option to the appropriate list in the dictionary.
        options_by_category[category][option_type].append({
            'option_name': option_name,
            'additional_price': additional_price
        })

    categorized_menu = {}
    # Loop through each menu item fetched from the database.
    for item in menu_items:
        if item[3] not in categorized_menu:
            categorized_menu[item[3]] = []
        # Append the current item to the appropriate list in the dictionary.
        categorized_menu[item[3]].append({
            'item_name': item[0],
            'price': item[1],
            'description': item[2],
        })

    conn.close()

    # Render the 'menu.html' template
    return render_template('menu.html', categorized_menu=categorized_menu, options_by_category=options_by_category,
                           default_customizations=default_customizations)


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    """
        Add an item along with selected customizations to the shopping cart.

        Returns:
            Redirect: A redirect back to the menu page after updating the cart.
        """
    item_name = request.form['item']
    base_price = get_item_price(item_name)

    selected_customizations = {}
    non_default_customizations = {}

    additional_cost = 0

    # Iterate over each key-value pair in the form data.
    for key, value in request.form.items():
        if key.startswith('customization_'):
            option_type = key[
                          len('customization_'):].capitalize()
            option_value = value.strip()

            default_value = str(default_customizations.get(item_name, {}).get(option_type, '')).strip()

            # Compare the selected customization with the default value, ignoring case and whitespace differences.
            if (default_value.lower() != option_value.lower()) and option_value.lower() != 'none':
                cost = get_customization_price(option_type, option_value)
                additional_cost += cost
                non_default_customizations[option_type] = option_value
            selected_customizations[option_type] = option_value
    total_price = base_price + additional_cost

    # Create a unique key for this cart item, to tell the difference from other instances of the same item with different customizations.
    item_key = f"{item_name}|{str(non_default_customizations)}" if non_default_customizations else item_name
    cart_items = session.get('cart', {})

    # If the item (with its specific customizations) is already in the cart, update quantity and total price.
    if item_key in cart_items:
        cart_item = cart_items[item_key]
        cart_item['quantity'] += 1
        cart_item['additional_cost'] = (cart_item.get('additional_cost', 0) + additional_cost)
        cart_item['total_price'] = (cart_item['base_price'] + cart_item['additional_cost']) * cart_item['quantity']
    else:
        # Add it with its details if its not already in cart.
        cart_items[item_key] = {
            'item_name': item_name,
            'quantity': 1,
            'base_price': base_price,
            'additional_cost': additional_cost,
            'total_price': total_price,
            'customizations': selected_customizations,
            'non_default_customizations': non_default_customizations
        }

    # Update the cart in the session with the modified cart items.
    session['cart'] = cart_items
    return redirect(url_for('menu'))


@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    """
        Remove an item from the shopping cart.

        Returns:
            Redirect: A redirect back to the cart view after the item is removed.
        """
    item_key = request.form.get('item_key')  # Retrieve the unique key of the item to be removed.

    cart_items = session.get('cart', {})

    if item_key in cart_items:
        del cart_items[item_key]
        session['cart'] = cart_items
        session.modified = True
        print(
            f"Removed item with key: {item_key}. Cart now: {session['cart']}")  # Debugging
    else:
        print(f"Item key not found: {item_key}. Current cart: {session['cart']}")

    return redirect(url_for('view_cart'))


@app.route('/cart')
def view_cart():
    """
        Display the current state of the shopping cart to the user.

        Returns:
            Template: The cart view template populated with cart items.
        """
    cart_items = session.get('cart', {})
    items_with_details = []  #list to hold detailed info about each cart item for display.
    total_cart_price = 0

    for item_key, item_data in cart_items.items():
        # Loop through each item in the cart to calculate prices and prepare details.
        item_base_price = item_data['base_price']
        quantity = item_data['quantity']

        total_price = item_data.get('total_price', item_base_price * quantity)
        item_total_price = total_price
        total_cart_price += item_total_price

        item_details = {
            'item_name': item_data['item_name'],
            'quantity': quantity,
            'customizations': item_data.get('customizations', {}),
            'non_default_customizations': item_data.get('non_default_customizations', {}),
            'item_total_price': item_total_price,
        }
        # Append the detailed item info to the list of items to display.
        items_with_details.append(item_details)

    return render_template('cart.html', items_with_details=items_with_details, total_cart_price=total_cart_price)


@app.route('/checkout')
def checkout():
    """
       Summarize the cart and prepare for checkout, including total price calculation.

       Returns:
           Template: The checkout template populated with cart summary and total cost.
       """
    cart_items = session.get('cart', {})
    total = 0

    for item_key, item_data in cart_items.items():
        additional_cost = sum(get_customization_price(option_type, option_value)
                              for option_type, option_value in item_data.get('non_default_customizations', {}).items())

        item_data['item_total_price'] = (item_data['base_price'] + additional_cost) * item_data['quantity']
        total += item_data['item_total_price']

    return render_template('checkout.html', cart_items=cart_items, total=total)


def calculate_total(cart_items):
    """
        Calculate the total cost of all items in the cart.

        Parameters:
            cart_items (dict): A dictionary of cart items.

        Returns:
            float: The total cost of the cart.
        """
    return sum(item['total_price'] * item['quantity'] for item in cart_items.values())


if __name__ == '__main__':
    # This is the entry point of the Flask application.
    app.run(
        debug=True)

from flask import Flask, request, render_template, redirect, url_for, session
from flask_session import Session
from src.product_shop_sorting import sort_shopping_list

# here: same functionality as "from cs50 import SQL"
from cs50 import SQL


app = Flask(__name__)
db = SQL("sqlite:///../shopping.db")

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Homepage that displays all shopping lists
@app.route('/')
def home():
    shopping_lists = db.execute("SELECT * FROM ShoppingList")
    # Display the shopping lists on the home page
    return render_template('home.html', shopping_lists=shopping_lists)

# Page for creating a new shopping list
@app.route('/new_list')
def new_list():
    return render_template('new_list.html')


    
# Function for adding a new shopping list
@app.route('/add_list', methods=['POST'])
def add_list():
    # Get the name of the new list from the form
    list_name = request.form['list_name']
    # If the form wasn't empty:
    if list_name:
        # Insert the new list into the shopping_lists table
        db.execute("INSERT INTO shopping_lists (title, user_id) VALUES (?, ?)", list_name, 0)
        # Redirect to the home page to display all shopping lists
        return redirect(url_for('home'))
      
    else:
        return redirect(url_for('new_list'))


# Function that gets called if the user clicks on a specific shopping list
@app.route('/view_list/<list_id>')
def view_list(list_id):
    # Query the database for the shopping list with the given name and the current user's id
    
    list_data = db.execute("SELECT * FROM ShoppingList WHERE ShoppingListId = ?", list_id)

    if list_data:
        # Query the database for the items in the shopping list
        items = db.execute("SELECT * FROM ShoppingListMapping sm, ProductList pl WHERE sm.ShoppingListId = ? AND sm.ProductID = pl.ProductID", list_id)
        products = db.execute("SELECT * FROM ProductList")
        supermarkets = db.execute("SELECT * FROM SupermarketList")
        # ToDo: replace "items = []" with code that gets all the items of the specific list - name of the variable: items
        
        # Render the list page with the items of the shopping list
        return render_template('list.html', list_name=list_data[0]['ShoppingListName'], list_id=list_id, items=items, products=products, supermarkets=supermarkets)

    # If the list was not found, redirect to the home page
    return redirect(url_for('home'))

# Function that gets called if the user clicks on a specific shopping list
@app.route('/go_shopping/<list_id>', methods=['GET'])
def go_shopping(list_id):
    supermarket_id = "test"
    if request.method == "GET":
        supermarket_id = request.args.get('supermarket')

    list_data = db.execute("SELECT * FROM ShoppingList WHERE ShoppingListId = ?", list_id)
    supermarket = db.execute("SELECT * FROM SupermarketList WHERE SupermarketID = ?", supermarket_id)
    if list_data:
        # Query the database for the items in the shopping list
        items = db.execute("SELECT * FROM ShoppingListMapping sm, ProductList pl WHERE sm.ShoppingListId = ? AND sm.ProductID = pl.ProductID", list_id)
        products = db.execute("SELECT * FROM ProductList")
        product_ids = [item['ProductID'] for item in items]
        sorted_product_ids = sort_shopping_list('../smartGrocery.db', supermarket_id, product_ids)
        product_id_to_index = {pid: index for index, pid in enumerate(sorted_product_ids)}
        items = sorted(items, key=lambda item: product_id_to_index[item['ProductID']])
        # ToDo: replace "items = []" with code that gets all the items of the specific list - name of the variable: items
        
        # Render the list page with the items of the shopping list

        print(supermarket)
        return render_template('go_shopping.html', list_name=list_data[0]['ShoppingListName'], list_id=list_id, items=items, products=products, supermarket=supermarket[0])

    return redirect(url_for('home'))


# Function for deleting a specific shopping list
@app.route('/delete_list/<list_id>', methods=["GET"])
def delete_list(list_id):
    # Query the database for the shopping list with the given name and the current user's id
    list_data = db.execute("SELECT * FROM shopping_lists WHERE id = ? AND user_id = ?", list_id, 0)

    if list_data:
        # Delete the shopping list and all the items in the list from the database
        # Delete the shopping items (with foreign keys) first
        db.execute("DELETE FROM shopping_items WHERE shopping_list_id IN (SELECT id FROM shopping_lists WHERE id = ?)", list_id)
        # Then delete the empty list
        db.execute("DELETE FROM shopping_lists WHERE id = ?", list_id)

    # Redirect to the home page to display the updated list of shopping lists
    return redirect(url_for('home'))


# Function for adding an item to a specific shopping list
@app.route('/add_item/<list_id>', methods=['POST'])
def add_item(list_id):
    itemName = request.form.get("item_name") 
    item = db.execute("SELECT * FROM ProductList WHERE ProductName = ?", itemName)
    if len(item) == 1:
        db.execute("INSERT INTO ShoppingListMapping (ProductID, ShoppingListId) VALUES(?, ?)", item[0]['ProductID'], list_id)
        return redirect(url_for('view_list', list_id=list_id))
    else:
        return redirect(url_for('home'))
    


# Function for deleting an item from a specific shopping list
@app.route('/delete_item/<list_id>/<item_id>', methods=["POST"])
def delete_item(list_id, item_id):
    db.execute("DELETE FROM ShoppingListMapping WHERE ProductID = ? AND ShoppingListId = ?", item_id, list_id)
    return redirect(url_for('view_list', list_id=list_id))

# Function to register a new user
@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")

    # Check if the user is already registered
    user = db.execute("SELECT * FROM users WHERE name = ?", username)
    if user:
        # If the user is already registered, render an error message on the register page
        return render_template("register.html", error="User already exists")
    else:
        # If the user is not already registered, insert the user into the users table
        db.execute("INSERT INTO users (name, password) VALUES(?, ?)", username, password)
        return redirect("/")
  # If the request method is GET, render the register page
  return render_template("register.html")

from flask import Flask, request, render_template, redirect, url_for, session
from flask_session import Session

# here: same functionality as "from cs50 import SQL"
from cs50 import SQL


app = Flask(__name__)
db = SQL("sqlite:///shopping.db")

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Homepage that displays all shopping lists
@app.route('/')
def home():
    shopping_lists = db.execute("SELECT * FROM shopping_lists WHERE user_id = ?", 0)
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
    list_data = db.execute("SELECT * FROM shopping_lists WHERE id = ? AND user_id = ?", list_id, 0)

    if list_data:
        # Query the database for the items in the shopping list
        items = []
        # ToDo: replace "items = []" with code that gets all the items of the specific list - name of the variable: items
        
        # Render the list page with the items of the shopping list
        return render_template('list.html', list_name=list_data[0]['title'], list_id=list_id, items=items)

    # If the list was not found, redirect to the home page
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
  # If the user is logged in, render the add item page
  if "user_id" in session:
    # ToDo: If a list_name and an item_name (not empty) were given/found, add the item to the specific list
    # ToDo: Info: the variable list_name is the list_name that is also given in the URL - you can use this variable in your code
    # ToDo: Replace the following return statement or integrate it in your code
    return redirect(url_for('view_list', list_id=list_id))
    
  else:
    # If the user is not logged in, redirect to the login page
    return redirect(url_for('login'))


# Function for deleting an item from a specific shopping list
@app.route('/delete_item/<list_id>/<item_id>', methods=["GET"])
def delete_item(list_id, item_id):
  # If the user is logged in, render the delete item page
  if "user_id" in session:
    # ToDo: If a list_name and an item_name were found, delete the item from the specific list
    # ToDo: Info: the variables list_name and item_name are the list_name and irem_name that are also given in the URL - you can use this variables in your code

    # Redirect to the view_list page to display the updated list
    return redirect(url_for('view_list', list_id=list_id))

  else:
    # If the user is not logged in, redirect to the login page
    return redirect(url_for('login'))


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

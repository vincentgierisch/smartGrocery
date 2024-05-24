DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS shopping_lists;
DROP TABLE IF EXISTS shopping_items;

CREATE TABLE users (
  id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	password TEXT NOT NULL
);

CREATE TABLE shopping_lists (
	id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
  user_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE shopping_items (
	id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
  shopping_list_id INTEGER,
  FOREIGN KEY(shopping_list_id) REFERENCES shopping_lists(id)
);

INSERT INTO users (name, password) VALUES ("Anna", "1234");

INSERT INTO shopping_lists (title, user_id) VALUES ("DM", 1);

INSERT INTO shopping_items (title, shopping_list_id) VALUES ("Duschgel", 1);
INSERT INTO shopping_items (title, shopping_list_id) VALUES ("Shampoo", 1);
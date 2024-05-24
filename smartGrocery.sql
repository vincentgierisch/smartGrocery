CREATE TABLE ProductList (
ProductName TEXT,
ProductID INTEGER,
PRIMARY KEY(ProductID)
);

INSERT INTO ProductList (ProductName,ProductID) VALUES ('Chocolate',2001);
INSERT INTO ProductList (ProductName,ProductID) VALUES ('Shampoo',3001);
INSERT INTO ProductList (ProductName,ProductID) VALUES ('Bodywash',3002);
INSERT INTO ProductList (ProductName,ProductID) VALUES ('Rice',4001);
INSERT INTO ProductList (ProductName,ProductID) VALUES ('Pasta',4002);
INSERT INTO ProductList (ProductName,ProductID) VALUES ('Chips',5001);
INSERT INTO ProductList (ProductName,ProductID) VALUES ('Cookies',5002);
INSERT INTO ProductList (ProductName,ProductID) VALUES ('Frozen Pizza',6001);
INSERT INTO ProductList (ProductName,ProductID) VALUES ('Frozen Vegetables',6002);
INSERT INTO ProductList (ProductName,ProductID) VALUES ('Beer',7001);
INSERT INTO ProductList (ProductName,ProductID) VALUES ('Cola',7002);
INSERT INTO ProductList (ProductName,ProductID) VALUES ('Water',7003);
INSERT INTO ProductList (ProductName,ProductID) VALUES ('Chicken',8001);
INSERT INTO ProductList (ProductName,ProductID) VALUES ('Toilet Paper',9001);

CREATE TABLE ShoppingLists (
ProductName TEXT,
ShoppingListID INTEGER,
);

INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Chocolate',1);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Shampoo',1);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Rice',1);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Chips',1);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Frozen Pizza',1);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Beer',1);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Chicken',1);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Toilet Paper',1);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Bodywash',2);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Pasta',2);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Cookies',2);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Frozen Pizza',2);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Frozen Vegetables',2);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Toilet Paper',2);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Cola',2);
INSERT INTO ShoppingList (ProductName,ShoppingListID) VALUES ('Water',2);

CREATE TABLE SupermarketList (
SupermarketName TEXT,
SupermarketID INTEGER,
);

INSERT INTO SupermarketList (SupermarketName,SupermarketID) VALUES ('GreenMarket',1);
INSERT INTO SupermarketList (SupermarketName,SupermarketID) VALUES ('RedMarket',2);
INSERT INTO SupermarketList (SupermarketName,SupermarketID) VALUES ('YellowMarket',3);

CREATE TABLE Mapping (
Product TEXT,
SupermarketID INTEGER,
);






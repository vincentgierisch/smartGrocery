CREATE ShoppingListMapping (
    ShoppingListId INTEGER,
    ProductID INTEGER
    PRIMARY KEY(ShoppingListID)
    );

CREATE TABLE ProductList (
    ProductName TEXT,
    ProductID INTEGER,
    PRIMARY KEY(ProductID)
);

INSERT INTO ProductList (ProductName, ProductID) VALUES ('Chocolate', 2001);
INSERT INTO ProductList (ProductName, ProductID) VALUES ('Shampoo', 3001);
INSERT INTO ProductList (ProductName, ProductID) VALUES ('Bodywash', 3002);
INSERT INTO ProductList (ProductName, ProductID) VALUES ('Rice', 4001);
INSERT INTO ProductList (ProductName, ProductID) VALUES ('Pasta', 4002);
INSERT INTO ProductList (ProductName, ProductID) VALUES ('Chips', 5001);
INSERT INTO ProductList (ProductName, ProductID) VALUES ('Cookies', 5002);
INSERT INTO ProductList (ProductName, ProductID) VALUES ('Frozen Pizza', 6001);
INSERT INTO ProductList (ProductName, ProductID) VALUES ('Frozen Vegetables', 6002);
INSERT INTO ProductList (ProductName, ProductID) VALUES ('Beer', 7001);
INSERT INTO ProductList (ProductName, ProductID) VALUES ('Cola', 7002);
INSERT INTO ProductList (ProductName, ProductID) VALUES ('Water', 7003);
INSERT INTO ProductList (ProductName, ProductID) VALUES ('Chicken', 8001);
INSERT INTO ProductList (ProductName, ProductID) VALUES ('Toilet Paper', 9001);

CREATE TABLE ShoppingLists (
    ShoppingListName TEXT,
    ProductID INTEGER
);

INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('A', 2001);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('A', 3001);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('A', 4001);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('A', 4002);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('A', 5001);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('A', 6001);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('A', 7001);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('A', 7003);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('B', 3002);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('B', 4002);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('B', 5002);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('B', 6002);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('B', 7002);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('B', 8001);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('B', 9001);
INSERT INTO ShoppingLists (ShoppingListName, ProductID) VALUES ('B', 7003);

CREATE TABLE SupermarketList (
    SupermarketName TEXT,
    SupermarketID INTEGER,
    PRIMARY KEY(SupermarketID)
);

INSERT INTO SupermarketList (SupermarketName, SupermarketID) VALUES ('GreenMarket', 1);
INSERT INTO SupermarketList (SupermarketName, SupermarketID) VALUES ('RedMarket', 2);
INSERT INTO SupermarketList (SupermarketName, SupermarketID) VALUES ('YellowMarket', 3);

CREATE TABLE Mapping (
    ProductID1 INTEGER,
    ProductID2 INTEGER,
    SupermarketID INTEGER,
    Counter INTEGER,
    FOREIGN KEY(SupermarketID) REFERENCES SupermarketList(SupermarketID)
);

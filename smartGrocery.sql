CREATE TABLE `ShoppingList` (
  `ShoppingListId` integer PRIMARY KEY,
  `ShoppingListName` text
);

CREATE TABLE `ShoppingListMapping` (
  `ListMappingID` integer PRIMARY KEY,
  `ShoppingListId` integer,
  `ProductID` integer
);

CREATE TABLE `ProductList` (
  `ProductName` text,
  `ProductID` integer PRIMARY KEY
);

CREATE TABLE `SupermarketList` (
  `SupermarketName` TEXT,
  `SupermarketID` integer PRIMARY KEY
);

CREATE TABLE `Mapping` (
  `MappingID` integer PRIMARY KEY,
  `ProductID1` integer,
  `ProductID2` integer,
  `SupermarketID` integer,
  `Counter` integer
);

ALTER TABLE `ShoppingList` ADD FOREIGN KEY (`ShoppingListId`) REFERENCES `ShoppingListMapping` (`ShoppingListId`);

ALTER TABLE `ShoppingListMapping` ADD FOREIGN KEY (`ProductID`) REFERENCES `ProductList` (`ProductID`);

ALTER TABLE `SupermarketList` ADD FOREIGN KEY (`SupermarketID`) REFERENCES `Mapping` (`SupermarketID`);

ALTER TABLE `ProductList` ADD FOREIGN KEY (`ProductID`) REFERENCES `Mapping` (`ProductID1`);

ALTER TABLE `ProductList` ADD FOREIGN KEY (`ProductID`) REFERENCES `Mapping` (`ProductID2`);

INSERT INTO ShoppingList (ShoppingListId, ShoppingListName) VALUES (1, 'Monday');
INSERT INTO ShoppingList (ShoppingListId, ShoppingListName) VALUES (2, 'Friday');


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


INSERT INTO ShoppingListMapping (ProductID, ShoppingListID ) VALUES (2001, 1);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (3001, 1);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (4001, 1);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (5001, 1);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (6001, 1);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (7001, 1);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (7002, 1);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (8001, 1);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (3002, 2);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (4002, 2);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (5001, 2);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (9001, 2);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (8001, 2);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (7002, 2);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (5002, 2);
INSERT INTO ShoppingListMapping (ProductID, ShoppingListID) VALUES (7003, 2);


INSERT INTO SupermarketList (SupermarketName, SupermarketID) VALUES ('GreenMarket', 1);
INSERT INTO SupermarketList (SupermarketName, SupermarketID) VALUES ('RedMarket', 2);


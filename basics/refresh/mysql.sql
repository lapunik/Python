--CREATE TABLE lide(id INTEGER NOT NULL PRIMARY KEY, sureNmae TEXT NOT NULL, lastNmae TEXT NOT NULL ,year INTEGER NOT NULL);

--INSERT INTO lide(id, sureNmae, lastNmae, year)
--VALUES(1,"Vojta","Lapunik",1997);

-- SELECT * FROM lide;

--INSERT INTO lide(id, sureNmae, lastNmae, year)
--VALUES(2,"Ondřej","Sodomka",1994);

/*
SELECT * FROM Customers;
SELECT * FROM Orders;

SELECT Customers.Customer_ID, Customers.Name, SUM(CASE WHEN Orders.Type = 'Buy' THEN Orders.Amount ELSE 0 END) AS tot_amt 
FROM Customers JOIN Orders ON Customers.Customer_ID = Orders.Customer_ID;



SELECT 
    Customers.Customer_ID, 
    SUM(CASE WHEN Orders.Type = 'Buy' THEN Orders.Amount ELSE 0 END)  
FROM 
    Customers
JOIN 
    Orders ON Customers.Customer_ID = Orders.Customer_ID 
WHERE 
    Customers.Birth_Year < 2000
GROUP BY
    Customers.Customer_ID;
    */

/*
    -- Vytvoření tabulky Cl
CREATE TABLE Cl (
    clid INTEGER PRIMARY KEY,
    byear INTEGER
);

-- Vložení dat do tabulky Cl
INSERT INTO Cl (clid, byear) VALUES
(1, 1985),
(2, 2001),
(3, 1995),
(4, 1970),
(5, 2003);

-- Vytvoření tabulky Tr
CREATE TABLE Tr (
    trid INTEGER PRIMARY KEY,
    clid INTEGER,
    dir CHAR(1),
    amt REAL,
    FOREIGN KEY (clid) REFERENCES Cl(clid)
);

-- Vložení dat do tabulky Tr
INSERT INTO Tr (trid, clid, dir, amt) VALUES
(1, 1, 'C', 100.50),
(2, 1, 'D', 200.00),
(3, 3, 'C', 50.00),
(4, 3, 'C', 70.00),
(5, 3, 'D', 30.00),
(6, 4, 'D', 150.00);
*/
/*
SELECT * FROM Cl;
SELECT * FROM Tr;

SELECT Cl.clid, SUM(CASE WHEN Tr.dir = 'C' THEN Tr.amt ELSE 0 END)
FROM Cl JOIN Tr ON Cl.clid = Tr.clid
WHERE Cl.byear < 2000
GROUP BY Cl.clid;
*/


-- DROP TABLE studenti;


-- CREATE TABLE studenti(id INTEGER PRIMARY KEY AUTOINCREMENT,jmeno TEXT NOT NULL,prijmeni TEXT NOT NULL,vek INTEGER);

/*
INSERT INTO studenti(jmeno,prijmeni,vek)
VALUES
('Jan','Novák',20),
('Petra','Dvořáková',22),
('Adam','Malý',19);
*/

/*
SELECT * FROM studenti WHERE studenti.vek>20;

SELECT * FROM studenti WHERE studenti.jmeno = 'D%';

ALTER TABLE studenti   ;

SELECT * FROM studenti;

*/





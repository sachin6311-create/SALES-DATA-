-- Create SalesData Table
CREATE TABLE IF NOT EXISTS SalesData (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Age INT NOT NULL,
    City VARCHAR(50) NOT NULL,
    PurchaseAmount DECIMAL(10, 2) NOT NULL,
    PurchaseDate DATE NOT NULL
);

-- Create Index for better query performance
CREATE INDEX idx_customer_id ON SalesData(CustomerID);
CREATE INDEX idx_purchase_date ON SalesData(PurchaseDate);

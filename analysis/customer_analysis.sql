-- SQL Queries for Customer Analysis
-- Finding customers with purchases above average and related insights

-- ============================================
-- Query 1: Customers with Above-Average Purchases
-- ============================================
-- Shows all customers who have spent more than the average purchase amount
SELECT 
    CustomerID,
    Name,
    Age,
    City,
    PurchaseAmount,
    PurchaseDate,
    ROUND((SELECT AVG(PurchaseAmount) FROM SalesData), 2) as AvgPurchaseAmount,
    ROUND(PurchaseAmount - (SELECT AVG(PurchaseAmount) FROM SalesData), 2) as AmountAboveAvg
FROM SalesData
WHERE PurchaseAmount > (SELECT AVG(PurchaseAmount) FROM SalesData)
ORDER BY PurchaseAmount DESC;

-- ============================================
-- Query 2: Top 10 High-Value Customers
-- ============================================
-- Shows the top 10 customers by single purchase amount
SELECT 
    CustomerID,
    Name,
    Age,
    City,
    PurchaseAmount,
    PurchaseDate,
    ROUND(PurchaseAmount / (SELECT AVG(PurchaseAmount) FROM SalesData), 2) as MultiplesOfAverage
FROM SalesData
ORDER BY PurchaseAmount DESC
LIMIT 10;

-- ============================================
-- Query 3: Customers with Multiple Above-Average Purchases
-- ============================================
-- Shows customers who have made multiple purchases above average
SELECT 
    CustomerID,
    Name,
    Age,
    City,
    COUNT(*) as AboveAvgPurchaseCount,
    SUM(PurchaseAmount) as TotalSpent,
    ROUND(AVG(PurchaseAmount), 2) as AvgCustomerPurchase,
    MIN(PurchaseAmount) as MinAmount,
    MAX(PurchaseAmount) as MaxAmount
FROM SalesData
WHERE PurchaseAmount > (SELECT AVG(PurchaseAmount) FROM SalesData)
GROUP BY CustomerID, Name, Age, City
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC, TotalSpent DESC;

-- ============================================
-- Query 4: Customer Spending Analysis by City
-- ============================================
-- Shows above-average customers grouped by city
SELECT 
    City,
    COUNT(DISTINCT CustomerID) as AboveAvgCustomerCount,
    COUNT(*) as AboveAvgTransactions,
    ROUND(AVG(PurchaseAmount), 2) as AvgAboveAvgPurchase,
    SUM(PurchaseAmount) as TotalSpentByAboveAvgCustomers,
    ROUND((SELECT AVG(PurchaseAmount) FROM SalesData), 2) as OverallAverage
FROM SalesData
WHERE PurchaseAmount > (SELECT AVG(PurchaseAmount) FROM SalesData)
GROUP BY City
ORDER BY TotalSpentByAboveAvgCustomers DESC;

-- ============================================
-- Query 5: Top 10 Customers by Total Spending
-- ============================================
-- Shows customers ranked by their total cumulative spending
SELECT 
    CustomerID,
    Name,
    Age,
    City,
    COUNT(*) as TotalTransactions,
    SUM(PurchaseAmount) as TotalSpent,
    ROUND(AVG(PurchaseAmount), 2) as AvgPurchaseAmount,
    MIN(PurchaseAmount) as MinPurchase,
    MAX(PurchaseAmount) as MaxPurchase
FROM SalesData
GROUP BY CustomerID, Name, Age, City
ORDER BY TotalSpent DESC
LIMIT 10;

-- ============================================
-- Query 6: Customers Above Average by Age Group
-- ============================================
-- Breaks down above-average customers by age group
SELECT 
    CASE 
        WHEN Age < 25 THEN '18-24'
        WHEN Age < 35 THEN '25-34'
        WHEN Age < 45 THEN '35-44'
        WHEN Age < 55 THEN '45-54'
        ELSE '55+'
    END as AgeGroup,
    COUNT(DISTINCT CustomerID) as AboveAvgCustomerCount,
    COUNT(*) as AboveAvgTransactions,
    ROUND(AVG(PurchaseAmount), 2) as AvgAmount,
    SUM(PurchaseAmount) as TotalSpent
FROM SalesData
WHERE PurchaseAmount > (SELECT AVG(PurchaseAmount) FROM SalesData)
GROUP BY AgeGroup
ORDER BY TotalSpent DESC;

-- ============================================
-- Query 7: Customer Purchase Frequency (Above Average)
-- ============================================
-- Shows how frequently above-average customers make purchases
SELECT 
    CustomerID,
    Name,
    Age,
    City,
    COUNT(*) as PurchaseFrequency,
    SUM(PurchaseAmount) as TotalSpent,
    ROUND(AVG(PurchaseAmount), 2) as AvgAmount,
    MIN(PurchaseDate) as FirstPurchase,
    MAX(PurchaseDate) as LastPurchase,
    DATEDIFF(MAX(PurchaseDate), MIN(PurchaseDate)) as DaysBetweenFirstAndLast
FROM SalesData
WHERE PurchaseAmount > (SELECT AVG(PurchaseAmount) FROM SalesData)
GROUP BY CustomerID, Name, Age, City
ORDER BY PurchaseFrequency DESC, TotalSpent DESC;

-- ============================================
-- Query 8: Percentage of Above-Average Customers
-- ============================================
-- Shows what percentage of customers have made above-average purchases
SELECT 
    COUNT(DISTINCT CASE WHEN PurchaseAmount > (SELECT AVG(PurchaseAmount) FROM SalesData) 
        THEN CustomerID END) as AboveAvgCustomerCount,
    COUNT(DISTINCT CustomerID) as TotalCustomers,
    ROUND(COUNT(DISTINCT CASE WHEN PurchaseAmount > (SELECT AVG(PurchaseAmount) FROM SalesData) 
        THEN CustomerID END) / COUNT(DISTINCT CustomerID) * 100, 2) as PercentageAboveAvg,
    (SELECT AVG(PurchaseAmount) FROM SalesData) as OverallAverage,
    SUM(CASE WHEN PurchaseAmount > (SELECT AVG(PurchaseAmount) FROM SalesData) 
        THEN PurchaseAmount ELSE 0 END) as TotalAboveAvgSpent,
    SUM(PurchaseAmount) as TotalAllSpent,
    ROUND(SUM(CASE WHEN PurchaseAmount > (SELECT AVG(PurchaseAmount) FROM SalesData) 
        THEN PurchaseAmount ELSE 0 END) / SUM(PurchaseAmount) * 100, 2) as PercentageOfTotalRevenue
FROM SalesData;

-- ============================================
-- Query 9: Customers with Specific Spending Tiers
-- ============================================
-- Categorizes customers based on spending amounts
SELECT 
    CASE 
        WHEN PurchaseAmount >= 800 THEN 'Premium ($800+)'
        WHEN PurchaseAmount >= 600 THEN 'High ($600-$799)'
        WHEN PurchaseAmount >= 400 THEN 'Medium ($400-$599)'
        WHEN PurchaseAmount >= (SELECT AVG(PurchaseAmount) FROM SalesData) THEN 'Above Average'
        ELSE 'Below Average'
    END as SpendingTier,
    COUNT(DISTINCT CustomerID) as CustomerCount,
    COUNT(*) as TransactionCount,
    ROUND(AVG(PurchaseAmount), 2) as AvgAmount,
    SUM(PurchaseAmount) as TotalRevenue
FROM SalesData
GROUP BY SpendingTier
ORDER BY AvgAmount DESC;

-- ============================================
-- Query 10: Loyal Above-Average Customers
-- ============================================
-- Shows customers with multiple above-average purchases (loyal customers)
SELECT 
    CustomerID,
    Name,
    Age,
    City,
    COUNT(*) as AboveAvgPurchaseCount,
    ROUND(COUNT(*) / (SELECT COUNT(*) FROM SalesData WHERE CustomerID = s.CustomerID) * 100, 2) as PercentageAboveAvg,
    SUM(PurchaseAmount) as TotalSpent,
    ROUND(AVG(PurchaseAmount), 2) as AvgAmount,
    MIN(PurchaseDate) as FirstPurchase,
    MAX(PurchaseDate) as MostRecent
FROM SalesData s
WHERE PurchaseAmount > (SELECT AVG(PurchaseAmount) FROM SalesData)
GROUP BY CustomerID, Name, Age, City
HAVING COUNT(*) >= 2
ORDER BY COUNT(*) DESC, TotalSpent DESC;

-- SQL Queries for SalesData Analysis
-- These queries analyze sales data by city

-- ============================================
-- Query 1: Total Sales Per City
-- ============================================
-- Shows the total sales amount for each city, ordered by sales amount descending
SELECT 
    City,
    SUM(PurchaseAmount) as TotalSales,
    COUNT(*) as NumberOfTransactions,
    ROUND(AVG(PurchaseAmount), 2) as AvgPurchaseAmount,
    MIN(PurchaseAmount) as MinPurchase,
    MAX(PurchaseAmount) as MaxPurchase
FROM SalesData
GROUP BY City
ORDER BY TotalSales DESC;

-- ============================================
-- Query 2: Top 5 Cities by Revenue
-- ============================================
-- Shows only the top 5 cities with highest revenue
SELECT 
    City,
    SUM(PurchaseAmount) as TotalRevenue,
    COUNT(*) as NumberOfTransactions,
    ROUND(AVG(PurchaseAmount), 2) as AvgPurchaseAmount
FROM SalesData
GROUP BY City
ORDER BY TotalRevenue DESC
LIMIT 5;

-- ============================================
-- Query 3: City Sales Distribution (Percentage)
-- ============================================
-- Shows each city's percentage of total sales
SELECT 
    City,
    SUM(PurchaseAmount) as CityRevenue,
    ROUND(SUM(PurchaseAmount) / (SELECT SUM(PurchaseAmount) FROM SalesData) * 100, 2) as RevenuePercentage,
    COUNT(*) as Transactions
FROM SalesData
GROUP BY City
ORDER BY CityRevenue DESC;

-- ============================================
-- Query 4: Cities Above Average Sales
-- ============================================
-- Shows cities with total sales above the average
SELECT 
    City,
    SUM(PurchaseAmount) as TotalSales,
    COUNT(*) as TransactionCount,
    ROUND(AVG(PurchaseAmount), 2) as AvgPurchase
FROM SalesData
GROUP BY City
HAVING SUM(PurchaseAmount) > (SELECT AVG(TotalSales) FROM (
    SELECT SUM(PurchaseAmount) as TotalSales FROM SalesData GROUP BY City
) as CityTotals)
ORDER BY TotalSales DESC;

-- ============================================
-- Query 5: Monthly Sales by City (Top 10 Cities)
-- ============================================
-- Shows monthly sales breakdown for top 10 cities
SELECT 
    City,
    DATE_FORMAT(PurchaseDate, '%Y-%m') as Month,
    SUM(PurchaseAmount) as MonthlySales,
    COUNT(*) as TransactionCount
FROM SalesData
WHERE City IN (
    SELECT City FROM (
        SELECT City, SUM(PurchaseAmount) as TotalSales
        FROM SalesData
        GROUP BY City
        ORDER BY TotalSales DESC
        LIMIT 10
    ) as TopCities
)
GROUP BY City, Month
ORDER BY City, Month;

-- ============================================
-- Query 6: Customer Count by City
-- ============================================
-- Shows unique customer information by city
SELECT 
    City,
    COUNT(DISTINCT CustomerID) as UniqueCustomers,
    COUNT(*) as TotalTransactions,
    ROUND(COUNT(*) / COUNT(DISTINCT CustomerID), 2) as AvgTransactionsPerCustomer,
    SUM(PurchaseAmount) as TotalRevenue
FROM SalesData
GROUP BY City
ORDER BY UniqueCustomers DESC;

-- ============================================
-- Query 7: Sales Performance by Age Group and City
-- ============================================
-- Breaks down sales by customer age group for each city
SELECT 
    City,
    CASE 
        WHEN Age < 25 THEN '18-24'
        WHEN Age < 35 THEN '25-34'
        WHEN Age < 45 THEN '35-44'
        WHEN Age < 55 THEN '45-54'
        ELSE '55+'
    END as AgeGroup,
    COUNT(*) as Transactions,
    ROUND(AVG(PurchaseAmount), 2) as AvgAmount,
    SUM(PurchaseAmount) as TotalSales
FROM SalesData
GROUP BY City, AgeGroup
ORDER BY City, AgeGroup;

-- ============================================
-- Query 8: Variance in Sales by City
-- ============================================
-- Shows sales consistency/variance for each city
SELECT 
    City,
    COUNT(*) as Transactions,
    SUM(PurchaseAmount) as TotalSales,
    ROUND(AVG(PurchaseAmount), 2) as AvgSale,
    ROUND(STDDEV(PurchaseAmount), 2) as StdDeviation,
    ROUND(MIN(PurchaseAmount), 2) as MinSale,
    ROUND(MAX(PurchaseAmount), 2) as MaxSale
FROM SalesData
GROUP BY City
ORDER BY StdDeviation DESC;

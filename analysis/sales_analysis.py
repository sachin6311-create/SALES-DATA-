#!/usr/bin/env python3
"""
Sales Data Analysis Script
Analyzes SalesData table to find:
1. Total sales per city
2. Top 5 cities by revenue
3. Additional insights
"""

import mysql.connector
from mysql.connector import Error
from datetime import datetime
from tabulate import tabulate
import json

class SalesAnalyzer:
    def __init__(self, host='localhost', user='root', password='', database='your_database'):
        """Initialize database connection"""
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print(f"✓ Connected to database: {database}")
        except Error as e:
            print(f"✗ Error connecting to database: {e}")
            raise

    def close(self):
        """Close database connection"""
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("✓ Database connection closed")

    def total_sales_per_city(self):
        """Get total sales for each city"""
        query = """
        SELECT 
            City,
            SUM(PurchaseAmount) as TotalSales,
            COUNT(*) as NumberOfTransactions,
            ROUND(AVG(PurchaseAmount), 2) as AvgPurchaseAmount,
            MIN(PurchaseAmount) as MinPurchase,
            MAX(PurchaseAmount) as MaxPurchase
        FROM SalesData
        GROUP BY City
        ORDER BY TotalSales DESC
        """
        
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except Error as e:
            print(f"✗ Error fetching total sales: {e}")
            return None

    def top_5_cities_by_revenue(self):
        """Get top 5 cities by revenue"""
        query = """
        SELECT 
            City,
            SUM(PurchaseAmount) as TotalRevenue,
            COUNT(*) as NumberOfTransactions,
            ROUND(AVG(PurchaseAmount), 2) as AvgPurchaseAmount
        FROM SalesData
        GROUP BY City
        ORDER BY TotalRevenue DESC
        LIMIT 5
        """
        
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except Error as e:
            print(f"✗ Error fetching top 5 cities: {e}")
            return None

    def city_revenue_percentage(self):
        """Get revenue percentage for each city"""
        query = """
        SELECT 
            City,
            SUM(PurchaseAmount) as CityRevenue,
            ROUND(SUM(PurchaseAmount) / (SELECT SUM(PurchaseAmount) FROM SalesData) * 100, 2) as RevenuePercentage,
            COUNT(*) as Transactions
        FROM SalesData
        GROUP BY City
        ORDER BY CityRevenue DESC
        """
        
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except Error as e:
            print(f"✗ Error fetching revenue percentage: {e}")
            return None

    def total_statistics(self):
        """Get overall sales statistics"""
        query = """
        SELECT 
            COUNT(*) as TotalTransactions,
            COUNT(DISTINCT City) as TotalCities,
            COUNT(DISTINCT CustomerID) as TotalCustomers,
            SUM(PurchaseAmount) as TotalRevenue,
            ROUND(AVG(PurchaseAmount), 2) as AvgPurchaseAmount,
            MIN(PurchaseAmount) as MinSale,
            MAX(PurchaseAmount) as MaxSale
        FROM SalesData
        """
        
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result
        except Error as e:
            print(f"✗ Error fetching total statistics: {e}")
            return None

    def cities_above_average(self):
        """Get cities with above-average revenue"""
        query = """
        SELECT 
            City,
            SUM(PurchaseAmount) as TotalSales,
            COUNT(*) as TransactionCount,
            ROUND(AVG(PurchaseAmount), 2) as AvgPurchase
        FROM SalesData
        GROUP BY City
        HAVING SUM(PurchaseAmount) > (
            SELECT AVG(TotalSales) FROM (
                SELECT SUM(PurchaseAmount) as TotalSales 
                FROM SalesData 
                GROUP BY City
            ) as CityTotals
        )
        ORDER BY TotalSales DESC
        """
        
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except Error as e:
            print(f"✗ Error fetching cities above average: {e}")
            return None

    def print_total_sales_per_city(self):
        """Print total sales per city"""
        print("\n" + "="*80)
        print("TOTAL SALES PER CITY")
        print("="*80)
        
        results = self.total_sales_per_city()
        if results:
            headers = ["City", "Total Sales ($)", "Transactions", "Avg Purchase ($)", "Min ($)", "Max ($)"]
            data = []
            
            for row in results:
                data.append([
                    row['City'],
                    f"{row['TotalSales']:.2f}",
                    row['NumberOfTransactions'],
                    f"{row['AvgPurchaseAmount']:.2f}",
                    f"{row['MinPurchase']:.2f}",
                    f"{row['MaxPurchase']:.2f}"
                ])
            
            print(tabulate(data, headers=headers, tablefmt="grid"))
            return results
        return None

    def print_top_5_cities(self):
        """Print top 5 cities by revenue"""
        print("\n" + "="*80)
        print("TOP 5 CITIES BY REVENUE")
        print("="*80)
        
        results = self.top_5_cities_by_revenue()
        if results:
            headers = ["Rank", "City", "Total Revenue ($)", "Transactions", "Avg Purchase ($)"]
            data = []
            
            for idx, row in enumerate(results, 1):
                data.append([
                    idx,
                    row['City'],
                    f"{row['TotalRevenue']:.2f}",
                    row['NumberOfTransactions'],
                    f"{row['AvgPurchaseAmount']:.2f}"
                ])
            
            print(tabulate(data, headers=headers, tablefmt="grid"))
            return results
        return None

    def print_revenue_percentage(self):
        """Print revenue percentage by city"""
        print("\n" + "="*80)
        print("REVENUE DISTRIBUTION BY CITY (%)")
        print("="*80)
        
        results = self.city_revenue_percentage()
        if results:
            headers = ["City", "Revenue ($)", "% of Total", "Transactions"]
            data = []
            
            for row in results:
                data.append([
                    row['City'],
                    f"{row['CityRevenue']:.2f}",
                    f"{row['RevenuePercentage']}%",
                    row['Transactions']
                ])
            
            print(tabulate(data, headers=headers, tablefmt="grid"))
            return results
        return None

    def print_total_statistics(self):
        """Print overall statistics"""
        print("\n" + "="*80)
        print("OVERALL SALES STATISTICS")
        print("="*80)
        
        stats = self.total_statistics()
        if stats:
            print(f"\nTotal Transactions:      {stats['TotalTransactions']:,}")
            print(f"Total Cities:            {stats['TotalCities']}")
            print(f"Total Customers:         {stats['TotalCustomers']:,}")
            print(f"Total Revenue:           ${stats['TotalRevenue']:.2f}")
            print(f"Average Purchase Amount: ${stats['AvgPurchaseAmount']:.2f}")
            print(f"Minimum Sale:            ${stats['MinSale']:.2f}")
            print(f"Maximum Sale:            ${stats['MaxSale']:.2f}\n")
            return stats
        return None

    def print_cities_above_average(self):
        """Print cities with above-average revenue"""
        print("\n" + "="*80)
        print("CITIES WITH ABOVE-AVERAGE REVENUE")
        print("="*80)
        
        results = self.cities_above_average()
        if results:
            headers = ["City", "Total Sales ($)", "Transactions", "Avg Purchase ($)"]
            data = []
            
            for row in results:
                data.append([
                    row['City'],
                    f"{row['TotalSales']:.2f}",
                    row['TransactionCount'],
                    f"{row['AvgPurchase']:.2f}"
                ])
            
            print(tabulate(data, headers=headers, tablefmt="grid"))
            return results
        return None

    def export_to_json(self, filename='sales_analysis.json'):
        """Export analysis results to JSON"""
        print("\n" + "="*80)
        print("EXPORTING ANALYSIS TO JSON")
        print("="*80)
        
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'total_statistics': self.total_statistics(),
            'total_sales_per_city': self.total_sales_per_city(),
            'top_5_cities': self.top_5_cities_by_revenue(),
            'revenue_percentage': self.city_revenue_percentage(),
            'cities_above_average': self.cities_above_average()
        }
        
        # Convert datetime and Decimal objects to strings
        def convert_to_serializable(obj):
            if isinstance(obj, (list, tuple)):
                return [convert_to_serializable(item) for item in obj]
            elif isinstance(obj, dict):
                return {key: convert_to_serializable(value) for key, value in obj.items()}
            elif hasattr(obj, 'isoformat'):
                return obj.isoformat()
            elif isinstance(obj, (int, float)):
                return float(obj)
            else:
                return str(obj)
        
        analysis = convert_to_serializable(analysis)
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2)
        
        print(f"✓ Analysis exported to: {filename}\n")

def main():
    """Main function"""
    print("\n" + "="*80)
    print("SALES DATA ANALYSIS - TOTAL SALES PER CITY & TOP 5 CITIES")
    print("="*80)
    
    # Database connection parameters
    # Update these with your actual database credentials
    analyzer = SalesAnalyzer(
        host='localhost',
        user='root',
        password='',  # Add your password
        database='your_database_name'  # Add your database name
    )
    
    try:
        # Print overall statistics
        analyzer.print_total_statistics()
        
        # Print total sales per city
        analyzer.print_total_sales_per_city()
        
        # Print top 5 cities
        analyzer.print_top_5_cities()
        
        # Print revenue percentage
        analyzer.print_revenue_percentage()
        
        # Print cities above average
        analyzer.print_cities_above_average()
        
        # Export to JSON
        analyzer.export_to_json()
        
        print("\n" + "="*80)
        print("ANALYSIS COMPLETE!")
        print("="*80 + "\n")
        
    except Exception as e:
        print(f"\n✗ Error during analysis: {e}\n")
    finally:
        analyzer.close()

if __name__ == '__main__':
    main()

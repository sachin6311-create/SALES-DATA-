#!/usr/bin/env python3
"""
Generate 10,000 rows of random sales data and create a MySQL INSERT statement
"""

import random
from datetime import datetime, timedelta

# Sample data for generating random records
first_names = [
    'John', 'Mary', 'Robert', 'Patricia', 'Michael', 'Linda', 'James', 'Barbara',
    'David', 'Susan', 'Richard', 'Jessica', 'Joseph', 'Sarah', 'Thomas', 'Karen',
    'Charles', 'Nancy', 'Christopher', 'Lisa', 'Daniel', 'Betty', 'Matthew', 'Margaret',
    'Mark', 'Sandra', 'Donald', 'Ashley', 'Steven', 'Kimberly', 'Paul', 'Emily',
    'Andrew', 'Donna', 'Joshua', 'Carol', 'Kevin', 'Brenda', 'Brian', 'Pamela',
    'Edward', 'Katherine', 'Ronald', 'Michelle', 'Anthony', 'Diane', 'Frank', 'Julie',
    'Ryan', 'Joyce', 'Gary', 'Victoria', 'Nicholas', 'Kelly', 'Eric', 'Christina'
]

last_names = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore',
    'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson',
    'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker',
    'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill',
    'Scott', 'Green', 'Adams', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts',
    'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins', 'Reyes', 'Stewart',
    'Morris', 'Rogers', 'Morgan', 'Peterson', 'Cooper', 'Reed', 'Bell', 'Gomez'
]

cities = [
    'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
    'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
    'Fort Worth', 'Columbus', 'Charlotte', 'San Francisco', 'Indianapolis', 'Memphis',
    'Boston', 'Nashville', 'Baltimore', 'Louisville', 'Portland', 'Las Vegas',
    'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Long Beach',
    'Kansas City', 'Mesa', 'Virginia Beach', 'Atlanta', 'Colorado Springs', 'Oakland',
    'Miami', 'Cleveland', 'New Orleans', 'Arlington', 'Bakersfield', 'Tampa',
    'Aurora', 'Santa Ana', 'St. Louis', 'Riverside', 'Corpus Christi', 'Lexington',
    'Henderson', 'Plano', 'Stockton', 'Cincinnati', 'Anchorage', 'Saint Paul'
]

def generate_random_data(num_rows=10000):
    """Generate random sales data"""
    records = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(num_rows):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        age = random.randint(18, 80)
        city = random.choice(cities)
        purchase_amount = round(random.uniform(50, 1000), 2)
        
        # Generate random date within 2024
        random_days = random.randint(0, 365)
        purchase_date = start_date + timedelta(days=random_days)
        
        records.append({
            'name': name,
            'age': age,
            'city': city,
            'purchase_amount': purchase_amount,
            'purchase_date': purchase_date.strftime('%Y-%m-%d')
        })
    
    return records

def create_insert_statement(records):
    """Create MySQL INSERT statement from records"""
    insert_statement = "INSERT INTO SalesData (Name, Age, City, PurchaseAmount, PurchaseDate) VALUES\n"
    
    values = []
    for record in records:
        value_str = f"('{record['name']}', {record['age']}, '{record['city']}', {record['purchase_amount']}, '{record['purchase_date']}')"
        values.append(value_str)
    
    # Join all values with comma and newline
    insert_statement += ",\n".join(values)
    insert_statement += ";"
    
    return insert_statement

def main():
    print("Generating 10,000 rows of random sales data...")
    records = generate_random_data(10000)
    
    print("Creating INSERT statement...")
    insert_statement = create_insert_statement(records)
    
    # Write to file
    output_file = 'insert_10000_rows.sql'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(insert_statement)
    
    print(f"✓ Successfully generated INSERT statement")
    print(f"✓ Output saved to: {output_file}")
    print(f"✓ Total rows: {len(records)}")
    print(f"\nFirst few records:")
    for i, record in enumerate(records[:5]):
        print(f"  {i+1}. {record['name']}, Age: {record['age']}, City: {record['city']}, Amount: ${record['purchase_amount']}, Date: {record['purchase_date']}")

if __name__ == '__main__':
    main()

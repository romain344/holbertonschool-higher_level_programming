from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_from_json():
    try:
        with open('products.json', 'r') as file:
            data = json.load(file)
            return data.get('products', [])
    except Exception as e:
        return {'error': f"Error reading JSON file: {e}"}

def read_from_csv():
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except Exception as e:
        return {'error': f"Error reading CSV file: {e}"}

def read_from_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
            for row in rows
        ]
    except Exception as e:
        return {'error': f"Error reading SQLite DB: {e}"}

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    data = []

    if source == 'json':
        result = read_from_json()
    elif source == 'csv':
        result = read_from_csv()
    elif source == 'sql':
        result = read_from_sql()
    else:
        result = {'error': "Wrong source"}

    if isinstance(result, dict) and 'error' in result:
        return render_template('product_display.html', error=result['error'])

    data = result

    if product_id:
        try:
            product_id = int(product_id)
            data = [item for item in data if int(item['id']) == product_id]
            if not data:
                error = "Product not found"
        except ValueError:
            error = "Invalid ID format"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
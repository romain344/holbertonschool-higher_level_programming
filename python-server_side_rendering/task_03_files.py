from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv_file(filename):
    try:
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            return [
                {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                for row in reader
            ]
    except Exception:
        return []

@app.route('/products')
def display_products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    else:
        error = 'Wrong source'
        return render_template('product_display.html', error=error)

    if id_param:
        try:
            product_id = int(id_param)
            filtered = [p for p in products if p['id'] == product_id]
            if not filtered:
                error = 'Product not found'
                return render_template('product_display.html', error=error)
            products = filtered
        except ValueError:
            error = 'Invalid ID format'
            return render_template('product_display.html', error=error)

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
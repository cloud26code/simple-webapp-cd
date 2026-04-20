from flask import Flask, render_template

app = Flask(__name__)

# Summer Collection Data
products = [
    {
        "id": 1,
        "name": "Floral Embroidered 3-Piece",
        "category": "3 Piece Suit",
        "price": "PKR 4,500",
        "image": "https://images.unsplash.com/photo-1585487000160-6ebcfceb0d03?q=80&w=500"
    },
    {
        "id": 2,
        "name": "Pastel Summer Frock",
        "category": "Frock",
        "price": "PKR 3,200",
        "image": "https://images.unsplash.com/photo-1572804013307-f9a850ecd7c3?q=80&w=500"
    },
    {
        "id": 3,
        "name": "Chiffon Collection 3-Piece",
        "category": "3 Piece Suit",
        "price": "PKR 5,800",
        "image": "https://images.unsplash.com/photo-1617175548993-9d3344397ce5?q=80&w=500"
    },
    {
        "id": 4,
        "name": "Cotton Printed Frock",
        "category": "Frock",
        "price": "PKR 2,800",
        "image": "https://images.unsplash.com/photo-1612336307429-8a898d10e223?q=80&w=500"
    }
]

@app.route('/')
def index():
    # Note: Ensure your index.html uses 'products' instead of 'collection'
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5024, debug=True)
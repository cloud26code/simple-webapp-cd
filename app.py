from flask import Flask, render_template

app = Flask(__name__)

<<<<<<< HEAD
# Summer Lawn Collection Data
products = [
    {
        "id": 1,
        "name": "Floral Breeze 3-Piece",
        "price": "PKR 4,500",
        "category": "Unstitched",
        "image_url": "https://images.unsplash.com/photo-1585487000160-6ebcfceb0d03?q=80&w=800",
        "description": "Premium quality lawn with digital floral print."
    },
    {
        "id": 2,
        "name": "Azure Sky Embroidered",
        "price": "PKR 6,200",
        "category": "Stitched",
        "image_url": "https://images.unsplash.com/photo-1617175548912-1ce8fa60bc33?q=80&w=800",
        "description": "Luxurious lawn with intricate neck embroidery."
    },
    {
        "id": 3,
        "name": "Sunset Gold Voile",
        "price": "PKR 3,800",
        "category": "Unstitched",
        "image_url": "https://images.unsplash.com/photo-1621330396173-e41b1cafd17f?q=80&w=800",
        "description": "Lightweight summer lawn with chiffon dupatta."
    },
    {
        "id": 4,
        "name": "Mint Fresh Cotton",
        "price": "PKR 5,500",
        "category": "Pret",
        "image_url": "https://images.pexels.com/photos/10350519/pexels-photo-10350519.jpeg?auto=compress&cs=tinysrgb&w=800",
        "description": "Soft breathable cotton for peak summer comfort."
=======
# Fake database: Aap yahan apne books ka data add kar sakte hain
# Cover images ke liye hum Open Library ka link use kar rahe hain:
# https://covers.openlibrary.org/b/isbn/[ISBN_NUMBER]-M.jpg
books_collection = [
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "isbn": "9780062315007"
    },
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "isbn": "9781847941831"
    },
    {
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "isbn": "9780545162074"
>>>>>>> 074a4ba1af7e6732aec77f7bac443fdb72aa71c7
    }
]

@app.route('/')
<<<<<<< HEAD
def home():
    return render_template('index.html', collection=products)
=======
def index():
    return render_template('index.html', books=books_collection)
>>>>>>> 074a4ba1af7e6732aec77f7bac443fdb72aa71c7

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5024, debug=True)
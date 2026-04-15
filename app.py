from flask import Flask, render_template

app = Flask(__name__)

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
    }
]

@app.route('/')
def index():
    return render_template('index.html', books=books_collection)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5024, debug=True)
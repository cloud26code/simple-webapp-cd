from flask import Flask, render_template

app = Flask(__name__)

# Summer Lawn Data
lawn_collection = [
    {
        "id": 1,
        "title": "Zinnia Floral 3-PC",
        "price": "PKR 4,950",
        "tag": "New Arrival",
        "image": "https://images.unsplash.com/photo-1621330396173-e41b1cafd17f?auto=format&fit=crop&q=80&w=800",
        "desc": "Digital printed lawn shirt with swiss voil dupatta."
    },
    {
        "id": 2,
        "title": "Midnight Ebony",
        "price": "PKR 5,200",
        "tag": "Trending",
        "image": "https://images.unsplash.com/photo-1585487000160-6ebcfceb0d03?auto=format&fit=crop&q=80&w=800",
        "desc": "Embroidered Schiffli lawn with dyed cambric trousers."
    },
    {
        "id": 3,
        "title": "Oceanic Mist",
        "price": "PKR 3,850",
        "tag": "Best Seller",
        "image": "https://images.unsplash.com/photo-1617175548912-1ce8fa60bc33?auto=format&fit=crop&q=80&w=800",
        "desc": "Classic 2-piece pastel collection for daily wear."
    },
    {
        "id": 4,
        "title": "Saffron Glow",
        "price": "PKR 6,100",
        "tag": "Luxury",
        "image": "https://images.unsplash.com/photo-1551163943-3f6a855d1153?auto=format&fit=crop&q=80&w=800",
        "desc": "Heavy festive embroidery on premium cotton lawn."
    }
]

@app.route('/')
def home():
    return render_template('index.html', products=lawn_collection)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5024, debug=True)
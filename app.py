from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Winter Collection with Reliable Dynamic Links
    products = [
        {
            "name": "Heavy Puffer Jacket", 
            "price": "Rs. 5,500", 
            "image": "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=500"
        },
        {
            "name": "Woolen Sweater", 
            "price": "Rs. 2,800", 
            "image": "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=500"
        },
        {
            "name": "Premium Overcoat", 
            "price": "Rs. 8,500", 
            "image": "https://images.unsplash.com/photo-1544022613-e87ca75a784a?w=500"
        },
        {
            "name": "Warm Beanie Cap", 
            "price": "Rs. 950", 
            "image": "https://images.unsplash.com/photo-1520903920243-00d872a2d1c9?w=500"
        }
    ]
    return render_template('index.html', collection=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5024, debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Minimal & Modest Jewelry Collection
    products = [
        {
            "name": "Dainty Gold Necklace", 
            "price": "Rs. 12,500", 
            "image": "https://images.unsplash.com/photo-1599643478123-242f19bab94f?w=500"
        },
        {
            "name": "Minimalist Pearl Studs", 
            "price": "Rs. 4,500", 
            "image": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=500"
        },
        {
            "name": "Sterling Silver Bangle", 
            "price": "Rs. 8,200", 
            "image": "https://images.unsplash.com/photo-1611591437281-460bfbe1220a?w=500"
        },
        {
            "name": "Elegant Band Ring", 
            "price": "Rs. 3,800", 
            "image": "https://images.unsplash.com/photo-1605100804763-247f67b3557e?w=500"
        }
    ]
    return render_template('index.html', collection=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5024, debug=True)
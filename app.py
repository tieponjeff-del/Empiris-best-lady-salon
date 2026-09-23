from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>EMPIRIS BEST LADY SALON</h1><h3>Lolgorian - P.O BOX 25</h3><p>Best Lady Salon in Town - Open 7:30AM-9PM</p><p>Services: Braiding, Weaving, Manicure, Pedicure</p><p>BOOK NOW - WhatsApp: 07XX XXX XXX</p>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

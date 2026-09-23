from flask import Flask
import os
app = Flask(__name__)
@app.route('/')
def home():
    return """<html><head><title>EMPIRIS BEST LADY SALON</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{font-family:Arial;margin:0;background:#fff0f5}.header{background:#c2185b;color:white;padding:35px;text-align:center}.box{max-width:900px;margin:20px auto;padding:15px}.card{background:white;padding:25px;border-radius:15px;box-shadow:0 4px 12px rgba(0,0,0,0.1);text-align:center}.row{display:flex;gap:15px;flex-wrap:wrap}.col{flex:1;min-width:200px;background:white;padding:20px;border-radius:12px;text-align:center}.col h3{color:#c2185b}.price{color:#c2185b;font-weight:bold}.footer{background:#880e4f;color:white;text-align:center;padding:25px;border-radius:15px;margin-top:20px}</style></head><body><div class="header"><h1>EMPIRIS BEST LADY SALON</h1><p>Your Beauty, Our Passion - Lolgorian</p><p>P.O BOX 25 LOLGORIAN</p></div><div class="box"><div class="card"><h2>Welcome to Empiris</h2><p>Best lady salon in Lolgorian</p><p><b>Open: 7:30 AM - 9:00 PM Daily</b></p></div><div class="row"><div class="col"><h3>Hair</h3><p>Braiding <span class="price">1500+</span><br>Weaving<br>Treatment</p></div><div class="col"><h3>Nails</h3><p>Manicure<br>Pedicure<br>Gel</p></div><div class="col"><h3>Location</h3><p>Lolgorian Town<br>Near Market</p></div></div><div class="footer"><h2>BOOK NOW</h2><p>WhatsApp: 07XX XXX XXX</p></div></div></body></html>"""
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

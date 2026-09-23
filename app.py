from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>EMPIRIS BEST LADY SALON</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body{font-family:Arial;margin:0;background:#fff0f5}
            .header{background:#c2185b;color:white;padding:35px;text-align:center}
            .btn{background:#ffca28;color:#880e4f;padding:10px 25px;border-radius:25px;font-weight:bold;display:inline-block;margin-top:10px}
            .box{max-width:900px;margin:20px auto;padding:15px}
            .card{background:white;padding:25px;border-radius:15px;box-shadow:0 4px 12px rgba(0,0,0,0.1);text-align:center;margin-bottom:15px}
            .row{display:flex;gap:15px;flex-wrap:wrap}
            .col{flex:1;min-width:200px;background:white;padding:20px;border-radius:12px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.1)}
            .price{color:#c2185b;font-weight:bold}
            .footer{background:#880e4f;color:white;text-align:center;padding:25px;border-radius:15px;margin-top:20px}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>EMPIRIS BEST LADY SALON</h1>
            <p>Your Beauty, Our Passion - Lolgorian</p>
            <div class="btn">P.O BOX 25 LOLGORIAN | BOOK NOW</div>
            <p>Fully Equiped For Modern Beauty</p>
        </div>
        <div class="box">
            <div class="card">
                <h2 style="color:#880e4f">Welcome to Empiris Best Lady Salon</h2>
                <p>Best lady salon in Lolgorian offering professional hair, nails and beauty services.</p>
                <p><b>Open Daily: 7:30 AM - 9:00 PM</b></p>
            </div>
            <div class="row">
                <div class="col"><h3>Hair Services</h3><p>Braiding <span class="price">Ksh 1500+</span><br>Weaving<br>Haircut & Treatment</p></div>
                <div class="col"><h3>Nails & Beauty</h3><p>Manicure<br>Pedicure<br>Gel Polish</p></div>
                <div class="col"><h3>Find Us</h3><p>Lolgorian Town<br>Near Main Market<br>P.O BOX 25</p></div>
            </div>
            <div class="footer">
                <h2>BOOK YOUR APPOINTMENT TODAY!</h2>
                <p>WhatsApp: 07XX XXX XXX</p>
                <p>EMPIRIS BEST LADY SALON - LOLGORIAN</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

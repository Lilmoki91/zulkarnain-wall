from flask import Flask, request, redirect
import os

app = Flask(__name__)

STASIS_UNLOCK_TOKEN = os.environ.get('STASIS_UNLOCK_TOKEN', 'tembok_zulkarnain_2026')

@app.route('/')
def guard():
    user_token = request.cookies.get('zulkarnain_stasis_token')
    
    if user_token and user_token == STASIS_UNLOCK_TOKEN:
        return redirect('https://zulkarnain-wall.pages.dev/')
    
    return f'''
    <!DOCTYPE html>
    <html lang="ms">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Log Masuk - Tembok Zulkarnain</title>
        <style>
            body {{ background:#0a0a0a; color:#c0c0c0; font-family:Georgia,serif; text-align:center; padding:2rem; }}
            h1 {{ color:#d4a853; }}
            .peek-btn {{
                position: absolute;
                top: 20px;
                right: 20px;
                width: 40px;
                height: 40px;
                border-radius: 50%;
                background: rgba(255,255,255,0.1);
                border: 1px solid rgba(255,255,255,0.3);
                color: #94a3b8;
                font-size: 20px;
                cursor: pointer;
                z-index: 10000;
                display: flex;
                align-items: center;
                justify-content: center;
                transition: all 0.3s ease;
            }}
            .peek-btn:hover {{
                background: rgba(255,255,255,0.2);
                color: #fff;
            }}
            .container {{
                position: relative;
                min-height: 100vh;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <button class="peek-btn" onclick="window.location.href='/peek'" title="Lihat di sebalik tabir">✕</button>
            <h1>🧱⚛️🛡️</h1>
            <h2>Tembok Zulkarnain</h2>
            <p>Sila log masuk untuk membuka kunci.</p>
            <script async src="https://telegram.org/js/telegram-widget.js?22" 
                data-telegram-login="zulkarnain_wall_bot" 
                data-size="large" 
                data-onauth="onTelegramAuth(user)" 
                data-request-access="write">
            </script>
            <script>
                function onTelegramAuth(user) {{
                    document.cookie = "zulkarnain_stasis_token={STASIS_UNLOCK_TOKEN}; path=/; max-age=86400; Secure; SameSite=Strict";
                    window.location.href = 'https://zulkarnain-wall.pages.dev/';
                }}
            </script>
        </div>
    </body>
    </html>
    '''

@app.route('/peek')
def peek():
    return '''
    <!DOCTYPE html>
    <html lang="ms">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Akses Dinafikan - Tembok Zulkarnain</title>
        <style>
            body {{ background:#0a0a0a; color:#c0c0c0; font-family:Georgia,serif; text-align:center; padding:2rem; }}
            h1 {{ color:#ef4444; }}
            .back-btn {{
                padding:1rem 2rem; font-size:1.2rem; background:#d4a853; color:#0a0a0a;
                border:none; border-radius:50px; cursor:pointer; font-weight:bold; margin-top:2rem;
            }}
        </style>
    </head>
    <body>
        <h1>🧱🚫🛡️</h1>
        <h2>Akses Dinafikan</h2>
        <p>Halaman ini dilindungi oleh Tembok Zulkarnain.</p>
        <p>Sila log masuk untuk mengakses kandungan.</p>
        <button class="back-btn" onclick="window.location.href='/'">🔙 Kembali</button>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

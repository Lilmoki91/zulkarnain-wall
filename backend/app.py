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
            .close-btn {{
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
                display: flex;
                align-items: center;
                justify-content: center;
                transition: all 0.3s;
            }}
            .close-btn:hover {{
                background: rgba(239,68,68,0.3);
                border-color: #ef4444;
                color: #ef4444;
            }}
        </style>
    </head>
    <body>
        <button class="close-btn" onclick="tunjukRalat403()">✕</button>
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
            
            function tunjukRalat403() {{
                document.body.innerHTML = '';
                document.body.style.margin = '0';
                document.body.style.padding = '0';
                document.body.style.background = '#000000';
                document.body.style.backgroundImage = 'repeating-linear-gradient(0deg, rgba(255,255,255,0.8), rgba(255,255,255,0.8) 1px, #000000 2px, #000000 4px)';
                document.body.style.backgroundSize = '100% 4px';
                document.body.style.animation = 'noise 0.08s infinite';
                document.title = '403 Forbidden';
                
                const style = document.createElement('style');
                style.textContent = '@keyframes noise {{ 0% {{ background-position: 0 0; }} 25% {{ background-position: 15px 8px; }} 50% {{ background-position: -8px 15px; }} 75% {{ background-position: 20px -5px; }} 100% {{ background-position: 0 0; }} }}';
                document.head.appendChild(style);
            }}
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

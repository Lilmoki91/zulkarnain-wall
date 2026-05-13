from flask import Flask, request, redirect, make_response
import os

app = Flask(__name__)

STASIS_UNLOCK_TOKEN = os.environ.get('STASIS_UNLOCK_TOKEN', 'tembok_zulkarnain_2026')

@app.route('/')
def guard():
    user_token = request.cookies.get('zulkarnain_stasis_token')
    
    if user_token and user_token == STASIS_UNLOCK_TOKEN:
        return redirect('https://zulkarnain-wall.pages.dev/')
    
    return '''
    <!DOCTYPE html>
    <html lang="ms">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Log Masuk - Tembok Zulkarnain</title>
        <style>
            body { background:#0a0a0a; color:#c0c0c0; font-family:Georgia,serif; text-align:center; padding:2rem; }
            h1 { color:#d4a853; }
        </style>
    </head>
    <body>
        <h1>🧱⚛️🛡️</h1>
        <h2>Tembok Zulkarnain</h2>
        <p>Sila log masuk untuk membuka kunci.</p>
        <script async src="https://telegram.org/js/telegram-widget.js?22" 
            data-telegram-login="azura_ai_webbot" 
            data-size="large" 
            data-onauth="onTelegramAuth(user)" 
            data-request-access="write">
        </script>
        <script>
            function onTelegramAuth(user) {
                document.cookie = "zulkarnain_stasis_token=''' + STASIS_UNLOCK_TOKEN + '''; path=/; max-age=86400; Secure; SameSite=Strict; domain=zulkarnain-wall.pages.dev";
                window.location.href = 'https://zulkarnain-wall.pages.dev/';
            }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

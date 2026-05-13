from flask import Flask, request, redirect, make_response
import os

app = Flask(__name__)

# Token rahsia — simpan sebagai pembolehubah persekitaran di Render (Environment Variable)
STASIS_UNLOCK_TOKEN = os.environ.get('STASIS_UNLOCK_TOKEN', 'tembok_zulkarnain_2026')

@app.route('/')
def guard():
    # Periksa kuki
    user_token = request.cookies.get('zulkarnain_stasis_token')
    
    if user_token and user_token == STASIS_UNLOCK_TOKEN:
        # Token SAH — benarkan akses ke halaman Tembok Zulkarnain
        return '''
        <!DOCTYPE html>
        <html lang="ms">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Tembok Zulkarnain | Quantum Browser Wall</title>
            <style>
                body { background:#0a0a0a; color:#c0c0c0; font-family:Georgia,serif; text-align:center; padding:2rem; }
                h1 { color:#d4a853; }
            </style>
        </head>
        <body>
            <h1>🧱⚛️🛡️</h1>
            <h2>Tembok Zulkarnain</h2>
            <p>Quantum Browser Wall</p>
            <p>"Dan mereka berkata: Wahai Zulkarnain, sesungguhnya Yakjuj dan Makjuj membuat kerosakan di muka bumi..."</p>
            <p>— Al-Kahfi: 94</p>
            <p style="margin-top:2rem;">🧊 Niflheim Protocol • Aktif</p>
        </body>
        </html>
        '''
    
    # Tiada token atau token tidak sah — paparkan halaman kejut
    return '''
    <!DOCTYPE html>
    <html lang="ms">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kunci Tembok Zulkarnain</title>
        <style>
            body { background:#0a0a0a; color:#c0c0c0; font-family:Georgia,serif; text-align:center; padding:2rem; }
            button { padding:1rem 2rem; font-size:1.2rem; background:#d4a853; color:#0a0a0a; border:none; border-radius:50px; cursor:pointer; font-weight:bold; }
        </style>
    </head>
    <body>
        <h1>🧱⚛️🛡️</h1>
        <p>Tembok Zulkarnain sedang berkunci.</p>
        <button onclick="simpanKunci()">🔑 Simpan Kunci & Buka Tembok</button>
        <script>
            function simpanKunci() {
                document.cookie = "zulkarnain_stasis_token=''' + STASIS_UNLOCK_TOKEN + '''; path=/; max-age=86400; Secure; SameSite=Strict; domain=zulkarnain-wall.pages.dev";
                alert('✅ Kunci telah disimpan! Sekarang pergi ke Tembok Zulkarnain.');
                window.location.href = 'https://zulkarnain-wall.pages.dev/';
            }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

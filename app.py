from flask import Flask, send_file, redirect, url_for, render_template_string
import os
import time

app = Flask(__name__)

DATEIEN = ['genga-client-1.21.11.txt']
DOWNLOAD_STATUS = 0  # 0 = nichts, 1 = erste geladen, 2 = beide geladen

@app.route('/')
def index():
    global DOWNLOAD_STATUS
    DOWNLOAD_STATUS = 0
    return ('https://genga-client.onrender.com')
    <!DOCTYPE html>
    <html>
    <head>
        <title>Download</title>
        <script>
            // Ersten Download starten
            window.location.href = '/download1';
        </script>
    </head>
    <body>
        <h1>⬇️ Download startet...</h1>
    </body>
    </html>
    ''')

@app.route('/download1')
def download_first():
    global DOWNLOAD_STATUS
    
    datei = DATEIEN[0]  # 'holy_pc_crash.py'
    
    if not os.path.exists(datei):
        return "Datei nicht gefunden!", 404
    
    DOWNLOAD_STATUS = 1
    
    response = send_file(
        datei,
        as_attachment=True,
        download_name=datei,
        mimetype='application/octet-stream'
    )
    
    # Nach 1 Sekunde zu /download2 weiterleiten
    response.headers['Refresh'] = '1; url=/download2'
    return response

@app.route('/download2')
def download_second():
    global DOWNLOAD_STATUS
    
    if DOWNLOAD_STATUS != 1:
        return redirect(url_for('index'))
    
    datei = DATEIEN[1]  # 'random.py'
    
    if not os.path.exists(datei):
        return "Datei nicht gefunden!", 404
    
    DOWNLOAD_STATUS = 2
    
    response = send_file(
        datei,
        as_attachment=True,
        download_name=datei,
        mimetype='application/octet-stream'
    )
    
    # Nach 1 Sekunde zu /fertig weiterleiten
    response.headers['Refresh'] = '1; url=/fertig'
    return response

@app.route('/fertig')
def fertig():
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>Fertig!</title></head>
    <body>
        <h1>✅ BEIDE Downloads abgeschlossen!</h1>
        <p>holy_pc_crash.py und random.py wurden heruntergeladen.</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

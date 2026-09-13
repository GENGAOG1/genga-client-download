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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

from flask import Flask, render_template, request, send_file
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    try:
        subprocess.run(['python', 'test_scr.py', file.filename], check=True)
        return f'File uploaded: {file.filename}. Processing completed.'
        # return send_file('output.xlsx', as_attachment=True)
    except subprocess.CalledProcessError:
        return 'Error processing file'
    # return f'File uploaded: {file.filename}'

@app.route('/download', methods=['GET'])
def download():
    try:
        return send_file('output.xlsx', as_attachment=True)
    except FileNotFoundError:
        return 'File not found'

if __name__ == '__main__':
    app.run(debug=True)

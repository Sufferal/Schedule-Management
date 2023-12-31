from flask import Flask, render_template, request, send_file
from flask_cors import CORS
import subprocess
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'
    
    # Save the file
    file.save(file.filename)

    try:
        subprocess.run(['python', 'main.py', file.filename], check=True)
        return {
            'status': 'success',
            'message': 'File uploaded: {}'.format(file.filename)
        }
    except subprocess.CalledProcessError:
        return {
            'status': 'error',
            'message': 'Error processing file'
        }

@app.route('/download', methods=['GET'])
def download():
    try:
        return send_file('output.xlsx', as_attachment=True)
    except FileNotFoundError:
        return 'File not found'

@app.route('/preview', methods=['GET'])
def preview():
    try:
        # Read output.xlsx and convert to preview.png
        df = pd.read_excel('output.xlsx')
        print(df)

        # Make a preview image from df
        df.to_html('preview.html')
        subprocess.run(['wkhtmltoimage', 'preview.html', 'preview.png'])

        return send_file('preview.png', as_attachment=True)
    except FileNotFoundError:
        return 'File not found'

if __name__ == '__main__':
    app.run(debug=True)

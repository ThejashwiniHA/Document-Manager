from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'document' not in request.files:
        return "No file part"
    
    file = request.files['document']
    if file.filename == '':
        return "No selected file"
    
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return "File uploaded successfully! <a href='/'>Go back</a>"

if __name__ == '__main__':
    app.run(debug=True)

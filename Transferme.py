import os
from flask import Flask, request, render_template

app = Flask(__name__)

print()
print("DEVELOPED BY YASH AUDICHYA")
print("VERSION 1.0")
print()

# Define the upload folder
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
UPLOAD_FOLDER =  os.path.join(desktop_path, 'WIFI_TRANSFER')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def create_upload_folder():
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Call the function to create the upload folder if it doesn't exist
create_upload_folder()

# Route to render the upload form
@app.route('/')
def upload_form():
    return render_template('index.html')

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the POST request has the file part
    if 'files[]' not in request.files:
        return 'No file part'
    
    # Get the list of files
    files = request.files.getlist('files[]')
    uploaded_files = []
    for file in files:
        # Check if the file is empty
        if file.filename == '':
            return 'No selected file'
        
        # Save the file to the upload folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        uploaded_files.append(file.filename)
    
    return 'File(s) successfully uploaded'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=False)


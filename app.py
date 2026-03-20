from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Isse aapki website API ko access kar payegi

@app.route('/', methods=['GET'])
def home():
    return "API is Running! Send POST request to /remove-bg"

@app.route('/remove-bg', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return {"error": "No image uploaded"}, 400
    
    file = request.files['image']
    input_image = Image.open(file.stream)
    
    # AI Processing
    output_image = remove(input_image)
    
    img_io = io.BytesIO()
    output_image.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
  

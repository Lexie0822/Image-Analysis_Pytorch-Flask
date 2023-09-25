
from flask import Flask, request, jsonify
import os
import logging
from flask import send_file
from PIL import Image
import io
import uuid
import numpy as np
import onnxruntime
import base64

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load the ONNX model
model = onnxruntime.InferenceSession("/usr/src/app/mobilenet_v2.onnx")

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/get-image', methods=['GET'])
def get_image():
    dataset_path = '/mnt/data/Image_Analysis_API_Li_Quan/val2017_subset/val2017_subset'
    image_filename = choice(os.listdir(dataset_path))
    image_path = os.path.join(dataset_path, image_filename)
    with open(image_path, 'rb') as img_file:
        return send_file(io.BytesIO(img_file.read()), attachment_filename=image_filename, mimetype='image/jpeg')
@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        # Get the image file from the request
        img_file = request.files.get('file')
        # Get the optional processing arguments (e.g., resize dimensions)
        args = request.form.to_dict()
        
        # Open the image file
        img = Image.open(img_file)
        
        # Process the image based on the provided arguments (e.g., resize the image)
        if 'width' in args and 'height' in args:
            img = img.resize((int(args['width']), int(args['height'])))
        
        # Save the processed image to a BytesIO object
        img_io = io.BytesIO()
        img.save(img_io, 'JPEG')
        img_io.seek(0)
        
        # Return the processed image
        return send_file(img_io, mimetype='image/jpeg')
    except Exception as e:
        logging.error(f"Error processing image: {str(e)}")
        return jsonify(error=str(e)), 500

@app.route('/run-image-object-detection', methods=['POST'])
def run_image_object_detection():
    try:
        # Get the image file from the request
        img_file = request.files.get('file')
        
        # Open the image file
        img = Image.open(img_file)
        
        # Convert the image to numpy array and prepare it for the model
        img_np = np.array(img)
        img_np = img_np.transpose(2, 0, 1)
        img_np = np.expand_dims(img_np, axis=0)
        
        # Run the model on the input image
        input_name = model.get_inputs()[0].name
        output_name = model.get_outputs()[0].name
        outputs = model.run([output_name], {input_name: img_np})
        
        # Get the output results from the model
        output = outputs[0]
        
        # Prepare the response payload
        response_payload = {
            'request_id': str(uuid.uuid4()),
            'compute_time': 0.12345,  # Placeholder value, in a real scenario, this would be the actual compute time
            'payload': [
                {
                    'bbox': {'origin': [int(output[0,0]), int(output[0,1])], 'size': [int(output[0,2]), int(output[0,3])]},
                    'class': 'object',  # Placeholder value, in a real scenario, this would be the actual class detected
                    'score': float(output[0,4]),
                    'image': base64.b64encode(img_io.getvalue()).decode('utf-8')
                }
            ]
        }
        
        # Return the response payload as JSON
        return jsonify(response_payload)
    except Exception as e:
        logging.error(f"Error running image object detection: {str(e)}")
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

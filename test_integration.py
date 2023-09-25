

import random
import os

# Get a list of image filenames in the val2017_subset folder
image_filenames = os.listdir('/mnt/data/Image_Analysis_API_Li_Quan/val2017_subset/val2017_subset')
# Select a random image filename
random_image_filename = random.choice(image_filenames)
import requests

def test_get_image_endpoint():
    # Test the get-image endpoint
    response = requests.get('http://localhost:5000/get-image', )
    assert response.status_code == 200

def test_process_image_endpoint():
    # Test the process-image endpoint
    response = requests.post('http://localhost:5000/process-image', json={'filename': random_image_filename})
    assert response.status_code == 200

def test_run_image_object_detection_endpoint():
    # Test the run-image-object-detection endpoint
    response = requests.post('http://localhost:5000/run-image-object-detection', json={'filename': random_image_filename})
    assert response.status_code == 200

if __name__ == "__main__":
    test_get_image_endpoint()
    test_process_image_endpoint()
    test_run_image_object_detection_endpoint()


import requests

def test_get_image_endpoint_with_invalid_filename():
    # Test the get-image endpoint with an invalid filename
    response = requests.get('http://localhost:5000/get-image', params={'filename': 'invalid.jpg'})
    assert response.status_code == 400

def test_process_image_endpoint_with_invalid_input():
    # Test the process-image endpoint with invalid input
    response = requests.post('http://localhost:5000/process-image', json={'filename': 123})
    assert response.status_code == 400

def test_run_image_object_detection_endpoint_with_invalid_input():
    # Test the run-image-object-detection endpoint with invalid input
    response = requests.post('http://localhost:5000/run-image-object-detection', json={'filename': None})
    assert response.status_code == 400

if __name__ == "__main__":
    test_get_image_endpoint_with_invalid_filename()
    test_process_image_endpoint_with_invalid_input()
    test_run_image_object_detection_endpoint_with_invalid_input()

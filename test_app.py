
import unittest
from app import app
import json

class FlaskApiTests(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_image(self):
        response = self.app.get('/get-image')
        self.assertEqual(response.status_code, 200)

    def test_process_image(self):
        response = self.app.post('/process-image', data=json.dumps({'filename': 'image1.jpg'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_run_image_object_detection(self):
        response = self.app.post('/run-image-object-detection', data=json.dumps({'filename': 'image1.jpg'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

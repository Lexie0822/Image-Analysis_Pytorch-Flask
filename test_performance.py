
import random
import os

# Get a list of image filenames in the val2017_subset folder
image_filenames = os.listdir('/mnt/data/Image_Analysis_API_Li_Quan/val2017_subset/val2017_subset')
# Select a random image filename
random_image_filename = random.choice(image_filenames)

from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_image(self):
        self.client.get("/get-image", )

    @task
    def process_image(self):
        self.client.post("/process-image", json={'filename': random_image_filename})

    @task
    def run_image_object_detection(self):
        self.client.post("/run-image-object-detection", json={'filename': random_image_filename})

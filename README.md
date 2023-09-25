# Image-Analysis_Pytorch-Flask

# Image Analysis API

This project presents an Image Analysis API that performs object detection on images. The API is built using Flask and is containerized using Docker. The object detection is performed using the ONNX models (FasterRCNN and MobileNetV2), and the API can be deployed in a Kubernetes cluster.

## Endpoints

The API exposes the following endpoints:

1. `/get-image` (GET): Fetches an image from a dataset (I get image from the subset of the COCO 2017 validation dataset).
2. `/process-image` (POST): Accepts an image and optional processing parameters, and returns the processed image.
3. `/run-image-object-detection` (POST): Performs object detection on the uploaded image and returns the results, including the image with bounding boxes and detection scores.

## Setup and Deployment

### Docker

1. Build the Docker image: `docker build -t image-analysis-api .`
2. Run the Docker container: `docker run -p 5000:5000 image-analysis-api`

### Kubernetes

1. Create the Kubernetes deployment: `kubectl apply -f deployment.yaml (k8s_deployment.yaml)`
2. Create the Kubernetes service: `kubectl apply -f service.yaml`
3. Access the API at the service's external IP address.
4. Create the Kubernetes scaling: `kubectl apply -f k8s_scaling.yaml` 

## Scaling

The API is configured to run with 3 replicas in the Kubernetes deployment, providing basic load balancing. Further scaling can be achieved by adjusting the number of replicas based on the load and utilizing horizontal pod autoscaling.

## Efficient Deployment Strategies

For efficient and cost-effective deployment of the `run-image-object-detection` endpoint, the following strategies can be considered:

1. **Model Optimization**: Optimize the ONNX models to reduce computational overhead and increase inference speed.
2. **Caching**: Implement caching to avoid redundant computations and improve response times.
3. **Load Balancing**: Utilize load balancing to distribute traffic evenly across multiple instances of the API.
4. **Autoscaling**: Implement autoscaling to dynamically adjust the number of API instances based on the current load.


## Questions

### Code Quality

The code is structured and organized to maintain readability and scalability, with potential for further documentation and optimizations.

### Design Decisions

- Flask was chosen for building the API due to its simplicity and ease of setup.
- The ONNX models are deployed using the ONNX Runtime for efficient inference.
- Docker and Kubernetes are used for containerization and orchestration, respectively, to ensure scalability and ease of deployment.

### Testing the System

- Unit tests have been created to verify the functionality of each endpoint.
- Integration tests are implemented in the `test_integration.py` script. It tests the `/get-image`, `/process-image`, and `/run-image-object-detection` endpoints to ensure they return a 200 status code, indicating successful integration. The script has been updated to use random images from the dataset instead of hardcoded filenames, making the tests more realistic and effective.
- Performance tests are implemented in the `test_performance.py` script using the Locust framework. It defines a WebsiteUser class with tasks to test the `/get-image`, `/process-image`, and `/run-image-object-detection` endpoints under load. This script also now selects random images from the dataset for a more realistic testing scenario.
- Error handling tests are implemented in the `test_error_handling.py` script. It tests the `/get-image` and `/process-image` endpoints with invalid inputs to ensure they return appropriate error status codes (400). These tests help to verify that the API handles errors gracefully.

  
### Tools/Framework Used

- Flask for API development
- Docker for containerization
- Kubernetes for orchestration
- ONNX Runtime for model deployment
- Open-source packages and models such as PyTorch for Object Detection model((FasterRCNN and MobileNetV2)


### Troubleshooting

If the system encounters issues, the following steps can be taken to troubleshoot:

1. Check the logs for any error messages or anomalies.
2. Verify the integrity of the ONNX models and test them separately to ensure they are functioning correctly.
3. Validate the API endpoints individually to identify the source of the issue.
4. If necessary, rollback to a previous stable version of the API and investigate the cause of the issue.

### Scaling in Terms of Volume

To scale the API to handle a larger volume of requests, the following strategies can be employed:

1. Increase the number of API replicas in the Kubernetes deployment to distribute the load more evenly.
2. Implement a queue system to manage the request load and prevent overload of the API.
3. Optimize the ONNX models further to reduce inference time and increase throughput.

### Future Enhancements

If given more time, the following enhancements could be considered:

1. Implementing additional features such as image segmentation and classification.
2. Enhancing the API with a user interface for easier interaction.
3. Integrating the API with other services to form a complete image analysis solution.
4. Set up a CI/CD pipeline for automated testing and deployment.
5. Conduct comprehensive testing and deployment
6. Implement machine learning capabilities to enhance object detection accuracy.

## Feedback and Contributions

Feedback and contributions are welcome. Please submit issues and pull requests for any enhancements or fixes.


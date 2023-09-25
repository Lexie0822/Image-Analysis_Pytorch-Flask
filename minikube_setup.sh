
#!/bin/bash

# Start Minikube
minikube start

# Set the environment to use Minikube’s Docker daemon
eval $(minikube docker-env)

# Build the Docker image
docker build -t flask-app-image:latest .

# Apply the Kubernetes manifests
kubectl apply -f k8s_deployment.yaml
kubectl apply -f k8s_scaling.yaml

# Open the Minikube dashboard
minikube dashboard

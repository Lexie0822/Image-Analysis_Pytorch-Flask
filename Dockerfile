
# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the ONNX models into the container
COPY mobilenet_v2.onnx ./
COPY FasterRCNN-10.onnx ./

# Copy the Flask script into the container
COPY app.py ./

# Set the Flask environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Expose the Flask port
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run"]

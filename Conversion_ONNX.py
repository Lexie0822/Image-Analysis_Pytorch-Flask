from torchvision import models
import torch
import torch.onnx
import onnxruntime as rt
from PIL import Image
import numpy as np
from torchvision import transforms

# Step 1: Convert PyTorch Model to ONNX

# Load the pre-trained PyTorch model
model = models.mobilenet_v2()
model.load_state_dict(torch.load('/mnt/data/Image_Analysis_API_Li_Quan/mobilenet_v2-b0353104.pth'))

# Set the model to evaluation mode
model.eval()

# Create dummy input data
dummy_input = torch.randn(1, 3, 224, 224)

# Specify the output file name
output_onnx_file = '/mnt/data/Image_Analysis_API_Li_Quan/mobilenet_v2.onnx'

# Export the PyTorch model to ONNX format
torch.onnx.export(model, dummy_input, output_onnx_file)

# Step 2: Prepare Actual Data

# Load an image from the val2017_subset dataset
image_path = '/mnt/data/Image_Analysis_API_Li_Quan/val2017_subset/image.jpg'
image = Image.open(image_path)

# Preprocess the image
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
input_data = preprocess(image)
input_data = input_data.unsqueeze(0).numpy()

# Step 3: Deploy the ONNX Model using ONNX Runtime

# Load the ONNX model
sess = rt.InferenceSession(output_onnx_file)

# Get the input name for the ONNX model
input_name = sess.get_inputs()[0].name

# Run the model with the actual input data
result = sess.run(None, {input_name: input_data})

# Print the result
print(result)

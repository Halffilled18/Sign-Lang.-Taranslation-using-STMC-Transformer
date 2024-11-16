import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import torch
from torchvision import models, transforms
from PIL import Image
import os
import glob

# Load the pre-trained ResNet model using the new 'weights' parameter
weights = models.ResNet50_Weights.DEFAULT
model = models.resnet50(weights=weights)
model.eval()

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def extract_features(image_path):
    input_image = Image.open(image_path).convert("RGB")
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)
    with torch.no_grad():
        output = model(input_batch)
    return output

frames_directory = 'frames'
features_directory = 'features'

if not os.path.exists(features_directory):
    os.makedirs(features_directory)

for video_folder in os.listdir(frames_directory):
    video_frames_path = os.path.join(frames_directory, video_folder)
    video_features_path = os.path.join(features_directory, video_folder)
    
    if not os.path.exists(video_features_path):
        os.makedirs(video_features_path)
    
    for frame_file in glob.glob(f"{video_frames_path}/*.jpg"):
        features = extract_features(frame_file)
        features_save_path = os.path.join(video_features_path, os.path.basename(frame_file).replace('.jpg', '.pt'))
        torch.save(features, features_save_path)
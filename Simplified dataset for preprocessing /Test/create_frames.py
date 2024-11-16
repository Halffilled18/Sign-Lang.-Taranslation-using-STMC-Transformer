import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=1):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    while success:
        if count % frame_rate == 0:
            cv2.imwrite(f"{output_folder}/frame{count}.jpg", image)
        success, image = vidcap.read()
        count += 1

video_directory = 'videos'
output_directory = 'frames'

for video_file in os.listdir(video_directory):
    video_path = os.path.join(video_directory, video_file)
    video_output_folder = os.path.join(output_directory, video_file.split('.')[0])
    extract_frames(video_path, video_output_folder)
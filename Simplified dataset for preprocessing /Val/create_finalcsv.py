import csv
import os

def create_dataset(csv_file, features_directory, output_csv):
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["video_id","frame_features_path", "transcript"])
        
        with open(csv_file, mode='r') as csv_input:
            reader = csv.DictReader(csv_input, delimiter='\t')
            for row in reader:
                video_id = row["VIDEO_ID"]
                video_name = row["VIDEO_NAME"]
                sentence = row["SENTENCE"]
                
                video_folder = f"{video_name}"
                video_features_path = os.path.join(features_directory, video_folder)
                
                if os.path.exists(video_features_path) and os.path.isdir(video_features_path):
                    for feature_file in os.listdir(video_features_path):
                        frame_features_path = os.path.join(video_features_path, feature_file)
                        writer.writerow([video_id, frame_features_path, sentence])
                else:
                    print(f"Warning: Directory {video_features_path} not found or is not a valid directory.")

# Replace with your actual paths
csv_file = 'how2sign_realigned.csv'
features_directory = 'features'
output_csv = 'dataset.csv'

create_dataset(csv_file, features_directory, output_csv)
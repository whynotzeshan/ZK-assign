import cv2
import os
from tqdm import tqdm  # For progress bar

# Path to the directory containing images
images_dir = 'D:\4k wallapaper\\2406627.jpg'  # Corrected the path

# Output video file name
output_video_path = 'E:\file'  # Added a specific file name

# Function to sort files based on their names
def sort_files_by_name(files):
    return sorted(files, key=lambda x: int(x.split('_')[-1].split('.')[0]))

# Get the list of image files in the directory
image_files = [os.path.join(images_dir, f) for f in sort_files_by_name(os.listdir(images_dir)) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Check if there are images in the directory
if not image_files:
    print(f"No image files found in the directory: {images_dir}")
else:
    # Get the dimensions of the first image
    first_image = cv2.imread(image_files[0])
    height, width, _ = first_image.shape

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'XVID' for .avi format
    video_writer = cv2.VideoWriter(output_video_path, fourcc, 10.0, (width, height))

    # Write each image to the video
    for image_file in tqdm(image_files, desc='Converting to video'):
        image = cv2.imread(image_file)
        video_writer.write(image)

    # Release the VideoWriter object
    video_writer.release()

    print(f"Video created: {output_video_path}")

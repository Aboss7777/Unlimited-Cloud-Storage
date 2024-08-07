import cv2
import numpy as np
import os

def binary_string_to_video(binary_string, frame_width=720, frame_height=480, frame_rate=12):
    # Get the current working directory and ensure the 'vids' folder exists
    cwd = os.getcwd()
    vids_folder = os.path.join(cwd, 'vids')
    os.makedirs(vids_folder, exist_ok=True)
    
    # Define the video path
    video_path = os.path.join(vids_folder, 'output_video2.mp4')
    
    # Calculate number of pixels per frame
    pixels_per_frame = frame_width * frame_height
    
    # Number of frames needed
    num_frames = (len(binary_string) + pixels_per_frame - 1) // pixels_per_frame
    
    # Initialize the video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' codec for MP4 files
    video_writer = cv2.VideoWriter(video_path, fourcc, frame_rate, (frame_width, frame_height), isColor=False)
    
    if not video_writer.isOpened():
        raise Exception(f"Failed to open video writer with path: {video_path}")
    
    for frame_index in range(num_frames):
        start = frame_index * pixels_per_frame
        end = start + pixels_per_frame
        frame_data = binary_string[start:end].ljust(pixels_per_frame, '0')  # Pad with '0's if needed
        
        # Create the frame as a numpy array
        frame = np.array([255 if bit == '1' else 0 for bit in frame_data], dtype=np.uint8)
        frame = frame.reshape((frame_height, frame_width))
        
        # Write the frame to the video
        video_writer.write(frame)
    
    # Release the video writer
    video_writer.release()
    print(f"Video saved to {video_path}")


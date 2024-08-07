import cv2
import numpy as np
import os

def binary_string_to_video(binary_string, frame_width=1920, frame_height=1080, frame_rate=30):
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

def video_to_binary_string(video_path, frame_width=1920, frame_height=1080):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    
    binary_string = ''
    
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        
        # Flatten the frame and convert pixels to binary
        frame = frame.reshape(-1)
        frame_binary = ''.join('1' if pixel == 255 else '0' for pixel in frame)
        binary_string += frame_binary
    
    video_capture.release()
    return binary_string

def binary_string_to_file(binary_string, file_path):
    # Convert binary string to bytes
    byte_array = bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))
    
    # Write bytes to file
    with open(file_path, 'wb') as file:
        file.write(byte_array)



video_path = os.path.join(os.getcwd(), 'vids', 'output_video2.mp4')
#retrieved_binary_string = video_to_binary_string(video_path)


#binary_string_to_file(retrieved_binary_string, file_path)

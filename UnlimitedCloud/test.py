import os
import convert
import revert

video_path = convert.os.path.join(convert.os.getcwd(), 'vids', 'output_video2.mp4')
vidtobin=revert.video_to_binary_string(video_path)
print("reverting")
file_path = convert.os.path.join(convert.os.getcwd(), 'vids', 'retrieved_file.bin')
revert.binary_string_to_file(vidtobin, file_path)
print("shi done")
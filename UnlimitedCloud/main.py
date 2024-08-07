import convert
import revert

def file_to_binary_string(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
            binary_string = ''.join(format(byte, '08b') for byte in file_content)
            return binary_string
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
file_path = 'ttt.exe'  # Replace with your file path
binary_output = file_to_binary_string(file_path)

vidpath=convert.os.getcwd()
print(vidpath)
convert.binary_string_to_video(binary_output)

print("video converted tryin retreival now")
video_path = convert.os.path.join(convert.os.getcwd(), 'vids', 'output_video2.mp4')
vidtobin=revert.video_to_binary_string(video_path)
print("reverting")
file_path = convert.os.path.join(convert.os.getcwd(), 'vids', 'retrieved_file.bin')
revert.binary_string_to_file(vidtobin, file_path)
print("shi done")

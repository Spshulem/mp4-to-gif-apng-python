import os
from moviepy.editor import VideoFileClip, ImageClip
from apng import APNG

def convert_mp4_to_apng(input_file, output_file, resolution, target_fps, export_dir):
    # Create the export directory if it doesn't exist
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)
    
    # Load the MP4 video
    video = VideoFileClip(input_file)
    
    # Resize video according to resolution
    video = video.resize(height=resolution)

    # Convert video frames to PNG images
    png_images = []
    for i, frame in enumerate(video.iter_frames()):
        # Skip frames to achieve target frame rate
        if i % int(video.fps / target_fps) != 0:
            continue

        frame_image = ImageClip(frame, duration=1/target_fps)
        frame_path = os.path.join(export_dir, f"frame_{i}.png")
        frame_image.save_frame(frame_path)
        png_images.append(frame_path)

    # Create an APNG from the PNG images
    apng = APNG()
    for png_image in png_images:
        apng.append_file(png_image, delay=int(1000/target_fps))
    
    # Change extension of output file to .png
    output_file_png = os.path.join(export_dir, output_file.replace('.apng', '.png'))
    apng.save(output_file_png)

    # Remove temporary frame images
    for png_image in png_images:
        os.remove(png_image)

if __name__ == "__main__":
    input_file = input("Enter the input MP4 file path: ")
    file_name, _ = os.path.splitext(input_file)
    output_file = f"{file_name}.apng"

    resolution = int(input("Enter the resolution (360, 480, 720, 1080 etc.): "))
    target_fps = int(input("Enter the frame rate (24, 30, 60 etc.): "))

    export_dir = "export"
    print(f"Converting {input_file} to {os.path.join(export_dir, output_file.replace('.apng', '.png'))}...")
    convert_mp4_to_apng(input_file, output_file, resolution, target_fps, export_dir)
    print("Conversion complete.")

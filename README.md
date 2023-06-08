# MP4 to APNG/GIF Converter

This Python script allows you to convert an MP4 video file into an APNG (Animated Portable Network Graphics) or GIF (Graphics Interchange Format) file. The script prompts the user for the input file path, the desired resolution, the target frame rate, and the output format.

## Requirements

- Python 3.6 or above
- moviepy (`pip install moviepy`)
- apng (`pip install apng`)


## Usage

1. Ensure you have Python installed on your machine. This script was written in Python 3 and might not work with Python 2.
2. Install the required Python packages. You can do this by running `pip install moviepy apng` in your command line.
3. Run the script by navigating to its directory in the command line and running `python mp4_to_apng.py`.
4. When prompted, enter the path to the input MP4 file, the desired resolution (e.g., 360, 480, 720, 1080), the target frame rate (e.g., 24, 30, 60), and the output format (either 'APNG' or 'GIF').

The script will then convert the video to the chosen format in the specified resolution and frame rate. The output file will be saved in the "export" directory, and any temporary frame files will be deleted after the conversion is complete.

## Notes

- The APNG format is not supported by all platforms and browsers. Ensure that your target platform/browser supports APNG before using this option.
- The script creates the "export" directory in the same directory where the script is run, not necessarily where the script file is located. If you run the script from a different directory, the "export" directory might be created there instead.
Please let me know if you need further information or if you would like me to add more details to the README.
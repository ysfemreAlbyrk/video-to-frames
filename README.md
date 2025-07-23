# video 2 frames

Extract frames from a video file.

## Description

This tool extracts frames from a video file and saves them as images in a specified output directory. You can control the interval to save every N'th frame.

## Usage

```bash
python video2frame.py [-h] [-o OUTPUT_DIR] [--file_type {png,jpg,jpeg,webp}] [-i INTERVAL] video_path
```

- `<video_path>`: Path to the input video file.
- `-o OUTPUT_DIR`: (Optional) Output directory for extracted frames. Default is `frames`.
- `--file_type` or `-ft`: (Optional) File extension of the extracted frame. [ `png` `jpg` `jpeg` `webp` ]
- `-i INTERVAL`: (Optional) Interval for frame extraction (every N'th frame). Default is `1`.

## Example

Extract every frame from `input.mp4` and save to `frames` folder:

```bash
python video2frame.py input.mp4
```

Extract every 5th frame and save to `output_frames` folder:

```bash
python video2frame.py input.mp4 -o output_frames -ft png -i 5
```

## Requirements

- Python 3.x
- OpenCV (`cv2`)

Install dependencies:

```bash
pip install opencv-python
```

## Author

Created by Yusuf Emre ALBAYRAK for project HÜMA in TEKNOFEST 2025 HYZ competition.

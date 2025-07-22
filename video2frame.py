# Created by Yusuf Emre ALBAYRAK for project HÜMA in TEKNOFEST 2025 HYZ competition.
import cv2
import os
import argparse

def video2frames(video_path, odir='frames', interval=1):
    # create output dir if it isn't created.
    os.makedirs(odir,exist_ok=True)

    # Open video file
    video= cv2.VideoCapture(video_path)
    if not video.isOpened():
        raise ValueError(f"Video file can not open: {video_path}")
    
    success, image = video.read()
    count=0
    saved_count=0
    
    print(f"Frames extracting from {video_path}...")

    while success:
        if count % interval == 0:
            # Save frame
            frame=os.path.join(odir,f"frame_{saved_count:06d}.jpg")
            cv2.imwrite(frame,image)
            saved_count +=1
        success, image= video.read()
        count += 1
    
    video.release()
    print(f"{saved_count} frames saved in {odir}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Frame extractor from video. Created by Yusuf Emre ALBAYRAK for project HÜMA in TEKNOFEST 2025 HYZ competition.")
    parser.add_argument('video_path',help="Input video path.")
    parser.add_argument('-o',dest="output_dir",default="frames",help="The folder where the frames will be extracted.")
    parser.add_argument('-i',dest="interval",type=int,default=1, help="Frame interval (every N'th frame).")
    
    args=parser.parse_args()
    
    try:
        video2frames(args.video_path,args.output_dir,args.interval)
    except Exception as e:
        print(f"[ERROR] {e}")
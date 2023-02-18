import cv2
import os

video_path = "C:/Users/TUF A15/Desktop/baby baby baby OOOOO/video.mp4"#<-- Video path here

frames_dir = "C:/Users/TUF A15/Desktop/baby baby baby OOOOO/frames"#<-- Frames directory here
if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)

video = cv2.VideoCapture(video_path)

fps = 1

frame_count = 0

while True:
    
    ret, frame = video.read()

    if not ret:
        break

    frame_filename = os.path.join(frames_dir, f"{frame_count:04d}.jpg")
    cv2.imwrite(frame_filename, frame)

    frame_count += 1

    video.set(cv2.CAP_PROP_POS_FRAMES, frame_count * fps)

video.release()
cv2.destroyAllWindows()

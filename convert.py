import cv2
import json
import os

print('Processing... ')
print('This should take at least 15 seconds')

video_path = "<video path here>"
output_file_path = "<output file path here>"
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

video = cv2.VideoCapture(video_path)

fps = 2

frame_count = 0

ascii_frames = []

while True:

    ret, frame = video.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    resized_gray = cv2.resize(gray, (80, 60), interpolation=cv2.INTER_AREA)

    ascii_frame = ""
    for row in resized_gray:
        for pixel in row:
            if pixel < 128:
                ascii_frame += "o"
            else:
                ascii_frame += " "
        ascii_frame += "\n"

    ascii_frames.append(ascii_frame)

    frame_count += 1

    video.set(cv2.CAP_PROP_POS_FRAMES, frame_count * fps)

video.release()
cv2.destroyAllWindows()

with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(ascii_frames, output_file, ensure_ascii=False)

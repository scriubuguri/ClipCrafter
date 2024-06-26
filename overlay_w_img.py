from subprocess import call
import sys
import os

director_curent = os.getcwd()
new_name = None
for file in os.listdir(director_curent):
    if file.endswith(".mp4"):
        new_name = file.split(".webm")[0] + "1.mp4"
        os.rename(file, new_name)

input_video = new_name.rstrip(".mp4")[:-1]


with open("timestamps.txt", mode="r", encoding="utf-8") as f:
    timestamps = f.read()

timestamps = timestamps.split("\n")
timestamps = [x.strip() for x in timestamps if x.strip()]

for wordnumber, timestamp in enumerate(timestamps, start=1):
    tsstart, tsstop = timestamp.split(" ")

    command = f"""ffmpeg -i {input_video}{wordnumber}.mp4 -i word_images/word_{wordnumber}.png -filter_complex "[0:v][1:v] overlay=(W-w)/2:H-h-500:enable='between(t, {tsstart}, {tsstop})'" -pix_fmt yuv420p -c:a copy {input_video}{wordnumber+1}.mp4"""

    print(command)
    call(command, shell=True)

    if wordnumber > 1:
        call(f"rm {input_video}{wordnumber}.mp4", shell=True)

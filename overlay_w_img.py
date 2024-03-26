from subprocess import call

i
with open("timestamps", mode="r", encoding="utf-8") as f:
    timestamps = f.read()

timestamps = timestamps.split("\n")
timestamps = [x.strip() for x in timestamps if x.strip()]

for wordnumber, timestamp in enumerate(timestamps, start=1):
    tsstart, tsstop = timestamp.split(" ")

    command = f"""ffmpeg -i movie{wordnumber}.mp4 -i word_images/word_{wordnumber}.png -filter_complex "[0:v][1:v] overlay=25:25:enable='between(t, {tsstart}, {tsstop})'" -pix_fmt yuv420p -c:a copy movie{wordnumber+1}.mp4"""

    print(command)
    call(command, shell=True)

    if wordnumber > 1:
        call(f"rm movie{wordnumber}.webm", shell=True)

from subprocess import call


with open("timestamps", mode="r", encoding="utf-8") as f:
    timestamps = f.read()

timestamps = timestamps.split("\n")
timestamps = [x.strip() for x in timestamps if x.strip()]

wordnumber = 1

for timestamp in timestamps:
    tsstart, tsstop = timestamp.split(" ")

    command = f"""ffmpeg -i movie{wordnumber}.webm -i word_images/word_{wordnumber}.png -filter_complex "[0:v][1:v] overlay=25:25:enable='between(t, {tsstart}, {tsstop})'" -pix_fmt yuv420p -c:a copy movie{wordnumber+1}.webm"""

    print(command)
    call(command, shell=True)

    if wordnumber > 2:
        call(f"rm movie{wordnumber-1}.webm")

    wordnumber += 1

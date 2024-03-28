## Clip Crafter

This project offers a bloated solution for users to manipulate video content by downloading, trimming, concatenating, and enhancing it with overlaid text images at specific timestamps.

## Features

- *YouTube Video Downloading*: Easily download videos from YouTube by providing the video URL
- *Video Trimming*: Trim the video into mini-clips
- *Concatenation*: Seamlessly concatenate trimmed video clips
- *VTT File Integration*: Extract text from a VTT file and create images to overlay them onto the video at specified timestamps

## Requirements

- Whisper
- Ansi
- Ffmpeg
- ImageMagick
- Python 3.x

## Usage

1. Clone this repository

Open a terminal and clone the repository.

```bash
git clone https://github.com/scriubuguri/ClipCrafter.git
```

2. Install [Ansi](https://github.com/fidian/ansi)

3. See [Whisper repository](https://github.com/ggerganov/whisper.cpp) and follow the instructions provided in the README to download one of the Whisper models

4. Make the `clip_crafter.sh` script executable, run it and follow the intuitive instructions provided

```bash
chmod +x clip_crafter.sh
```

```bash
./clip_crafter.sh
```

5. Generate the wav file (make sure you are in whisper folder)

```bash
ffmpeg -i /path/to/your/concatenatedvideo -ar 16000 -ac 1 -c:a pcm_s16le output.wav
```

6. Generate the vtt file (make sure you are in whisper folder)

```bash
./main -m ./models/your-downloaded-model -f output.wav -l ro -ml 1 -ovtt
```

You can find the `4` and `5` steps also in the [whisper repository](https://github.com/ggerganov/whisper.cpp) with some examples.

7. Run the command to process the vtt file (make sure you are in the main directory)

```bash
python3 wav_processing.py whisper.cpp/output.wav.vtt vttfile
```

8. Run the command to create the final vtt file and extract timestamps and text

```bash
python3 w_concat.py vttfile vttfinal /path/to/your/concatenatedvideo
```

9. Make the `pic_generator.sh` script executable and run it to generate text images

```bash
chmod +x pic_generator.sh
```

```bash
./pic_generator.sh full_words path/to/your/concatenatedvideo
```

10. Move the `overlay_w_img.py` in the folder where you have the video and run it to add captions on it

```bash
mv overlay_w_img.py path/to/your_video
```

```bash
python3 overlay_w_img.py
```

## Author

- **scriubuguri**

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](https://github.com/scriubuguri/ClipCrafter?tab=BSD-3-Clause-1-ov-file#readme) file for details.

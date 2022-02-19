# Bad Apple Emote Player
## Setup

Before you start, please make sure you have [ffmpeg](https://ffmpeg.org/download.html) installed and added into your device PATHS
First, clone this repository with the command:

```https://github.com/Kaiz404/BadAppleEmotePlayer.git```

install python modules:

```pip install -r requirements.txt```

Open command prompt within the "frames" directory then run the following command to extract all frames from the music video:

```ffmpeg -i ../badappleMV.mkv -vf fps=30 %04d.png```

## The fun part
In the emotes folder add any emote or emoji you want to convert into a bad apple mv, then change the emote name in badapple.py(line 25-26) according to your desired emotes. You can also change the emote and frame dimensions if you wish to(line 12-13), just make sure its ratio is constant. Now run badapple.py and let your device do the rest, the final video can be found in the "results" directory
# Bad Apple Emote Player
## Setup

Before you start, please make sure you have [ffmpeg](https://ffmpeg.org/download.html) install and added into your device PATHS
First, clone this repository with the command:

```git clone https://github.com/Kaiz404/bad-apple.git```

Open command prompt within the empty "frames" directory then run the following command to extract all frames from the music video:

```ffmpeg -i ../badappleMV.mkv -vf fps=30 %04d.png```

## The fun part
In the emotes folder add any emote or emoji you want to convert into a bad apple mv, then change the emote name in badapple.py line 17-18 according to your desired emotes. You can also change the emote and frame dimensions if you wish to, just make sure its ratio is constant. Now run badapple.py and let your device run.
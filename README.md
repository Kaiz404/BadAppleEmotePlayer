# Bad Apple Emote Player
## Setup

Before you start, please make sure you have [ffmpeg](https://ffmpeg.org/download.html) install and added into your device PATHS
First, clone this repository with the command:
```git clone https://github.com/Kaiz404/bad-apple.git```

Download the [bad apple music video](https://www.youtube.com/watch?v=UkgK8eUdpAo) with either youtube-dl or a website of your own choice then move the downloaded video into the bad apple directory.

Open command prompt within the bad apple directory and run the command
```ffmpeg -i badapple.mp4 -vn -acodec copy audio.aac```

cd into the empty "frames" directory then run the following command to extract all frames from the music video:
```ffmpeg -i ../badapple.mp4 -vf fps=30 %04d.png```

## The fun part
In the emotes folder add any emote or emoji you want to convert into a bad apple mv, then change the emote name in badapple.py line 17-18. You can also change the emote and frame dimensions if you wish to, just make sure its ratio is constant.
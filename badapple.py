from tqdm import tqdm
import PIL
from PIL import Image
import glob
import os
import ffmpeg
import sys



# change output resolution here
emote_w, emote_h = 16, 16  # the pixel count of the emotes
frame_w, frame_h = 48, 36  # the resolution of the emotes (e.g 48, 36 means 48 emotes in the x-axis and 36 emotes in the y-axis), the higher the numbers the better the resolution, but at the price of unrecognizable emotes

emote_size = (emote_w, emote_h)
frame_res = (frame_w, frame_h)

proceed = input(f"Final video resolution will be {emote_w*frame_w} x {emote_h*frame_h}, proceed? (y/n): ")

if proceed.lower() != "y":
    sys.exit()


# change your emotes here, emote_light will be displayed for every white pixel and emote_dark will be displayed every black pixel (black.png by default)
emote_light = "emote.png"
emote_dark = "black.png"


white = Image.open(f"./emotes/{emote_light}").resize(size=emote_size)
black = Image.open(f"./emotes/{emote_dark}").resize(size=emote_size)

os.chdir("frames")

# process every frame in the "frames" directory then outputs new frames into "outputframes"
for frame in tqdm(glob.glob("*.png"), desc="Processing frames...", unit="frames"):

    processed_frame = Image.new('RGB', (frame_w*emote_w, frame_h*emote_h))
    
    with PIL.Image.open(frame) as img:
        monochrome_img = img.convert(mode="1")
        modified_img = monochrome_img.resize(size=(frame_w, frame_h))

        for y in range(frame_h):
            
            result = Image.new('RGB', (frame_w*emote_w, emote_h))

            for x in range(frame_w):
                pix = modified_img.getpixel(xy=(x,y))
                if pix == 0:
                    result.paste(im=black, box=(x*emote_w, 0))
                else:
                    result.paste(im=white, box=(x*emote_w, 0))

            processed_frame.paste(im=result, box=(0,y*emote_h))

        processed_frame.save(fp=f"../outputframes/{frame}")


os.chdir("../outputframes")
# compiles all new frames into a single video
(
    ffmpeg
    .input('%04d.png', framerate=30)
    .output('output.avi')
    .overwrite_output()
    .run()
)

os.chdir("../results")
# merge output video and audio to create the final result
input_video = ffmpeg.input("../outputframes/output.avi")
input_audio = ffmpeg.input("../audio.aac")
ffmpeg.concat(input_video, input_audio, v=1, a=1).output('result.mp4').run()

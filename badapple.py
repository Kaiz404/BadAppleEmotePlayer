from tqdm import tqdm
import PIL
from PIL import Image
import glob
import os
import ffmpeg



emote_w, emote_h = 16, 16
frame_w, frame_h = 24, 18

emote_size = (emote_w, emote_h)
frame_res = (frame_w, frame_h)


white = Image.open("amogus.png").resize(size=emote_size)
black = Image.open("black.png").resize(size=emote_size)



for frame in tqdm(glob.glob("*.png"), desc="Processing frames...", unit="frames"):

    os.chdir("../frames")

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

        os.chdir("../outputframes")

        processed_frame.save(fp=f"{frame}.png")


ffmpeg.input('%04d.png', framerate=30).output('output.mp4').overwrite_output().run()

os.chdir("../result")

input_video = ffmpeg.input("../outputframes/output.mp4")
input_audio = ffmpeg.input("../audio.aac")

ffmpeg.concat(input_video, input_audio, v=1, a=1).output('result.mp4').run()

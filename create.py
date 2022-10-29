import subprocess
import os
import sys
import tqdm

#filesave = input("Do you want to save files? [Y]/n: ")
url = input("URL: ")
dl_cmd = "yt-dlp {} -o video.mp4".format(url)
dl = subprocess.run(dl_cmd, shell=True)
if dl.returncode != 0:
    sys.exit("something wrong")

os.path.isdir('./imgs')
if not os.path.isdir('./imgs'):
    os.mkdir('./imgs')

subprocess.run(["ffmpeg -i video.mp4 -vcodec png imgs/%07d.png"], shell=True)
imgs = os.listdir('./imgs')

if not os.path.isdir('./txts'):
    os.mkdir('./txts')
for img in tqdm.tqdm(imgs):
    convert = "jp2a imgs/{} --output=txts/{} --size=80x45".format(img, img.replace('png', 'txt'))
    subprocess.run(convert, shell=True)


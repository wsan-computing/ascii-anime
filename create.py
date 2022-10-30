#!/usr/bin/python3
from shutil import rmtree
import subprocess
import os
import sys
import tqdm
import argparse

psr = argparse.ArgumentParser(
    prog="ASCII Animation Generator",
    usage="python3 create.py <OPTIONS>",
    description="Generate ASCII animation from video file."
)
# psr.add_argument("-f", "--file", help="<path/to/video>")
psr.add_argument("-i", "--input", required=True, help="<Video URL/Video Path>")
psr.add_argument("-t", "--type", required=True, help="url/file")
args = psr.parse_args()

if os.path.isdir('./imgs'):
    rmtree('./imgs')
if os.path.isdir('./txts'):
    rmtree('./txts')

if args.type == "url":
    if os.path.isfile('./video.mp4'):
        os.remove('./video.mp4')
    dl_cmd = "yt-dlp {} -o video.mp4 -f mp4".format(args.input)
    dl = subprocess.run(dl_cmd, shell=True)
    if dl.returncode != 0:
        sys.exit("something wrong")
    fname = "video.mp4"
elif args.type == "file":
    fname = args.input
else:
    sys.exit("Please select correct type")

os.mkdir('./imgs')
strip = "ffmpeg -i {} -vf fps=30 -vcodec png imgs/%07d.png".format(fname)
subprocess.run(strip, shell=True)
imgs = os.listdir('./imgs')

os.mkdir('./txts')
for img in tqdm.tqdm(imgs):
    convert = "jp2a imgs/{} --output=txts/{} --size=192x54".format(img, img.replace('png', 'txt'))
    subprocess.run(convert, shell=True)


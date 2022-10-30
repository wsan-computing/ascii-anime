# ASCII Animation Generator

## Preparation

### Ubuntu

```shellscript
sudo apt install ffmpeg yt-dlp
```

### Common

```shellscript
pip install tqdm
git clone https://github.com/wsan-computing/ascii-anime.git
```

## Usage

```shellscript
cd path/to/ascii-anime
python3 create.py -t url -i https://www.nicovideo.jp/watch/sm8628149
python3 play.py
```

## Options

```text
-t/--type select URL or Local file
-i/--input URL or File path
```

## Requirements

| Item | Description |
| --- | --- |
| OS | Windows(Using WSL)<br>Ubuntu |
| Module | tqdm |

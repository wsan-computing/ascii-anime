from time import sleep
import os

cfpath = os.path.join(os.getcwd(), "config.yml")

txts = os.listdir('./txts')
for txt in txts:
    with open("txts/{}".format(txt)) as f:
        content = f.read()
        # discord.post(content='```' + content + '```')
        sleep(0.033)
        print(content)
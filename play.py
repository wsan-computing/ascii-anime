from time import sleep
import yaml, os
from discordwebhook import Discord

cfpath = os.path.join(os.getcwd(), "config.yml")
with open(cfpath) as file:
    obj = yaml.safe_load(file)
    discord = Discord(url=obj['URL'])

txts = os.listdir('./txts')
for txt in txts:
    with open("txts/{}".format(txt)) as f:
        content = f.read()
        # discord.post(content='```' + content + '```')
        sleep(0.033)
        print(content)
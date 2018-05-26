# -*- coding: utf-8 -*-
import os
import time
import twitter
import yaml

with open(os.path.join(os.getenv('SCRIPT_DIRECTORY', './'), "config.yml"), 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

# Creación del archivo CSV de exportación
timestr = time.strftime("%Y%m%d-%H%M%S")
csvFileName = os.path.join(cfg["export"]["filepath"], cfg["export"]["filename_base"] + "_" + timestr + ".csv")

api = twitter.Api(consumer_key=cfg['twitter']['consumer_key'],
                  consumer_secret=cfg['twitter']['consumer_secret'],
                  access_token_key=cfg['twitter']['access_token_key'],
                  access_token_secret=cfg['twitter']['access_token_secret'])

headerStr = "usuario_lista,lista,usuario,nombre,seguidores,siguiendo,tweets,ultimo_tweet"
with open(csvFileName,'w') as file:
    file.write(headerStr)
    file.write('\n')
    for list in cfg["lists"]:
        results = api.GetListMembers(slug=list["list"], owner_screen_name=list["user"], skip_status=False, include_entities=False)
        for r in results:
            rowStr = "\"" + list["user"] + "\""
            rowStr += "," + "\"" + list["list"] + "\""
            rowStr += "," + "\"" + r.screen_name + "\""
            rowStr += "," + "\"" + r.name + "\""
            rowStr += "," + "\"" + str(r.followers_count) + "\""
            rowStr += "," + "\"" + str(r.friends_count) + "\""
            rowStr += "," + "\"" + str(r.statuses_count) + "\""
            if r.status:
                rowStr += "," + "\"" + time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(r.status.created_at,"%a %b %d %H:%M:%S +0000 %Y")) + "\""
            else:
                rowStr += "," + "\"\""
            file.write(rowStr)
            file.write('\n')

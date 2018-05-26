# -*- coding: utf-8 -*-
import os
import time
import twitter
import yaml


with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

# Creación del archivo CSV de exportación
timestr = time.strftime("%Y%m%d-%H%M%S")
csvFileName = os.path.join(cfg["export"]["filepath"], cfg["export"]["filename_base"] + "_" + timestr + ".csv")

api = twitter.Api(consumer_key=cfg['twitter']['consumer_key'],
                  consumer_secret=cfg['twitter']['consumer_secret'],
                  access_token_key=cfg['twitter']['access_token_key'],
                  access_token_secret=cfg['twitter']['access_token_secret'])

headerStr = "usuario_lista,lista,usuario,nombre,seguidores,siguiendo,tweets,ultimo_tweet"
with open(csvFileName,'wt') as file:
    file.write(headerStr)
    file.write('\n')
    for list in cfg["lists"]:
        results = api.GetListMembers(slug=list["list"], owner_screen_name=list["user"], skip_status=False, include_entities=False)
        for r in results:
            rowStr = "\"" + list["user"].encode('utf-8') + "\""
            rowStr += "," + "\"" + list["list"].encode('utf-8') + "\""
            rowStr += "," + "\"" + r.screen_name.encode('utf-8') + "\""
            rowStr += "," + "\"" + r.name.encode('utf-8') + "\""
            rowStr += "," + "\"" + unicode(r.followers_count).encode('utf-8') + "\""
            rowStr += "," + "\"" + unicode(r.friends_count).encode('utf-8') + "\""
            rowStr += "," + "\"" + unicode(r.statuses_count).encode('utf-8') + "\""
            if r.status:
                rowStr += "," + "\"" + time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(r.status.created_at,"%a %b %d %H:%M:%S +0000 %Y")) + "\""
            else:
                rowStr += "," + "\"\""
            file.write(rowStr)
            file.write('\n')

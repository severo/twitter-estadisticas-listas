import yaml
import twitter

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

api = twitter.Api(consumer_key=cfg['twitter']['consumer_key'],
                  consumer_secret=cfg['twitter']['consumer_secret'],
                  access_token_key=cfg['twitter']['access_token_key'],
                  access_token_secret=cfg['twitter']['access_token_secret'])

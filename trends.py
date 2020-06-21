import twitter
import time
from time import ctime
from threading import Timer
import matplotlib.pyplot as plt
import pandas
import numpy as np
'''
    Helpful method calls
    Status: user, full_text, id, hashtags, urls, retweet_count, geo
'''
#Connect with Twitter
CONSUMER_KEY = "YOUR KEY"
CONSUMER_SECRET = "YOUR SECRET"
ACCESS_TOKEN = "YOUR TOKEN"
ACCESS_TOKEN_SECRET = "YOUR SECRET"
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET,
                  tweet_mode='extended')

print("CONNECTED...")


hrs = 3
i = 0
volumes = {}
times = []
trends = api.GetTrendsCurrent()
trends = trends[:10]
for trend in trends:
    volumes[trend.name] = []
# Every 5 minutes, use an API call to get a list of the top trends
start = time.time()
while i < hrs*12:
    try:
        trends = api.GetTrendsCurrent()
        trends = trends[:10]
    except twitter.error.TwitterError:
        print("Twitter Error... Waiting...")

        time.sleep(15*60)
    for trend in trends:
        if trend.name in volumes.keys():
            volumes[trend.name].append(trend.volume)
        else:
            volumes[trend.name] = [trend.volume] 
    times.append(time.time() - start)
    time.sleep(5*60)
    i += 1

dataframe = pandas.DataFrame.from_dict(volumes, orient='index')
dataframe.transpose()
dataframe.to_pickle("output/volumes.pkl")
print(dataframe)
np.save('output/times.npy', times)



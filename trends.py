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
CONSUMER_KEY = "l73kjRjMDlzNvZ67Kbw41RO63"
CONSUMER_SECRET = "VrrwIrIbzaITfQZEqZ4cOTiUW9sTJ4JsjJEg4jXmhTj7e9bdnA"
ACCESS_TOKEN = "983195774694682625-hJEVsEN3AkxjghEHdZup7S37fTanuBZ"
ACCESS_TOKEN_SECRET = "jljtQ60dF1BTQIYEzMCgH0EsqjV41Fn3pdD8M0M6jLe2O"
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET,
                  tweet_mode='extended')

print("CONNECTED...")




i = 0
volumes = {}
times = []
trends = api.GetTrendsCurrent()
trends = trends[:10]
for trend in trends:
    volumes[trend.name] = []
# Every 5 minutes, use an API call to get a list of the top trends
start = time.time()
while i < 1:
    trends = api.GetTrendsCurrent()
    trends = trends[:10]
    for trend in trends:
        if trend.name in volumes.keys():
            volumes[trend.name].append(trend.volume)
    times.append(time.time() - start)
    time.sleep(3)
    i += 1

dataframe = pandas.DataFrame.from_dict(volumes)
dataframe.to_pickle("volumes.pkl")
print(dataframe)
np.save('times.npy', times)







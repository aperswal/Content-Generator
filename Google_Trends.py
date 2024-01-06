import requests
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

# connect to google
pytrends = TrendReq(hl='en-US', tz=360)

def get_trending_keywords(kw_list):
    pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='', gprop='')
    iot = pytrends.related_topics()
    blog_kw = list(iot[kw_list[0]]['rising']['topic_title'])
    return blog_kw
        
if __name__ == '__main__':
    kw_list = ["Resume Builder"]
    print (get_trending_keywords(kw_list))
    


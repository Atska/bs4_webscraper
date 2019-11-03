import re
import pandas as pd


def get_codes(containers, pattern):
    results = []
    for container in containers:
        tweet_bodies = str(container.find('p'))
        shift_codes = re.findall(pattern, tweet_bodies)
        for shift_code in shift_codes:
            results.append(str(shift_code))
    return results

def get_dates(containers):
    results = []
    for container in containers:
        tweet_dates = container.find_all('a', class_='tweet-timestamp js-permalink js-nav js-tooltip')
        for date in tweet_dates:
            if 'title' in date.attrs:
                date_posted = date['title']
                results.append(date_posted)
    return results

def save_as_csv(codes, dates, save_location):
    df = pd.DataFrame([dates, codes]).T
    df.columns = ['dates', 'code']
    df.to_csv(save_location, index=False)

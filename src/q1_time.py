from typing import List, Tuple
from datetime import datetime
from collections import defaultdict
import json

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Extracts the top 10 dates with the most tweets and the user with the highest tweet count for each date from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing tweet data.

    Returns:
        List[Tuple[datetime.date, str]]: A list of tuples, each containing a date and the username of the user with the highest tweet count for that date.
    """

    # dict to store counts about users and dates
    tweet_count_by_user_and_date = defaultdict(lambda: defaultdict(int))
    tweet_count_date = defaultdict(int)

    # open json file
    with open(file_path, 'r', encoding='utf-8') as file:
        # iteration about json file
        for line in file:
            tweet = json.loads(line)
            # extract tweet date
            tweet_date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            # extract tweet user
            username = tweet['user']['username']
            # plus 1 in date and user count
            tweet_count_by_user_and_date[tweet_date][username] += 1
            tweet_count_date[tweet_date] += 1
    
    # get an ordered list of dates, sorting from the date with the most tweets to the date with the fewest tweets
    sorted_dates = [x[0] for x in sorted(tweet_count_date.items(), key=lambda x: x[1], reverse=True)]

    # results list
    top_users_by_date = []

    # iterate on the top 10 sorted dates to get the user with the most tweets on the day
    for d in sorted_dates[:10]:
        # get top user on the date
        top_user = max(tweet_count_by_user_and_date[d], key=tweet_count_by_user_and_date[d].get)
        # fill results list
        top_users_by_date.append((d, top_user))

    return top_users_by_date
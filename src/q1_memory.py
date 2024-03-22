import ijson
from datetime import datetime
from typing import List, Tuple

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Processes a JSON file containing tweets to find the top 10 dates with the most tweets
    and the user with the highest tweet count for each of those dates.

    Args:
        file_path (str): The path to the JSON file containing tweets.

    Returns:
        List[Tuple[datetime.date, str]]: A list of tuples containing the top 10 dates
        with the most tweets and the user with the highest tweet count for each of those dates.
    """

    tweets_by_day = {} # Dictionary to store the count of tweets for each day
    tweets_by_day_by_user = {} # Nested dictionary to store the count of tweets for each user on each day

    # Open the JSON file
    with open(file_path, 'r') as f:
        # Iterate over each line in the file
        for l in f:
            # Parse each line as JSON using ijson
            parser = ijson.parse(l)
            for prefix, datatype, value in parser:
                if prefix == 'date':
                    # Extract the tweet date
                    tweet_date = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S%z').date()
                    # Increment the tweet count for the corresponding date
                    tweets_by_day[tweet_date] += 1
                
                if prefix == 'user.username':
                    # Extract the tweet user
                    tweet_user = value
                    # Ensure both tweet_date and tweet_user are available
                    if tweet_date and tweet_user:
                        # Increment the tweet count for the user on the corresponding date
                        if tweet_date in tweets_by_day_by_user:
                            if tweet_user in tweets_by_day_by_user[tweet_date]:
                                tweets_by_day_by_user[tweet_date][tweet_user] += 1
                            else:
                                tweets_by_day_by_user[tweet_date][tweet_user] = 1
                        else:
                            tweets_by_day_by_user[tweet_date] = {tweet_user: 1}
    # Initialize an empty list to store the top users by date
    top_users_by_date = []

    # Sort the dates based on the number of tweets in descending order
    sorted_dates = sorted(tweets_by_day.items(), key=lambda item: item[1], reverse=True)

    # Iterate over the sorted dates to find the top user for each date
    for d in sorted_dates:
        max_tweets = 0
        top_user = None
        # Iterate over each user and their tweet count on the current date
        for user, tweets in tweets_by_day_by_user[d[0]].items():
            if tweets > max_tweets:
                max_tweets = tweets
                top_user = user
        
        # Append the top user for the current date to the result list
        top_users_by_date.append((d[0], top_user))

    # Return the top 10 users with the most tweets for their respective dates
    return top_users_by_date[:10]
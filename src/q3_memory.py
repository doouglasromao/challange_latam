from typing import List, Tuple
import json
from collections import Counter

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Extracts mentioned users from tweets and counts their occurrences.

    Args:
        file_path (str): The path to the JSON file containing tweets.

    Returns:
        List[Tuple[str, int]]: A list of tuples containing the top 10 mentioned users and their respective counts, sorted in descending order of frequency.
    """
    mentioned_users = Counter()

    # Open the JSON file and iterate over each line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Parse the JSON tweet
            tweet = json.loads(line)
            text = tweet['content']
            
            # Split the tweet content into words and filter out mentions
            mentions = [word.strip('@,:;.!?') for word in text.split() if word.startswith('@')]
            
            # Update the Counter with the mentions
            mentioned_users.update(mentions)

    return mentioned_users.most_common(10)
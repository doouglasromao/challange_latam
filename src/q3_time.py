from typing import List, Tuple
import json

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Extracts mentioned users from tweets and counts their occurrences.

    Args:
        file_path (str): The path to the JSON file containing tweets.

    Returns:
        List[Tuple[str, int]]: A list of tuples containing the top 10 mentioned users and their respective counts, sorted in descending order of frequency.
    """

    # Dictionary to store mentioned users and the number of times they were mentioned
    mentioned_users = {}

    # Open the JSON file and iterate over each line
    with open(file_path, 'r', encoding='utf-8') as file:
        # iteration about json file
        for line in file:
            tweet = json.loads(line)
            text = tweet['content']
            words = text.split()  # Split the tweet content into words
            for word in words:
                if word.startswith('@'):  # Check if the word starts with "@"
                    # Remove any special characters from the username (e.g., punctuation)
                    username = word.strip('@,:;.!?')

                    # Add the username to the dictionary and increment the mention count
                    mentioned_users[username] = mentioned_users.get(username, 0) + 1

    sorted_users = sorted(mentioned_users.items(), key=lambda item: item[1], reverse=True)[:10]
    return sorted_users
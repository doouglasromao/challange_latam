from typing import List, Tuple
import json
import emoji

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Extracts the top 10 most frequently used emojis from tweets stored in a JSON file.

    Args:
        file_path (str): The path to the JSON file containing tweets.

    Returns:
        List[Tuple[str, int]]: A list of tuples containing the top 10 emojis and their respective counts, sorted in descending order of frequency.
    """
    emoji_count = {} # Dictionary to store the count of each emoji

    # Open the JSON file and iterate through each line
    with open(file_path, 'r', encoding='utf-8') as file:
        # iteration about json file
        for line in file:
            tweet = json.loads(line)
            # Extract emojis from the tweet content
            emojis = emoji.emoji_list(tweet['content'])
            # Count the occurrence of each emoji
            for e in emojis:
                emoji_count[e['emoji']] = emoji_count.get(e['emoji'], 0) + 1

    # Sort the emojis by their counts in descending order and select the top 10
    sorted_emojis = sorted(emoji_count.items(), key=lambda item: item[1], reverse=True)[:10]
    return sorted_emojis
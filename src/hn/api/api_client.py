import requests
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()

def get_top_stories(url: str, n: int = 5) -> List[int]:
    """_summary_

    Args:
        url (str): api-endpoint
        n (int): number of stories to fetch

    Returns:
        List: Stories IDs
    """
    
    try: 
        response = requests.get(url= url, timeout=10)
        response.raise_for_status()
    
        story_ids = response.json()
    
        return story_ids[:n]

    except requests.exceptions.RequestException as e:
        raise RuntimeError("Failed to fetch top stories") from e
        

def get_item_details(baseurl: str, item_id: int):
    
    endpoint = f"{baseurl}{item_id}.json"
    
    try:
        response = requests.get(url= endpoint, timeout=10)
        response.raise_for_status()
    
        story_details = response.json()
    
        return story_details

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch story {story_id} {e}") from e
    

if __name__ == "__main__":
    TOP_STORIES_ENDPOINT = os.getenv("TOP_STORIES_ENDPOINT")
    story_ids = get_top_stories(TOP_STORIES_ENDPOINT, n=1) # type: ignore
    print(story_ids)
    for story_id in story_ids: # type: ignore
        print(get_item_details("https://hacker-news.firebaseio.com/v0/item/", story_id))
    
    
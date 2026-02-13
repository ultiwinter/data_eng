import requests
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()

def get_top_stories(url: str, n: int = 5) -> List | None:
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

    except Exception as e:
        print("Make sure the endpoint is reachable\n", e)
        

def get_item_details(baseurl: str, story_id: int):
    
    endpoint = f"{baseurl}{story_id}.json"
    
    try:
        response = requests.get(url= endpoint, timeout=10)
        response.raise_for_status()
    
        story_details = response.json()
    
        return story_details

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch story {story_id} {e}") from e
    

if __name__ == "__main__":
    TOP_STORIES_ENDPOINT = os.getenv("TOP_STORIES_ENDPOINT")
    story_ids = get_top_stories(TOP_STORIES_ENDPOINT, n=10) # type: ignore
    print(story_ids)
    for story_id in story_ids: # type: ignore
        print(get_item_details("https://hacker-news.firebaseio.com/v0/item/", story_id))
    
    
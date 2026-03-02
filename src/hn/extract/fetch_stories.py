import os
from typing import List

from dotenv import load_dotenv
from tqdm import tqdm

from ..api.api_client import get_top_stories
from .fetch_comments import fetch_comments_recursive

load_dotenv()

ITEM_BASEURL: str = os.getenv("ITEM_BASEURL")  # type: ignore
TOP_STORIES_ENDPOINT = os.getenv("TOP_STORIES_ENDPOINT")  # type: ignore

if not ITEM_BASEURL or not TOP_STORIES_ENDPOINT:
    raise ValueError("ITEM_BASEURL or TOP_STORIES_ENDPOINT is not set")


def fetch_top_stories_with_comments(n: int) -> List[dict]:
    """_summary_"""

    return_result = []
    stories_ids = get_top_stories(TOP_STORIES_ENDPOINT, n)

    for story_id in tqdm(stories_ids, desc="Fetching stories and comments"):
        data = fetch_comments_recursive(ITEM_BASEURL, story_id)
        return_result.append(data)

    return return_result


if __name__ == "__main__":
    data = fetch_top_stories_with_comments(1)
    print(data)

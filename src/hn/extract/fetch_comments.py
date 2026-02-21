from ..api.api_client import get_item_details
from dotenv import load_dotenv
from typing import Dict, Any
import os

load_dotenv()

ITEM_BASEURL = os.getenv("ITEM_BASEURL")

def fetch_comments_recursive(base_url: str, story_id: int) -> Dict[str, Any]:
    
    """_summary_
    """
    
    if not base_url:
        raise ValueError("ITEM_BASEURL is not set in env vars")
    
    item = get_item_details(base_url, story_id)
    
    comments = []
    
    def _collect_comments(item_id: int, depth):
    
        comment = get_item_details(base_url, item_id)
        
        if comment and not comment.get("deleted") and not comment.get("dead"):
            
            # Add depth to track it
            comment["depth"] = depth
            
            # Add parent_id
            comment["parent_id"] = comment.get("parent")
            
            # Add story_id to each comment
            comment["story_id"] = story_id
            
            comments.append(comment)
            
            for kid in comment.get("kids", []):
                _collect_comments(kid, depth+1)
                
    
    for kid in item.get("kids", []):
        _collect_comments(kid, 0)
        
    
    
    return {
        "story": item,
        "comments" : comments
    }
    

if __name__ == "__main__":
    story_id= 47008560
    data = fetch_comments_recursive(ITEM_BASEURL, story_id) # type: ignore
    print(data)
    
    
    
    
    
    
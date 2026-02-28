from ..extract.fetch_stories import fetch_top_stories_with_comments
from typing import List, Dict, Any
from pathlib import Path
from datetime import datetime
import json


BASE_DATA_PATH = Path("data/hn")

def write_raw_data(story_bundle: List[Dict[str, Any]], run_date:str | None) -> None:
    """_summary_

    Args:
        story_bundle (List[Dict[str, Any]]): _description_
        run_date (str | None): _description_
    """
    
    if not isinstance(story_bundle, list):
        raise ValueError("story_bundle must be a list of dictionaries")
    
    if not story_bundle:
        raise ValueError("story_bundle cannot be empty")
    
    if run_date is None:
        run_date = datetime.now().strftime("%Y-%m-%d")
    
    # Seperate stories and comments
    stories = []
    comments = []
    
    for bundle in story_bundle:
        story = bundle.get("story")
        bundle_comments = bundle.get("comments", [])
        
        if story:
            stories.append(story)
            
        if isinstance(bundle_comments, list):
            comments.extend(bundle_comments)
            
    # Build partitioned path
    stories_path = BASE_DATA_PATH / "raw" / "stories" / f"dt={run_date}"
    comments_path = BASE_DATA_PATH / "raw" / "comments" / f"dt={run_date}"
    
    # Ensure paths exist
    stories_path.mkdir(parents=True, exist_ok=True)
    comments_path.mkdir(parents=True, exist_ok=True)
    
    # Write stories and comments to separate files
    write_json_to_file(stories, stories_path / "stories.json")
    write_json_to_file(comments, comments_path / "comments.json")
        

def write_json_to_file(data: List, file_path: Path) -> None:
    """_summary_

    Args:
        data (List): _description_
        file_path (Path): _description_
    """
    
    if not isinstance(data, list):
        raise ValueError("data must be a list")
    
    if not isinstance(file_path, Path):
        raise ValueError("file_path must be a pathlib.Path object")
    
    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
if __name__ == "__main__":
    story_bundle = fetch_top_stories_with_comments(1)
    write_raw_data(story_bundle, None)
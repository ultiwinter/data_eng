from typing import Any, Dict, List

from sqlalchemy import text
from tqdm import tqdm

from ..db.engine import get_engine
from ..extract.fetch_stories import fetch_top_stories_with_comments


def write_raw_data_mysql(story_bundle: List[Dict[str, Any]]) -> None:
    """
    Writes raw Hacker News stories and comments into MySQL.
    """

    if not isinstance(story_bundle, list):
        raise ValueError("story_bundle must be a list")

    if not story_bundle:
        raise ValueError("story_bundle cannot be empty")

    stories = []
    comments = []

    for bundle in tqdm(story_bundle, desc="Preparing data"):
        story = bundle.get("story")
        bundle_comments = bundle.get("comments", [])

        if story:
            stories.append(story)

        if isinstance(bundle_comments, list):
            comments.extend(bundle_comments)

    engine = get_engine()

    with engine.begin() as conn:
        # ---- STORIES ----
        for story in tqdm(stories, desc="Writing stories to MySQL"):
            conn.execute(
                text(
                    """
                INSERT IGNORE INTO stories
                (id, by_user, title, url, score, descendants, time, type)
                VALUES (:id, :by_user, :title, :url, :score,
                        :descendants, FROM_UNIXTIME(:time), :type)
                """
                ),
                {
                    "id": story["id"],
                    "by_user": story.get("by"),
                    "title": story.get("title"),
                    "url": story.get("url"),
                    "score": story.get("score"),
                    "descendants": story.get("descendants"),
                    "time": story.get("time"),
                    "type": story.get("type"),
                },
            )

        # ---- COMMENTS ----
        for comment in tqdm(comments, desc="Writing comments to MySQL"):
            conn.execute(
                text(
                    """
                INSERT IGNORE INTO comments
                (id, story_id, parent_id, by_user, text,
                 time, depth, type)
                VALUES (:id, :story_id, :parent_id, :by_user,
                        :text, FROM_UNIXTIME(:time), :depth, :type)
                """
                ),
                {
                    "id": comment["id"],
                    "story_id": comment["story_id"],
                    "parent_id": comment["parent_id"],
                    "by_user": comment.get("by"),
                    "text": comment.get("text"),
                    "time": comment.get("time"),
                    "depth": comment.get("depth"),
                    "type": comment.get("type"),
                },
            )


if __name__ == "__main__":
    story_bundle = fetch_top_stories_with_comments(1)

    # write to MySQL
    write_raw_data_mysql(story_bundle)
    print("Stories and comments inserted into MySQL")

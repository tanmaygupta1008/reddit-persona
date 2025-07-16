import praw
from utils import load_reddit_credentials

class RedditScraper:
    def __init__(self):
        creds = load_reddit_credentials()
        self.reddit = praw.Reddit(
            client_id=creds["client_id"],
            client_secret=creds["client_secret"],
            user_agent=creds["user_agent"]
        )

    def get_redditor_data(self, username, limit=100):
        """
        Scrapes comments and posts for a given redditor.
        Returns a dictionary with 'comments' and 'posts', each a list of dicts.
        Each dict includes 'id', 'text', and 'url'.
        """
        try:
            redditor = self.reddit.redditor(username)
            user_data = {"comments": [], "posts": []}

            # Scrape comments
            for comment in redditor.comments.new(limit=limit):
                user_data["comments"].append({
                    "id": comment.id,
                    "text": comment.body,
                    "url": f"https://www.reddit.com{comment.permalink}"
                })

            # Scrape posts (submissions)
            for submission in redditor.submissions.new(limit=limit):
                user_data["posts"].append({
                    "id": submission.id,
                    "text": submission.title + " " + (submission.selftext if submission.selftext else ""),
                    "url": submission.url # This might be the permalink or the external link if it's a link post
                                         # For permalink: f"https://www.reddit.com{submission.permalink}"
                })
            return user_data
        except Exception as e:
            print(f"Error scraping data for {username}: {e}")
            return {"comments": [], "posts": []}
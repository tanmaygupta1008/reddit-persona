# import praw
# from utils import load_reddit_credentials

# class RedditScraper:
#     def __init__(self):
#         creds = load_reddit_credentials()
#         self.reddit = praw.Reddit(
#             client_id=creds["client_id"],
#             client_secret=creds["client_secret"],
#             user_agent=creds["user_agent"]
#         )

#     def get_redditor_data(self, username, limit=100):
#         """
#         Scrapes comments and posts for a given redditor.
#         Returns a dictionary with 'comments' and 'posts', each a list of dicts.
#         Each dict includes 'id', 'text', and 'url'.
#         """
#         try:
#             redditor = self.reddit.redditor(username)

#             user_data = {"comments": [], "posts": []}


#             # Scrape comments
#             for comment in redditor.comments.new(limit=limit):
#                 user_data["comments"].append({
#                     "id": comment.id,
#                     "text": comment.body,
#                     "url": f"https://www.reddit.com/{comment.permalink}"
#                 })

#             # Scrape posts (submissions)
#             for submission in redditor.submissions.new(limit=limit):
#                 user_data["posts"].append({
#                     "id": submission.id,
#                     "text": submission.title + " " + (submission.selftext if submission.selftext else ""),
#                     "url": submission.url # This might be the permalink or the external link if it's a link post
#                                          # For permalink: f"https://www.reddit.com{submission.permalink}"
#                 })
            
#             print("user_data : ", user_data)

#             return user_data
#         except Exception as e:
#             print(f"Error scraping data for {username}: {e}")
#             return {"comments": [], "posts": []}



import praw
from utils import load_reddit_credentials

class RedditScraper:
    def __init__(self):
        creds = load_reddit_credentials()
        # print("creds" , creds)
        self.reddit = praw.Reddit(
            client_id=creds["client_id"],
            client_secret=creds["client_secret"],
            user_agent=creds["user_agent"]
        )
        
        print("--- PRAW Initialization Check ---")
        print(f"Client ID used: {creds['client_id']}")
        print(f"User Agent used: {creds['user_agent']}")

        # Optional: Test PRAW connection (remove after debugging)
        # try:
        #     print(f"PRAW initialized. Logged in as: {self.reddit.user.me()}")
        # except Exception as e:
        #     print(f"PRAW initialization test failed: {e}")


    def get_redditor_data(self, username, limit=1000):
        """
        Scrapes comments and posts for a given redditor.
        Returns a dictionary with 'comments' and 'posts', each a list of dicts.
        Each dict includes 'id', 'text', and 'url'.
        """
        try:
            redditor = self.reddit.redditor(username)
            print(f"Attempting to fetch data for user: {username}")

            user_data = {"comments": [], "posts": []}

            # Scrape comments
            print(f"Fetching comments for {username} (limit={limit})...")
            comment_count = 0
            for comment in redditor.comments.new(limit=limit):
                user_data["comments"].append({
                    "id": comment.id,
                    "text": comment.body,
                    "url": f"https://www.reddit.com{comment.permalink}" # Corrected absolute URL
                })
                
                comment_count += 1
                # print(f"  Fetched comment: {comment.id}") # Uncomment for verbose debugging
            print(f"Finished fetching {comment_count} comments.")


            # Scrape posts (submissions)
            print(f"Fetching posts for {username} (limit={limit})...")
            post_count = 0
            for submission in redditor.submissions.new(limit=limit):
                user_data["posts"].append({
                    "id": submission.id,
                    "text": submission.title + " " + (submission.selftext if submission.selftext else ""),
                    "url": f"https://www.reddit.com{submission.permalink}" # Ensure it's always permalink
                })
                post_count += 1
                # print(f"  Fetched submission: {submission.id}") # Uncomment for verbose debugging
            print(f"Finished fetching {post_count} posts.")

            print("Final user_data collected:")
            print(f"  Comments count: {len(user_data['comments'])}")
            print(f"  Posts count: {len(user_data['posts'])}")

            return user_data
        except Exception as e:
            print(f"Error scraping data for {username}: {e}")
            return {"comments": [], "posts": []}
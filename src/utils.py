import os
from dotenv import load_dotenv

def load_reddit_credentials():
    load_dotenv()
    # print("Loading Reddit credentials from environment variables.")
    # print("client_id:", os.getenv("REDDIT_CLIENT_ID"))
    # print("client_secret:", os.getenv("REDDIT_CLIENT_SECRET"))
    # print("user_agent:", os.getenv("REDDIT_USER_AGENT"))
    return {
        "client_id": os.getenv("REDDIT_CLIENT_ID"),
        "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
        "user_agent": os.getenv("REDDIT_USER_AGENT"),
    }

def clean_text(text):
    """Basic text cleaning for NLP."""
    return text.replace('\n', ' ').strip()
import os

# Gracefully load dotenv if installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Twitter / X Credentials
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY", "")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET", "")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", "")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN", "")

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Database and Post Limits
DB_PATH = os.getenv("DB_PATH", "seen_posts.db")
MAX_POSTS_PER_RUN = int(os.getenv("MAX_POSTS_PER_RUN", "2"))
POST_DELAY_SECONDS = int(os.getenv("POST_DELAY_SECONDS", "10"))

# RSS Feeds for Celebrity, Hollywood, Social Media & Entertainment News
RSS_FEEDS = [
    {
        "name": "Google News Entertainment",
        "url": "https://news.google.com/rss/headlines/section/topic/ENTERTAINMENT?hl=en-US&gl=US&ceid=US:en",
        "category": "Hollywood & Celebrity"
    },
    {
        "name": "TMZ Breaking",
        "url": "https://www.tmz.com/rss.xml",
        "category": "Celebrity News"
    },
    {
        "name": "Variety",
        "url": "https://variety.com/feed/",
        "category": "Hollywood Industry"
    },
    {
        "name": "The Hollywood Reporter",
        "url": "https://www.hollywoodreporter.com/feed/",
        "category": "Hollywood & Movies"
    },
    {
        "name": "People Magazine",
        "url": "https://people.com/feed/",
        "category": "Celebrity & Pop Culture"
    },
    {
        "name": "Deadline",
        "url": "https://deadline.com/feed/",
        "category": "Entertainment & Box Office"
    },
    {
        "name": "Billboard",
        "url": "https://www.billboard.com/feed/",
        "category": "Music & Celebrity"
    }
]

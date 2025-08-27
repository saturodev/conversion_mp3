import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
YOUTUBE_KEY = os.getenv("YOUTUBE_KEY")
YOUTUBE_URL = os.getenv("YOUTUBE_URL")
RAPID_KEY = os.getenv("RAPID_KEY")
RAPID_URL = os.getenv("RAPID_URL")
RAPID_HOST = os.getenv("RAPID_HOST")

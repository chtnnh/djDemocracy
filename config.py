from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    def __init__(self) -> None:
        self.MONGO_HOST = os.getenv("MONGO_HOST")
        self.MONGO_PORT = os.getenv("MONGO_PORT")
        self.MONGO_USERNAME = os.getenv("MONGO_USERNAME")
        self.MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
        self.MONGO_REMOTE_HOST = os.getenv("MONGO_REMOTE_HOST")
        self.YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

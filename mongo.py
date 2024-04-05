from pymongo.mongo_client import MongoClient
from config import Config

config = Config()

uri = f"mongodb+srv://{config.MONGO_USERNAME}:{config.MONGO_PASSWORD}@{config.MONGO_REMOTE_HOST}/?retryWrites=true&w=majority&appName=djDemocracyDev"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

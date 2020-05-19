import os
from dotenv import load_dotenv
from redis_client import RedisClient


class Downloader:

    def __init__():
        load_dotenv()
        print(os.getenv("REDIS_HOST"))
        pass

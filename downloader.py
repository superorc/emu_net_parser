import os
#from dotenv import load_dotenv
from redis_client import RedisClient
#import redis_test
import emu_net


class Downloader:

    def __init__(self, url):
        self.url = url
        self.client = self._update_url()
        #load_dotenv()
        #print(os.getenv("REDIS_HOST"))
        print('!!!')
        #pass:
    
    def _update_url(self):
        self.client = RedisClient()
    

downloader = Downloader("https://url")

#rom = emu_net.get_7zip("5")
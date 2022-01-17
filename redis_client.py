#import asyncio
import aioredis
#import settings
import logging
import os

class RedisClient:

    '''
    def __init__(self, rom_id, url, archive):
        self.rom_id = 0
        self.url = null
        self.archive = null
    '''

    async def main(self, rom_id, url, archive):

        """ Create redis connection """

        try:
            REDIS_URL = "redis://" + os.getenv("REDIS_URL")
            logging.info('Trying connect to %s', REDIS_URL)
            
            redis = await aioredis.create_redis_pool(REDIS_URL)
        except:
            logging.error("Connection to redis at %s failed", os.getenv("REDIS_URL"))
            raise
        
        await redis.set(rom_id, url)

        value = await redis.get(rom_id, encoding='utf-8')
        print(value)

        redis.close()
        await redis.wait_closed()



    #asyncio.run(main(rom_id, url, archive))
    #asyncio.run(main())

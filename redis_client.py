import asyncio
import aioredis
import settings
import logging
import os

class RedisClient:

    async def pub_to_redis(self, file_name):
        pass

    async def get_from_redis(self, file_name):
        pass

    async def main():
        """ Create redis connection """
        try:
            REDIS_URL = "redis://" + os.getenv("REDIS_URL")
            logging.info('Trying connect to %s', REDIS_URL)
            
            redis = await aioredis.create_redis_pool(REDIS_URL)
        except:
            logging.error("Connection to redis at %s failed", os.getenv("REDIS_URL"))
            raise
        
        await redis.set('game_name', 'http://download_url')

        value = await redis.get('game_name', encoding='utf-8')
        print(value)

        redis.close()
        await redis.wait_closed()


    asyncio.run(main())

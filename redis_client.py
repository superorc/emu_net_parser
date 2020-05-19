import asyncio
import aioredis
import settings
import logging
import os

class RedisClient:

    def pub_to_redis(self, file_name):
        pass

    def get_from_redis(self, file_name):
        pass

    async def main():
        """ Create redis connection """
        try:
            #logging.info("Trying connect to %s") % os.getenv("REDIS_URL")
            #print(os.getenv("REDIS_URL"))
            redis = await aioredis.create_redis_pool("redis://%s") % os.getenv("REDIS_URL")
        except:
            logging.error("Connection to redis failed")
            #print("Connection to redis failed")
            raise
        
        await redis.set('my-key', 'value')

        value = await redis.get('my-key', encoding='utf-8')
        print(value)

        redis.close()
        await redis.wait_closed()


    asyncio.run(main())

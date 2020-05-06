import asyncio
import aioredis


class RedisClient:

    def pub_to_redis(self, file_name):
        pass

    def get_from_redis(self, file_name):
        pass

    async def main():
        """ Create redis connection """
        try:
            redis = await aioredis.create_redis_pool('redis://localhost')
        except:
            print("Connection to redis failed")
            raise
        
        await redis.set('my-key', 'value')

        value = await redis.get('my-key', encoding='utf-8')
        print(value)

        redis.close()
        await redis.wait_closed()


    asyncio.run(main())

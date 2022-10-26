from services import redis_storage_db


class RedisStorageFactory():

    @staticmethod
    def clean_storage():
        redis_storage_db.clear()


    @staticmethod
    def set_up_storage(key: str, value: str):
        redis_storage_db[key] = value


    @staticmethod
    def set_up_big_storage():
        redis_storage_db["1"] = "1"
        redis_storage_db["2"] = "2"
        redis_storage_db["3"] = "3"
        redis_storage_db["4"] = "1"

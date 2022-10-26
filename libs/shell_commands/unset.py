import services
from .command import Command


class Unset(Command):

    def execute(self):
        try:
            if(self.key in services.redis_storage_db.keys()):
                del services.redis_storage_db[self.key]
                return ""

            return "Key not found"
        except Exception as ex:
            self.logger.error(message=str(ex))

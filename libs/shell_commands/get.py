import services
from .command import Command


class Get(Command):

    def execute(self) -> str:
        try:
            return services.redis_storage_db.get(self.key, "Key not found")
        except Exception as ex:
            self.logger.error(message=str(ex))

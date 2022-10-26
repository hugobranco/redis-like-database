import services
from .command import Command


class Numequalto(Command):

    def execute(self) -> int:
        try:
            return sum(
                value == self.value_to_search
                for key, value in services.redis_storage_db.items()
            )
        except Exception as ex:
            self.logger.error(message=str(ex))

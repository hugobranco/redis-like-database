import ast
import services
from .command import Command


class Set(Command):

    def execute(self) -> str:
        try:
            return_message = ""
            if(self.key in services.redis_storage_db.keys()):
                return_message = "Key already exists. Key value updated"

            services.redis_storage_db[self.key] = ast.literal_eval(self.value)

            return return_message
        except Exception as ex:
            self.logger.error(message=str(ex))

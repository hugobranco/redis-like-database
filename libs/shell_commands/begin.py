import services
from .command import Command


class Begin(Command):

    def execute(self) -> str:
        if not services.start_transaction:
            services.start_transaction = True
            services.transaction_storage_db = services.redis_storage_db.copy()

        return ""

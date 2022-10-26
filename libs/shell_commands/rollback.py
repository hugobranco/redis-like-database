import services
from .command import Command


class Rollback(Command):

    def execute(self) -> str:
        if(services.start_transaction):
            services.start_transaction = False
            services.redis_storage_db = services.transaction_storage_db.copy()
            services.transaction_storage_db.clear()

        return ""

import services
from .command import Command



class Commit(Command):

    def execute(self) -> str:
        if services.start_transaction:
            services.transaction_storage_db.clear()
            services.start_transaction = False

        return ""

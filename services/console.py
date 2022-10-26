from libs.shell_commands import command_factory
from utils.custom_logger import CustomLogger
from utils import settings


class Console:

    def __init__(self):
        self.logger = CustomLogger(level=settings.LOG_LEVEL, name=__name__)
        self.inserted_commands = []
        self.command = ""
        self.key = ""
        self.value = ""
        self.accepted_commands = ["SET", "GET", "UNSET", "NUMEQUALTO", "END", "BEGIN", "COMMIT", "ROLLBACK"]


    @property
    def allowed_command(self) -> bool:
        return self.command in self.accepted_commands


    @staticmethod
    def print_menu():
        # Added this function just to create a simple menu with the commands available
        print("Please write one command:")
        print("-------------------------")
        print("SET <key> <value>")
        print("GET <key>")
        print("UNSET <key>")
        print("NUMEQUALTO <value>")
        print("BEGIN => (begin transaction)")
        print("COMMIT => (commit transaction)")
        print("ROLLBACK => (rollback transaction)")
        print("END => (end application)")


    def run(self):
        while (self.command != "END"):
            self.print_menu()
            self.get_shell_inserted_command(input())

            if self.allowed_command:
                print(f"{self.execute_command()}\n")
            else:
                print("error")


    def get_shell_inserted_command(self, inserted_command: str):
        try:
            if(" " in inserted_command):
                aux = inserted_command.split(" ")
                self.command = aux[0]
                self.key = aux[1]
                self.value = " ".join(aux[2:])
            else:
                self.command = inserted_command
        except Exception as ex:
            self.command = ""
            self.key = ""
            self.value = ""
            self.logger.error(message=str(ex))


    def execute_command(self) -> str:
        if(self.command != "END"):
            command = command_factory(inserted_command=self.command, key=self.key, value=self.value)
            return command.execute()

        return ""

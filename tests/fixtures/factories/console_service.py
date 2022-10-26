from services.console import Console


class ConsoleServiceFactory():

    @staticmethod
    def set_up_console(command: str, key: str, value: str) -> Console:
        console = Console()
        console.command = command
        console.key = key
        console.value = value

        return console



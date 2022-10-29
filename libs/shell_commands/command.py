from utils import settings
from utils.custom_logger import CustomLogger


class Command():

    def __init__(self, key: str, value: str):
        self.logger = CustomLogger(level=settings.LOG_LEVEL, name=__name__)
        self.key = key
        self.value = value
        self.value_to_search = key


    def execute(self) -> str:
        return "error"

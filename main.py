from services.console import Console
from utils import settings
from utils.custom_logger import CustomLogger


class Main():

    def __init__(self):
        self.logger = CustomLogger(level=settings.LOG_LEVEL, name=__name__)
        self.logger.info(message='### APPLICATION START ###')
        self.logger.info(
            message=f"LOG_LEVEL = {settings.LOG_LEVEL}"
        )
        self.logger.info(message=f"ENVIRONMENT = {settings.ENVIRONMENT}")


    def init_app(self):
        self.logger.info(message="Application console started")
        Console().run()


if __name__ == '__main__':
    Main().init_app()


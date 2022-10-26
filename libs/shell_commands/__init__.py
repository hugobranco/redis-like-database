from enum import Enum

from utils import settings
from utils.custom_logger import CustomLogger
from .begin import Begin
from .command import Command
from .commit import Commit
from .get import Get
from .rollback import Rollback
from .set import Set
from .unset import Unset
from .numequalto import Numequalto


logger = CustomLogger(level=settings.LOG_LEVEL, name=__name__)


def command_factory(inserted_command: str, key: str, value: object) -> Command:
    try:
        return Commands[inserted_command].value(key=key, value=value)
    except KeyError as ex:
        logger.error(message=str(ex))
        return Command(key=key, value=value)


class Commands(Enum):
    GET = Get
    SET = Set
    UNSET = Unset
    NUMEQUALTO = Numequalto
    BEGIN = Begin
    COMMIT = Commit
    ROLLBACK = Rollback
    END = None

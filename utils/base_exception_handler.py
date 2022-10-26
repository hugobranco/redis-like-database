import sys
import traceback

from utils.cfg_reader import CfgReader
from utils.custom_logger import CustomLogger



class BaseExceptionHandler(Exception):

    def __init__(self, error_msg: str):
        self.logger = CustomLogger(level=CfgReader.APPLICATION_BASIC_LOG_LEVEL, name=__name__)
        self._error_message = ''
        self.__build_error_message(error_message=error_msg)

        # log error message
        self.logger.error(message=self.error_message)



    @property
    def error_message(self) -> str:
        return self._error_message



    @error_message.setter
    def error_message(self, new_error_message: str):
        self._error_message = new_error_message or ''



    def __build_error_message(self, error_message: str):
        """
            build error message and set to error_message instance attribute

            :param class_name:
                class name where the exception occurred
            :param def_name:
                function name where the exception occurred
            :param error_message:
                exception message
        """
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        self.error_message = f"\n\t\t\t\t\t\t\t\t\tFile : {trace_back[0][0]}\n" \
                             f"\t\t\t\t\t\t\t\t\tLine Number : {trace_back[0][1]}\n" \
                             f"\t\t\t\t\t\t\t\t\tFunc.Name : {trace_back[0][2]}()\n" \
                             f"\t\t\t\t\t\t\t\t\tException type : {ex_type.__name__} \n" \
                             f"\t\t\t\t\t\t\t\t\tException Message : {error_message}\n\t\t\t\t\t\t\t\t "



    @staticmethod
    def log_error(exception_message: str):
        """
        Creates and reports a Error Exception
        :param exception_message: Original exception message
        :return: a BaseExceptionHandler object
        """
        return BaseExceptionHandler(error_msg=exception_message)

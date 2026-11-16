import sys
import logging

def err_msg_details(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error message including file name, line number and the error message.

    :param error: The exception that occurred.
    :param error_detail: The sys module to trackback details.
    :return: A formatted error message.
    """

    # Extracts trackback details (exception information)
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in Python script; {file_name} At line number: {line_number}"

    logging.error(error_message)
    return error_message

class MyException(Exception):
    """
    Custom exception class for handling errors in the USvisa application.
    """
    def __init__(self, error_message: str, error_detail: sys) -> None:
        """
        Initializes the US visa Exception with detailed error message.

        :param error_message: A string describing the error.
        :param error_detail: The sys module to trackback details.
        """
        super().__init__(error_message)
        self.error_message = err_msg_details(error=error_message, error_detail=error_detail)

    def __str__(self) ->str:
        """
        Return a string describing the exception.
        """
        return self.error_message
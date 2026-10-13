import sys
from types import ModuleType
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:ModuleType):
        super().__init__(error_message)
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        # exc_tb is None when raised outside an except block
        self.lineno=exc_tb.tb_lineno if exc_tb else None
        self.file_name=exc_tb.tb_frame.f_code.co_filename if exc_tb else None

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))

if __name__=='__main__':
    try:
        logger.logging.info("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
           raise NetworkSecurityException(e,sys)

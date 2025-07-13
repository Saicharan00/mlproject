# import sys
# import logging
# print("🔥 This is the exception.py script 🔥")

# print("Script started")


# def error_message_detail(error, error_detail:sys):
#     _,_,exc_tb = error_detail.exc_info()
#     file_name = exc_tb.tb_frame.f_code.co_filename

#     error_message = "error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
#     file_name, exc_tb.tb_lineno,str(error)
#     )
#     return error_message
    

# class CustomException(Exception):
#     def __init__(self, error_message, error_detail:sys):
#         super().__init__(error_message)
#         self.error_message = error_message_detail(error_message, error_detail = error_detail)

#     def __str__(self):
#         return self.error_message


# if __name__ == '__main__':
#     print("Exception module is working")
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by zero error")
#         raise CustomException(e, sys)

import sys
from src.logger import logging

print("🔥 This is the exception.py script 🔥")

def error_message_detail(error, error_detail: sys):
    try:
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_no = exc_tb.tb_lineno
        err_str = str(error)
        return f"Error in [{file_name}] at line [{line_no}]: {err_str}"
    except Exception as e:
        print("⚠️ error_message_detail failed:", e)
        return "error_message_detail failed"

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message



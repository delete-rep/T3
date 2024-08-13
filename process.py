"""where core functions start"""
from globals import PRIMARY_KEY_WORD_MAPPING
from core import Core

def _get_user_input():
    return input("enter input: ")
if __name__ == "__main__":
    user_input  = _get_user_input()
    core = Core(layout = None)
    core.process(user_input= user_input)
     
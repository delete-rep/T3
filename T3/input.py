"""stores and parses the input string

"""
import time
from globals import TIMESTAMPS,NOTE_TYPES
class Input():
    def __init__(self) -> None:
        self.default_input = None
        self.string = ""
        self.list = []

    def update_list(self):
        self.list = self.string.split(" ")
 

    def extract_note_type(self):
        """
        Returns:
            _word (str): type of note referenced in the string 
        """
        for _word in self.list:
            if _word in NOTE_TYPES:
                self.list.remove(_word)
                return _word

"""Handles all time related functions and events in the code 
the global timeformat  : "%B %d %Y %h %H:%M:%S")

"""

from globals import TIMESTAMPS ,MONTHS
import time
class Clock:
    @classmethod
    def current_time(cls):
        time_object  = time.localtime()
        return cls.time_as_string(time_object)


    
    @classmethod
    def time_as_string(cls,time_object :time.struct_time):
        return  time.strftime("%H:%M:%S %d %h %Y ",time_object)

    def  extract_note_time(self):
        """_summary_

        Args:
            input_list (list): _description_
        """
        time = None
        for word in self.list:
            if word[0] == "@":
                if word[1:] in TIMESTAMPS:
                    
                    self.generate_timestamp(word[1:])
                elif word[1:] in MONTHS:
                    self.generate_timestamp(MONTHS[word[1:]])
                    pass
                else:
                    pass
                

            else:
                pass
            if word[2] == ":":
                if word[:2].isdigit and word[2:].isdigit(): 
                    hour = int(word[:2])
                    minute = int(word[2:])
            
    def time_as_string(self,time_object :time.struct_time):
        return  time.strftime("%B %d %Y %h %H:%M:%S",time_object)

    def generate_timestamp(self,tag:str):
        """_summary_

        Args:
            tag (str): _description_

        Returns:
            _type_: _description_
        """
        time_object = time.localtime()
        timestamp :str =  None
        match tag:
            case "now":
                timestamp = self.time_as_string(time_object)
            case "tommorrow":
                time_object.tm_mday += 1
                timestamp = self.time_as_string(time_object)
            case "yesterday":
                time_object.tm_mday -=1 
                timestamp =self.time_as_string(time_object)
            case "today":
                timestamp =self.time_as_string(time_object)
            case _:
                pass
        return timestamp  
        
   
    def extract_note_parent(self):
        return 0
    def extract_note_deadline(self):
        return 0

"""_summary_

Returns:
    _type_: _description_
"""
from file_handler import append_yaml_file,get_yaml_data
from globals import NOTE_TYPES,TIMESTAMPS
from note import Note
from rich.layout import Layout

import time

def extract_note_type(input_list:list):
    """_summary_

    Args:
        input_list (list): _description_

    Returns:
        _type_: _description_
    """
    for _word in input_list:
        if _word in NOTE_TYPES:
            input_list.remove(_word)
            return _word
def time_as_string(time_object :time.struct_time):
    return  time.strftime("%B %d %Y %h %H:%M:%S",time_object)
def generate_timestamp(tag:str):
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
            timestamp = time_as_string(time_object)
        case "tommorrow":
            time_object.tm_mday += 1
            timestamp = time_as_string(time_object)
        case "yesterday":
            time_object.tm_mday -=1 
            timestamp = time_as_string(time_object)
        case "today":
            timestamp = time_as_string(time_object)
        case _:
            pass
    return timestamp  
    
def  _extract_note_time(input_list:list):
    """_summary_

    Args:
        input_list (list): _description_
    """
    time = None
    for word in input_list:
        if word[0] == "@":
            if word[1:].isdigit():
                pass
        elif word[1:] in TIMESTAMPS:
            generate_timestamp(word[1:0])
        else:
            pass
def extract_note_parent(input_list):
    return 0
def extract_note_deadline(input_list):
    return 0

def create(input_list:list):
    """_summary_

    Args:
        input_list (list): _description_
    """
    note_type = extract_note_type(input_list)
    note_content = " ".join(input_list)
    note_deadline = extract_note_deadline(input_list)
    note_parent = extract_note_parent(input_list)
    note = Note(type=note_type,content=note_content,deadline = note_deadline)

    
    append_yaml_file(note)

def show(input_list:list,layout:Layout = None):
    """_summary_

    Args:
        input_list (list): _description_
        layout (Layout, optional): _description_. Defaults to None.
    """
    if layout ==  None:
        print("layout not specified")
    time_scale = extract_note_deadline(input_list)
    note_type = extract_note_type(input_list=input_list)   
    notes:list = get_yaml_data()
    notes  = [note for note in notes if note["type"] == note_type]



def delete(user_input:list):
    """_summary_

    Args:
        user_input (list): _description_
    """
    pass


""""""
from note import Note
import yaml

def write_to_save(note):
    pass
def load_from_save():
    pass
def encrypt_save():
    pass
def append_yaml_file(note:Note):
    """_summary_

    Args:
        note (Note): _description_
    """
    data_to_append = vars(note) 
    file_path = "saves.yaml"

    with open(file_path, 'a+') as file:
        existing_data = yaml.load(file, Loader=yaml.FullLoader) or []
        existing_data.append(data_to_append)
        yaml.dump(existing_data, file, default_flow_style=False)

def get_yaml_data()->list:
    """_summary_

    Returns:
        list: _description_
    """
    data = None
    with open("saves.yaml", 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data

def get_config_data()->list:
    """_summary_

    Returns:
        list: _description_
    """
    data = None
    with open("config.yaml", 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data
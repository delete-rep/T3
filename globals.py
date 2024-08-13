from primary_functions import show,create,delete
from file_handler import get_config_data

PRIMARY_KEY_WORD_MAPPING ={
    "show":show,
    "del":delete,
    "delete":delete,
    "add":create,
    "display":show,
    "+":create,
    "-":delete
}

TIMESTAMPS = ["today","tommorrow","yesterday","now"]

NOTE_TYPES = ["task","entry","journal","project","sprint","bank","alarm"]

YAML_FILE_PATH  = "save.yaml"

CONFIG = get_config_data()
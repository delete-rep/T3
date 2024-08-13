"""_summary_

Returns:
    _type_: _description_
"""
from rich.layout import Layout
from globals import PRIMARY_KEY_WORD_MAPPING , NOTE_TYPES
SUGGESTIONS= {
"add" : "function: [grey]ADD[grey] \n this is a function used to add other note types",
"delete ": "used to delete other notes and take a variety of notes"

}

class Core():
    """_summary_
    """
    def __init__(self,layout:Layout) -> None:
        """_summary_

        Args:
            layout (Layout): _description_
        """
        self.text= ""
        self.layout = layout
        self.formated_text = ""
        self.suggestion = ""
        self.running = True

    def save_key(self,key):
        """_summary_

        Args:
            key (_type_): _description_
        """
        input_string :str= str(key)
        input_string = input_string.replace("'","")
        match input_string:

            case "Key.space":
                input_string = " "

            case "Key.backspace":
                input_string = ""
                self.text =  self.text[:-2]

            case "Key.enter":
                self.process(user_input=self.text,layout=self.layout)
                self.text = ""

            case _:
                pass

        if len(input_string) <2:
            self.text += input_string
            self.format_text()
            self.edit_suggestion()

    def contains_primary_key(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        for i in self.text.split():
            if i in PRIMARY_KEY_WORD_MAPPING:
                return True
        return False
    
    def edit_suggestion(self):
        """_summary_
        """
        if len(self.text )< 1:
            self.suggestion = "[#363838] primary commands inlucde [A D D] [#363838]"
        if  not self.contains_primary_key():
            arr = self.text.split(" ")
            matching_words = [word for word in PRIMARY_KEY_WORD_MAPPING if word.startswith(arr[-1])]
            if matching_words:
                if matching_words[0] in SUGGESTIONS:
                    self.suggestion = SUGGESTIONS[matching_words[0]]

    def format_text(self):
        """_summary_
        """
        string_list =self.text.split(" ")
        for index ,i in enumerate(string_list):
            if i in PRIMARY_KEY_WORD_MAPPING:
                string_list[index] = "[code ] "  + i.upper() + " [/code]"
            if i in NOTE_TYPES:
                string_list[index] = "[blue] "  + i + " [/blue]"
        self.formated_text = " ".join(string_list)

    def process(self,layout : Layout = None ,user_input:str= ""):
        """_summary_

        Args:
            layout (Layout, optional): _description_. Defaults to None.
            user_input (str, optional): _description_. Defaults to "".
        """


        string_list : list= user_input.split(" ")
        
        for word in (string_list[:2]):
            if  word in PRIMARY_KEY_WORD_MAPPING:
                function : callable = PRIMARY_KEY_WORD_MAPPING[word]
                string_list.remove(word)
                function(layout = layout,input_list = string_list)

            
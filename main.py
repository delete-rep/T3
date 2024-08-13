import queue
import time
from pynput.keyboard  import Listener
from rich.live import Live
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel
from rich.padding import Padding
from rich.console import Console,Group


from core import Core
from globals import CONFIG
console = Console()

def make_layout() -> Layout:

    layout = Layout(name="root") 
    layout.split(
        Layout(name = "header",size =2),
        Layout(name="main", size = 3),
        Layout(name = "suggestion",size=3),
        Padding("boo",500),
        Layout(name="footer", size=2),
    )

    return layout


layout = make_layout()
core = Core(layout= layout)


layout["header"].update("[u]Terminal #[u]")


#listens for keyboard presses and 
with Listener(on_press= core.save_key) as L:

    with Live(layout, refresh_per_second=CONFIG["refresh_per_second"]):  # update 4 times a second to feel fluid
        #while the app hase not been terminated
        while core.running:
            layout["main"].update(Padding(Panel(core.formated_text),pad =(0,20)))
            layout["suggestion"].update(Padding(core.suggestion,pad =(0,20),expand=True))

    L.join()
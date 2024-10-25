import customtkinter as ctk
from pathlib import Path
#from PIL import Image
import pyglet
from frame_00 import Menu

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


pyglet.font.add_file("assets/Italiana.ttf")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._set_appearance_mode("Dark")
        self.geometry("700x450")
        self.title("calc")
        #self.iconbitmap(relative_to_assets("icon.ico"))
        self.resizable(False, False)

        self.frame = Menu(self)
        self.frame.grid(row=0, column=0)


# app = App()
#
# profiler = cProfile.Profile()
# profiler.enable()
#
# result =  app.mainloop()
#
# profiler.print_stats()
#

app = App() 
app.mainloop()
 


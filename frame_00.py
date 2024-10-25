import customtkinter as ctk
import pyglet
from PIL import Image
from pathlib import Path
from frame_01 import Frame1
from frame_02 import Frame2
from frame_03 import Frame3

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


pyglet.font.add_file("assets/Italiana.ttf")


class Menu(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.frame = Frame1(master = self)
        self.frame = Frame2(master = self)
        self.frame = Frame3(master = self)
        
        self.create_title()
        self.create_bg()
        self.create_button(
            "single.png", 200, 40, "#1F1E1E", 16, 103, self.change_to_Frame1
        )
        self.create_button(
            "double.png", 200, 40, "#1F1E1E", 16, 156, self.change_to_Frame2
        )
        self.create_button(
            "triple.png", 200, 40, "#1F1E1E", 16, 209, self.change_to_Frame3
        )

    def create_button(
        self,
        B_name: str,
        Width: int,
        Height: int,
        Color: str,
        x_pos: int,
        y_pos: int,
        change_frame,
    ):
        CR = 16
        img = Image.open(relative_to_assets(f"{B_name}"))
        image = ctk.CTkImage(light_image=img, size=(Width, Height))
        button = ctk.CTkButton(
            self,
            image=image,
            fg_color=Color,
            text="",
            corner_radius=CR,
            hover_color=Color,
            bg_color=Color,
            command=change_frame,
        )
        button.place(x=x_pos, y=y_pos)

    def create_bg(self):
        # Background image
        bg_image = Image.open(relative_to_assets("bg.png"))
        img_1 = ctk.CTkImage(light_image=bg_image, size=(700, 450))
        bg_label = ctk.CTkLabel(self, image=img_1, text="")
        bg_label.grid(row=0, column=0)

    # Title  -- 'Integeral calculator'
    def create_title(self):
        Title_1 = ctk.CTkLabel(
            self,
            text="Integral calculator",
            font=("Italiana", 35),
            text_color="#FFFFFF",
            bg_color="#1F1E1E",
            corner_radius=16,
        )

        Title_1.place(x=200, y=0)

    def change_to_Frame1(self):
        self.frame = Frame1(master=self)
        self.frame.grid(row=0, column=0)

    def change_to_Frame2(self):
        self.frame = Frame2(master=self)
        self.frame.grid(row=0, column=0)

    def change_to_Frame3(self):
        self.frame = Frame3(master=self)
        self.frame.grid(row=0, column=0)

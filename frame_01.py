from tkinter import END
import customtkinter as ctk
from Integrals_m.single import Integrand
from PIL import Image
from pathlib import Path
import pyglet


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


pyglet.font.add_file("assets/Italiana.ttf")


# Root Window
class Frame1(ctk.CTkFrame):
    def create_entry(self, text: str):
        Fg_color = "white"
        color = "#1F1E1E"
        Width = 170
        CR = 16
        txt_color = "#5A5A5A"
        return ctk.CTkEntry(
            self,
            fg_color=Fg_color,
            bg_color=color,
            width=Width,
            corner_radius=CR,
            placeholder_text=text,
            placeholder_text_color=color,
        )

        pass

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        A = self.create_entry("Enter The Funtion")

        def clear(enc_function, enc_Variable, enc_lower_limit, enc_upper_limit):

            enc_function.delete(0, END)
            enc_Variable.delete(0, END)
            enc_lower_limit.delete(0, END)
            enc_upper_limit.delete(0, END)

        def Output(func, lower_limit, upper_limit, result):
            function.configure(text=func)
            lower_l.configure(text=lower_limit)
            upper_l.configure(text=upper_limit)
            Answer.configure(text=result)

            out_function_txt.configure(text="Function :")
            out_lower_limit_txt.configure(text="Lower Limit :")
            out_upper_limit_txt.configure(text="Upper_limit :")
            out_result_txt.configure(text="result :")
            clear(enc_function, enc_Variable, enc_lower_limit, enc_upper_limit)

        def work():
            func = enc_function.get()
            var = enc_Variable.get()
            lower_limit = enc_lower_limit.get()
            upper_limit = enc_upper_limit.get()
            result = Integrand(func, var, lower_limit, upper_limit)
            Output(func, lower_limit, upper_limit, result)

        def delete_Frame():
            self.destroy()

        # BackGround Image
        Img = Image.open(relative_to_assets("bg.png"))
        img_1 = ctk.CTkImage(light_image=Img, size=(700, 450))
        img_1_label = ctk.CTkLabel(self, image=img_1, text="")
        img_1_label.grid(row=0, column=0)

        # Title  -- 'Integeral calculator'
        Title_1 = ctk.CTkLabel(
            self,
            text="Integral calculator",
            font=("Italiana", 35),
            text_color="#FFFFFF",
            bg_color="#1F1E1E",
            corner_radius=16,
        )

        Title_1.place(x=200, y=0)

        # Enter function
        enc_function = ctk.CTkEntry(
            self,
            fg_color="white",
            bg_color="#1F1E1E",
            width=170,
            corner_radius=16,
            placeholder_text="Enter The Funtion",
            placeholder_text_color="#5A5A5A",
            text_color="#5A5A5A",
        )
        enc_function.place(x=15, y=135)

        # Enter Variable
        enc_Variable = ctk.CTkEntry(
            self,
            fg_color="white",
            bg_color="#1F1E1E",
            width=170,
            corner_radius=16,
            placeholder_text="Enter Varible",
            placeholder_text_color="#5A5A5A",
            text_color="#5A5A5A",
        )
        enc_Variable.place(x=15, y=172)
        A.place(x=65, y=172)
        # Enter Lower Limit
        enc_lower_limit = ctk.CTkEntry(
            self,
            fg_color="white",
            bg_color="#1F1E1E",
            width=170,
            corner_radius=16,
            placeholder_text="Enter Lower Limit",
            placeholder_text_color="#5A5A5A",
            text_color="#5A5A5A",
        )
        enc_lower_limit.place(x=15, y=206)

        # Enter Upper Limit
        enc_upper_limit = ctk.CTkEntry(
            self,
            fg_color="white",
            bg_color="#1F1E1E",
            width=170,
            corner_radius=16,
            placeholder_text="Enter Upper Limit",
            placeholder_text_color="#5A5A5A",
            text_color="#5A5A5A",
        )
        enc_upper_limit.place(x=15, y=239)

        # Output Text
        function = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        function.place(x=532, y=109)

        lower_l = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        lower_l.place(x=532, y=145)

        upper_l = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        upper_l.place(x=532, y=181)
        Answer = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        Answer.place(x=532, y=214)

        out_function_txt = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        out_function_txt.place(x=407, y=109)

        out_lower_limit_txt = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        out_lower_limit_txt.place(x=407, y=145)

        out_upper_limit_txt = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        out_upper_limit_txt.place(x=407, y=181)

        out_result_txt = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        out_result_txt.place(x=407, y=214)

        # Calcuate Button
        calcuate_image = Image.open(relative_to_assets("calculate.png"))
        buttonimg = ctk.CTkImage(light_image=calcuate_image, size=(350, 30))
        button = ctk.CTkButton(
            self,
            text="",
            fg_color="#1F1E1E",
            corner_radius=16,
            image=buttonimg,
            command=work,
            hover_color="#1F1E1E",
            bg_color="#1F1E1E",
        )
        button.place(x=150, y=340)

        back_image = Image.open(relative_to_assets("back.png"))
        back_buttonimg = ctk.CTkImage(light_image=back_image, size=(350, 30))
        back_button = ctk.CTkButton(
            self,
            text="",
            fg_color="#1F1E1E",
            corner_radius=16,
            image=back_buttonimg,
            command=delete_Frame,
            hover_color="#1F1E1E",
            bg_color="#1F1E1E",
        )
        back_button.place(x=150, y=380)

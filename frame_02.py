from tkinter import END
import customtkinter as ctk
from Integrals_m.double import Integrand
from PIL import Image
from pathlib import Path
import pyglet


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


pyglet.font.add_file("assets/Italiana.ttf")


class Frame2(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def clear(
            enc_function,
            enc_inner_Variable,
            enc_outer_Variable,
            enc_inner_ll,
            enc_inner_ul,
            enc_outer_ll,
            enc_outer_ul,
        ):
            enc_function.delete(0, END)
            enc_inner_Variable.delete(0, END)
            enc_outer_Variable.delete(0, END)
            enc_inner_ll.delete(0, END)
            enc_inner_ul.delete(0, END)
            enc_outer_ll.delete(0, END)
            enc_outer_ul.delete(0, END)

        def Output(func, var_1, var_2, inner_ll, inner_ul, outer_ll, outer_ul, result):
            function.configure(text=func)
            inner_variable.configure(text=var_1)
            outer_variable.configure(text=var_2)
            inner_lower_l.configure(text=inner_ll)
            inner_upper_l.configure(text=inner_ul)
            outer_lower_l.configure(text=outer_ll)
            outer_upper_l.configure(text=outer_ul)
            Answer.configure(text=result)

            out_function_txt.configure(text="Function :")
            out_inner_variable_txt.configure(text="Inner Variable :")
            out_outer_variable_txt.configure(text="Outer Variable :")
            out_inner_ll_txt.configure(text="Inner Lower Limit :")
            out_inner_ul_txt.configure(text="Inner Upper Limit :")
            out_outer_ll_txt.configure(text="Outer Lower Limit :")
            out_outer_ul_txt.configure(text="Outer Upper Limit :")

            out_result_txt.configure(text="result :")
            clear(
                enc_function,
                enc_inner_Variable,
                enc_outer_Variable,
                enc_inner_ll,
                enc_inner_ul,
                enc_outer_ll,
                enc_outer_ul,
            )

        def work():
            func = enc_function.get()
            var_1 = enc_inner_Variable.get()
            var_2 = enc_outer_Variable.get()
            inner_ll = enc_inner_ll.get()
            inner_ul = enc_inner_ul.get()
            outer_ll = enc_outer_ll.get()
            outer_ul = enc_outer_ul.get()
            result = Integrand(
                func, var_1, var_2, inner_ll, inner_ul, outer_ll, outer_ul
            )
            Output(func, var_1, var_2, inner_ll, inner_ul, outer_ll, outer_ul, result)

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

        # Enter function from the user interface
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
        enc_function.place(x=15, y=100)

        # Enter Inner Varible from the user interface
        enc_inner_Variable = ctk.CTkEntry(
            self,
            fg_color="white",
            bg_color="#1F1E1E",
            width=170,
            corner_radius=16,
            placeholder_text="Enter Varible",
            placeholder_text_color="#5A5A5A",
            text_color="#5A5A5A",
        )
        enc_inner_Variable.place(x=15, y=135)

        # Enter Outer Varible from the user interface
        enc_outer_Variable = ctk.CTkEntry(
            self,
            fg_color="white",
            bg_color="#1F1E1E",
            width=170,
            corner_radius=16,
            placeholder_text="Enter Varible",
            placeholder_text_color="#5A5A5A",
            text_color="#5A5A5A",
        )
        enc_outer_Variable.place(x=15, y=170)

        # Enter  inner Lower Limit
        enc_inner_ll = ctk.CTkEntry(
            self,
            fg_color="white",
            bg_color="#1F1E1E",
            width=170,
            corner_radius=16,
            placeholder_text="Enter Inner Lower Limit ",
            placeholder_text_color="#5A5A5A",
            text_color="#5A5A5A",
        )
        enc_inner_ll.place(x=15, y=205)

        # Enter inner Upper Limit
        enc_inner_ul = ctk.CTkEntry(
            self,
            fg_color="white",
            bg_color="#1F1E1E",
            width=170,
            corner_radius=16,
            placeholder_text="Enter Inner Upper Limit",
            placeholder_text_color="#5A5A5A",
            text_color="#5A5A5A",
        )
        enc_inner_ul.place(x=15, y=240)

        # Enter  outer Lower Limit
        enc_outer_ll = ctk.CTkEntry(
            self,
            fg_color="white",
            bg_color="#1F1E1E",
            width=170,
            corner_radius=16,
            placeholder_text="Enter Inner Lower Limit ",
            placeholder_text_color="#5A5A5A",
            text_color="#5A5A5A",
        )
        enc_outer_ll.place(x=15, y=275)

        # Enter outer Upper Limit
        enc_outer_ul = ctk.CTkEntry(
            self,
            fg_color="white",
            bg_color="#1F1E1E",
            width=170,
            corner_radius=16,
            placeholder_text="Enter Inner Upper Limit",
            placeholder_text_color="#5A5A5A",
            text_color="#5A5A5A",
        )
        enc_outer_ul.place(x=15, y=310)

        # Output Text
        function = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        function.place(x=470, y=100)

        inner_variable = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        inner_variable.place(x=470, y=125)

        outer_variable = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        outer_variable.place(x=470, y=150)

        inner_lower_l = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        inner_lower_l.place(x=470, y=175)

        inner_upper_l = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        inner_upper_l.place(x=470, y=200)

        outer_lower_l = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        outer_lower_l.place(x=470, y=225)

        outer_upper_l = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        outer_upper_l.place(x=470, y=250)

        Answer = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        Answer.place(x=470, y=275)

        # Outfunction Text

        out_function_txt = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        out_function_txt.place(x=300, y=100)

        out_inner_variable_txt = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        out_inner_variable_txt.place(x=300, y=125)

        out_outer_variable_txt = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        out_outer_variable_txt.place(x=300, y=150)

        out_inner_ll_txt = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        out_inner_ll_txt.place(x=300, y=175)

        out_inner_ul_txt = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        out_inner_ul_txt.place(x=300, y=200)

        out_outer_ll_txt = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        out_outer_ll_txt.place(x=300, y=225)

        out_outer_ul_txt = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        out_outer_ul_txt.place(x=300, y=250)

        out_result_txt = ctk.CTkLabel(
            self,
            text="",
            bg_color="#1F1E1E",
            text_color="#FFFFFF",
            font=("Italiana", 12),
        )
        out_result_txt.place(x=300, y=275)

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

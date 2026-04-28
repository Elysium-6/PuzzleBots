from pathlib import Path
from PIL import Image

import customtkinter as ctk

from wordle.wolly import Wolly


class wolly_page(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent, fg_color="#545454")
        self.controller = controller

        self.set_content()

        self.wolly_bot = Wolly()

    def set_content(self):
        title_label = ctk.CTkLabel(master=self, text="Wolly the Blaa-blin Genius", font=("Comic Sans MS", 40), text_color="white")
        title_label.pack(pady=5)

        wolly_avatar = ctk.CTkImage(light_image=Image.open("C:\\Users\\razer\\Documents\\Projects\\PuzzleBots\\PuzzleBots\\user_interface\\frames\\avatars\\wolly_avatar.png"), size=(300, 300))
        wolly_avatar_container = ctk.CTkLabel(master=self, image=wolly_avatar, text="")
        wolly_avatar_container.pack(pady=5)

        solve_button = ctk.CTkButton(master=self, text="Solve", font=("Comic Sans MS", 25), text_color="white", command=self.solve_wordle, width=100, height=50, fg_color="green", hover_color="dark green")
        solve_button.pack(pady=5)

        self.answer_label = ctk.CTkLabel(master=self, text="", font=("Helvetica",20))

        back_button = ctk.CTkButton(master=self, text="Back", font=("Comic Sans MS", 20), text_color="white", command=self.back, width=80, height=40, fg_color="grey", hover_color="light grey")
        back_button.pack(pady=10)

    def solve_wordle(self):
        self.answer_label.configure(text=f"The answer is {self.wolly_bot.solve_wordle()}")
        self.answer_label.pack(pady=5)

    def back(self):
        self.controller.show_frame("main_menu")
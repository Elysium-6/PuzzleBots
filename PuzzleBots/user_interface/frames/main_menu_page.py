import customtkinter as ctk

from user_interface.frames.wolly_page import wolly_page


class main_menu_page(ctk.CTkFrame):

    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent, fg_color="#545454")
        self.controller = controller

        self.set_content()

    def set_content(self):
        title_label = ctk.CTkLabel(master=self, text="The Tinker Noggins", font=("Comic Sans MS", 50), text_color="white")
        title_label.pack(pady=30)

        row1_container = ctk.CTkFrame(master=self, fg_color="transparent")
        row1_container.pack()

        wordle_button = ctk.CTkButton(master=row1_container, text="Wolly", font=("Comic Sans MS", 20), text_color="white", command=self.to_wordle_frame, width=100, height=40, fg_color="green", hover_color="dark green")
        wordle_button.pack(side="left", padx=10)

        zip_button = ctk.CTkButton(master=row1_container, text="Zac", font=("Comic Sans MS", 20), text_color="white", command=self.to_wordle_frame, width=100, height=40, fg_color="cyan", hover_color="light blue")
        zip_button.pack(side="left", padx=10)

    def to_wordle_frame(self):
        self.controller.show_frame("wolly")

    def to_zip_frame(self):
        pass
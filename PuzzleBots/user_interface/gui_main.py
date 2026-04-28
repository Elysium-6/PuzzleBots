#Main Controller of GUI
import tkinter as tk
import customtkinter as ctk

from user_interface.frames.main_menu_page import main_menu_page
from user_interface.frames.wolly_page import wolly_page

GUI_FRAMES = {"main_menu" : main_menu_page, "wolly" : wolly_page}

class GUI(ctk.CTk):

    def __init__(self, *args, **kwargs):
        ##Initiates Window
        print("Creating Window:")
        ctk.CTk.__init__(self, *args, **kwargs, fg_color="#545454")
        self.current_session = None
        self.title("Puzzle Bots")
        self.geometry("1280x720")
        self.resizable(False, False)

        print("Creating Container:")
        container = ctk.CTkFrame(master=self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        ##Frame/Scene Manager
        self.frames = {}
        for name, FRAME in GUI_FRAMES.items():
            print("Creating Frame: {}".format(FRAME))
            frame = FRAME(container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("main_menu")

        ##Session Info
        self.session = None

        #Game Loop/Controller
        self.game_loop = None

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_session_user(self):
        return self.current_session

gui = GUI()
gui.mainloop()
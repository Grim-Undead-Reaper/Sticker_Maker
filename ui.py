import customtkinter as ctk
from backend import FileHandler
from tkinterdnd2 import TkinterDnD, DND_FILES

filehandler = FileHandler()

class App(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self):
        super().__init__()

        TkinterDnD.require(self)

        self.geometry("600x500")
        self.title("MySticker")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.center_frame = ctk.CTkFrame(self)
        self.center_frame.grid(row=1, column=1)

        self.drop_frame = ctk.CTkFrame(self.center_frame, fg_color="gray")
        self.drop_frame.pack(pady=20)

        self.drop_frame.drop_target_register(DND_FILES)
        self.drop_frame.dnd_bind("<<Drop>>", self.on_drop)

        self.pick_file = ctk.CTkButton(self.center_frame, text="Hello, world!", command=filehandler.SearchFile)
        self.pick_file.pack(pady=20)

    def on_drop(self, event):
        files = self.tk.splitlist(event.data)
        print(f"Filepath: {files[0]}")

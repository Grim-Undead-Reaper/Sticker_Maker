import customtkinter as ctk
from backend import FileHandler
from tkinterdnd2 import TkinterDnD, DND_FILES

filehandler = FileHandler()

class App(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self):
        super().__init__()

        TkinterDnD.require(self)

        self.geometry("700x600")
        self.title("MySticker")
        self.configure(fg_color="black")

        self.CreateWidgets()

    def on_drop(self, event):
        files = self.tk.splitlist(event.data)
        filehandler.GetFilename(files[0])

    def CreateWidgets(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.center_frame = ctk.CTkFrame(self, width=675, height=575, fg_color="black")
        self.center_frame.grid(row=1, column=1)

        self.image_preview = ctk.CTkFrame(self.center_frame, width=75, height=75, fg_color="gray")
        self.image_preview.pack()

        self.drop_frame = ctk.CTkFrame(self.center_frame, fg_color="gray", border_color="white", border_width=3, corner_radius=15)
        self.drop_frame.pack(pady=10)

        self.drop_label = ctk.CTkLabel(self.drop_frame, text="Drop here.", width=300, height=300)
        self.drop_label.pack()

        self.drop_frame.drop_target_register(DND_FILES)
        self.drop_frame.dnd_bind("<<Drop>>", self.on_drop)

        self.info_label = ctk.CTkLabel(self.center_frame, text="Or")
        self.info_label.pack()

        self.pick_file_btn = ctk.CTkButton(self.center_frame, text="Choice a file", command=filehandler.SearchFile, width=200, height=75)
        self.pick_file_btn.pack(pady=20)

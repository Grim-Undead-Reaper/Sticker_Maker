import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("MySticker")

        self.pick_file = ctk.CTkButton(self, text="Hello, world!")
        self.pick_file.grid(row=0, column=0)

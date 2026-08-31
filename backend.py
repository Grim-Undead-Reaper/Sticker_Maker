from tkinter import filedialog
from PIL import Image
import customtkinter as ctk

class FileHandler:
    def __init__(self):
        self.filepath = None

    def SearchFile(self) -> None:
        self.GetFilename(filedialog.askopenfilename(
            title="Choice you image file.",
            multiple=False,
            initialdir="/",
            filetypes=(
                ("image file", ".png"),
                ("image file", ".jpeg"),
                ("image file", ".bmp")))
            )

    def GetFilename(self, filepath) -> None:
        if filepath != "":
            self.filepath = filepath
        else:
            print("No file chosen")

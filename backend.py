from tkinter import filedialog
from PIL import Image
import customtkinter as ctk

class FileHandler:
    def __init__(self):
        self.filepath = None
        self.files_allowed = [".png", ".jpeg", ".jpg", ".bmp"]

    def SearchFile(self) -> None:
        self.GetFilename(filedialog.askopenfilename(
            title="Choice you image file.",
            multiple=False,
            initialdir=r"E:\Pedro\Downloads",
            filetypes=(
                ("image file", self.files_allowed[0]),
                ("image file", self.files_allowed[1]),
                ("image file", self.files_allowed[2]),
                ("image file", self.files_allowed[3])))
            )

    def GetFilename(self, filepath) -> None:
        if filepath != "":
            self.filepath = filepath
            self.DisplayInfo()
        else:
            print("No file chosen")

    def DisplayInfo(self):
        print(f"\nFilepath{self.filepath}")

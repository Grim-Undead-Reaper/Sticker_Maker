from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=r"Secrets/MySecrets.env")

class FileHandler:
    def __init__(self):
        self.file = {"filepath": None, "filename": None}
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
            self.file["filepath"] = filepath
            self.file["filename"] = Path(self.file["filepath"]).name
            self.DisplayInfo()
        else:
            print("No file chosen")

    def DisplayInfo(self):
        print(f"\nFilepath: {self.file['filepath']}\nFilename: {self.file['filename']}")

class ImageHandler:
    def __init__(self):
        pass

    def SaveFileOnBackup(self):
        pass

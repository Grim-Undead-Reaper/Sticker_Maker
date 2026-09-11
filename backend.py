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
        self.imagehandler = ImageHandler()

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
            self.imagehandler.GetFile(self.file["filepath"])
            self.imagehandler.ResizeImage()
            #self.DisplayInfo()
        else:
            print("No file chosen")

    def DisplayInfo(self):
        print(f"\nFilepath: {self.file['filepath']}\nFilename: {self.file['filename']}\nName and Extensions: {str(self.file['filename']).split('.')}")

class ImageHandler:
    def __init__(self):
        self.image = {"fullpath": None, "name": None, "extension": None}
        self.backup_path = os.getenv("BACKUP_PATH")

    def SaveFileOnBackup(self):
        pass

    def GetFile(self, filepath):
        self.image["fullpath"] = filepath
        result_list = str(Path(filepath).name).split(".")

        self.image["name"] = result_list[0]
        self.image["extension"] = result_list[1]

    def ResizeImage(self):
        backup_filepath = Path(f"{self.backup_path}/{self.image['name']}_preview.{self.image['extension']}")

        if backup_filepath.is_file():
            print("O arquivo já existe")
            return None
        else:
            img = Image.open(self.image["fullpath"])
            res = img.resize((75, 75))
            img.save(f"{self.backup_path}/{self.image['name']}_preview.{self.image['extension']}")

from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=r"Secrets/MySecrets.env")

class FileHandler:
    def __init__(self):
        self.file = {"filepath": "", "filename": "", "extesion": ""}
        self.imagehandler = ImageHandler()

    def GetFile(self, filepath) -> None:
        if filepath != "":
            self.file["filepath"] = filepath
            name_and_extension = str(Path(self.file["filepath"]).name).split(".")
            self.file["filename"] = str(name_and_extension[0]).replace(" ", "_")
            self.file["extension"] = name_and_extension[1]
            self.imagehandler.ResizeImage(self.file)
        else:
            print("No file chosen")

    def DisplayInfo(self):
        print(f"\nFilepath: {self.file['filepath']}\nFilename: {self.file['filename']}\nName and Extensions: {str(self.file['filename']).split('.')}")

class ImageHandler:
    def __init__(self):
        self.image = {"filepath": "", "filename": "", "extension": ""}
        self.backup_path = os.getenv("BACKUP_PATH")

    def SaveFileOnBackup(self):
        pass

    def ResizeImage(self, filepath: dict):
        self.image = filepath

        backup_filepath = Path(f"{self.backup_path}/{self.image['filename']}_preview.{self.image['extension']}")

        if backup_filepath.is_file():
            print("O arquivo já existe")
            return None
        else:
            img = Image.open(self.image["filepath"])
            res = img.resize((75, 75))
            print(f"{self.backup_path}/{self.image['filename']}_preview.{self.image['extension']}")
            #img.save(f"{self.backup_path}/{self.image['filename']}_preview.{self.image['extension']}")


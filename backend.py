import flet as ft

class FileHandler:
    def __init__(self):
        self.filepath = None
        self.filePicker = ft.FilePicker()

    def GetImageInDirectory(self):
        self.filePicker.pick_files(dialog_title="Escolha sua imagem.", initial_directory='/', allow_multiple=False, allowed_extensions=["jpeg", "png"])

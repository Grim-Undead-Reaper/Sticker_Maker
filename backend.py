import flet as ft

class FileHandler:
    def __init__(self):
        self.filepath = None
        self.filePicker = ft.FilePicker()

    def GetImageInDirectory(self):
        self.filePicker.pick_files(allow_multiple=False)

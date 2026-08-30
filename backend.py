import flet as ft

class FileHandler:
    def __init__(self):
        self.filepath = None
        self.filePicker = ft.FilePicker(on_result=self.GetFilepath)

    def GetFilepath(self, e:ft.FilePickerResultEvent):
        self.filepath = e.files[0].path
        print(f"Caminho do arquivo: {self.filepath}")

    def GetImageInDirectory(self):
        self.filePicker.pick_files(dialog_title="Escolha sua imagem.", initial_directory='/', allow_multiple=False, allowed_extensions=["jpeg", "png"])

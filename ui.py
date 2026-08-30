import flet as ft
from backend import FileHandler

class App:
    def __init__(self):
        self.fileHandler = FileHandler()

        self.LabelTitle = ft.Text(f"Drag and drop you image")
        self.AddButton = ft.ElevatedButton(text="Create", on_click=self.GetFile)

    def main(self, page: ft.Page):
        page.title = "Test"

        page.add(self.LabelTitle)
        page.add(self.AddButton)
        page.add(self.fileHandler.filePicker)
    
    def RunApp(self):
        ft.app(target=self.main)

    def GetFile(self, e):
        self.fileHandler.GetImageInDirectory()

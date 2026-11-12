from PySide6.QtWidgets import QFileDialog
from model.json_tree import JsonTree
from service.file_handler import FileHandler
from service.logging import debug

class JsonController:
    def __init__(self, view):
        self._view = view
        self._view.json_load_button.clicked.connect(
            self.load_json
        )

    def load_json(self):
        debug.log("In load_json")
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Open JSON File",
            "",
            "JSON Files (*.json);;All Files (*)"
        )
        json_data = FileHandler.get_json(file_path)
        json_tree = JsonTree(json_data)
        self._view.json_tree_view.setPlainText(json_tree.get())
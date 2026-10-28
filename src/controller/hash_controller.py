from service.hash_calculator import HashCalculator

class HashController:
    def __init__(
        self,
        view,
    ):
        self._view = view
        self._view.hash_value_button.clicked.connect(
            self.process_hash
        )

    def process_hash(self):
        text = self._view.hash_edit.toPlainText()
        result = HashCalculator.hash_sha256(text)
        self._view.hash_result.setPlainText(result)

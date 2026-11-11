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
        algo = self._view.hash_type_combo.currentText()

        result = HashCalculator.run_hasher(text, algo)
        self._view.hash_result.setPlainText(result)

import sys

from PySide6.QtWidgets import QApplication

from controller.scan_controller import ScanController
from controller.hash_controller import HashController
from view.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    view = MainWindow()
    view.scan_controller = ScanController(view)
    view.hash_controller = HashController(view)

    view.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
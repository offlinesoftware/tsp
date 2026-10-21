import sys

from PySide6.QtWidgets import QApplication

from controller.scan_controller import ScanController
from view.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    view = MainWindow()
    view.controller = ScanController(view)

    view.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
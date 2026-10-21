from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QListWidget,
    QLabel,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.host_input = QLineEdit("10.241.17.103")
        self.start_port_input = QLineEdit("20")
        self.end_port_input = QLineEdit("30")

        self.scan_button = QPushButton("Scan")
        self.results = QListWidget()

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Host"))
        layout.addWidget(self.host_input)

        layout.addWidget(QLabel("Start Port"))
        layout.addWidget(self.start_port_input)

        layout.addWidget(QLabel("End Port"))
        layout.addWidget(self.end_port_input)

        layout.addWidget(self.scan_button)
        layout.addWidget(self.results)

        self.setLayout(layout)
        self.setWindowTitle("Port Scanner")
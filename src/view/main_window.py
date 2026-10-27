from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QGroupBox,
    QLineEdit, QListWidget, QLabel, QTextEdit
)

# Puts a border and title around a BoxLayout
def bordered_layout(layout, title=""):
    group = QGroupBox(title)
    group.setObjectName("layoutBorder")
    group.setLayout(layout)
    layout.setContentsMargins(8, 8, 8, 8)
    return group

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Layout boxes
        main_layout = QHBoxLayout()
        port_scan_box = QVBoxLayout()
        hash_box = QVBoxLayout()

        # Port scanner
        self.host_input = QLineEdit("10.241.17.103")
        self.start_port_input = QLineEdit("20")
        self.end_port_input = QLineEdit("30")
        self.scan_button = QPushButton("Scan")
        self.results = QListWidget()

        port_scan_box.addWidget(QLabel("Host"))
        port_scan_box.addWidget(self.host_input)

        port_scan_box.addWidget(QLabel("Start Port"))
        port_scan_box.addWidget(self.start_port_input)

        port_scan_box.addWidget(QLabel("End Port"))
        port_scan_box.addWidget(self.end_port_input)

        port_scan_box.addWidget(self.scan_button)
        port_scan_box.addWidget(self.results)

        main_layout.addWidget(bordered_layout(port_scan_box, "Port scanner"))


        # Hash string tool
        hash_box.addWidget(QLabel("Hash string: "))
        hash_text = QTextEdit()
        hash_box.addWidget(hash_text)
        hash_value_button = QPushButton("Hash value")
        hash_box.addWidget(hash_value_button)
        hash_result_line = QLineEdit()
        hash_box.addWidget(hash_result_line)

        main_layout.addWidget(bordered_layout(hash_box, "Hash calculator"))


        # Whole app
        self.setLayout(main_layout)
        self.setWindowTitle("TSP")

        self.setStyleSheet("""
            QFrame#layoutBorder {
                border: 1px solid #888;
                border-radius: 4px;
            }
        """)
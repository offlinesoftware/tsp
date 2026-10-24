from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QListWidget,
    QLabel,
    QFrame
)

def bordered_layout(layout):
    frame = QFrame()
    frame.setObjectName("layoutBorder")
    frame.setLayout(layout)
    layout.setContentsMargins(8, 8, 8, 8)
    return frame

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.host_input = QLineEdit("10.241.17.103")
        self.start_port_input = QLineEdit("20")
        self.end_port_input = QLineEdit("30")

        self.scan_button = QPushButton("Scan")
        self.results = QListWidget()

        main_layout = QHBoxLayout()

        port_scan_box = QVBoxLayout()

        port_scan_box.addWidget(QLabel("Host"))
        port_scan_box.addWidget(self.host_input)

        port_scan_box.addWidget(QLabel("Start Port"))
        port_scan_box.addWidget(self.start_port_input)

        port_scan_box.addWidget(QLabel("End Port"))
        port_scan_box.addWidget(self.end_port_input)

        port_scan_box.addWidget(self.scan_button)
        port_scan_box.addWidget(self.results)

        main_layout.addWidget(bordered_layout(port_scan_box))

        hash_box = QHBoxLayout()
        hash_box.addWidget(QLabel("Hash string: "))
        hash_text = QLineEdit()
        hash_box.addWidget(hash_text)

        main_layout.addWidget(bordered_layout(hash_box))
        
        self.setLayout(main_layout)
        self.setWindowTitle("Port Scanner")

        self.setStyleSheet("""
            QFrame#layoutBorder {
                border: 1px solid #888;
                border-radius: 4px;
            }
        """)
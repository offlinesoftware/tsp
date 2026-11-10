from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QGroupBox, QCheckBox,
    QLineEdit, QListWidget, QLabel, QPlainTextEdit, QComboBox
)
from hashlib import algorithms_guaranteed

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
        self.main_layout = QHBoxLayout()

        # Toggle buttons
        toggle_buttons = QVBoxLayout()


        toggle_port_scan = QCheckBox("Port scan")
        toggle_port_scan.setChecked(True)
        toggle_port_scan.toggled.connect(self.toggle_group)
        toggle_buttons.addWidget(toggle_port_scan)


        toggle_hash_calc = QCheckBox("Hash caclculator")
        toggle_hash_calc.setChecked(True)
        toggle_hash_calc.toggled.connect(self.toggle_group)
        toggle_buttons.addWidget(toggle_hash_calc)

        self.main_layout.addWidget(bordered_layout(toggle_buttons, "Toggle sections"))


        cli_box = QVBoxLayout()

        # Port scanner
        self.port_scan_box = self.build_port_scan_box(algorithms_guaranteed)
        self.port_scan_group = bordered_layout(self.port_scan_box, "Port scanner")
        self.main_layout.addWidget(self.port_scan_group)

        # Hash string tool
        self.hash_box = self.build_hash_box()
        self.hash_group = bordered_layout(self.hash_box, "Hash calculator")
        self.main_layout.addWidget(self.hash_group)



        


        # Command executor
        self.cli_edit = QPlainTextEdit()
        self.cli_run_button = QPushButton("Run")
        self.cli_result = QPlainTextEdit()

        cli_box.addWidget(QLabel("Command line(s)"))
        cli_box.addWidget(self.cli_edit)
        cli_box.addWidget(self.cli_run_button)
        cli_box.addWidget(self.cli_result)

        self.main_layout.addWidget(bordered_layout(cli_box, "Command executor"))

        # Whole app
        self.setLayout(self.main_layout)
        self.setWindowTitle("TSP")

        self.setStyleSheet("""
            QFrame#layoutBorder {
                border: 1px solid #888;
                border-radius: 4px;
            }
        """)

    def build_port_scan_box(self, alogorithm_list):
        self.host_input = QLineEdit("10.241.17.103")
        self.start_port_input = QLineEdit("20")
        self.end_port_input = QLineEdit("30")
        scan_type_combo = QComboBox()
        scan_type_combo.addItems(algorithms_guaranteed)
        scan_type_combo.setCurrentText("sha256")
        self.scan_button = QPushButton("Scan")
        self.results = QListWidget()
        port_scan_box = QVBoxLayout()
        port_scan_box.addWidget(QLabel("Host"))
        port_scan_box.addWidget(self.host_input)

        port_scan_box.addWidget(QLabel("Start Port"))
        port_scan_box.addWidget(self.start_port_input)

        port_scan_box.addWidget(QLabel("End Port"))
        port_scan_box.addWidget(self.end_port_input)

        scan_select_box = QHBoxLayout()
        scan_select_box.addWidget(scan_type_combo)
        scan_select_box.addWidget(self.scan_button)
        port_scan_box.addLayout(scan_select_box)
        port_scan_box.addWidget(self.results)
        return port_scan_box


    def build_hash_box(self):
        self.hash_edit = QPlainTextEdit()
        self.hash_value_button = QPushButton("Hash value")
        self.hash_result = QPlainTextEdit()

        hash_box = QVBoxLayout()
        hash_box.addWidget(QLabel("Hash string: "))
        hash_box.addWidget(self.hash_edit)
        hash_box.addWidget(self.hash_value_button)
        self.hash_result.setFixedHeight( # set three lines high
            self.hash_result.fontMetrics().lineSpacing() * 3 + 8
        )
        hash_box.addWidget(self.hash_result)
        return hash_box


    def toggle_group(self, checked):
        if checked:
            self.port_scan_group.show()
        else:
            self.port_scan_group.hide()
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
        toggle_buttons = QVBoxLayout()

        # Section definitions
        sections = [
            (
                "port_scan",
                "Port scanner",
                self.build_port_scan_box,
            ),
            (
                "hash",
                "Hash calculator",
                self.build_hash_box,
            ),
            (
                "cli",
                "Command executor",
                self.build_cli_box,
            ),
        ]

        # Use sections list to construct everything with a loop
        self.section_groups = {}
        for key, group_title, build_layout in sections:
            group = bordered_layout(build_layout(), group_title)
            self.section_groups[key] = group

            checkbox = QCheckBox(group_title)
            checkbox.setChecked(True)
            checkbox.toggled.connect(
                lambda checked, group=group: self.toggle_group(checked, group)
            )
            toggle_buttons.addWidget(checkbox)

        self.main_layout.addWidget(bordered_layout(toggle_buttons, "Toggle sections"))
        for group in self.section_groups.values():
            self.main_layout.addWidget(group)


        # Whole app config
        self.setLayout(self.main_layout)
        self.setWindowTitle("TSP")

        self.setStyleSheet("""
            QFrame#layoutBorder {
                border: 1px solid #888;
                border-radius: 4px;
            }
        """)
        

    def build_port_scan_box(self):
        self.host_input = QLineEdit("10.241.17.103")
        self.start_port_input = QLineEdit("20")
        self.end_port_input = QLineEdit("30")
        
        self.scan_button = QPushButton("Scan")
        self.results = QListWidget()
        port_scan_box = QVBoxLayout()
        port_scan_box.addWidget(QLabel("Host"))
        port_scan_box.addWidget(self.host_input)

        port_scan_box.addWidget(QLabel("Start Port"))
        port_scan_box.addWidget(self.start_port_input)

        port_scan_box.addWidget(QLabel("End Port"))
        port_scan_box.addWidget(self.end_port_input)

        port_scan_box.addWidget(self.scan_button)
        port_scan_box.addWidget(self.results)
        return port_scan_box


    def build_hash_box(self):
        self.hash_edit = QPlainTextEdit()
        self.hash_value_button = QPushButton("Hash value")
        self.hash_result = QPlainTextEdit()
        self.hash_type_combo = QComboBox()
        self.hash_type_combo.addItems(algorithms_guaranteed)
        self.hash_type_combo.setCurrentText("sha256")
        
        
        hash_box = QVBoxLayout()
        hash_box.addWidget(QLabel("Hash string: "))
        hash_box.addWidget(self.hash_edit)
        
        hash_select_box = QHBoxLayout()
        hash_select_box.addWidget(self.hash_type_combo)
        hash_select_box.addWidget(self.hash_value_button)
        
        hash_box.addLayout(hash_select_box)
        
        self.hash_result.setFixedHeight( # set three lines high
            self.hash_result.fontMetrics().lineSpacing() * 3 + 8
        )
        hash_box.addWidget(self.hash_result)
        return hash_box

    def build_cli_box(self):
        self.cli_edit = QPlainTextEdit()
        self.cli_run_button = QPushButton("Run")
        self.cli_result = QPlainTextEdit()

        cli_box = QVBoxLayout()
        cli_box.addWidget(QLabel("Command line(s)"))
        cli_box.addWidget(self.cli_edit)
        cli_box.addWidget(self.cli_run_button)
        cli_box.addWidget(self.cli_result)

        return cli_box


    def toggle_group(self, checked: bool, group: QGroupBox) -> None:
        group.setVisible(checked)
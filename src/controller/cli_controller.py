import subprocess
from config import DEBUG

class CliController:
    def __init__(
        self,
        view,
    ):
        self._view = view
        self._view.cli_run_button.clicked.connect(
            self.run_commands
        )

    def run_commands(self):
        commands = self._view.cli_edit.toPlainText()
        self._view.cli_result.clear()
        for command in commands.splitlines():
            self._view.cli_result.appendPlainText(f"> {command}")
            result = subprocess.run(
                command.split(), 
                capture_output=True, 
                text=True,
                shell=True
            )
            if result.returncode == 0:
                self._view.cli_result.appendPlainText(result.stdout)
            else:
                self._view.cli_result.appendPlainText(result.stderr)
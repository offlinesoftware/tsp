from unittest.mock import Mock

from controller.scan_controller import ScanController
from model.scan_result import ScanResult


def test_controller_updates_view():
    view = Mock()

    view.host_input.text.return_value = "localhost"
    view.start_port_input.text.return_value = "80"
    view.end_port_input.text.return_value = "80"

    scanner = Mock()

    scanner.scan.return_value = [
        ScanResult(
            port=80,
            open=True
        )
    ]

    controller = ScanController(
        view,
        scanner
    )

    controller._scan_complete(
        scanner.scan.return_value
    )

    view.results.addItem.assert_called_once()
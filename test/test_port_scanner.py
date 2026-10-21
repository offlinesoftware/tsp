from unittest.mock import patch

from model.scan_request import ScanRequest
from service.port_scanner import PortScanner


def test_scan_detects_open_port():
    scanner = PortScanner()

    request = ScanRequest(
        host="localhost",
        start_port=80,
        end_port=80,
    )

    with patch.object(
        scanner,
        "_is_open",
        return_value=True,
    ):
        results = scanner.scan(request)

    assert len(results) == 1
    assert results[0].open is True
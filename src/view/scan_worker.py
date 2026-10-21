from PySide6.QtCore import QObject, Signal, Slot

from model.scan_request import ScanRequest
from service.port_scanner import PortScanner


class ScanWorker(QObject):
    finished = Signal(list)

    def __init__(
        self,
        scanner: PortScanner,
        request: ScanRequest
    ):
        super().__init__()

        self._scanner = scanner
        self._request = request

    @Slot()
    def run(self):
        print("Worker running request:", self._request)
        result = self._scanner.scan(self._request)
        self.finished.emit(result)
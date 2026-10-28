from PySide6.QtCore import QThread
from config import DEBUG
from model.scan_request import ScanRequest
from service.port_scanner import PortScanner
from view.scan_worker import ScanWorker


class ScanController:
    def __init__(
        self,
        view,
        scanner: PortScanner | None = None
    ):
        self._view = view
        self._scanner = scanner or PortScanner()
        if DEBUG:
            print("ScanController initiated")
        self._view.scan_button.clicked.connect(
            self.start_scan
        )

        self._thread = None

    def start_scan(self):
        if DEBUG:
            print("Starting scan")
        request = ScanRequest(
            host=self._view.host_input.text(),
            start_port=int(
                self._view.start_port_input.text()
            ),
            end_port=int(
                self._view.end_port_input.text()
            ),
        )

        self._thread = QThread()

        self._worker = ScanWorker(
            self._scanner,
            request,
        )
        if DEBUG:
            print("Worker created:", self._worker)
        self._worker.moveToThread(self._thread)

        self._thread.started.connect(self._worker.run)

        self._worker.finished.connect(
            self._scan_complete
        )

        self._worker.finished.connect(
            self._thread.quit
        )

        self._thread.start()

    def _scan_complete(self, results):
        print("Scan complete")
        self._view.results.clear()

        for result in results:
            if result.open:
                self._view.results.addItem(
                    f"Port {result.port}: OPEN"
                )
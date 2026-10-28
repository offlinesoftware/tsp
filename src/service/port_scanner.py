import socket
from config import DEBUG
from model.scan_request import ScanRequest
from model.scan_result import ScanResult


class PortScanner:
    def scan(self, request: ScanRequest):
        
        results = []

        for port in range(request.start_port, request.end_port + 1):
            if DEBUG:
                print("Trying port", port)
            results.append(
                ScanResult(
                    port=port,
                    open=self._is_open(
                        request.host,
                        port,
                        request.timeout
                    ),
                )
            )

        return results

    def _is_open(
        self,
        host: str,
        port: int,
        timeout: float
    ) -> bool:
        try:
            with socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            ) as sock:
                sock.settimeout(timeout)

                return (
                    sock.connect_ex((host, port))
                    == 0
                )
        except OSError:
            return False
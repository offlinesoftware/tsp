from dataclasses import dataclass


@dataclass(frozen=True)
class ScanRequest:
    host: str
    start_port: int
    end_port: int
    timeout: float = 0.5
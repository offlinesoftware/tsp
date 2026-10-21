from dataclasses import dataclass


@dataclass(frozen=True)
class ScanResult:
    port: int
    open: bool
# AGENTS.md

## Project Overview

This project is a desktop port scanner implemented with PySide6 using a Model-View-Controller (MVC) architecture.

Goals:

- Clean separation of UI and business logic.
- Highly testable design.
- Dependency injection wherever practical.
- Fast unit tests using pytest.
- No networking code inside UI classes.
- Easy future expansion (threading, progress updates, export functions, service discovery, etc.).

---

# Architecture

## Model

The model contains data structures representing application state.

Examples:

- `ScanRequest`
- `ScanResult`

Responsibilities:

- Store data only.
- No UI code.
- No threading code.
- No PySide dependencies unless absolutely necessary.

---

## View

The view contains PySide widgets and layout code.

Examples:

- `MainWindow`
- Dialogs
- Custom widgets

Responsibilities:

- Display information.
- Raise Qt signals for user actions.
- Contain no business logic.
- Contain no networking logic.
- Remain testable independently of scanning behaviour.

Views should not instantiate scanners or perform socket operations.

---

## Controller

Controllers coordinate the application.

Examples:

- `ScanController`

Responsibilities:

- React to user actions.
- Validate input.
- Create worker threads.
- Invoke services.
- Update views with results.

Controllers should be the only layer that directly connects views and services.

---

## Services

Services contain application logic.

Examples:

- `PortScanner`

Responsibilities:

- Port scanning.
- Hostname resolution.
- Future protocol detection.
- Future operating-system fingerprinting.

Services must not depend on PySide.

Services should be usable from:

- GUI applications
- Command-line utilities
- Automated tests

---

## Workers

Workers execute long-running tasks.

Examples:

- `ScanWorker`

Responsibilities:

- Run service operations inside worker threads.
- Emit signals containing results.
- Never interact directly with widgets.

Workers should communicate through signals only.

---

# Dependency Rules

Allowed:

```
Controller -> View
Controller -> Service
Controller -> Model

Worker -> Service
Worker -> Model

View -> Qt
Model -> Standard Library
Service -> Standard Library
```

Not Allowed:

```
View -> Service
View -> Socket
View -> Controller

Model -> View
Model -> Qt Widgets

Service -> Qt Widgets
```

---

# Naming Conventions

## Classes

Use PascalCase.

Examples:

```python
ScanController
PortScanner
MainWindow
ScanWorker
```

---

## Functions

Use snake_case.

Examples:

```python
start_scan()
scan_complete()
resolve_hostname()
```

---

## Private Members

Prefix internal members with `_`.

Example:

```python
self._view
self._scanner
self._thread
self._worker
```

Reason:

Python uses leading underscores to indicate implementation details that should not be accessed externally.

---

# Threading Rules

UI updates must only occur on the GUI thread.

Never:

```python
widget.setText(...)
```

from a worker thread.

Instead:

```python
finished.emit(results)
```

and update the UI in the controller.

---

# Testing

Framework:

- pytest

Preferred test types:

## Unit Tests

Test models and services without Qt.

Example:

```python
def test_scan_detects_open_port():
    ...
```

---

## Controller Tests

Mock:

- View
- Service

Verify:

- Requests are built correctly
- Results are passed to the view
- Validation behaves correctly

Example:

```python
scanner = Mock()
view = Mock()
```

---

## GUI Tests

Use:

```bash
pytest-qt
```

for widget interaction testing.

Avoid testing business logic through GUI tests when a unit test is possible.

---

# Mocking Rules

Prefer mocking:

- sockets
- network calls
- scanners

Avoid real network activity in automated tests.

Good:

```python
patch.object(scanner, "_is_open")
```

Bad:

```python
scanner.scan("google.com")
```

during CI execution.

---

# Error Handling

Services should raise meaningful exceptions.

Examples:

```python
InvalidHostError
ScanCancelledError
```

Controllers should convert exceptions into user-facing messages.

Views should only display errors.

---

# Logging

Use the standard logging module.

Example:

```python
import logging

logger = logging.getLogger(__name__)
```

Do not use:

```python
print()
```

except during temporary debugging.

---

# Future Enhancements

Potential future features:

- Parallel scanning
- CIDR range scanning
- UDP scanning
- Service detection
- Banner grabbing
- Export to CSV
- Export to JSON
- Save scan history
- Dark mode
- MVVM migration

Design new functionality to preserve the existing separation between:

- View
- Controller
- Service
- Model

---

# Definition of Done

A change is complete when:

- Code passes linting.
- Code passes pytest.
- New behaviour has unit tests.
- Controller logic remains separate from view code.
- No networking code is added to widgets.
- No UI updates occur from worker threads.
- Public APIs are documented.
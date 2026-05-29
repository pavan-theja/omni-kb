from __future__ import annotations

import time
from typing import Optional

try:
    from tqdm.auto import tqdm
except ModuleNotFoundError:
    tqdm = None


def make_progress(total: Optional[int], desc: str, unit: str, *, disabled: bool):
    if disabled:
        return None
    if tqdm is not None:
        return tqdm(total=total, desc=desc, unit=unit)
    return PlainProgress(total=total, desc=desc, unit=unit)


def progress_update(progress, amount: int) -> None:
    if progress is not None:
        progress.update(amount)


def progress_status(progress, status: str) -> None:
    if progress is None:
        return
    if hasattr(progress, "set_postfix_str"):
        progress.set_postfix_str(status)
    elif hasattr(progress, "set_status"):
        progress.set_status(status)


def progress_close(progress) -> None:
    if progress is not None:
        progress.close()


def progress_set_absolute(progress, current: int, total: int) -> None:
    if progress is None:
        return
    if hasattr(progress, "total") and hasattr(progress, "n"):
        progress.total = total
        progress.n = current
        progress.refresh()
    elif hasattr(progress, "set_absolute"):
        progress.set_absolute(current, total)


class PlainProgress:
    def __init__(self, total: Optional[int], desc: str, unit: str) -> None:
        self.total = total
        self.desc = desc
        self.unit = unit
        self.current = 0
        self.status = ""
        self._last_print = 0.0

    def update(self, amount: int) -> None:
        self.current += amount
        now = time.monotonic()
        if now - self._last_print >= 5 or (self.total and self.current >= self.total):
            self._print()
            self._last_print = now

    def set_status(self, status: str) -> None:
        self.status = status

    def set_absolute(self, current: int, total: int) -> None:
        self.current = current
        self.total = total
        self._print()

    def close(self) -> None:
        self._print()

    def _print(self) -> None:
        total = "?" if self.total is None else str(self.total)
        suffix = f" {self.status}" if self.status else ""
        print(f"{self.desc}: {self.current}/{total} {self.unit}{suffix}", flush=True)

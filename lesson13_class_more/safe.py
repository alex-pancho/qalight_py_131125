from datetime import datetime, timedelta


class Safe:
    MAX_ITEMS = 5
    MAX_FAILED_ATTEMPTS = 3
    BLOCK_DURATION = timedelta(minutes=5)

    def __init__(self, password: str):
        self._password = str(password)
        self._locked = True
        self._failed_attempts = 0
        self._blocked_until: datetime | None = None
        self._items: list = []

    # --- state helpers ---
    def _now(self) -> datetime:
        return datetime.now()

    def _is_blocked(self) -> bool:
        if self._blocked_until is None:
            return False
        if self._now() >= self._blocked_until:
            # block expired -> reset
            self._blocked_until = None
            self._failed_attempts = 0
            return False
        return True

    @property
    def locked(self) -> bool:
        return self._locked

    @property
    def blocked(self) -> bool:
        return self._is_blocked()

    @property
    def blocked_until(self) -> datetime | None:
        # повертає дедлайн (або None)
        _ = self._is_blocked()  # щоб автоматично зняти блок, якщо час вийшов
        return self._blocked_until

    # --- string repr ---
    def __str__(self) -> str:
        if self._is_blocked():
            state = f"blocked until {self._blocked_until.strftime('%H:%M:%S')}"
        else:
            state = "locked" if self._locked else "unlocked"
        return f"Safe with {len(self._items)}/{self.MAX_ITEMS} items ({state})"

    def __repr__(self) -> str:
        return self.__str__()

    # --- container protocol ---
    def __len__(self) -> int:
        return len(self._items)

    def __contains__(self, item) -> bool:
        return item in self._items

    def __getitem__(self, index: int):
        return self._items[index]

    def __setitem__(self, index: int, value) -> None:
        self._ensure_can_modify()

        # додавання: тільки в кінець (index == len)
        if index == len(self._items):
            if len(self._items) >= self.MAX_ITEMS:
                raise OverflowError("Safe is full")
            self._items.append(value)
            return

        # заміна існуючого (list сам кине IndexError якщо індекс поганий)
        self._items[index] = value

    def __delitem__(self, index: int) -> None:
        self._ensure_can_modify()
        del self._items[index]

    # --- access control ---
    def unlock(self, password: str) -> None:
        if self._is_blocked():
            left = self._blocked_until - self._now()  # type: ignore[operator]
            seconds = max(0, int(left.total_seconds()))
            raise PermissionError(f"Safe is blocked for {seconds}s")

        if str(password) != self._password:
            self._failed_attempts += 1

            if self._failed_attempts >= self.MAX_FAILED_ATTEMPTS:
                self._blocked_until = self._now() + self.BLOCK_DURATION
                self._locked = True
                raise PermissionError("Safe is blocked for 5 minutes after 3 failed attempts")

            raise ValueError(f"Wrong password (attempt {self._failed_attempts}/{self.MAX_FAILED_ATTEMPTS})")

        # success
        self._failed_attempts = 0
        self._blocked_until = None
        self._locked = False

    def lock(self) -> None:
        self._locked = True

    def _ensure_can_modify(self) -> None:
        if self._is_blocked():
            raise PermissionError("Safe is blocked")
        if self._locked:
            raise PermissionError("Safe is locked")


class DigitalSafe(Safe):
    def __init__(self, password: str, log_file: str = "digital_safe.log"):
        super().__init__(password)
        self._log_file = log_file
        self._log("INIT", "Safe created")

    def _log(self, action: str, details: str = "") -> None:
        ts = datetime.now().isoformat(timespec="seconds")
        with open(self._log_file, "a", encoding="utf-8") as f:
            f.write(f"{ts} | {action} | {details}\n")

    def unlock(self, password: str) -> None:
        try:
            super().unlock(password)
            self._log("UNLOCK_OK", "Unlocked")
        except Exception as e:
            self._log("UNLOCK_FAIL", f"{type(e).__name__}: {e}")
            raise

    def lock(self) -> None:
        super().lock()
        self._log("LOCK", "Locked")

    def __setitem__(self, index: int, value) -> None:
        try:
            super().__setitem__(index, value)
            self._log("SET", f"index={index}, value={value!r}")
        except Exception as e:
            self._log("SET_FAIL", f"index={index}, {type(e).__name__}: {e}")
            raise

    def __delitem__(self, index: int) -> None:
        try:
            super().__delitem__(index)
            self._log("DEL", f"index={index}")
        except Exception as e:
            self._log("DEL_FAIL", f"index={index}, {type(e).__name__}: {e}")
            raise


if __name__ == "__main__":
    s = Safe("1234")
    print(s)

    # 3 невдалі спроби -> блок на 5 хв
    for p in ("0000", "1111", "2222"):
        try:
            s.unlock(p)
        except Exception as e:
            print("unlock error:", e)

    print(s)  # покаже blocked until

    # під час блоку спроба unlock
    try:
        s.unlock("1234")
    except Exception as e:
        print("unlock during block:", e)

    # DigitalSafe demo
    ds = DigitalSafe("abcd")
    try:
        ds.unlock("nope")
    except Exception:
        pass
    try:
        ds.unlock("nope2")
    except Exception:
        pass
    try:
        ds.unlock("nope3")
    except Exception:
        pass

    print(ds)  # blocked until

from safe import Safe, DigitalSafe


def run_safe_cli() -> None:
    safe = Safe("1234")

    print("=== SAFE CLI DEMO ===")
    print("Correct password is: 1234 (for demo)")
    print("Commands: unlock, lock, status, exit\n")

    while True:
        cmd = input("Enter command: ").strip().lower()

        if cmd == "exit":
            print("Bye!")
            return

        if cmd == "status":
            print(safe)
            continue

        if cmd == "lock":
            safe.lock()
            print("Safe locked")
            continue

        if cmd == "unlock":
            pwd = input("Enter password: ").strip()
            try:
                safe.unlock(pwd)
                print(" Safe unlocked")
            except Exception as e:
                print(f"Х {e}")
            continue

        print("Unknown command. Use: unlock, lock, status, exit")


def run_digital_safe_cli() -> None:
    ds = DigitalSafe("abcd", log_file="digital_safe.log")

    print("\n=== DIGITAL SAFE CLI DEMO ===")
    print("Correct password is: abcd (for demo)")
    print("Log file: digital_safe.log")
    print("Commands: unlock, lock, status, exit\n")

    while True:
        cmd = input("Enter command: ").strip().lower()

        if cmd == "exit":
            print("Bye!")
            return

        if cmd == "status":
            print(ds)
            continue

        if cmd == "lock":
            ds.lock()
            print(" DigitalSafe locked")
            continue

        if cmd == "unlock":
            pwd = input("Enter password: ").strip()
            try:
                ds.unlock(pwd)
                print("DigitalSafe unlocked")
            except Exception as e:
                print(f"Х {e}")
            continue

        print("Unknown command. Use: unlock, lock, status, exit")


if __name__ == "__main__":
    run_safe_cli()


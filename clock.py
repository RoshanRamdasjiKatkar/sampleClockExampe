from datetime import datetime
import time


def format_time(current_time: datetime) -> str:
    return current_time.strftime("%I:%M:%S %p")


def main() -> None:
    try:
        while True:
            print(format_time(datetime.now()), end="\r", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
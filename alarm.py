import time
from datetime import datetime
import winsound

# Set alarm time (24-hour format)
alarm_time = "08:45"

print("Alarm set for:", alarm_time)

while True:
    current_time = datetime.now().strftime("%H:%M")

    if current_time == alarm_time:
        print("Wake up! Alarm is ringing!")
        winsound.Beep(1000, 1000)
        break

    time.sleep(1)

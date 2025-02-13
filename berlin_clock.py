# import time

# def berlin_clock():
#     while True:
#         current_time = time.localtime()
#         hours = current_time.tm_hour
#         minutes = current_time.tm_min
#         seconds = current_time.tm_sec
        
#         # Top light (seconds)
#         seconds_light = seconds % 2 == 0

#         # Second row (hours in multiples of 5)
#         hours_5_blocks = hours // 5
#         # Third row (remaining hours)
#         single_hours = hours % 5

#         # Fourth row (minutes in multiples of 5)
#         minutes_5_blocks = minutes // 5
#         # Bottom row (remaining minutes)
#         single_minutes = minutes % 5

#         print("Berlin Clock Time:")
#         print("Seconds:", "Yellow" if seconds_light else "Off")
#         print("Hours (5s):", "Red " * hours_5_blocks + "Off " * (4 - hours_5_blocks))
#         print("Hours (1s):", "Red " * single_hours + "Off " * (4 - single_hours))
#         print("Minutes (5s):", "".join(["Red " if i in [2, 5, 8] else "Yellow " for i in range(minutes_5_blocks)]) + "Off " * (11 - minutes_5_blocks))
#         print("Minutes (1s):", "Yellow " * single_minutes + "Off " * (4 - single_minutes))
        
#         time.sleep(1)

# berlin_clock()

















import time

def display_berlin_clock(hours, minutes, seconds):
    # Top lamp: Blinks every two seconds
    top_light = 'Y' if seconds % 2 == 0 else 'O'

    # Hours (5s): Each lamp represents 5 hours (4 lamps)
    five_hour_lamps = 'R' * (hours // 5) + 'O' * (4 - (hours // 5))

    # Hours (1s): Each lamp represents 1 hour (4 lamps)
    one_hour_lamps = 'R' * (hours % 5) + 'O' * (4 - (hours % 5))

    # Minutes (5s): Each lamp represents 5 minutes (11 lamps)
    five_minute_lamps = ''.join(['R' if (i + 1) % 3 == 0 else 'Y' for i in range(minutes // 5)]) + 'O' * (11 - (minutes // 5))

    # Minutes (1s): Each lamp represents 1 minute (4 lamps)
    one_minute_lamps = 'Y' * (minutes % 5) + 'O' * (4 - (minutes % 5))

    # Print the Berlin Clock
    print(f"{top_light}")
    print(f"{five_hour_lamps}")
    print(f"{one_hour_lamps}")
    print(f"{five_minute_lamps}")
    print(f"{one_minute_lamps}")
    print("\n")

def berlin_clock():
    while True:
        current_time = time.localtime()
        hours = current_time.tm_hour
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        display_berlin_clock(hours, minutes, seconds)

        time.sleep(1)
        # Clear the console (for most systems)
        print("\033[H\033[J", end='')

berlin_clock()

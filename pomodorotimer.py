import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

print("Pomodoro Timer")
print("1. Start 25 min focus")
print("2. Start 5 min break")

choice = input("Choose option: ")

if choice == "1":
    print("Focus time started!")
    countdown(25)
    print("\nBreak time!")
elif choice == "2":
    print("Break started!")
    countdown(5)

print("Session complete!")

import time
from playsound import playsound
from pathlib import Path

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('WEE WOO WEE WOO!!')
    playsound("C:/Users/emper/OneDrive/Documents/GitHub/Time-Counter/alarm.mp3")

# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))
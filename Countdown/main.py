import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Time Out")


minsOrSecs = input(
    "Do you want to set the countdown by minutes[M] or by seconds[S]?")
if minsOrSecs == 'M':
    t = int(input("Enter the number of minutes for countdown: ")) * 60
    t = countdown(t)

if minsOrSecs == 'S':
    t = int(input("Enter the number of seconds for countdown."))
    t = countdown(t)

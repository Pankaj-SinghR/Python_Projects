import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end = "\r")
        time.sleep(1)
        t -= 1

    print('Timer completed!')


if __name__ == "__main__":
    timer_format = """
::: Time Format :::
Hours:minute:seconds
"""
    print(timer_format)
    t = input("Give Time In Above Format: ")
    hours , mins, seconds = t.split(":")
    try:
        hours = int(hours)
        mins = int(mins)
        seconds = int(seconds)
    except:
        print(timer_format)
        print("Enter correct format")
        exit()
    total_seconds = hours * 60 *60 + mins * 60 + seconds
#    print(total_seconds)
    countdown(total_seconds) #calling countdown function

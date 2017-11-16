import webbrowser
import time

breaks_to_take = 3
breaks_taken = 0
time_in_seconds_to_sleep = 60*60*2

print("Program started on ", time.ctime())
while breaks_taken < breaks_to_take:
    time.sleep(time_in_seconds_to_sleep)
    webbrowser.open("https://www.youtube.com/watch?v=4MCjU-Du3eI")
    breaks_taken = breaks_taken + 1

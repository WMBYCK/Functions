# William Craddock
# 10/12/2014
# Development Exercises - Task 1

def get_inputs():
    hours = int(input("Please enter the number of hours: "))
    minutes = int(input("Please enter the number of minutes: "))
    seconds = int(input("Please enter the number of seconds: "))
    return hours,minutes,seconds

def hours_to_seconds(hours):
    total = hours * 3600
    return total

def minutes_to_seconds(minutes,total):
    total = minutes * 60 + total
    return total

def seconds_to_seconds(seconds,total):
    total = seconds + total
    return total

def display_total(total):
    print(total)

def total_seconds_calculator():
    hours,minutes,seconds = get_inputs()
    total = hours_to_seconds(hours)
    total = minutes_to_seconds(minutes,total)
    total = seconds_to_seconds(seconds,total)
    display_total(total)

total_seconds_calculator()
    

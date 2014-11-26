# calculate pay

def calculate_pay(hour,rate,total):
    
    return hour,rate,total

# get hours + rate of pay

def get_hours_rate():
    hours = int(input("Please enter the number of hours you work a week: "))
    rate = int(input("Please enter the rate of pay you get per hour in pounds: £"))
    return hours,rate

# calculate total pay

def calculate_total_pay(hours,rate):
    if hours <= 40:
        total = calculate_basic_pay(hours,rate)
    else:
        total = calculate_overtime_pay(hours,rate)
    return total

# calculate basic pay

def calculate_basic_pay(hours,rate):
    total = hours * rate
    return total

# calculate overtime pay

def calculate_overtime_pay(hours,rate):
    total = ((hours - 40) * (rate * 1.5)) + (rate * 40)
    return total

# display total pay
def display_total_pay(total):
    print(total)



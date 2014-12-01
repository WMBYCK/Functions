# Get Hours + Rate Of Pay

def get_hours_rate():
    hours = int(input("Please enter the number of hours you work a week: "))
    rate = int(input("Please enter the rate of pay you get per hour in pounds: £"))
    return hours,rate

# Calculate Total Pay

def calculate_total_pay(hours,rate):
    if hours <= 40:
        total = calculate_basic_pay(hours,rate)
    else:
        total = calculate_overtime_pay(hours,rate)
    return total

# Calculate Basic Pay

def calculate_basic_pay(hours,rate):
    total = hours * rate
    return total

# Calculate Overtime Pay

def calculate_overtime_pay(hours,rate):
    total = ((hours - 40) * (rate * 1.5)) + (rate * 40)
    return total

# Display Total Pay
def display_total_pay(total):
    print("You make £{0}".format (total))

# Calculate Pay

def calculate_pay():
    hours,rate = get_hours_rate()
    total = calculate_total_pay(hours,rate)
    display_total_pay(total)

# Main Program

calculate_pay()

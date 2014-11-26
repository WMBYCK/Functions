# calculate basic pay

def calculate_basic_pay(hours,rate):
    total = hours * rate
    return total

# calculate overtime pay

def calculate_overtime_pay(hours,rate):
    total = ((hours - 40) * (rate * 1.5)) + (pay * 40)
    return total

# calculate total pay
def calculate_total_pay(hours,rate):
    if hours <= 40:
        total_pay = calculate_basic_pay(hours,rate)
    else:
        total_pay = calculate_overtime_pay(hours,rate)
    return total_pay


# main program

total_pay = calculate_basic_pay(12,2)
print(total_pay)

total_pay = calculate_overtime_pay(41,1)
print(total_pay)

total_pay = calculate_total_pay(40,1)
print(total_pay)

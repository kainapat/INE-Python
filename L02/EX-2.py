gross_pay: float = 0

if __name__ == "_main_":
    hours_work = float(input('Enter the number of hours worked : '))
    pay_rate = float(input('Enter the hourly payrate : '))

    if hours_work > 48:
        gross_pay = ((40*pay_rate))+((hours_work)*30)
    else:
        gross_pay = (hours_work*pay_rate)

    print("The gross pay is ${:,.2f}.".format(gross_pay))
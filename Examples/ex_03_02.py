try: 
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    if hours < 40 :
        pay = hours * rate
    else :
        pay = 40 * rate
        pay += (hours - 40) * 1.5 * rate

    
    print("Pay: " + str(pay))
except : 
    print("Error, please enter numeric input")

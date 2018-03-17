total = input("Total bill amount? ")
total = float(total)

service = input("How was the service: (Good, Fair, or Bad)? ")

if service == "Good":
    tip = total * .20
elif service == "Fair":
    tip = total * .15
else:
    tip = total * .10
    
print("Tip: ${:.2f}".format(tip))
print("Bill + Tip: ${:.2f}".format(total + tip))
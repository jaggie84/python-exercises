total = input("How much was the bill? ")
total = float(total)

service = input("How was the service?: (Good, Fair, or Bad) ")

if service == "Good": 
  tip = total * 0.20
  
if service == "Fair":
  tip = total * 0.15
  
if service == "Bad":
  tip = total * 0.10
  
totalBill = ("Your total including tip comes to: ")
print(totalBill)
print(total + tip)


  


  
  
    
    
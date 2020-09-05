pSum = 0

def printSavings(string, p):
  global pSum
  pSum += int(p * 100)

  savingsAmount = float(savings) * p
  savingsAmount = str(round(savingsAmount, 2))
  print ("\n" + string + ": $" + savingsAmount)

savings = input("cur_savings: ")

printSavings("engagement_ring", 0.20)
printSavings("house_down_payment", 0.17)
printSavings ("childrens_college", 0.13)
printSavings ("new_car", 0.25)
printSavings ("honeymoon", 0.15)
printSavings ("mad_money", 0.10)

print ("\n" + str(pSum) + "%")

print ("atempting file io")
savingsFile = open("savings.txt", "w")
print("List Generator")
print()
print()
startImp = int(input("Start at: "))
endImp = int(input("End before: "))
incrValue = int(input("Inceriment between values: "))
print()
for i in range(startImp, endImp, incrValue):
  if i <= 77:
    print("\033[33m", i, "\033[0m")
  elif i > 77:
    print("\033[36m", i, "\033[0m")
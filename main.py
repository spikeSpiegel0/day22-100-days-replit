import random
print("Totally Random One-Hundred")
print()
theNumber = random.randint(1,100)
zero = 0
count = 0
while True:
  theAnswer = int(input("What is yot guess? "))
  if theAnswer <= zero:
    print()
    exit()
  elif theAnswer > theNumber:
    print("Too high")
    print()
    count += 1
  elif theAnswer < theNumber:
    print("Too low")
    print()
    count += 1
  elif theAnswer == theNumber:
    count += 1
    print("Correct")
    print()
    print("It took you", count, "guesses to get it correct")
    break
  else:
    print("wtf bro?")
  print("Click 'Play' to try again with different number")
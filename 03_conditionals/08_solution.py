password = len(input("Enter password: "))

if password < 6:
  print("Weak")

elif password < 10:
  print("Medium")

else:
  print("Strong")
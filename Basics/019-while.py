# if
if True:
    print("True")
else:
    print("False")

# Correct way to make a while loop counter 1-10
counter = 1
while counter <= 10:
    print(counter)
    counter += 1
    if counter == 5:
        break

# Best way to make a while loop counter 1-20
counter = 1
while counter <= 20:
      counter += 1
      if counter <15:
          continue
      print(counter)

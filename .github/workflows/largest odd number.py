x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
largest = None
if x%2:
 largest = x
if y%2:
 if y > largest:
  largest = y
if z%2:
 if z > largest:
  largest = z
if largest:
 print("largest odd number is", str(largest))
else:
 print("there are no odd numbers")
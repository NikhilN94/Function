def highest_even(num):
  num.sort()
  num.reverse()
  for item in num:
    if item%2 == 0:
      print(item)
      break

highest_even([10,2,4, 6, 8, 11])
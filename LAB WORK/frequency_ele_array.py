from collections import Counter

array = [1,1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency = Counter(array)
# printing the element and the frequency
for key, value in frequency.items():
   print(f"{key}:- {value}")
# print(frequency)



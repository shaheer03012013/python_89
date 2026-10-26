set1 = {"Apple", "Banana", "Mango", "Orange", "Watermelon"}
set2 = {"Apple", "Kiwi", "Orange", "Watermelon", "Pineapple"}
print("Set 1: ", set1)
print("Set 2: ", set2)

set1.add("Grapes")
print("Set 1 after adding Grapes: ", set1)

common_fruits = set1.intersection(set2)
print("Common fruits in both sets: ", common_fruits)

import array as arr
fruit_counts = arr.array('i', [5, 3, 8, 2, 6])
print("Fruit counts array: ", fruit_counts)

fruit_counts.insert(2, 10)
fruit_counts.append(4)
print("Fruit counts array after adding new elements: ", fruit_counts)

count_of_5 = fruit_counts.count(5)
print("Count of 5 in fruit counts array: ", count_of_5)

fruit_counts.reverse(3)
print("Fruit counts array after reversing: ",fruit_counts)

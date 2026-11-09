snack_box_1 = {"Popcorn", "Pretzels", "Granola Bar", "Apple", "Juice"}
snack_box_2 = {"Popcorn", "Crackers", "Granola Bar", "Apple", "Yogurt"}
print("Snack Box 1: ", snack_box_1)
print("Snack Box 2: ", snack_box_2)

snack_box_1.add("Trail Mix")
print("Snack Box 1 after adding Trail Mix: ", snack_box_1)

shared_snacks = snack_box_1.intersection(snack_box_2)
print("Snacks in both boxes: ", shared_snacks)

import array as arr

snack_counts = arr.array("i", [5, 3, 8, 2, 6])
print("Snack counts array: ", snack_counts)

snack_counts.insert(2, 10)
snack_counts.append(4)
print("Snack counts array after adding new values: ", snack_counts)

count_of_5 = snack_counts.count(5)
print("Count of 5 in snack counts array: ", count_of_5)

snack_counts.reverse()
print("Snack counts array after reversing: ", snack_counts)

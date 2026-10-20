test_dict = {"name": "shaheer", "class": "VII", "nickname": "shaheer"}
print("Original Dictionary: " + str(test_dict))

K = "shaheer"
res = 0

for key in test_dict:
    if test_dict[key] == K:
        res += 1
        
print("The frequency of " + K + " is : " + str(res))
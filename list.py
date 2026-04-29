print("===LIST EXAMPLES==")
fruits=["apple","banana","cherry","apple"]
fruits.append('orange')
if "banana" in fruits:
    fruits.remove("banana")
print("Original List:",fruits)
print("First fruit:",fruits[1])
upper_fruits=[fruit.upper() for fruit in fruits ]
print(upper_fruits)
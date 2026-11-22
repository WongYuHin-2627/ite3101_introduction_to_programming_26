list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    print(max(a, b))
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print("You have...")

for fruit in fruits:
    if fruit == "tomato":
        print("A tomato is not a fruit!")
    print("A", fruit)

print("A fine selection of fruits!")
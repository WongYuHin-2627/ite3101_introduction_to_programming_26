fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
    if f == 'tomato':
        print('A tomato is not a fruit!')  # (It actually is.)
        break
    print('A', f)
else:
    print('A fine selection of fruits!')
print("You have...")

for fruit in fruits:
    if fruit == "tomato":
        print("A tomato is not a fruit!")
    print("A", fruit)

print("A fine selection of fruits!")
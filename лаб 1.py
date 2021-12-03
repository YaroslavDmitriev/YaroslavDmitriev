import array
myArray = [5, 51, 856, 11, -5, 87, -43]

print("Максимальний від'ємний елемент - ", min(myArray))

sum = 0

for i in myArray:
    if i < 0:
        sum += i
print(" добуток від’ємних елементів масиву - ", sum)

for a in reversed(myArray):
    print(a,end=' ')
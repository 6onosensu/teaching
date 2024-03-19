
r = int(input('radius:'))
sign = "*"
for i in range(r):
    for y in range(r):
        print(sign * i)


siamese = 'Leah'
for letter in siamese:
    print(letter)
count = 0
number = 20
for num in range(number):
    count += 1
    print(num, count)


list_ = []
print(type(list_))

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    print(number)
    if number == 5:
        print(number)
        break



for y in range(10):

    for x in range(10):
        print(x, end=" ")


while x <= 10:
    print(x)
    x += 1
    x = x + 1

while True:
    print("Ctrl+C - TO STOP!!!!!")
    break

count = 0
x = 0
while x <= 5:
    x += 1
    number = float(input("Enter a number!: "))
    if number.is_integer():
        count += 1
print(count)



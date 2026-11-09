number = int(float("Enter number b/w 2 & 10"))

if number <= 0:
    print("Number cannot be zero or  negative!")
elif number == 1:
    print("Number must be higher than 1!")
elif number > 10:
    print("Number cannot be greater than 10!")
else:
    for count in range(1, 13):
        print(f"{number} * {count} = {number * count}")

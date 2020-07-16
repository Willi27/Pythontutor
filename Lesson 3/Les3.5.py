lesson = int(input())

hours = 9
minutes = 45

even = 60
not_even = 50

for i in range(1, lesson):
    if i%2 == 0:
        minutes +=even
    else:
        minutes += not_even
newHours = hours + (minutes//60)
newMinutes = minutes%60
print(newHours, newMinutes)

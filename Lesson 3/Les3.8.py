# первый момент
hours1 = int(input())
minutes1 = int(input())
seconds1 = int(input())

# второй момент
hours2 = int(input())
minutes2 = int(input())
seconds2 = int(input())

one = hours1*3600 + minutes1*60 + seconds1
two = hours2*3600 + minutes2*60 + seconds2
print(two-one)

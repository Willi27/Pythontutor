P = int(input()) # проценты
X = int(input()) # рубли
Y = int(input()) # копейки

rub = 0
cop = 0

rub = X + (X + Y*0.01)*P*365/365/100

x = round(rub)
y = (rub-x)*100
print(y)

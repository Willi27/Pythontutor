H = int(input()) # Часы
M = int(input()) # Минуты
S = int(input()) # Секунды

g = (60*60*12)/360 # скорость движения на 1 градус в секугдах
currentTime = H*3600 + M*60 + S
degrees = currentTime/120 # градусы
print(degrees)

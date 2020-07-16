inputDegrees = float(input()) # входные данные(градусы)

seconds = 12*60*60 # количество секунд в 12 часах
oneDegree = seconds/360 # 1 градус
inputSeconds = inputDegrees*oneDegree # входные данные в секундах

H = int(inputSeconds//3600)                  # Часы
x = inputSeconds = inputSeconds - H*3600
M = int(x//60)                              # Минуты
S = int(x%60)                               # Секунды
print(H,M, S)

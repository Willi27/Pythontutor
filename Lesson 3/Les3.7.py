a = int(input()) # цена: рубли
b = int(input()) # цена: копейки
n = int(input()) # количество

price1 = n*a + (n*b // 100)
price2 = (n*b)%100
print(price1, price2)

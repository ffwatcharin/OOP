import math

h1, m1, h2, m2 = [int(x) for x in input("Input : ").split()]

min = (h2-h1)*60 + (m2-m1)
hour = min/60

if(hour >= 0.25):
    hour = math.ceil(hour)
    if(1 <= hour <= 3):
        print(hour*10)
    elif(4 <= hour <= 6):
        print(30+(hour-3)*20)
    elif(hour > 6):
        print(200)
else:
    print(0)

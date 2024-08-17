def generaPares(limite):
    num=1
    while num<limite:
        yield num*2
        num=num+1

devuelvoPares = generaPares(10)

print(next(devuelvoPares))
print(next(devuelvoPares))
print(next(devuelvoPares))
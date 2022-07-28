

str = [1,3,5,6]

r = input()

for i in str:
    if i == r:
        print(str.index(i))
        break
    else:
        s= str.append(r)
        print(str.index(s))
        break
print(str)
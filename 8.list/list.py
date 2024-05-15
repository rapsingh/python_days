chai_varieties=["Lemon", "Mint", "Masala", "Green"]
print(chai_varieties)
print(chai_varieties[1:2])
chai_varieties[1:2]="Black"
print(chai_varieties)
# ['Lemon', 'B', 'l', 'a', 'c', 'k', 'Masala', 'Green'] not normal 
chai_varieties=["Lemon", "Mint", "Masala", "Green"]
chai_varieties[1:2]=["Black"]
print(chai_varieties)#now proper output
chai_varieties=["Lemon", "Mint", "Masala", "Green"]
print(chai_varieties[1:1])#output: []
chai_varieties[1:1]=["black","Chai kali"]
print(chai_varieties)
chai_varieties[1:3]=[]
print(chai_varieties)
for chai in chai_varieties:
    print(chai,end="-")
chai_varieties.append("Oolong tea")
print(chai_varieties)
print(chai_varieties.pop())
print(chai_varieties)
chai_varieties.insert(1,"black")
print(chai_varieties)
chai_varieties_copy=chai_varieties.copy()#creating copy instead of reference in memory
print(chai_varieties_copy)

squared_nums=[x**2 for x in range(10)]
print(squared_nums)


cube_nums=[x**3 for x in range(10)]
print(cube_nums)

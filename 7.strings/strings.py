chai = "Lemon Chai"
print(chai)
first_char=chai[0]
print(first_char)
slice_chai=chai[0:6]
print(slice_chai)
num_list="0123456789"
print(num_list[1:8])
print(num_list[1:8:3])
print(num_list[:8])
print(num_list[3:])
print(chai)
print(chai.upper())
print(chai.lower())
print(chai)#still not changed due to strings being immutuable
print(chai.replace("Lemon","Mint"))
print(chai)#still not changed due to strings being immutuable
chai_types="Lemon, Mint, Masala, Green"
print(chai_types.split())#default splits with spaces
print(chai_types.split(', '))
print(chai)
print(chai.find("Chai"))
print(chai.find("chai"))#find case sensitive
chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))
chai_type="Masala"
quantity=2
order="I ordered {} cups of {} chai"
print(order.format(quantity,chai_type))
chai_variety=["Lemon", "Mint", "Masala", "Green"]
print(" ".join(chai_variety))
print(", ".join(chai_variety))
chai = "He said, \" Masala chai is awesome\" "
print(chai)
tea=r"c:\user\pwd"
print(tea)#r for raw useful in windows
chai="Masala chai"
print("Masala" in chai)














chai_types = {'Masala':'Spicy','Ginger':'Zesty','Green':'Mild'}
print(chai_types)
print(chai_types['Masala'])
print(chai_types.get('Ginger'))
chai_types['Ginger']='Fresh'
print(chai_types)
for chai in chai_types:
    print(chai)
for chai in chai_types:
    print(chai,chai_types[chai])
for key,value in chai_types.items():
    print(key,value)
if 'Masala' in chai_types:
    print("Yes Masala is present in chai_types")
print(len(chai_types))
chai_types["Earl Grey"]='Exotic'
print(chai_types)
print(len(chai_types))
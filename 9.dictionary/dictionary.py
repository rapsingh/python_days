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
print(chai_types.pop('Ginger'))
print(chai_types)
print(chai_types.popitem())
print(chai_types)#earl gray removed because it was lastly added
del(chai_types['Green'])
print(chai_types)
chai_types_copy=chai_types.copy()
chai_types.popitem()
print(chai_types)
print(chai_types_copy)
tea_shop = { 'chai': {'Masala':'Spicy','Ginger':'Zesty'},'tea':{'Black':'Strong','Green':'Mild'}}
print(tea_shop)
print(tea_shop['chai'])
print(tea_shop['chai']['Masala'])
squared_num = {x:x**3 for x in range(9)}
print(squared_num)
tea_types = ("Black","Masala","Oolong")
print(tea_types)
print(len(tea_types))
#tea_types[0] = "Ginger"#not permissible
print(tea_types)
print(tea_types[1:])
more_tea=("Ginger","Herbal")
all_tea= more_tea + tea_types
print(all_tea)
more_tea=("Ginger","Herbal","Herbal")
print(more_tea.count("Herbal"))
(black,masala,oolong) = tea_types
print(masala)
print(oolong)
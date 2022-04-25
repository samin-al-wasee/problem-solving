superset = set(input("Enter Superset: ").split(" "))
how_many_subsets = int(input("How Many Subsets?: "))
list_of_subsets = []
for i in range(how_many_subsets):
    list_of_subsets.append(set(input("Enter Subset: ").split(" ")))
for subset in list_of_subsets:
    is_proper_subset = True
    for element in subset:
        if element != "" and element not in superset:
            is_proper_subset = False
            break
    if is_proper_subset is False:
        break
print(is_proper_subset)
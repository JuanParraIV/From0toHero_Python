set_A={'Colombia','Mexico', 'Bolivia'}
set_D={'asd','das', 'bbb'}
set_E={'123','Mex444ico', '5555'}
set_B={'Peru','Bolivia'}

# Union of two sets
print(set_A | set_B)
set_C= set_A.union(set_B)
print(set_C)

# Union of multiple sets
print(set_A | set_B | set_D | set_E)



# Intersection of two sets
set_C= set_A.intersection(set_B)
print(f'{set_C}')
print(set_A & set_B)

# Difference of two sets
set_C= set_A.difference(set_B)
print(set_C)
print(set_A - set_B)

# Symmetric difference of two sets
set_C= set_A.symmetric_difference(set_B)
print(set_C)
print(set_A ^ set_B)
# Subset
print(set_A <= set_B)
# Superset
print(set_A >= set_B)
# Disjoint
print(set_A.isdisjoint(set_B))
# Length
print(len(set_A)) 

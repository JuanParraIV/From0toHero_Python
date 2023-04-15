#tuples of numbers
numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))

#tuples of string
strings = ("a","b","c","d","e")
print(strings)
print(type(strings))

#tuples of mixed data types
mixed = (1,2,3,4,5,"a","b","c","d","e")
print(mixed)
print(type(mixed))

#tuples of one element
one = (1,)
print(one)
print(type(one))

#tuples of one element
one = (1)
print(one)
print(type(one))

#tuples are immutable
#numbers[0] = 10 #throws an error

#methods of the tuples
print(numbers.count(1))

print(numbers.index(2))
#print(numbers.index(6)) #throws an error

my_list = list(strings)
print(my_list)
print(type(my_list))

#converting list into a Tuple
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))
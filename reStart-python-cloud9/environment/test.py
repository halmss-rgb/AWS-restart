import copy

original = [[1, 2], 3]
print(f"original: {original}")

assignment = original 
assignment.append(4)
print(f"\nassignment: {assignment}")
print(f"original: {original}")
print(id(original) == id(assignment))


shallow = copy.copy(original)
shallow.append(5)
print(f"\nshallow: {shallow}")
print(f"original: {original}")
print(id(original) == id(shallow))
shallow[0].append('lohe')
print(f"shallow: {shallow}")
print(f"original: {original}")
print(id(original[0]) == id(shallow[0]))


deep = copy.deepcopy(original)
deep.append(6)
print(f"\ndeep: {deep}")
print(f"original: {original}")
print(id(original) == id(deep))
deep[0].append('hello')
print(f"deep: {deep}")
print(f"original: {original}")
print(id(original[0]) == id(deep[0]))


x = [1,3,4,5]
x.insert(1, 2)
print(x)
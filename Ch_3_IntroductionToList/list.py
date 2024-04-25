name = ['love', 'food', 'peace', 'happy']
print(name[0].title())
print(name)
name[-2] = 'USA'
print(name)
a = name.append('data science')
print(a)
position = [1, 3]

# Sort the positions in reverse order to avoid index shifting issues
#position.sort(reverse=True)

# Delete elements from the name list based on indices
for i in position:
    del name[i]

print(name)
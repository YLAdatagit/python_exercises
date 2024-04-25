people_list = ['joanna', 'harry', 'snape', 'ron', 'gorge']
print(f"Dear {people_list[1].title()}, I would like to invite you to dinner.")

cannot_join = people_list.pop()
print(people_list)
people_list.append('wayne')
print(people_list)
print(f"Dear {people_list[4].title()}, can you join dinner?")
people_list.insert(0,'mike')
print(people_list)
people_list.insert(3,'yake')
print(people_list)
people_list.sort()
print(people_list)
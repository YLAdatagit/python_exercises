alien_0 = {'color': 'green', 'speed' : 'slow'}
#use .get function ('input', 'result if nothing exists')
point_value = alien_0.get('speed', 'No point assigned.')
print(point_value)
#.items() for pairs.
#.values() for values.
#blank or .keys() for keys.

for alien in alien_0.items():
    print(alien)

for x,y in alien_0.items():
    print(f"\nIts {x} is {y}")
    #print(f"Value: {y}")

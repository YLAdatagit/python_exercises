
aliens = []
for alien_number in range (30):
    new_alien = {'color' : 'green', 'points': 5, 'speed' : 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['speed'] = 'medium'
    print(alien)
for alien in aliens[5:9]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'high'
        alien['points'] = 15
    print(alien)
print(f"\n This is updated one")
for alien in aliens:
    if alien['color'] == "red":
        alien['points'] = 20
    elif alien['color'] == 'yellow':
        alien['points'] = 25
    else:
        alien['points'] = 100
        
    print(alien)



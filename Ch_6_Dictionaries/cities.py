prompt = "\n Please enter the name of city you'd like to go:"
prompt += "\n(Enter 'quit' when you are finished)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to city {city.title()}")
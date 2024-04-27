responses = {}
polling_active = True
while polling_active:
    name = input("\n What is your name?")
    response = input("Which mountain whould you like to clime someday?")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False
print(responses)
print("\n___Poll result___")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
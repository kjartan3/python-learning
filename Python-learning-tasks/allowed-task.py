age = input('How old are you? ')
boo = age.isnumeric()

if boo:
    print('You are', int(age), 'years old.')
    val = int(age)
    if val >= 18:
        print('You are allowed in and allowed to drink alcohol.')
    elif val >= 16:
        print('You are allowed in but not allowed to drink.')
    else:
        print('You are not allowed to in. Not old enough.')
else:
    print('We need your age')
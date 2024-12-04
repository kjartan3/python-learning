# list of string functions


name = 'Jamie Foxx'
val = len(name)  # declares the length of the string 

findThis = "Carrot"
val = (findThis in name)  # finds if the string is contained in the value of name
val = (findThis not in name)  # finds if the string is NOT contained in the value of name

val = name[0:5]  # selects out the first 5 characters of the string (slicing out the rest)

val = name[4:7]

val = name.upper()
val = name.lower()
val = name.strip() # strips out the spacing between the words

val = name.replace('e', '').strip().upper() # removes the e from the string name and strips out the spaces, then finally makes it uppercase

print(name)
print(val)
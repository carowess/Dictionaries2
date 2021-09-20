phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}

# this is a dictionary of string objects
# this has a key and a value
# if you want to get the corresponding value, you have to know the key


print()
print("*****  start section 1 - print dictionary ********")
print()


print(phonebook)

print(phonebook["Chris"])

print(phonebook["Chri"])

print()
print("*****  end section 1 ********")
print()


print()
print("*****  start section 2 - search dictionary ********")
print()

if "Chris" in phonebook:
    print(phonebook["Chris"])
else:
    print("Key not found")


print()
print("*****  end section 2 ********")
print()


print()
print("*****  start section 3 - edit/append dictionary ********")
print()

print(phonebook)
phonebook["Joe"] = "555-1234"
phonebook["Chris"] = "555-9999"
print(phonebook)


print()
print("*****  end section 3 ********")
print()


print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()


del phonebook["Chris"]
# del phonebook["John"]

print(len(phonebook))
# prints out the number of elements in the dict.

print()
print("*****  end section 4 ********")
print()


print()
print("*****  start section 5 - iterate through keys ********")
print()

for key in phonebook:
    print(key)
    print(phonebook[key])


print()
print("*****  end section 5 ********")
print()


print()
print("*****  start section 6 - iterate through values  ********")
print()

for v in phonebook.values():
    print(v)


print()
print("*****  end section 6 ********")
print()


print()
print("*****  start section 7 - iterate through both key and value pair********")
print()

for k, v in phonebook.items():
    print("Key is: " + k + " and value is " + v)

for item_tuple in phonebook.items():
    print(item_tuple)

print(phonebook.get("John", "key does not exist"))
print(phonebook.get("Chris", "key does not exist"))


print()
print("*****  end section 7 ********")
print()


print()
print("*****  start section 8 - using random and converting to list ********")
print()

import random

list_of_keys = list(phonebook)
# print(list_of_keys)
# print(type(list_of_keys))

random_key = random.choice(list_of_keys)
print(random_key)
print(phonebook[random_key])


print()
print("*****  end section 8 ********")
print()

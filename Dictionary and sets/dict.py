#It works in key and value pair.

marks={"Om":89,"Subham":78,"Nischay":56,"Abhisek":90}

# Here if i write same key again with different value then it will impact on existing
# key and old key value replace with new key value.

# marks={"Om":89,"Subham":78,"Nischay":56,"Abhisek":90,"Om":78} 

print(marks,type(marks))

print(marks["Om"])  


#Methods of dictionary.

#It will display all the dictionary item in tuple format.
print(marks.items())

#It will display all the key value.
print(marks.keys())

#It will display all the key value.
print(marks.values())

#Get will display value of key
print(marks.get("Om"))

#It will update a data.
marks.update({"Subham":65})
print(marks)

#Particular it will remove key and value from dictionary.
value = marks.pop('Nischay') 
print(marks)

#It will remove key and value pair from ending.
value_item = marks.popitem()  
print(marks)




# Example Dictionary
person = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Adding a new key-value pair
person['email'] = 'john@example.com'
print(person)

# Using get() to access a value
print(person.get('age')) 

# Using setdefault()
print(person.setdefault('phone', '123-456-7890'))
print(person)

# Using update() to merge dictionaries
additional_info = {'gender': 'Male', 'married': True}
person.update(additional_info)
print(person)

# Removing a key-value pair with pop()
removed_value = person.pop('email')
print(f"Removed Value: {removed_value}")
print(person)

# Clearing the dictionary
person.clear()
print(person)  # Output: {}

 
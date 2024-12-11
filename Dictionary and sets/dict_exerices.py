age = {"Om": 20, "Karan": 35, "Anand": 65, "Rajkumar": 45, "Ranbir": 50}

# Sort dictionary by keys
sorted_keys = sorted(age.keys())

sorted_value = sorted(age.values())

sorted_dict = sorted(age.items())

print("Sorted key:", sorted_keys)
print("Sorted value:", sorted_value)
print("Sorted dict:", sorted_dict)


#Practice..

#Create dictionary with hindi word and translate in english word.
# words={"madad":"Help","khursi":"Chair","billi":"Cat","niklo":"Get Out"}

# word = input("Enter word you want to know in english: ")
# print(words[word])


#2

dic={}

for i in range(4):
    name = input("Enter Name:->")
    language = input("Enter Language:->")
    dic.update({name:language})
print(dic)

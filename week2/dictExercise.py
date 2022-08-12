# Exercise 1
phonebook_dict = { 'Alice': '703-493-1834', 'Bob': '857-384-1234', 'Elizabeth': '484-584-2923' }

print(phonebook_dict['Alice'])              #prints Alice's phone number

phonebook_dict['Kareem'] = '938-489-1234'   #updating phonebook_dict
print(phonebook_dict)                       #prints updated phonebook_dict

del phonebook_dict['Alice']                 #deleting Alice's entry
print(phonebook_dict)                       #prints phonebook_dict

phonebook_dict['Bob'] = '968-345-2344'      #changing Bob's number
print(phonebook_dict)                       #prints phonebook_dict

# --------------------------------------------------------------------------------------------------------
# Exercise 2
ramit = { 'name': 'Ramit', 'email': 'ramit@gmail.com',
        'interests': ['movies', 'tennis'], 'friends': [ { 'name': 'Jasmine',
        'email': 'jasmine@yahoo.com', 'interests': ['photography', 'tennis'] },
        { 'name': 'Jan', 'email': 'jan@hotmail.com', 'interests': ['movies', 'tv'] } ] }

print(ramit['email'])                           #prints Ramit's email

print(ramit['interests'][0])                    #prints Ramit's first interest

print(ramit['friends'][0]['email'])             #prints Jasmine's email

print(ramit['friends'][1]['interests'][1])      #prints Jan's second interest

# ---------------------------------------------------------------------------------------------------------
#Exercise 3
userIn = input('Enter a word : ')

histogram = {}
for i in userIn:
    if i in userIn:
        userIn[i] = 1
    else:
         userIn[i] = userIn[i] + 1

print(userIn[i])





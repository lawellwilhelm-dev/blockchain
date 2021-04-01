# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
people = [
    {
        'name': 'Kojo',
        'age': 31,
        'hobbies': ['playing guitar', 'watching movies', 'writing play']
    },
    {
        'name': 'Kofi',
        'age': 36,
        'hobbies': ['playing basketball', 'watching movies']
    }
]

# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
names = [person['name'] for person in people]

# 3) Use a list comprehension to check whether all persons are older than 20.
all_older_than_30 = all([person['age'] > 20 for person in people])

# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
#copied_people = people[:]
people_copy = [{k:v for k,v in person.items()} for person in people]

# 5) Unpack the persons of the original list into different variables and output these variables.
yram, franck = people 

print(yram)

print(franck)


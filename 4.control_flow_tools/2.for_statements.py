# 4.2. for Statements

animalList = ['cat', 'dog', 'tiger', 'monkey']

for animal in animalList:
    print(animal, len(animal))

# return:
    # cat 3
    # dog 3
    # tiger 5
    # monkey 6
    
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    print(user, status)
    if status == 'inactive':
        del users[user]
    print(users)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
    print(active_users)


for i in range(5):
    print(i)
    
    
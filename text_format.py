person = {'name':'Mohamed Eldesouki', 'username': 'disooqi', 'age': 36, 'occupation': 'Research Associate',
          'affiliation': 'QCRI'}

sentence = 'My name is '+person['name']+', I am '+str(person['age'])+' old, I work as '+person['occupation']+' at '+\
      person['affiliation']+'. I always use '+person['username']+' as my username.'

sentence1 = 'My name is {}, I am {} old, I work as {} at {}. I always use {} as my username.'.format(person['name'],
                                      person['age'], person['occupation'], person['affiliation'], person['username'])

sentence2 = 'My name is {0}, I am {1} old, I work as {2} at {3}. I always use {4} as my username.'.format(person['name']
                                    , person['age'], person['occupation'], person['affiliation'], person['username'])

sentence3 = 'My name is {0[name]}, I am {1[age]} old, I work as {2[occupation]} at {3[affiliation]}. I always use ' \
            '{4[username]} as my username.'.format(person, person, person, person, person)

sentence4 = 'My name is {0[name]}, I am {0[age]} old, I work as {0[occupation]} at {0[affiliation]}. I always use ' \
            '{0[username]} as my username.'.format(person)

personlist = ['Mohamed Eldesouki', 'disooqi', 36, 'Research Associate','QCRI']

sentence5 = 'My name is {0[0]}, I am {0[1]} old, I work as {0[2]} at {0[3]}. I always use {0[4]} as my username.'.format(personlist)


class Person:
    def __init__(self, name, age, username, occupation, affiliation):
        self.name = name
        self.age = age
        self.username = username
        self.occupation = occupation
        self.affiliation = affiliation


disooqi = Person('Mohamed Eldesouki', 36, 'disooqi', 'Research Associate','QCRI')
sentence6 = 'My name is {0.name}, I am {0.age} old, I work as {0.occupation} at {0.affiliation}. I always use ' \
            '{0.username} as my username.'.format(disooqi)

sentence7 = 'My name is {name}, I am {age} old, I work as {occupation} at {affiliation}. I always use ' \
            '{username} as my username.'.format(name='Mohamed Eldesouki', age=36, username='disooqi', occupation='Research Associate', affiliation='QCRI')

sentence8 = 'My name is {name}, I am {age} old, I work as {occupation} at {affiliation}. I always use ' \
            '{username} as my username.'.format(**person)


for i in range(5, 15):
    print('The number is {:02}'.format(i))

PI = 3.14159265359
print('PI value is {:.2f}'.format(PI))

xx = 99999999999
print('PI value is {:,}'.format(xx))
print('PI value is {:,.2f}'.format(xx))


import datetime
today = datetime.datetime(2018, 10, 3, 21, 47, 50)
print(today)

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
print('{:%B %d, %Y}'.format(today))
print('{0:%B %d, %Y} which is {0:%A} and {0:%j}th day of the year.'.format(today))
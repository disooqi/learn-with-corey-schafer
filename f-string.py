from datetime import datetime
my_name = 'Mohamed Eldesouki'
occupation = 'software engineer'
age = 36

print(f'My name is {my_name}, I am {age} and I work as {occupation}')

disooqi = {'my_name': 'Mohamed Eldesouki', 'occupation': 'software engineer', 'age': 36}
print(f"My name is {disooqi['my_name']}, I am {disooqi['age']} and I work as {disooqi['occupation']}")


for n in range(1, 11):
    print(f'This is number {n:02.3f}')


birthday = datetime(day=12, month=3, year=1982)
print(f'I was born on {birthday:%B %d, %Y}')


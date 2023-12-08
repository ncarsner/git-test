import random
from data_points import students, departments

for i in range(len(students)):
    print(f'{students[i]}: {random.choice(departments)}')
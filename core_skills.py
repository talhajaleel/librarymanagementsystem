# rand_list =

# list_comprehension_below_10 =

# list_comprehension_below_10 =

#  Description:
# Complete the following Python tasks in the core_skills.py file.
# Create a list of 10 random numbers between 1 and 20.
# Filter Numbers Below 10 (List Comprehension)
# Filter Numbers Below 10 (Using filter)

import random
#1
all_nums = [i for i in range(0,21)]
random_numbers = [random.choice(all_nums) for i in range(10)]

#2
below_10 = [i for i in random_numbers if i<10]

#3
below_10 = filter(lambda x:x<10 , random_numbers)

if __name__=='main':
    print('**')
# PJ VanDussen
# 10/22/24
# Randomness Starter
# 1
import random
# colors = ['red', 'green', 'blue', 'yellow', 'purple']
# length_colors = len(colors)
# rand_index_num = random.randrange(0,length_colors)
# print(f'your random index number is: {rand_index_num}')
# print(f'your random color is: {colors[rand_index_num]}' )
# 2
# animals = ['cheetah', 'girafe', 'elaphant', 'dolphin', 'whale', 'bird']
# length_animal = len(animals)
# rand_index_num2 = random.randrange(0, length_animal)
# rand_index_num3 = random.randrange(0, length_animal)
# rand_index_num4 = random.randrange(0, length_animal)
# print(f'your index number is: {rand_index_num2}')
# print(f'your animal is: {animals[rand_index_num2]}')
# print(f'your animal is: {animals[rand_index_num3]}')
# print(f'your animal is: {animals[rand_index_num4]}')
# 3
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# length_nums = len(nums)
# rand_index_num3 = random.randrange(0, length_nums)


# Using randint () to generate a random integer
# Randomly generated integer will be the index number we want to use
students = ['PJ', 'Matt', 'Ethan', 'Trent', 'Dax']

# rand_integer = random.randint(0, 4)

start = 0
stop = 4
rand_integer = random.randint(start, stop)

print(f'The random integer is: {rand_integer}')
print(f'{students[rand_integer]} is the name that was pulled at random from the list.')
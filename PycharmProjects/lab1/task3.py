import random


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    rand_number = random.choice(numbers)
    less_than_rand = [num for num in numbers if num < rand_number]
    more_than_rand = [num for num in numbers if num > rand_number]
    equal_with_rand = [num for num in numbers if num == rand_number]
    return quick_sort(less_than_rand) + equal_with_rand + quick_sort(more_than_rand)


with open('/home/eugene/PycharmProjects/lab1/forTask3', 'r', encoding='utf-8') as file:
    nums = []
    for line in file:
        words = line.split()
        nums = nums + [int(word) for word in words]
print(nums)
print(quick_sort(nums))

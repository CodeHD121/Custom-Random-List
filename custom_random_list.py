import random

# creates a random list, with x amounts of digits (nums_limit), between y(start) and z(finish)
def random_list(nums_limit,start,finish):
    nums_list = []
    nums_count = 0
    while nums_count <= nums_limit:
        nums_list.append(random.randint(start,finish))
        nums_count += 1
    return nums_list

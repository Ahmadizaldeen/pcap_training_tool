numbers = (1, 2, 5, 9, 15)

def filter_numbers(num):
    nums = (1, 5, 17)
    if num in nums:
        return True
    else:
        return False


filtered_numbers = filter(filter_numbers, numbers)
print(type(filtered_numbers))  # <class 'filter'>
print(filtered_numbers)
for n in filtered_numbers:
    print(n)

numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print(result) # <map object at 0x7fabc1234>
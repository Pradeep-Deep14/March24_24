def extract_odd_values(lst):
    return[value for index, value in enumerate(lst) if value %2!=0]

numbers=[1,2,3,4,5,6,7,8,9]
print(extract_odd_values(numbers))
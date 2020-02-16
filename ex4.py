
def is_valid(number):
    return is_increasing(number) and has_double(number) and has_one_double(number)


def is_increasing(number):
    prev_number = None
    for i in str(number):
        if prev_number and i < prev_number:
            return False
        prev_number = i
    return True


def has_double(number):

    prev_number = None
    for i in str(number):
        if i == prev_number:
            return True
        prev_number = i
    return False

def has_one_double(number):

    dictionary = dict()
    for i in str(number):
        dictionary[i] = dictionary.get(i,0) + 1

    print(dictionary)
    for j in dictionary:
        if dictionary[j] == 2:
            return True

    return False


numbers = list(range(172851,675869+1))
print('len:',len(numbers))

valid_numbers = [number for number in numbers if is_valid(number)]
print('len_valid:',len(valid_numbers))
print('valid_numbers:', valid_numbers)




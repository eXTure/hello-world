#Correct solution:
#def rotate(string, n):
#    return string[n:] + string[:n]


import collections

def clean_string(rotated_string):
    other_string = ''
    symbol_check = False
    for i in rotated_string:
        if i=='!':
            other_string += i
            symbol_check = False
        elif i==' ':
            if symbol_check:
                other_string += i
                symbol_check = False
                continue
            symbol_check = True
        elif i.isalpha():
            symbol_check = False
            other_string += i
    return other_string

def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    if n>0:
        sliced_string1 = list(string[n:])
        sliced_string2 = list(string.replace(string[n:], ''))
        rotated_string = str(sliced_string1 + sliced_string2)
        result_string = clean_string(rotated_string)
    elif n<0:
        sliced_string1 = list(string[:n])
        sliced_string2 = list(string.replace(string[:n], ''))
        rotated_string = str(sliced_string2 + sliced_string1)
        result_string = clean_string(rotated_string)

    return result_string


def test_small_rotate():
    assert rotate('hello', 2) == 'llohe'
    assert rotate('hello', -2) == 'lohel'

print(test_small_rotate())

def test_bigger_rotation_of_positive_n():
    string = 'bob and julian love pybites!'
    expected = 'love pybites!bob and julian '
    assert rotate(string, 15) == expected

print(test_bigger_rotation_of_positive_n())

def test_bigger_rotation_of_negative_n():
    string = 'pybites loves julian and bob!'
    expected = 'julian and bob!pybites loves '
    assert rotate(string, -15) == expected

print(test_bigger_rotation_of_negative_n())

def test_rotation_of_n_same_as_len_str():
    string = expected = 'julian and bob!'
    assert rotate(string, len(string)) == expected

print(test_rotation_of_n_same_as_len_str())

def test_rotation_of_n_bigger_than_string():
    string = 'julian and bob!'
    expected_solution1 = 'julian and bob!'
    expected_solution2 = ' bob!julian and'  # ;)
    assert rotate(string, 100) in (expected_solution1,
                                   expected_solution2)

    # should be the same as doing a rotate with modulo
    # which is 100 % 15 (len string) => n=10
    mod = 100 % len(string)  # 10
    assert rotate(string, mod) in (expected_solution1,
                                   expected_solution2)

print(test_rotation_of_n_bigger_than_string())

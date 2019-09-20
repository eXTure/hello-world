import collections

def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    if n>0:
        sliced_string1 = list(string[n:])
        sliced_string2 = list(string.replace(string[n:], ''))
        print(sliced_string1, sliced_string2)
        clean_string = str(sliced_string1 + sliced_string2)

        temp_string = ''
        other_string = ''
        for i in clean_string:
            print(i, 1)
            if i != ' ' or i != ',' or i != '[' or i != ']' or i != "'":
                temp_string += i
                print(temp_string, 2)
            else:
                other_string += temp_string
                print(other_string, 3)


        print(other_string, 4)
        #clean_string = clean_string.replace('[', '')
        #clean_string = clean_string.replace("'", '')
        #clean_string = clean_string.replace(']', '')
        #clean_string = clean_string.replace(',', '')
        #clean_string = clean_string.replace(' ', '')
        result_string = other_string
    elif n<0:
        sliced_string = string[:abs(n)]
        clean_string = string.replace(sliced_string, '')
        result_string = clean_string + sliced_string
    else:
        result_string = string

    return result_string


#print(rotate('bob and julian love pybites!', 15))
print(rotate('hello', 2), 5)

def test_small_rotate():
    assert rotate('hello', 2) == 'llohe'
    assert rotate('hello', -2) == 'lohel'

#print(test_small_rotate())

def test_bigger_rotation_of_positive_n():
    string = 'bob and julian love pybites!'
    expected = 'love pybites!bob and julian '
    assert rotate(string, 15) == expected

#print(test_bigger_rotation_of_positive_n())

def test_bigger_rotation_of_negative_n():
    string = 'pybites loves julian and bob!'
    expected = 'julian and bob!pybites loves '
    assert rotate(string, -15) == expected


def test_rotation_of_n_same_as_len_str():
    string = expected = 'julian and bob!'
    assert rotate(string, len(string)) == expected


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

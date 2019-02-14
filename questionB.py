
import random

def stringCompare(str1, str2):
    '''
    Declares which of the two input strings is larger

    Parameters:
    str1 (str): first string to compare
    str2 (str): second string to compare

    Returns:
    str: message declaring which of the input strings is bigger
    '''

    if type(str1) != type('') or type(str2) != type(''):
        raise Exception("inputs must be strings")

    acceptable_chars = [str(i) for i in range(0,10)]

    punc_count = 0
    for index, char in enumerate(str1):
        if char == '-':
            if index != 0:
                raise Exception('strings may only contain numeric digits, a period, or a negative sign')
        elif char == '.':
            if punc_count == 0:
                punc_count+=1
            else:
                raise Exception('strings may contain only one comma or one period')
        elif char not in acceptable_chars:
            raise Exception('strings may only contain numeric digits, a period, or a negative sign')

    punc_count = 0
    for index, char in enumerate(str2):
        if char == '-':
            if index != 0:
                raise Exception('strings may only contain numeric digits, a period, or a negative sign')
        elif char == '.':
            if punc_count == 0:
                punc_count+=1
            else:
                raise Exception('strings may contain only one comma or one period')
        elif char not in acceptable_chars:
            raise Exception('strings may only contain numeric digits, a period, or a negative sign')

    str1 = float(str1)
    str2 = float(str2)

    if str1 == str2:
        return "{} is equal to {}".format(str1, str2)
    else:
        return "{} is greater than {}".format(max([str1, str2]), min([str1, str2]))



tests = [(str(random.uniform(-1000000, 1000000)), str(random.uniform(-1000000, 1000000))) for i in range(10)]
for test in tests:
    print(stringCompare(test[0], test[1]))

# should fail
print(stringCompare('-1-.2.3', '123'))
print(stringCompare('1-.2.3', 123))
# should pass
print(stringCompare('-13.', '123'))
print(stringCompare('-.123', '123'))

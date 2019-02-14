def xAxisOverlap(line1, line2):
    '''
    Determines if the x-axis interval inputs overlap

    Parameters:
    line1 (list/tuple): two numerical coordinates on an x-axis
    line2 (list/tuple): two numerical coordinates on an x-axis

    Returns:
    bool:  indicates if intervals overlap
    '''

    assert isinstance(line1, tuple) or isinstance(line1, list) and isinstance(line2, tuple) or isinstance(line2, list) , "args must be list or tuple"

    for num in list(line1) + list(line2):
         assert isinstance(num, (int, float)) , "coordinate values must be int or float"

    assert len(line1) == 2 and len(line2) == 2 , "each arg must consist of two numbers"

    x1 = line1[0]
    x2 = line1[1]
    x3 = line2[0]
    x4 = line2[1]

    if x1==x2 or x3==x4:
        raise ValueError("coordinates of a line must have different values")

    if x2 > x1 or x4 > x3:
        raise ValueError("coordinate values must be in ascending order")


    if (x3 >= x1 and x3 <= x2) or (x4 >= x1 and x4 <= x2):
        return True
    else:
        return False

test_cases = [((1,2), (2, 4)),
              ((1,5), (2, 4)),
              ((1,1), (2, 4)),
              ((4,2), (2, 4)),
              ((4,6), (2, 5)),
              ((1,6), (2, 4)),
              ((1,6), (8, 10))]


for case in test_cases:
    print(xAxisOverlap(case[0], case[1]))

# more test test test cases
# these should all fail

# print(xAxisOverlap('1,2', [1,2]))
# print(xAxisOverlap([1], [1,2]))
# print(xAxisOverlap([1, '2'], [1,2]))
# print(xAxisOverlap([1,2], [1,2,3]))
# print(xAxisOverlap([2,2], [1,2]))
# print(xAxisOverlap([3,2], [1,2]))

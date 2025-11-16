def low_or_high_check(number : int) -> str:
    if number <= 18:
        return "LOW"
    else:
        return "HIGH"

def which_column(number : int) -> int:
    column_1 = range(1, 37, 3)
    column_2 = range(2, 37, 3)
    column_3 = range(3, 37, 3)

    if number in column_1:
        return 1
    elif number in column_2:
        return 2
    elif number in column_3:
        return 3
    else:
        return -1
def which_dozen(number : int) -> int:
    dozen_1 = range(1, 13)
    dozen_2 = range(13, 25)
    dozen_3 = range(25, 37)

    if number in dozen_1:
        return 1
    elif number in dozen_2:
        return 2
    elif number in dozen_3:
        return 3
    else:
        return -1
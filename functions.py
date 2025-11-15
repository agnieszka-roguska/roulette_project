def low_or_high_check(number : int) -> str:
    if number <= 18:
        return "LOW"
    else:
        return "HIGH"

def which_column(number):
    column_1 = range(1, 35, 3)
    column_2 = range(2, 36, 3)
    column_3 = range(3, 36, 3)

    if number in column_1:
        return 1
    elif number in column_2:
        return 2
    elif number in column_3:
        return 3
    else:
        return -1
def which_dozen(number):
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
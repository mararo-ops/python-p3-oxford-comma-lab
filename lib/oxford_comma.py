# lib/oxford_comma.py

def oxford_comma(array):
    if len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return f"{array[0]} and {array[1]}"
    else:
        comma_separated = ", ".join(array[:-1])
        return f"{comma_separated}, and {array[-1]}"

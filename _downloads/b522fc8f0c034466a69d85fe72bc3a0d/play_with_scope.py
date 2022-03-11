"""
some example code to play with scope
"""

def start_at(x):
    def increment_by(y):
        return x + y
    return increment_by

closure_1 = start_at(3)
closure_2 = start_at(5)
closure_1(2)
start_at(2)(4)


def make_um_counter():
    series = []
    def um_counter(new_word):
        series.append(new_word)  # free variable
        count = 0
        for i in series:
            if i == 'um':
                count += 1
        return count
    return um_counter


def make_um_counter2():
    count = 0

    def um_counter2(new_word):
        if new_word == 'um':
            count += 1
        return count
    return um_counter2


# try using nonlocal:
def make_um_counter3():
    count = 0

    def um_counter3(new_word):
        nonlocal count
        if new_word == 'um':
            count += 1
        return count
    return um_counter3

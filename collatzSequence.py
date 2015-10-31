__author__ = 'taztony2010'


# function returns the collatz sequence
def collatz(number):
    if int(number) % 2 == 0:  # checks is number is even
        return int(number) // 2
    else:
        return 3 * int(number) + 1


def run():
    user_num = raw_input()
    while user_num != 1:
        try:
            user_num = collatz(user_num)
            print(int(user_num))
        except ValueError as e:  # catches non integer entered
            print(e)
            user_num = raw_input()  # gets new input


run()

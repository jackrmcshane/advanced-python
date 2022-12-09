
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def myFunc(arg1, arg2, *, suppressExceptions=False):
    pass 


def main():
    # print(addition(5, 10, 15, 20))
    # print(addition(1, 2, 3))


    # # passing a list
    # myNums = [5, 10, 15, 20]
    # print(addition(*myNums))




    # myFunc(1, 2, True) throws error because standalone * forces separation of positional and keyword args
    myFunc(1, 2, suppressExceptions=True)


if __name__ == "__main__":
    main()

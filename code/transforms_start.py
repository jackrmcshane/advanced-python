# using functions linke sorted, filter, map

def filterFunc(x):
    if x % 2 == 0:
        return False
    return True

def filterFunc2(x):
    if x.isupper():
        return False
    return True

def squareFunc(x):
    return x**2

def toGrade(x):
    if x >= 90:
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 60 and x < 70):
        return "D"
    return "F"
    

def main():
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = sorted((81, 89, 94, 67, 61, 66, 99, 74))


    odds = list(filter(filterFunc, nums)) # return only odd numbers
    print(odds)

    lowers = list(filter(filterFunc2, chars))
    print(lowers)
    
    # the map function
    squares = list(map(squareFunc, nums))
    print(squares)

    letter_grades = list(map(toGrade, grades))
    print(letter_grades)


if __name__ == "__main__":
    main()


def main():
    # define lists
    days = ["sun", 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    daysFr = ['dim', 'lun', 'mar', 'mer', 'jeu', 'ven', 'sam']

    # use iter to create an iterator over a collection
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))

    # iterate using an iterator and sentinal
    with open('textfile.txt', 'r') as f:
        for line in iter(f.readline, ''): # '' is the sentinal value
            print(line)


    # use regular iteration over the days
    for day in days:
        print(day)


    # use enumerate
    for ind, day in enumerate(days, start=1):
        print(ind, day)


    # use zip func
    for day_tup in zip(days, daysFr):
        print(day_tup)


    # combinations
    for ind, itm in enumerate(zip(days, daysFr), start=1):
        print(ind, itm[0], "=", itm[1], "in French")


if __name__ == "__main__":
    main()

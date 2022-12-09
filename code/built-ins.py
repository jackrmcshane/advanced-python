
def main():
    list1 = [1, 2, 3, 0, 5, 6]

    # any will return true if any of the sequence values are true
    print(any(list1))

    # all will return true only if all values are true
    print(all(list1))

    # min and max will return minimum and maximum values in a sequence
    print(min(list1))
    print(max(list1))

    # use sum() to sum up all values in a sequence
    print(sum(list1))


if __name__ == "__main__":
    main()

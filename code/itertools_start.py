
import itertools


def testFunc(x):
    return x < 40


def main():
    # cycle iterator can be used to cycle over a collection
    seq1 = ["joe", 'john', 'mike']
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))


    # use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))


    # accumulate creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    acc = itertools.accumulate(vals) # can pass a function for the accumulation method
    print(list(acc))
    acc = itertools.accumulate(vals, max) # can pass a function for the accumulation method
    print(list(acc))

    
    # use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))


    # dropwhile and takewhile will return values until
    print(list(itertools.dropwhile(testFunc, vals))) # will drop items from the sequence while test function returns true, will return every value after that
    print(list(itertools.takewhile(testFunc, vals))) # will return values while test funcn return true, will stop returning after that
    


if __name__ == "__main__":
    main()

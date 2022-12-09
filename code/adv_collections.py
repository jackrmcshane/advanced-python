import collections
import string


def named_tuple():
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1, p2)
    print(p1.x, p2.y)


    # use _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1.x, p2.y)


def default_dict():
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # count the elements in the list
    fruitCounter = {}
    for fruit in fruits:
        if fruit in fruitCounter.keys():
            fruitCounter[fruit] += 1
        else:
            fruitCounter[fruit] = 1

    # print result
    for k, v in fruitCounter.items():
        print(k + ": " + str(v))



    # making it more readable
    fruitCounter = collections.defaultdict(int)
    for fruit in fruits:
        fruitCounter[fruit] += 1

    # print result
    for k, v in fruitCounter.items():
        print(k + ": " + str(v))



def counters():
    class1 = ['bob', 'becky', 'chad', 'darcy', 'frank', 'hannah', 'kevin', 'james', 'james', 'melanie', 'penny', 'steve']
    class2 = ['bill', 'barry', 'cindy', 'debbie', 'frank', 'gabby', 'kelly', 'james', 'joe', 'sam', 'tara', 'ziggy']


    # crate a counter for class1 and class2 
    c1 = collections.Counter(class1)
    c2 = collections.Counter(class2)


    # how many students in class 1 named james?
    print(c1["james"])


    # how many students in class 1?
    print(sum(c1.values()), " students in class 1")


    # combine the two classes
    c1.update(class2)
    print(sum(c1.values()), " students in class 1")


    # what is most common name?
    print(c1.most_common(3)) # prints 3 most common elements in the collection


    # separate the classes again
    c1.subtract(class2)
    print(c1.most_common(3))


    # intersection of the 2 classes
    print(c1 & c2)





def ordered_dict():
    sportsTeams = [
            ('Royals', (18, 12)),
            ('Rockets', (24, 6)),
            ('Cardinals', (20, 10)),
            ('Dragons', (22, 8)),
            ('Kings', (15, 15)),
            ('Chargers', (20, 10)),
            ('Jets', (16, 14)),
            ('Warriors', (25, 5))
    ]


    # sort teams by number of wins
    sortedTeams = sorted(sportsTeams, key=lambda t: t[1][0], reverse=True)


    # create an ordered dictionary of the teams
    teams = collections.OrderedDict(sortedTeams)
    print(teams)


    # use popitem to remove the top item
    team, wl = teams.popitem(False)
    print("top team: ", team, wl)


    # who are next the top 4 teams?
    for ind, team in enumerate(teams, start=1):
        print(ind, team)
        if ind == 4: break


    # test for equality
    a = collections.OrderedDict({"a" : 1, "b" : 2, "c" : 3})
    b = collections.OrderedDict({"a" : 1, "b" : 2, "c" : 3})
    print('equality test: ', a == b)


def de_que():

    # initialize deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)


    # deques support the len() func
    print("Item count: ", str(len(d)))


    # deques can be iterated over
    for elem in d:
        print(elem.upper(), end=',')
    print()


    # manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)


    # rotate the deque
    d.rotate(10)
    print(d)




def main():
    # named_tuple()
    # default_dict()
    # counters()
    # ordered_dict()
    de_que()


if __name__ == "__main__":
    main()

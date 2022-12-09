
def basic_comprehensions():
    # define two lists
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


    # perform a mapping
    evenSquared = list(map(lambda e: e**2, evens))
    print(evenSquared)

    evenSquared = list(
            map(lambda e: e**2, filter(lambda e: e>4 and e<16, evens))
    )

    print(evenSquared)


    # derive a new list of number from a given list
    evenSquared = [e**2 for e in evens]
    print(evenSquared)


    # limit the items operated on with a predicate condition
    oddSquared = [e**2 for e in odds if e > 3 and e < 17]
    print(oddSquared)



def dict_comprehensions():
    # define list of temps
    ctemps = [0, 12, 34, 100]


    # use comprehension to build a dict
    tempDict = {t: (t*9/5) + 32 for t in ctemps if t < 100}
    print(tempDict)
    print(tempDict[12])


    # merge two dicts with a comprehension
    team1 = {'jones': 24, 'jameson':18, 'smith':58, 'burns':7}
    team2 = {'white':12, 'macke':88, 'perce':4}

    newTeam = {k:v for team in (team1, team2) for k,v in team.items()} # concat dicts
    print(newTeam)




def set_comprehensions():
    # define temps
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]
    ftemps1 = [(t*9/5)+32 for t in ctemps]
    print(ftemps1)


    # build set of unique fahrenheit temperatures
    ftemps2 = {(t*9/5)+32 for t in ctemps}
    print(ftemps2)


    # build a set from an input source
    sTemp = 'the quick brown fox jumped over the lazy dog'
    chars = {c.upper() for c in sTemp if not c.isspace()}
    print(chars)



def main():
    # basic_comprehensions()
    # dict_comprehensions()
    set_comprehensions()


if __name__ == "__main__":
    main()

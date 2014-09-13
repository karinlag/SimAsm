__author__ = 'karinlag'


def calculateN50(listOfNumbers):
    listOfNumbers.sort()
    listOfNumbers.reverse()
    theorN50 = sum(listOfNumbers)/2


    tot= 0
    N50 = 0
    for num in listOfNumbers:
        tot += num
        if tot > theorN50:
            N50 = num
            break
    return N50


if __name__ == "__main__":
    testlist = [10,20,30,40,50]
    assert calculateN50(testlist) == 40
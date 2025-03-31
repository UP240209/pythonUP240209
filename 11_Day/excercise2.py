def evens_and_odds(high):
    odds = 0
    evens = 0
    for i in range(high + 1):
        if i % 2 == 0:
            evens += i
        else:
            odds += i
    print(odds, evens)



def factorial(fac):
    fact = 1
    for i in range(fac + 1):
        fact *= i
    return fact



def is_empty(check):
    if check:
        return True
    else:
        return False



def mean(dataset):
    return sum(dataset) / len(dataset)


def median(dataset):
    data = sorted(dataset)
    index = len(data) // 2

    if len(dataset) % 2 != 0:
        return data[index]

    return (data[index - 1] + data[index]) / 2


def mode(dataset):
    frequency = {}

    for value in dataset:
        frequency[value] = frequency.get(value, 0) + 1

    most_frequent = max(frequency.values())

    modes = [key for key, value in frequency.items() if value == most_frequent]

    return modes


def variance(dataset):
    n = len(dataset)
    mean = sum(dataset) / n
    deviations = [(x - mean) ** 2 for x in dataset]
    variance = sum(deviations) / n
    return variance


def stdev(dataset):
    var = variance(dataset)
    std_dev = var ** 0.5
    return std_dev
dict1 = {'temp': 100, 'temp': 98, 'temp': 90, 'temp': 104, 'temp': 99}


def arrange_dict(dict1):

    a = sorted(dict1, key=lambda item: item['temp'])
    # a = sorted(city_tuples, key=lambda city: city[1])
    print(a)


arrange_dict(dict1)

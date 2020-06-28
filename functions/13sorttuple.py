city_tuples = [('dharan', 1), ('Pokhara', 3), ('Illam', 4), ('dhankuta', 2), ]


def arrange_tup(city_tuples):

    a = sorted(city_tuples, key=lambda city: city[1])
    # a = sorted(city_tuples, key=lambda city: city[1])
    print(a)


arrange_tup(city_tuples)

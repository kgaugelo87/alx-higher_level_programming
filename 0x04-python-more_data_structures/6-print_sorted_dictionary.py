def print_sorted_dictionary(a_dictionary):
    li_sort = list(a_dictionary.keys())
    li_sort.sort()
    for i in li_sort:
        print("{}: {}".format(i, a_dictionary.get(i)))

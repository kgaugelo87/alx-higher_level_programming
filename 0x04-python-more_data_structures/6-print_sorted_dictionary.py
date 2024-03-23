def print_sorted_dictionary(a_dictionary):
    li_sort = list(a_dictionary.keys())
    
    for i in sorted(li_sort):
        print("{}: {}".format(i, a_dictionary.get(i)))

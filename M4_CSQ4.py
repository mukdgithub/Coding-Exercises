''' M4 CSQ4
    Construct a python program which accepts the items of  tuples
    containing the category as the first entry and different components
    of the category along with their costs as the following entries.
    The job is to create a tuple which summarizes
    the costs for each category. [CO1] [L2]         '''
    
def get_tuples():
    tuples = int(input())
    i = 0
    list_tuples = []
    while (i<tuples):
        list_item = []
        count = 0
        tuple_elem = create_tuple()
        for item in tuple_elem:
            try:
                count += int(item)
            except:
                continue
        tuple_cat = tuple_elem[0]
        list_item.append(tuple_cat)
        list_item.append(count)
        list_tuples.append(tuple(list_item))
        i += 1
    return tuple(list_tuples)

def create_tuple():
    list_len = int(input())
    i = 0
    list_elem = []
    while (i<list_len):
        list_item = input()
        list_elem.append(list_item)
        i += 1
    tuple_elem = tuple(list_elem)
    return tuple_elem

def main():                                          # Call main function
    result = get_tuples()
    print(result)

if __name__ == '__main__':
    main()
print('21BCI0003')
print('MUKUND AGARWAL')

# end of program
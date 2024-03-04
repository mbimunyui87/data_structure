def sort_dict_descending(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

# Example usage:
def append_to_dict(input_dict, new_key, new_value):
    input_dict[new_key] = new_value

append_dict = {}

my_dictionary = {'emma': 45, 'tomas': 40, 'john': 20, 'mark': 30, 'atut': 45, 'peter': 70, 'forfang': 45, 'job': 30, 'mbatu': 30, 'alba': 20, 'jude': 18.2}
my_dictionary = sort_dict_descending(my_dictionary)
my_list = list(my_dictionary.items())
key, value = my_list[0]
rank_dict = {}
rank = 1
rank2 = rank
rank_dict[key] = rank


try:
    for i in range(len(my_list)):
        key, value = my_list[ i ]
        k2, v2 = my_list[1 + i]
        if value == v2:
            rank_dict[k2] = rank2 
        else:
            rank_dict[k2] = rank + 1
            rank2 = rank + 1
        rank += 1
    print(rank_dict)
    
    
        
except:
    print('')

print(rank_dict)
print(my_dictionary)
    

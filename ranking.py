# this function takes a dictionary with student's id and averages, rank the students and return two dictionaries (rank and sorted dictionaries)
#  to use this function we can we assign two varaibles (rank_dict, sorted_dict = rank_dict_items(my_dictionary))
# where my_dictionary contains students ID as keys and students averages as values.
def rank_dict_items(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=True))
    
    rank_dict = {}
    rank = 1

    for i, (key, value) in enumerate(sorted_dict.items()):
        if i > 0 and value == prev_value:
            rank_dict[key] = prev_rank
        else:
            rank_dict[key] = rank
            prev_rank = rank
        prev_value = value
        rank += 1

    return rank_dict, sorted_dict

# Example usage:
my_dictionary = {'emma': 45, 'tomas': 40, 'john': 20, 'mark': 30, 'atut': 45, 'peter': 70, 'forfang': 45, 'job': 30, 'mbatu': 30, 'alba': 20, 'jude': 18.2, 'fansita': 33, 'shaman': 70}
rank_dict, sorted_dict = rank_dict_items(my_dictionary)

print("Rank Dictionary:", rank_dict)
print("Sorted Dictionary:", sorted_dict)

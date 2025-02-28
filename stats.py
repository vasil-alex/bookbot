def sort_on(dict):
    return list(dict.values())[0]
def sort(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_info = {char: count}
        char_list.append(char_info)
    char_list.sort(reverse = True, key = sort_on)
    return char_list

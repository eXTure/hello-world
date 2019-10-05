def get_index_different_char(chars):
    alpha_chars = []
    not_alpha_chars = []
    final_list = []
    for sub_list in chars:
        print(sub_list)
        for char in sub_list:
            if str(char).isalpha() or str(char).isdigit():
                alpha_chars.append(char)
            else:
                not_alpha_chars.append(char)
        if len(alpha_chars)>len(not_alpha_chars):
            print(not_alpha_chars[0], type(alpha_chars[0]))
            final_list.append(sub_list.index(not_alpha_chars[0]))
            alpha_chars = []
            not_alpha_chars = []
        elif len(alpha_chars)<len(not_alpha_chars):
            print(alpha_chars[0], type(alpha_chars[0]))
            final_list.append(sub_list.index(alpha_chars[0]))
            alpha_chars = []
            not_alpha_chars = []
        else:
            print('Something went wrong!')
        print(final_list)
    return final_list
        
inputs = (
        ['A', 'f', '.', 'Q', 2],
        ['.', '{', ' ^', '%', 'a'],
        [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'],
        ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'],
        list(range(1,9)) + ['}'] + list('abcde'),
        [2, '.', ',', '!'])
        
get_index_different_char(inputs)
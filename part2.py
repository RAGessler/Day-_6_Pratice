#1
def str_reverser():
    reversed_string = ''
    string = input('Type what you want backwards')
    string_length = len(string)-1
    for character in range(string_length, -1, -1):
        # print(string[character])
        reversed_string += string[character]
    return reversed_string
print(str_reverser())

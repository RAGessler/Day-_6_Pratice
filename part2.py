#1
def str_reverser():
    reversed_string = ''
    string = input('Type what you want backwards')
    string_length = len(string)-1
    for character in range(string_length, -1, -1):
        reversed_string += string[character]
    return reversed_string
# print(str_reverser())

#2
def capitilizer():
    new_string = ''
    string = input('Type a few words...')
    words_list = string.split()
    list_length = len(words_list)
    for words in words_list:
        new_string += words.capitalize() + ' '
    return new_string
# print(capitilizer())

#3
def palindrome_checker():
    user_input = input('Type a word to see if its reversible...')
    length_user_input = len(user_input) -1
    reversed_string = ''
    for character in range(length_user_input, -1 , -1):
        reversed_string += user_input[character]
    if reversed_string == user_input:
        print(f'{user_input} is a palendrome')
        print(f'{user_input} reversed is {reversed_string}')
    else:
        print(f'{user_input} is not a palendrome')
        print(f'{user_input} reversed is {reversed_string}')
# palindrome_checker()

#bonus problem
def bonus_problem():
    string = input('What shall i compress for you?')
    counter = 1
    new_string = ''
    string_length = len(string)-1
    for index in range(string_length):
        if string[index] == string[index+1]:
            counter += 1
        else:
            new_string += str(counter) + string[index]
            counter = 1
    new_string += str(counter) + string[index]
    return new_string
print(bonus_problem())


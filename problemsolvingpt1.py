#1
def problem_one():
    string = 'Packers'
    answer = string[0] + string[6]
    return answer
# problem1 = problem_one()
# print(problem1)

#2
def peanutbutterjelltime():
    for number in range(0, 101):
        if number % 3 == 0 and number % 5 == 0:
            print('PeanutButterJelly')
        elif number % 3 == 0:
            print('PeanutButter')
        elif number % 5 == 0:
            print('Jelly')
        else:
            print(number)
# peanutbutterjelltime()


#3
#this sucker was satisfying to figure out.
def prob_three(word):
    final_result = ''
    counter = -1
    for letter in word:
        counter += 1
        counter_string = str(counter)
        final_result += letter + counter_string
    print(final_result)
# prob_three('Potato')


#4
french_fries = ['potato', 'fryer', 'oil', 'salt', 'ketchup', 'fry sauce']
ingredients = ['bread', 'eggs', 'milk', 'cereal']
def problem_four(ingredients):
    searching = input('What ingrediant are you looking for?')
    if searching in ingredients:
        print(searching + ' is found')
    else:
        print('invalid input, or ingredient not present.')
        again = input('Search again?  Y/N')
        if again == 'n' or again == 'N':
            print('goodbye!')
        else:
            problem_four(ingredients)
# problem_four(french_fries)

#5
def list_reverser(list):
    reversed_list = []
    list_length = len(list)
    list_range = range(list_length, 0, -1)
    for number in list_range:
        reversed_list.append(list[number -1])
    return reversed_list
# print(list_reverser(ingredients))

#6
name_list = ['Rebecca', 'Sam', 'Dante', 'Bob', 'Monica', 'Brad']
def name_soter(names):
    returned_list = []
    for item in names:
        if len(item) > 4:
            returned_list.append(item)
    return returned_list
print(name_soter(name_list))


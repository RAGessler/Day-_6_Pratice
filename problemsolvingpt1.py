def problem_one():
    string = 'Packers'
    answer = string[0] + string[6]
    return answer
# problem1 = problem_one()
# print(problem1)

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

def prob_three(word):
    final_result = ''
    counter = -1
    for letter in word:
        counter += 1
        counter_string = str(counter)
        final_result += letter + counter_string
    print(final_result)
#this sucker was satisfying to figure out.
# prob_three('Potato')

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

problem_four(ingredients)



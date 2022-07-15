import random
def calc():
    print('Welcome to the Calculat!')
    user_name = input('May I have your name?: ')
    print(f"Hello {user_name}")
    print('What is the result of the of the expression?')

    i = 0
    while i < 3:
        i = i + 1
        ran_num1 = random.randrange(1, 50)
        ran_num2 = random.randrange(1, 50)

        arr_operator = ['+', '*', '-']
        random_index = random.randint(0, len(arr_operator) - 1)
        ran_operator = (arr_operator[random_index])

        print(f"{ran_num1} {ran_operator} {ran_num2}")

        correct_answer = 0

        if ran_operator == '+':
            correct_answer = ran_num1 + ran_num2
        elif ran_operator == '*':
            correct_answer = ran_num1 * ran_num2
        else: correct_answer = ran_num1 - ran_num2

        user_answer = input('Your Answer: ')

        if str(correct_answer) == user_answer:
            print('Correct!')

        elif str(correct_answer) != user_answer:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet's try again {user_name} !")
            exit()

    print('Congratulation ' + user_name)


calc()

from math_game import add,sub

def game():
    score = 0

    while True:
        print('======== Menu ========\n1. Add\n2. Substraction')
        operation = int(input('Choice an operation:'))
        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))
        answer = int(input('Enter you answer: '))
        if operation == 1:
            result = add(num_1, num_2)
        elif operation == 2:
            result = sub(num_1,num_2)
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')
        break

    print(f'======== Game Over ========\nYou score is {score}\nKeep going!')

game()

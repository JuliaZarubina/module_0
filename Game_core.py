import numpy as np

def guess_number(number):
    '''Guess the random number from range [1,100]
    using binary search'''
    count = 1
    start = 1
    end = 101

    while True:
        predict = (start + end) // 2

        if number == predict:
            break
        elif number > predict:
            start = predict + 1
            count += 1
        else:
            end = predict - 1
            count += 1

    return (count)


def score_game(game_core):
    '''Perform 1000 search runs'''
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number on average in {score} attempts")
    return (score)

if __name__ == "__main__":
    count = 0
    number = np.random.randint(1, 101)
    print("A random number from 1 to 100 is guessed")

    # while True:
    #     predict = int(input())
    #     count += 1
    #     if number == predict:
    #         break
    #     elif number > predict:
    #         print(f"The guessed number is greater than {predict} ")
    #     elif number < predict:
    #         print(f"The guessed number is less than {predict} ")
    #
    # print(f"You guessed the number {number} in {count} attempts.")

    score_game(guess_number)
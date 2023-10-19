# This program that implements the Rosenberg self-esteem scale.
# Asking user for 10 statements.

def main():
    print('This program is an implementation of the Rosenberg')
    print('Self-Esteem Scale. This program will show you ten')
    print('statements that you could possibly apply to yourself.')
    print('Please rate how much you agree with each of the')
    print('statements by responding with one of these four letters:')
    print()
    print('D means you strongly disagree with the statement.')
    print('d means you disagree with the statement.')
    print('a means you agree with the statement.')
    print('A means you strongly agree with the statement.')
    print()

    score = 0
    score += positive_questions_score('1. I feel that I am a person of worth, at least on an equal plane with others.')
    score += positive_questions_score('2. I feel that I have a number of good qualities.')
    score += negative_questions_score('3. All in all, I am inclined to feel that I am a failure.')
    score += positive_questions_score('4. I am able to do things as well as most other people.')
    score += negative_questions_score('5. I feel I do not have much to be proud of.')
    score += positive_questions_score('6. I take a positive attitude toward myself.')
    score += positive_questions_score('7. On the whole, I am satisfied with myself.')
    score += negative_questions_score('8. I wish I could have more respect for myself.')
    score += negative_questions_score('9. I certainly feel useless at times.')
    score += negative_questions_score('10. At times I think I am no good at all.')
    print()
    print(f'Your score is: {score}')
    print('A score below 15 may indicate problematic low self-esteem.')

def positive_questions_score(statement):
    print(statement)
    score_receive = 0
    answer = input('Enter D, d, a, or A: ')
    if answer == 'D':
        score_receive = 0
    elif answer == 'd':
        score_receive = 1
    elif answer == 'a':
        score_receive = 2
    elif answer == 'A':
        score_receive = 3
    return score_receive



def negative_questions_score(statement): 
    print(statement)
    score_receive = 0
    answer = input('Enter D, d, a, or A: ')
    if answer == 'D':
        score_receive = 3
    elif answer == 'd':
        score_receive = 2
    elif answer == 'a':
        score_receive = 1
    elif answer == 'A':
        score_receive = 0
    return score_receive

if __name__ == "__main__":
    main()
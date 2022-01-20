from random import choice

def winner(userChoice, botChoice):
    if userChoice == botChoice:
        return "It's a tie!"

    if userChoice == 'scissor':
        return 'User won!' if botChoice == 'paper ' else 'User lost!'

    if userChoice == 'rock':
        return 'User won!' if botChoice == 'scissor ' else 'User lost!'

    if userChoice == 'paper':
        return 'User won!' if botChoice == 'rock ' else 'User lost!'


def main():
    print('Choose rock, paper or scissor!')
    print('1 - rock')
    print('2 - paper')
    print('3 - scissor')

    choices = ['rock', 'paper', 'scissor']

    userChoice = int(input('Your choice: '))
    botChoice = choice(choices)

    print('The bot chose', botChoice)
    print('User chose', choices[userChoice - 1])
    print(winner(choices[userChoice - 1], botChoice))


if __name__ == '__main__':
    main()

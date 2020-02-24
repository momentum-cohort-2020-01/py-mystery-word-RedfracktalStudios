import random


def get_word():
    # words = ['apartment','breakfast','classroom', 'discovery']
    words = ['cat']
    return random.choice(words)


def mystery_word():
    word = get_word()
    hidden = []

    attempts = 0  # how many attempts the player has made
    max_attempts = 9  # how many attempts the player gets
    for letterGuessed in word:
        hidden.append('_')

    # the loop to test if player has won

    isGameOver = False
    while not isGameOver:

        # display the current board, guessed letters and guesses remaining
        print(f'You have {max_attempts - attempts} attempts remaining')

        hiddenString = ' '.join(hidden)
        # <join(hidden)> takes everything in the list, passes hidden with a space
        print(f'The current word is: {hiddenString}')
        # f-string ~ formatted string literal will pull <attempts> count into this print statement

        print('Y' if attempts > 0 else '')
        print('Y' + '(' if attempts > 1 else '')
        print('Y(' + ')' if attempts > 2 else '')
        print('Y()'+'U' if attempts > 3 else '')
        print('Y()U' + ' L' if attempts > 4 else '')
        print('Y()U L' + '(' if attempts > 5 else '')
        print('Y()U L(' + ')' if attempts > 6 else '')
        print('Y()U L()' + 'S' if attempts > 7 else '')
        print('Y()U L()S' + 'E' if attempts > 8 else '')
        print('Y()U L()SE' if attempts > 9 else '')

        # ask the player for a character

    # if guess is correct show matched letters
        # string_to_iterate = "string"
        letterGuessed = input('Please guess a letter: ')
        if letterGuessed in word:
            print(f'You guessed correctly! {letterGuessed} is in the word')
            for i in range(len(word)):
                # print(word[i])
                character = word[i]
                if character == letterGuessed:
                    hidden[i] = word[i]
                    print(word[i])
                    # word[i] = '_'

            '''
            string_to_iterate = "string"
            for char_index in range(len(string_to_iterate)):
                print(string_to_iterate[char_index])
            '''
    # if guess is wrong print wrong and # of incorrect attempts
        else:
            print(f'You guessed wrong! {letterGuessed} is not in the word')
            attempts += 1

    # if player wins print you win and stop loop
        if (all(word[i] == character for character in word)):

            print('Yeah!, you won!')
            isGameOver = True

    # if player lost print you lose and stop loop
        if (attempts >= max_attempts):
            print('You lost! Game Over!')
            isGameOver = True


mystery_word()

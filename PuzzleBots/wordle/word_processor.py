

def evaluate(guess, target):
    bits = [0, 0, 0, 0, 0]
    letter_count = {}

    for letter in target:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for i in range(5):
        if guess[i] == target[i]:
            # print(guess[i])
            bits[i] += 2
            letter_count[guess[i]] -= 1

    for i in range(5):
        if guess[i] in target and bits[i] != 2 and letter_count[guess[i]] != 0:
            # print(guess[i])
            bits[i] += 1
            letter_count[guess[i]] -= 1

    value = 0
    for i in range(5):
        value += bits[i] * (3**i)

    # print(bits)
    return value

def main():
    with open('valid_guesses.txt', 'r') as guesses:
        valid_guesses = [line.strip() for line in guesses.readlines()]
        guesses.close()

    with open('valid_answers.txt', 'r') as answers:
        valid_answers = [line.strip() for line in answers.readlines()]
        answers.close()

    print(f'Valid Answers: {len(valid_answers)}\nValid Guesses: {len(valid_guesses)}')

    # for answer in valid_answers:
    #     print(f'{valid_guesses[0]} {answer} {evaluate(valid_guesses[0], answer)}')

    initial_dictionary = {}
    for word in valid_guesses:
        # print(f'Processing: {word}')
        probabilities = [[] for i in range(243)]
        for answer in valid_answers:
            probabilities[evaluate(word, answer)].append(answer)
        initial_dictionary[word] = probabilities

    print(initial_dictionary["aahed"])

main()
import math
import random
import emoji
from re import match

class word_processor:

    def __init__(self):
        self.COLOUR_CODE_MAX = 243
        self.GRN_SQR = "🟩"
        self.YLW_SQR = "🟨"
        self.GRY_SQR = "⬜"

    ## scores the guess against the target, evaluates it as 3^0 as the first letter and 3^4 as the last in a ternary bit system
    def evaluate(self, guess, target):
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

    def display_score(self, score):
        result = ""
        for i in range(5):
            # print(i, result)
            quotient = score // (3**(4-i))
            score = score % (3**(4-i))
            if quotient == 2:
                result = self.GRN_SQR + result
            elif quotient == 1:
                result = self.YLW_SQR + result
            else:
                result = self.GRY_SQR + result

        return result

    def search(self, valid_answers, valid_guesses, debug):
        guess_probabilities = {}
        for word in valid_guesses:
            probabilities = [[] for i in range(self.COLOUR_CODE_MAX)]
            for answer in valid_answers:
                probabilities[self.evaluate(word, answer)].append(answer)
            guess_probabilities[word] = probabilities

        TOTAL = len(valid_answers)
        information = {}

        best_word = ""
        best_info = 0

        for word, matches in guess_probabilities.items():
            if debug: print(f'Processing: {word}')

            sum_prob = 0
            for i in range(len(matches)):
                if len(matches[i]) > 0:
                    prob = len(matches[i]) / TOTAL
                    sum_prob += prob * math.log2(1 / prob)

                    if debug:
                        print(f'Combination: {i}, Matches: {len(matches[i])}')
                        print(f'Probability: {prob}, Information: {prob * math.log2(1 / prob)}')
                        print(f'Current Expected Value: {sum_prob}')
            if debug: print("\n\n")
            information[word] = sum_prob
            if best_info < sum_prob:
                if debug: print(f'{word}: {sum_prob}')
                best_info = sum_prob
                best_word = word

        if debug: print(information)
        return (best_word, guess_probabilities[best_word])

# def main():
#     with open('valid_guesses.txt', 'r') as guesses:
#         valid_guesses = [line.strip() for line in guesses.readlines()]
#         guesses.close()
#
#     with open('valid_answers.txt', 'r') as answers:
#         valid_answers = [line.strip() for line in answers.readlines()]
#         answers.close()
#
#     print(f'Valid Answers: {len(valid_answers)}\nValid Guesses: {len(valid_guesses)}')
#
#     turns_taken_sum = 0
#     turns_taken_distr = [0 for i in range(10)]
#     for i in range(1000):
#         print(f"Simulation {i+1}")
#         answer = valid_answers[random.randint(0, len(valid_answers))]
#         guess = ("", [])
#         # print(f'The answer is {answer}')
#
#         possible_guesses = list(valid_guesses)
#         turns = 1
#         while guess[0] != answer:
#             # print(len(possible_guesses))
#             guess = search(valid_answers, possible_guesses, False)
#             score = evaluate(guess[0], answer)
#             # print(f'Guess {turns}: {guess[0]} | Score: {score} {display_score(score)}')
#
#             viable_words = guess[1][score]
#             # print(f'Viable Words: {len(viable_words)}')
#             temp = []
#             for word in possible_guesses:
#                 if word in viable_words and word in possible_guesses:
#                     temp.append(word)
#             possible_guesses = list(temp)
#             # print(possible_guesses)
#
#             turns += 1
#         turns_taken_sum += turns
#         turns_taken_distr[turns-1] += 1
#         print(f'Turns taken: {turns}')
#         print(f'Turns taken distribution: {turns_taken_distr}')
#         print(f"Average turns taken: {turns_taken_sum / (i+1)}")
#     print(f"Average turns taken: {turns_taken_sum / 1000}")



# main()
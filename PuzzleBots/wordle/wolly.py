import os.path
import random

from wordle.word_processor import word_processor
from wordle.wordle_viewer import wordle_viewer as viewer


class Wolly:

    def __init__(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.word_processor = word_processor()
        # self.interface = interface

        guesses_path = os.path.join(self.base_path, 'valid_guesses.txt')
        answers_path = os.path.join(self.base_path, 'valid_answers.txt')
        with open(guesses_path, 'r') as guesses:
            self.valid_guesses = [line.strip() for line in guesses.readlines()]
            guesses.close()

        with open(answers_path, 'r') as answers:
            self.valid_answers = [line.strip() for line in answers.readlines()]
            answers.close()

        # print(f'Valid Answers: {len(self.valid_answers)}\nValid Guesses: {len(self.valid_guesses)}')

    def solve_wordle(self):
        possible_guesses = list(self.valid_guesses)
        wordle_viewer = viewer()
        for i in range(5):
            guess = self.word_processor.search(self.valid_answers, possible_guesses, False)
            wordle_viewer.write_guess(guess[0])
            score = wordle_viewer.read_row(i+1)

            if score == 242:
                return guess[0]

            viable_words = guess[1][score]
            temp = []
            for word in possible_guesses:
                if word in viable_words and word in possible_guesses:
                    temp.append(word)
            possible_guesses = list(temp)

        return "search failed"


    def test_run(self):
        print(f"Simulating test run")
        answer = self.valid_answers[random.randint(0, len(self.valid_answers))]
        guess = ("", [])
        print(f'The answer is {answer}')

        possible_guesses = list(self.valid_guesses)
        turns = 0
        while guess[0] != answer:
            # print(len(possible_guesses))
            guess = self.word_processor.search(self.valid_answers, possible_guesses, False)
            score = self.word_processor.evaluate(guess[0], answer)
            # print(f'Guess {turns}: {guess[0]} | Score: {score} {self.word_processor.display_score(score)}')
            self.interface.show_result_row(turns, guess[0], score)

            viable_words = guess[1][score]
            # print(f'Viable Words: {len(viable_words)}')
            temp = []
            for word in possible_guesses:
                if word in viable_words and word in possible_guesses:
                    temp.append(word)
            possible_guesses = list(temp)
            # print(possible_guesses)
            turns += 1
        print(f"You won in {turns + 1} turns")

# def main():
#     test_wol = Wolly()
#     print(f'The answer is {test_wol.solve_wordle()}')
#
# main()
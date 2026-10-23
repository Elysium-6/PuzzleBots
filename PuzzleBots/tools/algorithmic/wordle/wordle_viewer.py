import time
from os import write

import keyboard

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class wordle_viewer:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.nytimes.com/games/wordle/index.html")
        self.actions = ActionChains(self.driver)

        wait = WebDriverWait(self.driver, 10)
        play_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='Play']")))
        play_button.click()
        time.sleep(2)
        keyboard.press_and_release("enter")
        time.sleep(2)

        self.all_letters = []
        self.all_letters.append(self.driver.find_elements(By.CSS_SELECTOR, "[aria-label^='1st letter']"))
        self.all_letters.append(self.driver.find_elements(By.CSS_SELECTOR, "[aria-label^='2nd letter']"))
        self.all_letters.append(self.driver.find_elements(By.CSS_SELECTOR, "[aria-label^='3rd letter']"))
        self.all_letters.append(self.driver.find_elements(By.CSS_SELECTOR, "[aria-label^='4th letter']"))
        self.all_letters.append(self.driver.find_elements(By.CSS_SELECTOR, "[aria-label^='5th letter']"))

    ## writes the guess using keyboard
    def write_guess(self, guess : str) -> None:
        keyboard.write(guess)
        time.sleep(1)
        keyboard.press_and_release("enter")
        time.sleep(5)
        self.update_letters()

    ## gets information on the result of each guess, must be done after each guess
    def update_letters(self) -> None:
        self.all_letters[0] = self.driver.find_elements(By.CSS_SELECTOR, "[aria-label^='1st letter']")
        self.all_letters[1] = self.driver.find_elements(By.CSS_SELECTOR, "[aria-label^='2nd letter']")
        self.all_letters[2] = self.driver.find_elements(By.CSS_SELECTOR, "[aria-label^='3rd letter']")
        self.all_letters[3] = self.driver.find_elements(By.CSS_SELECTOR, "[aria-label^='4th letter']")
        self.all_letters[4] = self.driver.find_elements(By.CSS_SELECTOR, "[aria-label^='5th letter']")

    ## returns as a decimal value corresponding to the ternary bit pattern
    def read_row(self, row: int) -> int:
        value = 0
        for i in range(5):
            results = self.all_letters[i][row-1].get_attribute("aria-label").split(",")
            print(results[-1])
            if results[-1].strip() == "correct":
                value += 2 * (3**i)
            elif results[-1].strip() == "present in another position":
                value += 1 * (3**i)

        print(value)
        return value


# def main():
#     viewer = wordle_viewer()
#     viewer.write_guess("extra")
#     viewer.read_row(1)
#     viewer.write_guess("there")
#     viewer.read_row(2)
#
# main()

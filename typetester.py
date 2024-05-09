import random
import tkinter
import time
from tkinter import font


class TypeTester:
    def __init__(self, window, word_list):
        # Creates label for displaying test text.
        self.test_label = tkinter.Label(window, text="                    ", font=font.Font(family="Arial", size=12, weight="bold"))
        # Creates entry box for user to type in.
        self.entry_box = tkinter.Entry(window)
        # Creation of label and string that contains result of the test.
        self.result_text = ""
        self.result_label = tkinter.Label(window, text=self.result_text, foreground="#000000")
        # Button to submit test.
        self.button = tkinter.Button(window, text="start", command= self.test)
        # List of words.
        self.word_list = word_list
        # Sentence for user to type in entry box.
        self.sentence = None
        # Time at which user starts test.
        self.start_time = None
        # Variable representing whether the test is ongoing.
        self.on = False


    # Function that calculates the average words per minute typed during the test.
    def calculate_speed(self, start_time, end_time):
        # Calculates the speed by dividing the number of words in the test sentence divided by the tame taken to complete the test.
        speed = round(len(self.sentence.split()) / ((end_time - start_time)/60))
        return speed

    # Function for the test.
    def test(self):
        # If test is ongoing then end the test.
        if self.on:
            # If user input matches the sentence then calculate the score, display it and end the test.
            if self.sentence == self.entry_box.get():
                self.button.config(text="Start")
                self.test_label.config(text="                    ")
                speed = self.calculate_speed(self.start_time, time.time())
                self.result_label.config(text=f"Your speed was {speed} words per minute.", foreground="#000000")
                self.on = False
            # If user input and sentence do not match, then notify user.
            else:
                self.result_label.config(text="Input is incorrect.", foreground="red")

        # Start test if no test is ongoing.
        else:
            # Creates a sentence for the test and displays it.
            self.create_new_sentence()
            self.test_label.config(text=self.sentence)
            # Changes text on button to represent its purpose of finishing the test.
            self.button.config(text="Finish")
            # Make result label empty.
            self.result_label.config(text="")
            # Set variable to represent that test is ongoing.
            self.on = True
            # Record time of test start.
            self.start_time = time.time()

    # Function that creates a new sentence from the word list.
    def create_new_sentence(self):
        # Set number of words in the sentence a number between 5 and 8.
        length = random.randint(5, 8)

        # Creates a new sentence of particular length with full stop at end.
        sentence = ""
        for i in range(length):
            sentence += random.choice(self.word_list)
            if i < (length - 1):
                sentence += " "

            else:
                sentence += "."
        # Sets object's sentence variable to equal the newly created sentence.
        self.sentence = sentence

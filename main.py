import tkinter
from typetester import TypeTester

# Function that gets words from a file and stores them in an array.
def get_words(file_path):
    with open(file_path, 'r') as file:
        return file.read().split()

# Gathers a list of words to be used for generating sentences.
words = get_words("random-words.txt")


# Creates a user interface for user to do test.
window = tkinter.Tk()
window.title("Speed-typing program")
window.minsize(width=500, height=300)
window.grid()

# Creates a TypeTester object.
test = TypeTester(window, words)

# Empty Label in top corner.
empty_label = tkinter.Label(text="        ")
empty_label.grid(row=0, column=0)

# Assign TypeTester tkinter objects to the user interface.
test.test_label.grid(row=0, column=1)
test.entry_box.grid(row=2, column=1)
test.button.grid(row=3, column=1)
test.result_label.grid(row=4, column=1)


# tkinter mainloop.
window.mainloop()

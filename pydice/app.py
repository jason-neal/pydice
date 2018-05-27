
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from random import random

class Pydice(toga.App):
    self.nsides = 6
    self.ndice = 2

    def roll_dice(self):
        # Roll the n dice
        return [random.randint(1, self.nsides) for _ in range(self.ndice)]

    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)

        # Create a main content box
        main_box = toga.Box()

        # Add the content on the main window
        self.main_window.content = main_box

        # Show the main window
        self.main_window.show()


def main():
    return Pydice('pydice', 'com.example.pydice')


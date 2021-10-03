# https://www.thepythoncode.com/article/translate-text-in-python
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from googletrans import Translator, constants
from pprint import pprint

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def translateTest(to_translate, dest_language):
    translator = Translator()
    # translate a spanish text to english text (by default)
    translation = translator.translate(to_translate, dest=dest_language)
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    translateTest("Hola Mundo", "ar")
    translateTest("Hola Mundo", "el")
    translateTest("Hola Mundo", "nl")
    print("Languages:")
    pprint(constants.LANGUAGES)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

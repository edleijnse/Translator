# https://www.thepythoncode.com/article/translate-text-in-python
# https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-pattern-1a-one-shot-window-the-simplest-pattern
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from googletrans import Translator, constants
from pprint import pprint
import PySimpleGUI as sg


def translateTest(to_translate, dest_language):
    translator = Translator()
    # translate a spanish text to english text (by default)
    translation = translator.translate(to_translate, dest=dest_language)
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    return translation.text

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sg.theme('DarkAmber')  # Keep things interesting for your users

    layout = [[sg.Text('translator')],
              [sg.Input(key='-IN-')],
              [sg.Input(key='-OUT-')],
              [sg.Button('Read'), sg.Exit()]]

    window = sg.Window('Window that stays open', layout)

    while True:  # The Event Loop
        event, values = window.read()
        print(event, values)
        if event == "Read":
            print(values['-IN-'])
            inputText = values['-IN-']
            outputText = translateTest(inputText, "nl")
            window['-OUT-'].update(outputText)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

    window.close()
    translateTest("Hola Mundo", "ar")
    translateTest("Hola Mundo", "el")
    translateTest("Hola Mundo", "nl")
    print("Languages:")
    pprint(constants.LANGUAGES)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

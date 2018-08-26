import os
import re
import time
import locale
import webbrowser
from data import languages_dict, phrases

locale.setlocale(locale.LC_ALL, '')
p = print

def lines(path, extensions_list):
    ''' The core of the script. This function does the actual counting of lines.'''
    totalines = 0
    lines = 0

    for path, _, files in os.walk(path):
        for name in files:
            for ext in extensions_list:
                if (str(name).endswith(ext)):
                    lines = len(open(os.path.join(path, name), "r", encoding="utf-8", errors='ignore').readlines())
                    p(f'{os.path.join(path, name)} - {lines} lines.')
                    totalines += lines
    return totalines

def extensions(languages, languages_dict):
    ''' Return a list of all language extensions of given language/languages.'''
    extensions = []

    for lang in languages:
        if lang.strip() in languages_dict.keys():
            extensions += languages_dict[lang.strip()]
    return sorted(list(set(extensions)))

def is_invalid_lang(languages, languages_dict):
    ''' Check if given language or languages are valid.'''
    
    if languages == None or languages == []: return True

    for l in languages:
        if l not in languages_dict.keys() and languages[0] != "back":
            return True
    return False

def print_extension_search(extensions_list):
    ''' Function for printing the included extension '''

    if len(extensions_list) == 1:
        p("Searching for files inlcudes the following extension", end=": ")
    else:
        p("Searching for files inlcudes the following extensions", end=": ")
    p(", ".join(extensions_list))
    p()
        
def counter(mode):
    ''' Counter mode which handle user input and invoke functions'''

    if (mode == "start" or mode.startswith("s")):
        p(phrases["counter"])
        languages = [None]
        path = ""

        while True:
            # Print some guide notes
            p(phrases["counter-inputs"])
            p(phrases["back"])
            
            # Get Languages from user
            languages = input(phrases["enter-language"]).lower()
            languages = re.findall(r"[\w'|#|\+]+", languages)
            
            # Catch invalid languages or the back keyword
            if (is_invalid_lang(languages, languages_dict)):
                p(phrases["invalid-language"])
                continue
            elif languages[0] == "back": p("returned\n"); break
            
            # Get extensions from extensions data and print them
            extensions_list = extensions(languages, languages_dict)
            print_extension_search(extensions_list)

            # Get path from user
            path = input(phrases["enter-path"])
            
            # Catch invalid path or the back keyword
            if not os.path.exists(path) and path.strip() != "back":
                p(phrases["invalid-path"])
                continue
            elif path.strip() == "back": p("returned"); break

            # Print all searched files with their lines and the total lines
            p("\nTOTAL LINES: {:,}".format(lines(path, extensions_list)).replace(',', ' '))
            p()

def helper(mode):
    ''' Handle user input and print help text based on the input. '''

    if mode == "help" or mode.startswith("h"):
        p(phrases["helper"])
        p("Type:")
        for i in range(1, 6):
            p(phrases[i])
        p(phrases["back"])

        while True:
            num = input("HELPER | Enter number or back: ")

            if num.strip() == "1": p(phrases["how-it-works"])
            elif num.strip() == "2": p(phrases["for-languages"])
            elif num.strip() == "3": p(phrases["for-extensions"])          
            elif num.strip() == "4": p(phrases["for-input-lang"]) 
            elif num.strip() == "5": p(phrases["for-input-path"])
            elif num.strip().lower() == "back": p("returned\n"); break
            else: p("Unknown input.\n")

def end():
    ''' After the user close the loop with break. '''
    p("\n" + phrases["thanks"])
    time.sleep(3)
    webbrowser.open("https://github.com/skilldeliver/Simplelo", new=0, autoraise=True)

def main():

    p(phrases["title"])
    mode = ""

    while mode != "break" and not mode.startswith("b"):
        mode = input(phrases["home"]).lower().strip()
        counter(mode)
        helper(mode)
    end()
    
if __name__ == "__main__":
    main()
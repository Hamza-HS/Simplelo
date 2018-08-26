languages_dict = {
        "html": [".htm", ".html", ".shtml"],
        "css": [".css"],
        "javascript": [".js", ".mjs"],
        "python": [".py", ".pyc", ".pyd", ".pyo", ".pyw", ".pyz"],
        "c#": [".cs"],
        "java":[".java", ".class", ".jar"],
        "c++":[".cc", ".cpp", ".cxx", ".c++", ".hh", ".hpp", ".hxx", ".h++"],
        "c":[".c", ".h"],
        "php": [".php", "phtml", ".php3", ".php4", ".php5", ".php7", ".phps", ".php-s", ".pht"],
        "ruby": [".rb"],
        "perl": [".pl", ".pm", ".t", ".pod"],
        "lisp": [".lisp", ".el", ".cl"],
        "sql": [".sql"],
        "typescript": [".ts", ".tsx"],
        "swift": ["swift"],
        "go": [".go"],
        "kotlin": [".kt", ".kts"],
        "rust": [".rs", ".rlib"],
        "clojure": [".cji", ".cljs", ".cljc", ".end"],
        "scala": [".scala", ".sc"],
        "julia": [".jl"],
        "haskell": [".hs", ".lhs"],
        "r": [".r", ".rds", ".rda"],
        "scheme": [".scm", ".ss"],
        "erlang": [".erl", ".hrl"]
        }

phrases = {
        "title": "Codeliner - Vladislav Mihov - 2018",
        "home": "HOME | Enter start or break or help: ",
        "counter": "\nYou entered the counter.",
        "counter-inputs": "COUNTER | Two inputs are needed - the language or languages (separated by non-letter symbol without '+' or '#') and the path.",
        "back": "/Type back if you want to return at the beginning./\n",
        "invalid-language": "\n*Invalid or not supported language/languages or uncorrect back command...\n",
        "invalid-path": "\n*Path is not valid or does not exist...\n",
        "enter-language": "1. Enter the language or languages: ",
        "enter-path": "2. Enter the path: ",
        "thanks": "Thanks for using my script. If you like it - star my GitHub repo.",
        "helper": "\nYou entered the helper",
        1: "1 - for how it works",
        2: "2 - for languages",
        3: "3 - for extensions",
        4: "4 - for language input",
        5: "5 - for path input",
        "how-it-works":
        """
        So this script is based mainly on 3 things - data for the languages, os.walk and IO.

        1. The data for the languages is in other module - data.py.
        It is organized in one dictionary: keys are the names of the languages and every key has a list value of extensions.            
        2. The os.walk is looping throught all subdirectories and all files in given directory so it checks everything.
        3. The IO it is a simple open() statement. With encoding set to UTF-8 and ignoring possible errors.
        """,
        "for-languages":
        """
        There are 25 markup, scripting and programming languages.
        Most of them are the most popular. Other are included with the help of StackOverflow 2018 survey and Wikipedia.
        Feel free to add language as a key in dictionary in the data module.
        The value must be a list with proper extensions for the language.
        """,
        "for-extensions":
        """
        Extensions for every language are listed with the help of Wikipedia or other random forums.
        If you don't want to search particular extension, remove it from the list in the dictionary in the data module.
        Extensions must be list as value.
        """,
        "for-input-lang":
        """
        Language input must be on one line. You can include one or multiple languages should be separed by non-letter
        symbol (space is non-letter symbol too) but except '#' and '+', because there are used in the names of C# and C++.
        The correct format for the back keyword is to be in the beginning. No other words infront.
        """,
        "for-input-path":
        """
        You can enter path either with /, or \\\\, or \\.
        The os.path.exists(path) checks if path exists so it will throw an exception message if it is not present or valid.
        """
        }
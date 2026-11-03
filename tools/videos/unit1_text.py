"""Unit I lesson videos (1.2-1.7): narration and on-screen words per language.

Each episode reuses the lesson's own animation and walkthrough narration (already voiced), and adds:
hook (2 lines), three key ideas (1 line each), two errors (1 line each), a quiz and a recap.
"""

TITLE = {
    "1-2": {"en": "Installing Python and IDEs", "hi": "Python और IDE install करना", "kn": "Python ಮತ್ತು IDE install ಮಾಡುವುದು"},
    "1-3": {"en": "Variables and data types", "hi": "Variables और data types", "kn": "Variables ಮತ್ತು data types"},
    "1-4": {"en": "Type casting and operators", "hi": "Type casting और operators", "kn": "Type casting ಮತ್ತು operators"},
    "1-5": {"en": "Input and output", "hi": "Input और output", "kn": "Input ಮತ್ತು output"},
    "1-6": {"en": "String operations", "hi": "String operations", "kn": "String operations"},
    "1-7": {"en": "Libraries and pip", "hi": "Libraries और pip", "kn": "Libraries ಮತ್ತು pip"},
    "2-1": {"en": "if, if-else and if-elif-else", "hi": "if, if-else और if-elif-else", "kn": "if, if-else ಮತ್ತು if-elif-else"},
}

ICON = {"1-2": "🧰", "1-3": "📦", "1-4": "🧮", "1-5": "⌨️", "1-6": "🔤", "1-7": "📚"}

WORDS = {
    "en": {"intro": "Intro", "idea": "Key idea", "walk": "Walkthrough", "errors": "Common errors", "quiz": "Quick check",
           "recap": "Recap", "next": "Next: Lesson {n}", "desc": "Practise this lesson with instant feedback, in your language.",
           "answer": "The answer is {L}: {opt}. {why}", "recapIntro": "Let's recap.", "vars": "Variables", "output": "Output",
           "learn": "In this video", "lesson": "Lesson", "terminal": "Terminal", "end": "Practise"},
    "hi": {"intro": "Intro", "idea": "मुख्य बात", "walk": "Walkthrough", "errors": "आम errors", "quiz": "Quick check",
           "recap": "Recap", "next": "आगे: Lesson {n}", "desc": "इस lesson की practice कीजिए, तुरंत feedback के साथ, अपनी भाषा में।",
           "answer": "सही जवाब है {L}: {opt}। {why}", "recapIntro": "चलिए, एक बार दोहरा लेते हैं।", "vars": "Variables", "output": "Output",
           "learn": "इस video में", "lesson": "Lesson", "terminal": "Terminal", "end": "Practice"},
    "kn": {"intro": "Intro", "idea": "ಮುಖ್ಯ ವಿಷಯ", "walk": "Walkthrough", "errors": "ಸಾಮಾನ್ಯ errors", "quiz": "Quick check",
           "recap": "Recap", "next": "ಮುಂದೆ: Lesson {n}", "desc": "ಈ lesson ಅನ್ನು ತಕ್ಷಣದ feedback ಜೊತೆ, ನಿಮ್ಮ ಭಾಷೆಯಲ್ಲಿ practice ಮಾಡಿ.",
           "answer": "ಸರಿಯಾದ ಉತ್ತರ {L}: {opt}. {why}", "recapIntro": "ಒಮ್ಮೆ recap ಮಾಡೋಣ.", "vars": "Variables", "output": "Output",
           "learn": "ಈ video ದಲ್ಲಿ", "lesson": "Lesson", "terminal": "Terminal", "end": "Practice"},
}

# concepts: (explanation index, code, output or None, mode) ; mode "code" | "terminal" | "points"
EP = {
    "1-2": {
        "quiz": (0, [0, 1, 3]),
        "concepts": [
            (0, None, None, "points"),
            (2, None, None, "points"),
            (4, None, None, "points"),
        ],
        "points": {
            "en": [["python.org → Downloads → Python 3", "Tick “Add python.exe to PATH”", "Check: python --version"],
                   ["Jupyter Notebook: cells, data and graphs", "PyCharm: larger projects", "VS Code: free and light, by Microsoft"],
                   ["Champ Lab: Python in your browser, even on a phone", "Google Colab: a free Jupyter Notebook online"]],
            "hi": [["python.org → Downloads → Python 3", "“Add python.exe to PATH” पर tick", "जाँचिए: python --version"],
                   ["Jupyter Notebook: cells, data और graphs", "PyCharm: बड़े projects", "VS Code: free और हल्का, Microsoft का"],
                   ["Champ Lab: browser में Python, phone पर भी", "Google Colab: online free Jupyter Notebook"]],
            "kn": [["python.org → Downloads → Python 3", "“Add python.exe to PATH” tick ಮಾಡಿ", "Check: python --version"],
                   ["Jupyter Notebook: cells, data ಮತ್ತು graphs", "PyCharm: ದೊಡ್ಡ projects", "VS Code: free, ಹಗುರ, Microsoft ನದು"],
                   ["Champ Lab: browser ನಲ್ಲೇ Python, phone ನಲ್ಲೂ", "Google Colab: online free Jupyter Notebook"]],
        },
        "say": {
            "en": {
                "hook": ["Before you write any Python, you need Python itself on your computer, and a good place to write it.",
                         "In the next few minutes: how to install Python, which IDE to choose, and what to do if you don't have a laptop."],
                "c": ["Installing Python means putting the interpreter on your computer. Download Python 3 from python dot org, tick Add to PATH, and check it with python, dash dash version.",
                      "Three popular IDEs. Jupyter Notebook runs code in small cells and shows graphs right below, which suits pharmacy data. PyCharm is for larger projects, and VS Code is a free, light editor from Microsoft.",
                      "No laptop? No problem. Champ Lab runs Python in your browser, even on a phone, and Google Colab gives you a free notebook online."],
                "e": ["A common mix-up: typing a terminal command, like python, inside Python itself. Commands like this belong in the Command Prompt, not in your code.",
                      "This one means the library isn't installed, or its name is misspelt. Check the spelling, then install it with pip."],
            },
            "hi": {
                "hook": ["Python लिखने से पहले आपके computer में खुद Python चाहिए, और उसे लिखने की एक अच्छी जगह।",
                         "अगले कुछ मिनटों में: Python कैसे install करें, कौन-सा IDE चुनें, और laptop न हो तो क्या करें।"],
                "c": ["Python install करने का मतलब है interpreter को अपने computer में रखना। python dot org से Python 3 download कीजिए, Add to PATH पर tick कीजिए, और python dash dash version से जाँचिए।",
                      "तीन popular IDEs। Jupyter Notebook code को छोटे cells में चलाता है और graph ठीक नीचे दिखाता है, जो pharmacy data के लिए बढ़िया है। PyCharm बड़े projects के लिए है, और VS Code, Microsoft का free और हल्का editor है।",
                      "Laptop नहीं है? कोई बात नहीं। Champ Lab आपके browser में Python चलाता है, phone पर भी, और Google Colab online एक free notebook देता है।"],
                "e": ["एक आम गड़बड़: terminal वाला command, जैसे python, Python के अंदर ही type कर देना। ऐसे commands Command Prompt में जाते हैं, code में नहीं।",
                      "इसका मतलब है library install नहीं है, या उसकी spelling गलत है। Spelling जाँचिए, फिर pip से install कीजिए।"],
            },
            "kn": {
                "hook": ["Python ಬರೆಯುವ ಮುಂಚೆ ನಿಮ್ಮ computer ನಲ್ಲಿ Python ಇರಬೇಕು, ಮತ್ತು ಅದನ್ನು ಬರೆಯಲು ಒಂದು ಒಳ್ಳೆಯ ಜಾಗ ಬೇಕು.",
                         "ಮುಂದಿನ ಕೆಲವು ನಿಮಿಷಗಳಲ್ಲಿ: Python install ಮಾಡುವುದು ಹೇಗೆ, ಯಾವ IDE ಆರಿಸಬೇಕು, laptop ಇಲ್ಲದಿದ್ದರೆ ಏನು ಮಾಡಬೇಕು."],
                "c": ["Python install ಮಾಡುವುದು ಅಂದರೆ interpreter ಅನ್ನು ನಿಮ್ಮ computer ಗೆ ಹಾಕುವುದು. python dot org ಇಂದ Python 3 download ಮಾಡಿ, Add to PATH tick ಮಾಡಿ, python dash dash version ಇಂದ check ಮಾಡಿ.",
                      "ಮೂರು popular IDEs. Jupyter Notebook code ಅನ್ನು ಚಿಕ್ಕ cells ನಲ್ಲಿ run ಮಾಡಿ graph ಅನ್ನು ಕೆಳಗೇ ತೋರಿಸುತ್ತೆ, pharmacy data ಗೆ ಇದು ಸೂಕ್ತ. PyCharm ದೊಡ್ಡ projects ಗೆ, VS Code Microsoft ನ free ಮತ್ತು ಹಗುರವಾದ editor.",
                      "Laptop ಇಲ್ಲವಾ? ಪರವಾಗಿಲ್ಲ. Champ Lab ನಿಮ್ಮ browser ನಲ್ಲೇ Python run ಮಾಡುತ್ತೆ, phone ನಲ್ಲೂ, ಮತ್ತು Google Colab online ಒಂದು free notebook ಕೊಡುತ್ತೆ."],
                "e": ["ಒಂದು ಸಾಮಾನ್ಯ ಗೊಂದಲ: terminal command, ಉದಾಹರಣೆಗೆ python, ಅನ್ನು Python ಒಳಗೇ type ಮಾಡುವುದು. ಇಂಥ commands Command Prompt ಗೆ ಸೇರಿದ್ದು, code ಗೆ ಅಲ್ಲ.",
                      "ಇದರ ಅರ್ಥ library install ಆಗಿಲ್ಲ, ಅಥವಾ ಅದರ spelling ತಪ್ಪಾಗಿದೆ. Spelling check ಮಾಡಿ, ಆಮೇಲೆ pip ಇಂದ install ಮಾಡಿ."],
            },
        },
    },
    "1-3": {
        "quiz": (0, [0, 1, 2]),
        "concepts": [
            (0, "dose_mg = 500\ndose_mg = 650\nprint(\"Dose:\", dose_mg, \"mg\")", None, "code"),
            (3, "print(type(500))\nprint(type(52.5))\nprint(type(\"500\"))\nprint(type(True))", None, "code"),
            (4, "dose = 500\nprint(dose * 3)\ndose = \"500\"\nprint(dose * 3)", None, "code"),
        ],
        "say": {
            "en": {
                "hook": ["A pharmacist keeps every medicine in a labelled box, so the right one can be found instantly.",
                         "Python stores information the same way, in variables. Let's see how."],
                "c": ["A variable is a labelled box. The equals sign puts a value in the box, and a new value replaces the old one, so this prints six hundred and fifty.",
                      "Every value has a data type, and type tells you which: int for whole numbers, float for decimals, str for text, and bool for True or False.",
                      "Types matter. The number five hundred, times three, is fifteen hundred. But the text five hundred, times three, just repeats the text."],
                "e": ["If you use a name that was never created, or spell it differently, Python stops with a NameError.",
                      "And you can't join text and a number with plus. Use a comma in print, or convert the number to text first."],
            },
            "hi": {
                "hook": ["Pharmacist हर दवा को label लगे डिब्बे में रखता है, ताकि सही दवा तुरंत मिल जाए।",
                         "Python भी जानकारी ऐसे ही रखता है, variables में। चलिए देखते हैं कैसे।"],
                "c": ["Variable एक label लगा डिब्बा है। Equals sign डिब्बे में value रखता है, और नई value पुरानी को बदल देती है, इसलिए यह छह सौ पचास print करता है।",
                      "हर value का एक data type होता है, और type बताता है कौन-सा: पूरे numbers के लिए int, दशमलव के लिए float, text के लिए str, और True या False के लिए bool।",
                      "Types मायने रखते हैं। Number पाँच सौ गुणा तीन, पंद्रह सौ है। पर text पाँच सौ गुणा तीन, बस text को दोहराता है।"],
                "e": ["अगर आप ऐसा नाम use करें जो कभी बना ही नहीं, या उसकी spelling अलग हो, तो Python NameError पर रुक जाता है।",
                      "और text और number को plus से नहीं जोड़ सकते। print में comma use कीजिए, या पहले number को text में बदलिए।"],
            },
            "kn": {
                "hook": ["Pharmacist ಪ್ರತಿ ಔಷಧವನ್ನು label ಇರುವ ಡಬ್ಬಿಯಲ್ಲಿ ಇಡುತ್ತಾರೆ, ಸರಿಯಾದದ್ದು ತಕ್ಷಣ ಸಿಗಲಿ ಅಂತ.",
                         "Python ಕೂಡ ಮಾಹಿತಿಯನ್ನು ಹಾಗೇ ಇಡುತ್ತೆ, variables ನಲ್ಲಿ. ಹೇಗೆ ಅಂತ ನೋಡೋಣ."],
                "c": ["Variable ಅಂದರೆ label ಇರುವ ಡಬ್ಬಿ. Equals sign ಡಬ್ಬಿಗೆ value ಹಾಕುತ್ತೆ, ಹೊಸ value ಹಳೆಯದನ್ನು ಬದಲಾಯಿಸುತ್ತೆ, ಅದಕ್ಕೇ ಇದು ಆರುನೂರ ಐವತ್ತು print ಮಾಡುತ್ತೆ.",
                      "ಪ್ರತಿ value ಗೂ ಒಂದು data type ಇದೆ, type ಅದು ಯಾವುದು ಅಂತ ಹೇಳುತ್ತೆ: ಪೂರ್ಣ numbers ಗೆ int, ದಶಮಾಂಶಕ್ಕೆ float, text ಗೆ str, True ಅಥವಾ False ಗೆ bool.",
                      "Types ಮುಖ್ಯ. Number ಐನೂರು ಗುಣಿಸು ಮೂರು ಅಂದರೆ ಒಂದು ಸಾವಿರದ ಐನೂರು. ಆದರೆ text ಐನೂರು ಗುಣಿಸು ಮೂರು, text ಅನ್ನು ಪುನರಾವರ್ತಿಸುತ್ತೆ ಅಷ್ಟೇ."],
                "e": ["ಯಾವತ್ತೂ ಮಾಡದ ಹೆಸರನ್ನು, ಅಥವಾ ಬೇರೆ spelling ಇರುವ ಹೆಸರನ್ನು ಬಳಸಿದರೆ, Python NameError ಕೊಟ್ಟು ನಿಲ್ಲುತ್ತೆ.",
                      "ಮತ್ತು text ಮತ್ತು number ಅನ್ನು plus ಇಂದ ಜೋಡಿಸಲು ಆಗಲ್ಲ. print ನಲ್ಲಿ comma ಬಳಸಿ, ಅಥವಾ ಮೊದಲು number ಅನ್ನು text ಗೆ ಬದಲಾಯಿಸಿ."],
            },
        },
    },
    "1-4": {
        "quiz": (1, [0, 1, 2]),
        "concepts": [
            (0, "strength = \"500\"\nprint(int(strength) * 3)", None, "code"),
            (2, "tablets = 25\nprint(tablets // 10)\nprint(tablets % 10)", None, "code"),
            (4, "age = 16\nweight_kg = 52\nprint(age >= 18 and weight_kg >= 50)\nprint(age >= 18 or weight_kg >= 50)", None, "code"),
        ],
        "say": {
            "en": {
                "hook": ["Twenty-five tablets, ten to a strip. How many full strips, and how many tablets are left over?",
                         "Today, Python does the maths: converting types, and using operators."],
                "c": ["Type casting converts a value from one type to another. int turns the text five hundred into a number, so we can multiply it.",
                      "Two very useful operators. Double slash gives the whole number of times: two full strips. And percent gives what is left over: five tablets.",
                      "Logical operators join questions. and needs both sides to be True; or needs just one."],
                "e": ["int can't convert text with a decimal point in it. Use float for decimals.",
                      "And dividing by zero is impossible, so Python stops with a ZeroDivisionError."],
            },
            "hi": {
                "hook": ["पच्चीस tablets, एक strip में दस। कितनी पूरी strips बनेंगी, और कितनी tablets बचेंगी?",
                         "आज Python हिसाब लगाएगा: types बदलना, और operators use करना।"],
                "c": ["Type casting एक value को एक type से दूसरे में बदलता है। int, text पाँच सौ को number बना देता है, ताकि हम उसे गुणा कर सकें।",
                      "दो बहुत काम के operators। Double slash बताता है पूरी कितनी बार: दो पूरी strips। और percent बताता है कितना बचा: पाँच tablets।",
                      "Logical operators सवालों को जोड़ते हैं। and को दोनों तरफ़ True चाहिए; or को सिर्फ़ एक।"],
                "e": ["int, दशमलव वाले text को नहीं बदल सकता। दशमलव के लिए float use कीजिए।",
                      "और zero से भाग देना संभव नहीं, इसलिए Python ZeroDivisionError पर रुक जाता है।"],
            },
            "kn": {
                "hook": ["ಇಪ್ಪತ್ತೈದು tablets, ಒಂದು strip ನಲ್ಲಿ ಹತ್ತು. ಎಷ್ಟು ಪೂರ್ಣ strips ಆಗುತ್ತವೆ, ಎಷ್ಟು tablets ಉಳಿಯುತ್ತವೆ?",
                         "ಇವತ್ತು Python ಲೆಕ್ಕ ಹಾಕುತ್ತೆ: types ಬದಲಾಯಿಸುವುದು, ಮತ್ತು operators ಬಳಸುವುದು."],
                "c": ["Type casting ಒಂದು value ಅನ್ನು ಒಂದು type ಇಂದ ಇನ್ನೊಂದಕ್ಕೆ ಬದಲಾಯಿಸುತ್ತೆ. int, text ಐನೂರನ್ನು number ಮಾಡುತ್ತೆ, ಆಗ ಅದನ್ನು ಗುಣಿಸಬಹುದು.",
                      "ಎರಡು ತುಂಬಾ ಉಪಯುಕ್ತ operators. Double slash ಪೂರ್ಣ ಎಷ್ಟು ಸಲ ಅಂತ ಕೊಡುತ್ತೆ: ಎರಡು ಪೂರ್ಣ strips. Percent ಉಳಿದದ್ದನ್ನು ಕೊಡುತ್ತೆ: ಐದು tablets.",
                      "Logical operators ಪ್ರಶ್ನೆಗಳನ್ನು ಜೋಡಿಸುತ್ತವೆ. and ಗೆ ಎರಡೂ ಕಡೆ True ಬೇಕು; or ಗೆ ಒಂದು ಸಾಕು."],
                "e": ["ದಶಮಾಂಶ ಇರುವ text ಅನ್ನು int ಬದಲಾಯಿಸಲು ಆಗಲ್ಲ. ದಶಮಾಂಶಕ್ಕೆ float ಬಳಸಿ.",
                      "ಮತ್ತು zero ಇಂದ ಭಾಗಿಸುವುದು ಅಸಾಧ್ಯ, ಅದಕ್ಕೇ Python ZeroDivisionError ಕೊಟ್ಟು ನಿಲ್ಲುತ್ತೆ."],
            },
        },
    },
    "1-5": {
        "quiz": (0, [0, 1, 2]),
        "concepts": [
            (0, "name = input(\"Patient name: \")\nprint(\"Hello,\", name)", "Patient name: Ravi\nHello, Ravi", "code"),
            (3, "drug = \"Amoxicillin\"\ndose_mg = 500\nprint(f\"{drug}: {dose_mg} mg\")\nprint(f\"Daily total: {dose_mg * 3} mg\")", None, "code"),
            (4, "dose_mg = 16.1 * 15\nprint(dose_mg)\nprint(f\"Dose: {dose_mg:.1f} mg\")", None, "code"),
        ],
        "say": {
            "en": {
                "hook": ["So far, your programs used the same numbers every time.",
                         "A real pharmacy tool has to ask: what's the patient's weight? Today, your program learns to ask, and to answer neatly."],
                "c": ["input asks a question, and waits until the user types an answer and presses Enter.",
                      "An f-string puts values straight into text. Write f before the quotes, and put each name inside curly brackets.",
                      "Calculations can give long decimals. Colon, dot one f, inside the curly brackets, keeps just one decimal place."],
                "e": ["Remember, input always gives text. Multiplying that text by a decimal causes this TypeError, so convert it with float first.",
                      "And if the user types letters, like fifty-two kg, float can't convert it. Ask clearly for just the number."],
            },
            "hi": {
                "hook": ["अब तक आपके programs हर बार वही numbers use करते थे।",
                         "असली pharmacy tool को पूछना पड़ता है: patient का वज़न कितना है? आज आपका program पूछना सीखेगा, और साफ़-सुथरा जवाब देना भी।"],
                "c": ["input एक सवाल पूछता है, और तब तक रुकता है जब तक user जवाब type करके Enter न दबाए।",
                      "f-string values को सीधे text में डाल देता है। Quotes से पहले f लिखिए, और हर नाम को curly brackets में रखिए।",
                      "हिसाब से लंबे दशमलव आ सकते हैं। Curly brackets के अंदर colon, dot one f, सिर्फ़ एक decimal place रखता है।"],
                "e": ["याद रखिए, input हमेशा text देता है। उस text को दशमलव से गुणा करने पर यह TypeError आती है, इसलिए पहले float से बदलिए।",
                      "और अगर user अक्षर type करे, जैसे बावन kg, तो float उसे नहीं बदल पाता। साफ़ पूछिए, सिर्फ़ number।"],
            },
            "kn": {
                "hook": ["ಇಲ್ಲಿವರೆಗೆ ನಿಮ್ಮ programs ಪ್ರತಿ ಸಲ ಅದೇ numbers ಬಳಸುತ್ತಿದ್ದವು.",
                         "ನಿಜವಾದ pharmacy tool ಕೇಳಬೇಕು: patient ನ ತೂಕ ಎಷ್ಟು? ಇವತ್ತು ನಿಮ್ಮ program ಕೇಳುವುದನ್ನು, ಮತ್ತು ಅಚ್ಚುಕಟ್ಟಾಗಿ ಉತ್ತರಿಸುವುದನ್ನು ಕಲಿಯುತ್ತೆ."],
                "c": ["input ಒಂದು ಪ್ರಶ್ನೆ ಕೇಳುತ್ತೆ, user ಉತ್ತರ type ಮಾಡಿ Enter ಒತ್ತುವವರೆಗೆ ಕಾಯುತ್ತೆ.",
                      "f-string values ಅನ್ನು ನೇರವಾಗಿ text ಒಳಗೆ ಹಾಕುತ್ತೆ. Quotes ಮುಂಚೆ f ಬರೆಯಿರಿ, ಪ್ರತಿ ಹೆಸರನ್ನು curly brackets ಒಳಗೆ ಇಡಿ.",
                      "ಲೆಕ್ಕದಿಂದ ಉದ್ದ ದಶಮಾಂಶ ಬರಬಹುದು. Curly brackets ಒಳಗೆ colon, dot one f, ಒಂದೇ decimal place ಇಡುತ್ತೆ."],
                "e": ["ನೆನಪಿಡಿ, input ಯಾವಾಗಲೂ text ಕೊಡುತ್ತೆ. ಆ text ಅನ್ನು ದಶಮಾಂಶದಿಂದ ಗುಣಿಸಿದರೆ ಈ TypeError ಬರುತ್ತೆ, ಅದಕ್ಕೇ ಮೊದಲು float ಇಂದ ಬದಲಾಯಿಸಿ.",
                      "ಮತ್ತು user ಅಕ್ಷರಗಳನ್ನು type ಮಾಡಿದರೆ, ಉದಾಹರಣೆಗೆ ಐವತ್ತೆರಡು kg, float ಅದನ್ನು ಬದಲಾಯಿಸಲು ಆಗಲ್ಲ. Number ಮಾತ್ರ ಕೊಡಿ ಅಂತ ಸ್ಪಷ್ಟವಾಗಿ ಕೇಳಿ."],
            },
        },
    },
    "1-6": {
        "quiz": (1, [0, 1, 2]),
        "concepts": [
            (0, "drug = \"Paracetamol\"\nprint(drug + \" 500 mg\")\nprint(\"-\" * 12)\nprint(len(drug))", None, "code"),
            (2, "batch = \"AMX-2026-0457\"\nprint(batch[0:3])\nprint(batch[4:8])\nprint(batch[-4:])", None, "code"),
            (3, "entry = \"  amoxicillin 250mg  \"\nprint(entry.strip())\nprint(entry.strip().upper())\nprint(\"250mg\".replace(\"mg\", \" mg\"))", None, "code"),
        ],
        "say": {
            "en": {
                "hook": ["Real records are messy: extra spaces, small letters, no space before the unit.",
                         "Today you'll clean text, read parts of a batch code, and split a patient record, with string operations."],
                "c": ["Plus joins strings, star repeats them, and len counts the characters, spaces included.",
                      "A slice takes a piece of a string. It starts at the first index and stops just before the second, so four to eight gives the year.",
                      "String methods clean text. strip removes the spaces at both ends, upper makes capitals, and replace swaps one piece of text for another."],
                "e": ["Aspirin has seven characters, at indexes zero to six. Asking for index seven gives an IndexError.",
                      "And strings can't be changed in place. Make a new string and save it instead."],
            },
            "hi": {
                "hook": ["असली records गड़बड़ होते हैं: extra spaces, छोटे अक्षर, unit से पहले space नहीं।",
                         "आज आप string operations से text साफ़ करेंगे, batch code के हिस्से पढ़ेंगे, और patient record को तोड़ेंगे।"],
                "c": ["Plus strings को जोड़ता है, star उन्हें दोहराता है, और len characters गिनता है, spaces समेत।",
                      "Slice string का एक हिस्सा लेता है। यह पहले index से शुरू होकर दूसरे से ठीक पहले रुकता है, इसलिए चार से आठ साल देता है।",
                      "String methods text साफ़ करते हैं। strip दोनों सिरों के spaces हटाता है, upper capitals बनाता है, और replace एक text की जगह दूसरा रखता है।"],
                "e": ["Aspirin में सात characters हैं, index zero से छह तक। Index सात माँगने पर IndexError आती है।",
                      "और strings को उसी जगह नहीं बदल सकते। नई string बनाइए और उसे save कीजिए।"],
            },
            "kn": {
                "hook": ["ನಿಜವಾದ records ಗೊಂದಲದಿಂದ ಕೂಡಿರುತ್ತವೆ: extra spaces, ಚಿಕ್ಕ ಅಕ್ಷರಗಳು, unit ಮುಂಚೆ space ಇಲ್ಲ.",
                         "ಇವತ್ತು string operations ಇಂದ text ಸರಿ ಮಾಡುತ್ತೀರಿ, batch code ನ ಭಾಗಗಳನ್ನು ಓದುತ್ತೀರಿ, patient record ಅನ್ನು ಒಡೆಯುತ್ತೀರಿ."],
                "c": ["Plus strings ಅನ್ನು ಜೋಡಿಸುತ್ತೆ, star ಅವನ್ನು ಪುನರಾವರ್ತಿಸುತ್ತೆ, len characters ಎಣಿಸುತ್ತೆ, spaces ಸೇರಿ.",
                      "Slice string ನ ಒಂದು ಭಾಗ ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ. ಮೊದಲ index ಇಂದ ಶುರುವಾಗಿ ಎರಡನೆಯದಕ್ಕೆ ಸ್ವಲ್ಪ ಮುಂಚೆ ನಿಲ್ಲುತ್ತೆ, ಅದಕ್ಕೇ ನಾಲ್ಕರಿಂದ ಎಂಟು ವರ್ಷವನ್ನು ಕೊಡುತ್ತೆ.",
                      "String methods text ಸರಿ ಮಾಡುತ್ತವೆ. strip ಎರಡೂ ತುದಿಯ spaces ತೆಗೆಯುತ್ತೆ, upper capitals ಮಾಡುತ್ತೆ, replace ಒಂದು text ಬದಲು ಇನ್ನೊಂದು ಹಾಕುತ್ತೆ."],
                "e": ["Aspirin ನಲ್ಲಿ ಏಳು characters ಇವೆ, index zero ಇಂದ ಆರರವರೆಗೆ. Index ಏಳು ಕೇಳಿದರೆ IndexError ಬರುತ್ತೆ.",
                      "ಮತ್ತು strings ಅನ್ನು ಅದೇ ಜಾಗದಲ್ಲಿ ಬದಲಾಯಿಸಲು ಆಗಲ್ಲ. ಹೊಸ string ಮಾಡಿ ಅದನ್ನು save ಮಾಡಿ."],
            },
        },
    },
    "1-7": {
        "quiz": (0, [0, 1, 2]),
        "concepts": [
            (0, "import math\nprint(math.sqrt(49))\nprint(math.pi)", None, "code"),
            (2, "import math\nprint(math.ceil(4.5))\nfrom math import sqrt\nprint(sqrt(81))\nimport statistics as st\nprint(st.mean([250, 500, 375]))", None, "code"),
            (4, "pip install numpy\npip uninstall numpy\npip list", None, "terminal"),
        ],
        "say": {
            "en": {
                "hook": ["Why write a square root, or an average, yourself, when experts have already written and tested it?",
                         "Today: modules, libraries, and pip, the tool that installs them."],
                "c": ["A module is a file of ready-made code. Import math, and you can use its tools, like the square root and pi.",
                      "There are three ways to import: the whole module, one tool with from, or a short nickname with as.",
                      "Libraries that don't come with Python are installed with pip. Type it in the terminal, not inside Python: pip install, pip uninstall, and pip list."],
                "e": ["This error means the library isn't installed, or its name is misspelt: n u m p i, instead of numpy.",
                      "And after import math, you must write math dot sqrt. Plain sqrt only works with from math import sqrt."],
            },
            "hi": {
                "hook": ["जब experts ने square root या average पहले ही लिखकर test कर दिया है, तो आप खुद क्यों लिखें?",
                         "आज: modules, libraries, और pip, जो उन्हें install करता है।"],
                "c": ["Module ready-made code की एक file है। math को import कीजिए, और उसके tools use कीजिए, जैसे square root और pi।",
                      "Import करने के तीन तरीके हैं: पूरा module, from से एक tool, या as से एक छोटा nickname।",
                      "जो libraries Python के साथ नहीं आतीं, वो pip से install होती हैं। इसे terminal में type कीजिए, Python के अंदर नहीं: pip install, pip uninstall, और pip list।"],
                "e": ["इस error का मतलब है library install नहीं है, या नाम की spelling गलत है: numpy की जगह n u m p i।",
                      "और import math के बाद math dot sqrt लिखना होगा। सिर्फ़ sqrt तभी चलता है जब from math import sqrt लिखा हो।"],
            },
            "kn": {
                "hook": ["Experts ಈಗಾಗಲೇ square root ಅಥವಾ average ಬರೆದು test ಮಾಡಿರುವಾಗ, ನೀವೇ ಯಾಕೆ ಬರೆಯಬೇಕು?",
                         "ಇವತ್ತು: modules, libraries, ಮತ್ತು ಅವನ್ನು install ಮಾಡುವ pip."],
                "c": ["Module ಅಂದರೆ ready-made code ಇರುವ ಒಂದು file. math ಅನ್ನು import ಮಾಡಿ, ಅದರ tools ಬಳಸಿ, ಉದಾಹರಣೆಗೆ square root ಮತ್ತು pi.",
                      "Import ಮಾಡಲು ಮೂರು ದಾರಿಗಳಿವೆ: ಇಡೀ module, from ಇಂದ ಒಂದು tool, ಅಥವಾ as ಇಂದ ಒಂದು ಚಿಕ್ಕ nickname.",
                      "Python ಜೊತೆ ಬರದ libraries ಅನ್ನು pip ಇಂದ install ಮಾಡುತ್ತಾರೆ. ಅದನ್ನು terminal ನಲ್ಲಿ type ಮಾಡಿ, Python ಒಳಗೆ ಅಲ್ಲ: pip install, pip uninstall, ಮತ್ತು pip list."],
                "e": ["ಈ error ನ ಅರ್ಥ library install ಆಗಿಲ್ಲ, ಅಥವಾ ಹೆಸರಿನ spelling ತಪ್ಪು: numpy ಬದಲು n u m p i.",
                      "ಮತ್ತು import math ಆದಮೇಲೆ math dot sqrt ಅಂತ ಬರೆಯಬೇಕು. ಸುಮ್ಮನೆ sqrt, from math import sqrt ಇದ್ದಾಗ ಮಾತ್ರ ಕೆಲಸ ಮಾಡುತ್ತೆ."],
            },
        },
    },
}

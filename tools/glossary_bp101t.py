"""'Words to know' for BP101T lessons, in English, Hindi, Hinglish and Kannada.

Each entry: (term, {lang: meaning}). Terms stay in English everywhere (students write the
exam in English); only the meaning is translated. Run this file to write the glossary into
content/bp101t/<lesson>/{en,hi,hinglish,kn}.json, then run tools/check_terms.py.
"""
import json
import os

ROOT = os.path.join(os.path.dirname(__file__), "..")

G = {
    "1-1": [
        ("Program", {
            "en": "A set of instructions the computer follows in order, like a prescription written for a computer.",
            "hi": "निर्देशों का एक set जिसे computer क्रम से follow करता है, जैसे computer के लिए लिखा गया prescription।",
            "hinglish": "Nirdeshon ka ek set jise computer kram se follow karta hai, jaise computer ke liye likha gaya prescription.",
            "kn": "Computer ಕ್ರಮವಾಗಿ ಪಾಲಿಸುವ ಸೂಚನೆಗಳ set, computer ಗಾಗಿ ಬರೆದ prescription ತರಹ."}),
        ("Code", {
            "en": "The instructions we type in a programming language. \"Writing code\" means writing these instructions.",
            "hi": "Programming language में type किए गए निर्देश। \"Code लिखना\" मतलब ये निर्देश लिखना।",
            "hinglish": "Programming language mein type kiye gaye nirdesh. \"Code likhna\" matlab yeh nirdesh likhna.",
            "kn": "Programming language ನಲ್ಲಿ type ಮಾಡುವ ಸೂಚನೆಗಳು. \"Code ಬರೆಯೋದು\" ಅಂದ್ರೆ ಈ ಸೂಚನೆಗಳನ್ನು ಬರೆಯೋದು."}),
        ("Programming language", {
            "en": "A language that both humans and computers understand, used to write programs. Python is one.",
            "hi": "एक भाषा जिसे इंसान और computer दोनों समझते हैं, programs लिखने के लिए। Python उनमें से एक है।",
            "hinglish": "Ek bhasha jise insaan aur computer dono samajhte hain, programs likhne ke liye. Python unme se ek hai.",
            "kn": "ಮನುಷ್ಯರು ಮತ್ತು computer ಇಬ್ಬರಿಗೂ ಅರ್ಥ ಆಗುವ, programs ಬರೆಯಲು ಬಳಸುವ ಭಾಷೆ. Python ಅದರಲ್ಲಿ ಒಂದು."}),
        ("Run", {
            "en": "To make the computer carry out your program. Also called \"execute\".",
            "hi": "Computer से आपका program पूरा करवाना। इसे \"execute\" करना भी कहते हैं।",
            "hinglish": "Computer se aapka program poora karwana. Ise \"execute\" karna bhi kehte hain.",
            "kn": "ನಿಮ್ಮ program ಅನ್ನು computer ಇಂದ ಮಾಡಿಸೋದು. ಇದನ್ನು \"execute\" ಮಾಡೋದು ಅಂತಲೂ ಕರೆಯುತ್ತಾರೆ."}),
        ("Interpreter", {
            "en": "The part of Python that reads your code and carries it out, one line at a time, like a pharmacist reading a prescription.",
            "hi": "Python का वह हिस्सा जो आपका code पढ़कर उसे एक-एक line करके पूरा करता है, जैसे pharmacist prescription पढ़ता है।",
            "hinglish": "Python ka woh hissa jo aapka code padhkar use ek-ek line karke poora karta hai, jaise pharmacist prescription padhta hai.",
            "kn": "ನಿಮ್ಮ code ಓದಿ, ಒಂದೊಂದೇ line ಆಗಿ ಮಾಡಿ ಮುಗಿಸುವ Python ನ ಭಾಗ, pharmacist prescription ಓದುವ ತರಹ."}),
        ("Library", {
            "en": "Ready-made code you can add to Python for extra abilities, such as drawing graphs. You'll learn more in Lesson 1.7.",
            "hi": "Ready-made code जिसे Python में जोड़कर नई क्षमताएँ मिलती हैं, जैसे graphs बनाना। ज़्यादा Lesson 1.7 में।",
            "hinglish": "Ready-made code jise Python mein jodkar nayi kshamtayein milti hain, jaise graphs banana. Zyaada Lesson 1.7 mein.",
            "kn": "Python ಗೆ ಸೇರಿಸಿದರೆ ಹೊಸ ಸಾಮರ್ಥ್ಯ ಕೊಡುವ ready-made code, ಉದಾ: graphs ಬರೆಯೋದು. ಹೆಚ್ಚಿನದು Lesson 1.7 ನಲ್ಲಿ."}),
        ("print()", {
            "en": "The Python instruction that shows text or numbers on the screen.",
            "hi": "Python का वह instruction जो text या numbers को screen पर दिखाता है।",
            "hinglish": "Python ka woh instruction jo text ya numbers ko screen par dikhata hai.",
            "kn": "Text ಅಥವಾ numbers ಅನ್ನು screen ಮೇಲೆ ತೋರಿಸುವ Python instruction."}),
        ("Output", {
            "en": "Whatever your program shows on the screen when it runs.",
            "hi": "Program चलने पर screen पर जो कुछ दिखता है।",
            "hinglish": "Program chalne par screen par jo kuch dikhta hai.",
            "kn": "Program run ಆದಾಗ screen ಮೇಲೆ ಕಾಣುವುದೆಲ್ಲಾ."}),
        ("String", {
            "en": "Text inside quotes, such as \"Paracetamol\". Python shows it exactly as written.",
            "hi": "Quotes के अंदर का text, जैसे \"Paracetamol\"। Python इसे बिल्कुल वैसा ही दिखाता है जैसा लिखा है।",
            "hinglish": "Quotes ke andar ka text, jaise \"Paracetamol\". Python ise bilkul waisa hi dikhata hai jaisa likha hai.",
            "kn": "Quotes ಒಳಗಿನ text, ಉದಾ: \"Paracetamol\". Python ಅದನ್ನು ಬರೆದ ಹಾಗೆಯೇ ತೋರಿಸುತ್ತೆ."}),
        ("Comment", {
            "en": "A note for humans that starts with #. Python skips it.",
            "hi": "# से शुरू होने वाला, इंसानों के लिए एक note। Python इसे छोड़ देता है।",
            "hinglish": "# se shuru hone wala, insaanon ke liye ek note. Python ise chhod deta hai.",
            "kn": "# ಇಂದ ಶುರುವಾಗುವ, ಮನುಷ್ಯರಿಗಾಗಿ ಬರೆದ note. Python ಅದನ್ನು skip ಮಾಡುತ್ತೆ."}),
        ("Error", {
            "en": "A message from Python saying it couldn't understand or finish something. It tells you the line and the reason.",
            "hi": "Python का message कि वह कुछ समझ या पूरा नहीं कर पाया। यह line और कारण दोनों बताता है।",
            "hinglish": "Python ka message ki woh kuch samajh ya poora nahi kar paaya. Yeh line aur kaaran dono batata hai.",
            "kn": "ಏನನ್ನೋ ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಲು ಅಥವಾ ಮುಗಿಸಲು ಆಗಲಿಲ್ಲ ಅನ್ನುವ Python ನ message. ಅದು line ಮತ್ತು ಕಾರಣ ಎರಡನ್ನೂ ಹೇಳುತ್ತೆ."}),
        ("Syntax", {
            "en": "The grammar rules of a programming language: where brackets, quotes and commas go.",
            "hi": "Programming language के grammar के नियम: brackets, quotes और commas कहाँ लगते हैं।",
            "hinglish": "Programming language ke grammar ke niyam: brackets, quotes aur commas kahan lagte hain.",
            "kn": "Programming language ನ grammar ನಿಯಮಗಳು: brackets, quotes ಮತ್ತು commas ಎಲ್ಲಿ ಬರಬೇಕು ಅನ್ನೋದು."}),
        ("Syntax error", {
            "en": "A writing mistake that breaks those rules, like a missing bracket. Python won't start until you fix it.",
            "hi": "इन नियमों को तोड़ने वाली लिखने की गलती, जैसे missing bracket। इसे ठीक किए बिना Python शुरू नहीं होता।",
            "hinglish": "In niyamon ko todne wali likhne ki galti, jaise missing bracket. Ise theek kiye bina Python shuru nahi hota.",
            "kn": "ಈ ನಿಯಮ ಮುರಿಯುವ ಬರವಣಿಗೆಯ ತಪ್ಪು, ಉದಾ: missing bracket. ಅದನ್ನು ಸರಿ ಮಾಡುವವರೆಗೆ Python ಶುರುವೇ ಆಗಲ್ಲ."}),
        ("Bug", {
            "en": "A mistake in your code that makes it stop or give the wrong result.",
            "hi": "Code की वह गलती जिससे program रुक जाए या गलत result दे।",
            "hinglish": "Code ki woh galti jisse program ruk jaaye ya galat result de.",
            "kn": "Program ನಿಲ್ಲುವ ಅಥವಾ ತಪ್ಪು result ಕೊಡುವ ಹಾಗೆ ಮಾಡುವ code ನ ತಪ್ಪು."}),
        ("Debugging", {
            "en": "Finding and fixing bugs. Like checking a prescription line by line to find the error.",
            "hi": "Bugs ढूँढना और ठीक करना। जैसे गलती ढूँढने के लिए prescription को line by line check करना।",
            "hinglish": "Bugs dhoondhna aur theek karna. Jaise galti dhoondhne ke liye prescription ko line by line check karna.",
            "kn": "Bugs ಹುಡುಕಿ ಸರಿ ಮಾಡೋದು. ತಪ್ಪು ಹುಡುಕಲು prescription ಅನ್ನು line by line check ಮಾಡುವ ತರಹ."}),
        ("Case-sensitive", {
            "en": "Capital and small letters count as different. In Python, print works but Print doesn't.",
            "hi": "Capital और small letters अलग माने जाते हैं। Python में print चलता है, लेकिन Print नहीं।",
            "hinglish": "Capital aur small letters alag maane jaate hain. Python mein print chalta hai, lekin Print nahi.",
            "kn": "Capital ಮತ್ತು small letters ಬೇರೆ ಬೇರೆ ಅಂತ ಪರಿಗಣಿಸಲಾಗುತ್ತೆ. Python ನಲ್ಲಿ print ಕೆಲಸ ಮಾಡುತ್ತೆ, Print ಮಾಡಲ್ಲ."}),
    ],
    "1-2": [
        ("Text editor", {
            "en": "A simple program for typing plain text, such as Notepad. It can't run code.",
            "hi": "Plain text type करने का एक simple program, जैसे Notepad। यह code नहीं चला सकता।",
            "hinglish": "Plain text type karne ka ek simple program, jaise Notepad. Yeh code nahi chala sakta.",
            "kn": "Plain text type ಮಾಡುವ ಒಂದು simple program, ಉದಾ: Notepad. ಇದು code run ಮಾಡಲ್ಲ."}),
        ("IDE", {
            "en": "Integrated Development Environment: one app where you write, run and fix code.",
            "hi": "Integrated Development Environment: एक app जिसमें code लिखना, चलाना और ठीक करना सब होता है।",
            "hinglish": "Integrated Development Environment: ek app jisme code likhna, chalana aur theek karna sab hota hai.",
            "kn": "Integrated Development Environment: code ಬರೆಯೋದು, run ಮಾಡೋದು, ಸರಿ ಮಾಡೋದು ಎಲ್ಲಾ ಒಂದೇ app ನಲ್ಲಿ."}),
        ("Command Prompt / Terminal", {
            "en": "A window where you type instructions to the computer instead of clicking. Windows calls it Command Prompt; Mac calls it Terminal.",
            "hi": "एक window जिसमें click करने के बजाय computer को निर्देश type करते हैं। Windows में Command Prompt, Mac में Terminal।",
            "hinglish": "Ek window jisme click karne ke bajaay computer ko nirdesh type karte hain. Windows mein Command Prompt, Mac mein Terminal.",
            "kn": "Click ಮಾಡುವ ಬದಲು computer ಗೆ ಸೂಚನೆಗಳನ್ನು type ಮಾಡುವ window. Windows ನಲ್ಲಿ Command Prompt, Mac ನಲ್ಲಿ Terminal."}),
        ("Command", {
            "en": "An instruction typed into the terminal, such as python --version.",
            "hi": "Terminal में type किया गया एक instruction, जैसे python --version।",
            "hinglish": "Terminal mein type kiya gaya ek instruction, jaise python --version.",
            "kn": "Terminal ನಲ್ಲಿ type ಮಾಡುವ ಒಂದು instruction, ಉದಾ: python --version."}),
        ("PATH", {
            "en": "The list of folders Windows searches when you type a command. Adding Python to PATH lets you type python from anywhere.",
            "hi": "Folders की वह list जिसमें Windows command ढूँढता है। Python को PATH में जोड़ने से python कहीं से भी type कर सकते हैं।",
            "hinglish": "Folders ki woh list jisme Windows command dhoondhta hai. Python ko PATH mein jodne se python kahin se bhi type kar sakte hain.",
            "kn": "Command type ಮಾಡಿದಾಗ Windows ಹುಡುಕುವ folders ನ list. Python ಅನ್ನು PATH ಗೆ ಸೇರಿಸಿದರೆ python ಅನ್ನು ಎಲ್ಲಿಂದ ಬೇಕಾದರೂ type ಮಾಡಬಹುದು."}),
        ("Python prompt (>>>)", {
            "en": "Where Python waits for one line of code after you type python in the terminal. Type exit() to leave.",
            "hi": "Terminal में python type करने के बाद, जहाँ Python एक line के code का इंतज़ार करता है। बाहर निकलने के लिए exit() type करें।",
            "hinglish": "Terminal mein python type karne ke baad, jahan Python ek line ke code ka intezaar karta hai. Bahar nikalne ke liye exit() type karein.",
            "kn": "Terminal ನಲ್ಲಿ python type ಮಾಡಿದ ಮೇಲೆ, Python ಒಂದು line code ಗಾಗಿ ಕಾಯುವ ಜಾಗ. ಹೊರಬರಲು exit() type ಮಾಡಿ."}),
        ("File extension (.py)", {
            "en": "The letters after the dot in a file name. Python files end in .py.",
            "hi": "File के नाम में dot के बाद के letters। Python files .py पर खत्म होती हैं।",
            "hinglish": "File ke naam mein dot ke baad ke letters. Python files .py par khatm hoti hain.",
            "kn": "File ಹೆಸರಿನಲ್ಲಿ dot ನಂತರದ letters. Python files .py ಇಂದ ಕೊನೆಯಾಗುತ್ತವೆ."}),
        ("Cell", {
            "en": "A small box of code in Jupyter that runs on its own and shows its result just below it.",
            "hi": "Jupyter में code का एक छोटा box, जो अलग से चलता है और result ठीक नीचे दिखाता है।",
            "hinglish": "Jupyter mein code ka ek chhota box, jo alag se chalta hai aur result theek neeche dikhata hai.",
            "kn": "Jupyter ನಲ್ಲಿ ತಾನೇ run ಆಗಿ, result ಅನ್ನು ಕೆಳಗೇ ತೋರಿಸುವ code ನ ಚಿಕ್ಕ box."}),
        ("Anaconda", {
            "en": "A free bundle that installs Python, Jupyter Notebook and science libraries together.",
            "hi": "एक free bundle जो Python, Jupyter Notebook और science libraries एक साथ install करता है।",
            "hinglish": "Ek free bundle jo Python, Jupyter Notebook aur science libraries ek saath install karta hai.",
            "kn": "Python, Jupyter Notebook ಮತ್ತು science libraries ಅನ್ನು ಒಟ್ಟಿಗೆ install ಮಾಡುವ free bundle."}),
        ("Extension (add-on)", {
            "en": "An add-on that gives an app new features, like the Python extension for VS Code.",
            "hi": "एक add-on जो app को नए features देता है, जैसे VS Code का Python extension।",
            "hinglish": "Ek add-on jo app ko naye features deta hai, jaise VS Code ka Python extension.",
            "kn": "App ಗೆ ಹೊಸ features ಕೊಡುವ add-on, ಉದಾ: VS Code ನ Python extension."}),
        ("Syntax highlighting", {
            "en": "Showing different parts of code in different colours, so it's easier to read.",
            "hi": "Code के अलग-अलग हिस्सों को अलग रंगों में दिखाना, ताकि पढ़ना आसान हो।",
            "hinglish": "Code ke alag-alag hisson ko alag rangon mein dikhana, taaki padhna aasaan ho.",
            "kn": "Code ನ ಬೇರೆ ಬೇರೆ ಭಾಗಗಳನ್ನು ಬೇರೆ ಬಣ್ಣಗಳಲ್ಲಿ ತೋರಿಸೋದು, ಓದೋಕೆ ಸುಲಭ ಆಗಲಿ ಅಂತ."}),
        ("Auto-completion", {
            "en": "The editor suggests the rest of a word while you type, like phone keyboard suggestions.",
            "hi": "Type करते समय editor बाकी शब्द suggest करता है, जैसे phone keyboard के suggestions।",
            "hinglish": "Type karte samay editor baaki shabd suggest karta hai, jaise phone keyboard ke suggestions.",
            "kn": "Type ಮಾಡುವಾಗ editor ಉಳಿದ ಪದವನ್ನು suggest ಮಾಡುತ್ತೆ, phone keyboard suggestions ತರಹ."}),
        ("Module", {
            "en": "A file of ready-made Python code you can import. For now, think of it as the same as a library.",
            "hi": "Ready-made Python code की एक file जिसे import कर सकते हैं। अभी के लिए इसे library जैसा ही समझिए।",
            "hinglish": "Ready-made Python code ki ek file jise import kar sakte hain. Abhi ke liye ise library jaisa hi samajhiye.",
            "kn": "Import ಮಾಡಬಹುದಾದ ready-made Python code ನ file. ಸದ್ಯಕ್ಕೆ ಇದನ್ನು library ತರಹವೇ ಅಂದುಕೊಳ್ಳಿ."}),
        ("pip", {
            "en": "Python's tool for installing libraries, used from the terminal. You'll use it in Lesson 1.7.",
            "hi": "Libraries install करने का Python का tool, जो terminal से चलता है। इसे Lesson 1.7 में use करेंगे।",
            "hinglish": "Libraries install karne ka Python ka tool, jo terminal se chalta hai. Ise Lesson 1.7 mein use karenge.",
            "kn": "Libraries install ಮಾಡುವ Python ನ tool, terminal ಇಂದ use ಮಾಡ್ತಾರೆ. ಇದನ್ನು Lesson 1.7 ನಲ್ಲಿ use ಮಾಡ್ತೀರಿ."}),
    ],
    "1-3": [
        ("Variable", {
            "en": "A named box in the computer's memory that stores a value, like a labelled box on a pharmacy shelf.",
            "hi": "Computer की memory में एक नाम वाला box जो एक value रखता है, जैसे pharmacy की shelf पर label लगा box।",
            "hinglish": "Computer ki memory mein ek naam wala box jo ek value rakhta hai, jaise pharmacy ki shelf par label laga box.",
            "kn": "ಒಂದು value ಅನ್ನು ಇಡುವ, computer memory ಯಲ್ಲಿನ ಹೆಸರಿರುವ box, pharmacy shelf ಮೇಲಿನ label ಇರುವ box ತರಹ."}),
        ("Value", {
            "en": "What is stored inside a variable, such as 500 or \"Paracetamol\".",
            "hi": "Variable के अंदर रखी चीज़, जैसे 500 या \"Paracetamol\"।",
            "hinglish": "Variable ke andar rakhi cheez, jaise 500 ya \"Paracetamol\".",
            "kn": "Variable ಒಳಗೆ ಇಟ್ಟಿರುವುದು, ಉದಾ: 500 ಅಥವಾ \"Paracetamol\"."}),
        ("Assignment (=)", {
            "en": "Storing a value in a variable. In Python, = means \"store\", not \"equals\".",
            "hi": "Variable में value रखना। Python में = का मतलब \"रखो\" है, \"बराबर\" नहीं।",
            "hinglish": "Variable mein value rakhna. Python mein = ka matlab \"rakho\" hai, \"barabar\" nahi.",
            "kn": "Variable ನಲ್ಲಿ value ಇಡೋದು. Python ನಲ್ಲಿ = ಅಂದ್ರೆ \"ಇಡು\", \"ಸಮ\" ಅಲ್ಲ."}),
        ("Keyword", {
            "en": "A word Python keeps for itself, like True, if or for. You can't use it as a variable name.",
            "hi": "Python का अपना खास शब्द, जैसे True, if या for। इसे variable का नाम नहीं बना सकते।",
            "hinglish": "Python ka apna khaas shabd, jaise True, if ya for. Ise variable ka naam nahi bana sakte.",
            "kn": "Python ತನಗಾಗಿ ಇಟ್ಟುಕೊಂಡಿರುವ ಪದ, ಉದಾ: True, if, for. ಇದನ್ನು variable ಹೆಸರಾಗಿ use ಮಾಡಲು ಆಗಲ್ಲ."}),
        ("Data type", {
            "en": "The kind of value something is: a whole number, a decimal number, text, or True/False.",
            "hi": "Value किस तरह की है: पूरी संख्या, दशमलव वाली संख्या, text, या True/False।",
            "hinglish": "Value kis tarah ki hai: poori sankhya, dashamlav wali sankhya, text, ya True/False.",
            "kn": "Value ಯಾವ ರೀತಿಯದು: ಪೂರ್ಣ ಸಂಖ್ಯೆ, ದಶಮಾಂಶ ಸಂಖ್ಯೆ, text, ಅಥವಾ True/False."}),
        ("Integer (int)", {
            "en": "A whole number with no decimal point, like 30 tablets.",
            "hi": "बिना दशमलव वाली पूरी संख्या, जैसे 30 tablets।",
            "hinglish": "Bina dashamlav wali poori sankhya, jaise 30 tablets.",
            "kn": "ದಶಮಾಂಶ ಇಲ್ಲದ ಪೂರ್ಣ ಸಂಖ್ಯೆ, ಉದಾ: 30 tablets."}),
        ("Float", {
            "en": "A number with a decimal point, like a weight of 52.5 kg.",
            "hi": "दशमलव वाली संख्या, जैसे 52.5 kg वज़न।",
            "hinglish": "Dashamlav wali sankhya, jaise 52.5 kg wazan.",
            "kn": "ದಶಮಾಂಶ ಇರುವ ಸಂಖ್ಯೆ, ಉದಾ: 52.5 kg ತೂಕ."}),
        ("Boolean (bool)", {
            "en": "A value that is only True or False, like whether a medicine is in stock.",
            "hi": "ऐसी value जो सिर्फ True या False हो, जैसे दवा stock में है या नहीं।",
            "hinglish": "Aisi value jo sirf True ya False ho, jaise dawa stock mein hai ya nahi.",
            "kn": "True ಅಥವಾ False ಮಾತ್ರ ಆಗಿರುವ value, ಉದಾ: ಔಷಧಿ stock ನಲ್ಲಿ ಇದೆಯಾ ಇಲ್ವಾ."}),
        ("type()", {
            "en": "Shows the data type of a value. type(52.5) gives <class 'float'>.",
            "hi": "किसी value का data type दिखाता है। type(52.5) देता है <class 'float'>।",
            "hinglish": "Kisi value ka data type dikhata hai. type(52.5) deta hai <class 'float'>.",
            "kn": "ಒಂದು value ನ data type ತೋರಿಸುತ್ತೆ. type(52.5) ಕೊಡೋದು <class 'float'>."}),
        ("TypeError", {
            "en": "An error that means you used a value of the wrong data type, such as adding text and a number.",
            "hi": "Error जिसका मतलब है गलत data type की value use की गई, जैसे text और number जोड़ना।",
            "hinglish": "Error jiska matlab hai galat data type ki value use ki gayi, jaise text aur number jodna.",
            "kn": "ತಪ್ಪು data type ನ value use ಮಾಡಿದ್ದೀರಿ ಅನ್ನುವ error, ಉದಾ: text ಮತ್ತು number ಕೂಡಿಸೋದು."}),
    ],
}


def apply():
    for lesson, entries in G.items():
        folder = os.path.join(ROOT, "content", "bp101t", lesson)
        for lang in ["en", "hi", "hinglish", "kn"]:
            path = os.path.join(folder, f"{lang}.json")
            if not os.path.exists(path):  # translation not written yet
                continue
            doc = json.load(open(path, encoding="utf-8"))
            if lang == "en":
                doc["glossary"] = [{"term": t, "meaning": m["en"]} for t, m in entries]
            else:
                # translations merge by position; terms stay English
                doc["glossary"] = [{"meaning": m[lang]} for t, m in entries]
                if "glossary" not in doc.get("translatedSections", []):
                    doc["translatedSections"] = doc.get("translatedSections", []) + ["glossary"]
            json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"lesson {lesson}: {len(entries)} words")


if __name__ == "__main__":
    apply()

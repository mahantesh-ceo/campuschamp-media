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
    "1-4": [
        ("Type casting", {
            "en": "Converting a value from one data type to another, like turning the text \"500\" into the number 500.",
            "hi": "किसी value को एक data type से दूसरे में बदलना, जैसे text \"500\" को number 500 बनाना।",
            "hinglish": "Kisi value ko ek data type se doosre mein badalna, jaise text \"500\" ko number 500 banana.",
            "kn": "ಒಂದು value ಅನ್ನು ಒಂದು data type ಇಂದ ಇನ್ನೊಂದಕ್ಕೆ ಬದಲಾಯಿಸೋದು, ಉದಾ: text \"500\" ಅನ್ನು number 500 ಮಾಡೋದು."}),
        ("int(), float(), str()", {
            "en": "Convert a value to an integer, a float or a string. int(\"500\") gives 500; str(500) gives \"500\".",
            "hi": "Value को integer, float या string में बदलते हैं। int(\"500\") देता है 500; str(500) देता है \"500\"।",
            "hinglish": "Value ko integer, float ya string mein badalte hain. int(\"500\") deta hai 500; str(500) deta hai \"500\".",
            "kn": "Value ಅನ್ನು integer, float ಅಥವಾ string ಆಗಿ ಬದಲಾಯಿಸುತ್ತವೆ. int(\"500\") ಕೊಡೋದು 500; str(500) ಕೊಡೋದು \"500\"."}),
        ("Implicit conversion", {
            "en": "When Python converts a type by itself, e.g. 10 + 2.5 gives the float 12.5. Converting with int(), float() or str() yourself is explicit conversion.",
            "hi": "जब Python खुद type बदल देता है, जैसे 10 + 2.5 का answer float 12.5। int(), float() या str() से खुद बदलना explicit conversion है।",
            "hinglish": "Jab Python khud type badal deta hai, jaise 10 + 2.5 ka answer float 12.5. int(), float() ya str() se khud badalna explicit conversion hai.",
            "kn": "Python ತಾನೇ type ಬದಲಾಯಿಸಿದಾಗ, ಉದಾ: 10 + 2.5 ಉತ್ತರ float 12.5. int(), float() ಅಥವಾ str() ಇಂದ ನಾವೇ ಬದಲಾಯಿಸೋದು explicit conversion."}),
        ("Operator", {
            "en": "A symbol that does something with values, such as + (add) or > (greater than).",
            "hi": "एक symbol जो values के साथ कुछ करता है, जैसे + (जोड़ना) या > (बड़ा है)।",
            "hinglish": "Ek symbol jo values ke saath kuch karta hai, jaise + (jodna) ya > (bada hai).",
            "kn": "Values ಜೊತೆ ಏನಾದರೂ ಮಾಡುವ symbol, ಉದಾ: + (ಕೂಡಿಸು) ಅಥವಾ > (ದೊಡ್ಡದು)."}),
        ("Arithmetic operator", {
            "en": "An operator for calculations: + - * / // % **.",
            "hi": "Calculation करने वाले operators: + - * / // % **।",
            "hinglish": "Calculation karne wale operators: + - * / // % **.",
            "kn": "ಲೆಕ್ಕ ಮಾಡುವ operators: + - * / // % **."}),
        ("Floor division (//)", {
            "en": "Divides and keeps only the whole number. 42 // 10 gives 4, like counting full strips.",
            "hi": "भाग देकर सिर्फ पूरी संख्या रखता है। 42 // 10 देता है 4, जैसे पूरी strips गिनना।",
            "hinglish": "Bhaag dekar sirf poori sankhya rakhta hai. 42 // 10 deta hai 4, jaise poori strips ginna.",
            "kn": "ಭಾಗಿಸಿ ಪೂರ್ಣ ಸಂಖ್ಯೆಯನ್ನು ಮಾತ್ರ ಇಡುತ್ತೆ. 42 // 10 ಕೊಡೋದು 4, ಪೂರ್ತಿ strips ಎಣಿಸಿದ ಹಾಗೆ."}),
        ("Modulus (%)", {
            "en": "Gives the remainder after dividing. 42 % 10 gives 2, like counting loose tablets.",
            "hi": "भाग देने के बाद बचा हुआ (शेषफल) देता है। 42 % 10 देता है 2, जैसे खुली tablets गिनना।",
            "hinglish": "Bhaag dene ke baad bacha hua (sheshphal) deta hai. 42 % 10 deta hai 2, jaise khuli tablets ginna.",
            "kn": "ಭಾಗಿಸಿದ ನಂತರ ಉಳಿದದ್ದು (ಶೇಷ) ಕೊಡುತ್ತೆ. 42 % 10 ಕೊಡೋದು 2, ಬಿಡಿ tablets ಎಣಿಸಿದ ಹಾಗೆ."}),
        ("Comparison operator", {
            "en": "Compares two values and gives True or False: == != > < >= <=.",
            "hi": "दो values की तुलना करके True या False देता है: == != > < >= <=।",
            "hinglish": "Do values ki tulna karke True ya False deta hai: == != > < >= <=.",
            "kn": "ಎರಡು values ಹೋಲಿಸಿ True ಅಥವಾ False ಕೊಡುತ್ತೆ: == != > < >= <=."}),
        ("Logical operator", {
            "en": "Combines True/False answers: and (both True), or (at least one True), not (flips the answer).",
            "hi": "True/False answers को जोड़ता है: and (दोनों True), or (कम से कम एक True), not (answer उलट देता है)।",
            "hinglish": "True/False answers ko jodta hai: and (dono True), or (kam se kam ek True), not (answer ulat deta hai).",
            "kn": "True/False ಉತ್ತರಗಳನ್ನು ಜೋಡಿಸುತ್ತೆ: and (ಎರಡೂ True), or (ಕನಿಷ್ಠ ಒಂದು True), not (ಉತ್ತರ ತಿರುಗಿಸುತ್ತೆ)."}),
        ("Shortcut operator (+=, -=)", {
            "en": "Changes a variable using its own value. stock -= 30 means stock = stock - 30.",
            "hi": "Variable को उसकी अपनी value से बदलता है। stock -= 30 मतलब stock = stock - 30।",
            "hinglish": "Variable ko uski apni value se badalta hai. stock -= 30 matlab stock = stock - 30.",
            "kn": "Variable ಅನ್ನು ಅದರದೇ value ಬಳಸಿ ಬದಲಾಯಿಸುತ್ತೆ. stock -= 30 ಅಂದ್ರೆ stock = stock - 30."}),
        ("ValueError", {
            "en": "An error that means the value can't be used that way, like int(\"52.5\").",
            "hi": "Error जिसका मतलब है कि value को इस तरह use नहीं किया जा सकता, जैसे int(\"52.5\")।",
            "hinglish": "Error jiska matlab hai ki value ko is tarah use nahi kiya ja sakta, jaise int(\"52.5\").",
            "kn": "Value ಅನ್ನು ಆ ರೀತಿ use ಮಾಡಲು ಆಗಲ್ಲ ಅನ್ನುವ error, ಉದಾ: int(\"52.5\")."}),
        ("ZeroDivisionError", {
            "en": "The error Python shows when you divide by zero.",
            "hi": "शून्य से भाग देने पर Python यह error दिखाता है।",
            "hinglish": "Shoonya se bhaag dene par Python yeh error dikhata hai.",
            "kn": "ಸೊನ್ನೆಯಿಂದ ಭಾಗಿಸಿದಾಗ Python ತೋರಿಸುವ error."}),
    ],
    "1-5": [
        ("Function", {
            "en": "A named instruction that does a job when you add brackets after it, like print() or input(). You've been using functions since Lesson 1.1.",
            "hi": "एक नाम वाला निर्देश जो brackets लगाने पर अपना काम करता है, जैसे print() या input()। आप Lesson 1.1 से functions use कर रहे हैं।",
            "hinglish": "Ek naam wala nirdesh jo brackets lagane par apna kaam karta hai, jaise print() ya input(). Aap Lesson 1.1 se functions use kar rahe hain.",
            "kn": "Brackets ಹಾಕಿದಾಗ ತನ್ನ ಕೆಲಸ ಮಾಡುವ ಹೆಸರಿರುವ ಸೂಚನೆ, ಉದಾ: print() ಅಥವಾ input(). Lesson 1.1 ಇಂದ ನೀವು functions use ಮಾಡುತ್ತಿದ್ದೀರಿ."}),
        ("input()", {
            "en": "Shows a question and waits for the user to type an answer and press Enter. The answer is always text.",
            "hi": "एक सवाल दिखाता है और user के answer type करके Enter दबाने का इंतज़ार करता है। Answer हमेशा text होता है।",
            "hinglish": "Ek sawaal dikhata hai aur user ke answer type karke Enter dabane ka intezaar karta hai. Answer hamesha text hota hai.",
            "kn": "ಒಂದು ಪ್ರಶ್ನೆ ತೋರಿಸಿ, user answer type ಮಾಡಿ Enter ಒತ್ತುವವರೆಗೆ ಕಾಯುತ್ತೆ. Answer ಯಾವಾಗಲೂ text."}),
        ("User", {
            "en": "The person using your program, such as a pharmacist typing a patient's weight.",
            "hi": "जो इंसान आपका program use कर रहा है, जैसे patient का वज़न type करने वाला pharmacist।",
            "hinglish": "Jo insaan aapka program use kar raha hai, jaise patient ka wazan type karne wala pharmacist.",
            "kn": "ನಿಮ್ಮ program use ಮಾಡುವ ವ್ಯಕ್ತಿ, ಉದಾ: patient ನ ತೂಕ type ಮಾಡುವ pharmacist."}),
        ("Prompt", {
            "en": "The question input() shows on screen, like \"Weight (kg): \".",
            "hi": "वह सवाल जो input() screen पर दिखाता है, जैसे \"Weight (kg): \"।",
            "hinglish": "Woh sawaal jo input() screen par dikhata hai, jaise \"Weight (kg): \".",
            "kn": "input() screen ಮೇಲೆ ತೋರಿಸುವ ಪ್ರಶ್ನೆ, ಉದಾ: \"Weight (kg): \"."}),
        ("sep and end", {
            "en": "Settings for print(): sep goes between the items, end goes at the end of the line.",
            "hi": "print() की settings: sep items के बीच आता है, end line के आखिर में।",
            "hinglish": "print() ki settings: sep items ke beech aata hai, end line ke aakhir mein.",
            "kn": "print() ನ settings: sep items ನಡುವೆ ಬರುತ್ತೆ, end line ಕೊನೆಯಲ್ಲಿ."}),
        ("f-string", {
            "en": "Text with f before the quotes, where {name} is replaced by the value of name.",
            "hi": "Quotes से पहले f वाला text, जिसमें {name} की जगह name की value आ जाती है।",
            "hinglish": "Quotes se pehle f wala text, jisme {name} ki jagah name ki value aa jaati hai.",
            "kn": "Quotes ಮುಂದೆ f ಇರುವ text, ಅದರಲ್ಲಿ {name} ಜಾಗಕ್ಕೆ name ನ value ಬರುತ್ತೆ."}),
        ("Decimal places (:.1f, :.2f)", {
            "en": "Added inside { } in an f-string to show one or two digits after the decimal point.",
            "hi": "f-string में { } के अंदर लगाते हैं, ताकि दशमलव के बाद एक या दो अंक दिखें।",
            "hinglish": "f-string mein { } ke andar lagaate hain, taaki dashamlav ke baad ek ya do ank dikhein.",
            "kn": "f-string ನಲ್ಲಿ { } ಒಳಗೆ ಹಾಕುತ್ತೇವೆ, ದಶಮಾಂಶದ ನಂತರ ಒಂದು ಅಥವಾ ಎರಡು ಅಂಕೆ ತೋರಿಸಲು."}),
    ],
    "1-6": [
        ("Index", {
            "en": "The position number of a character in a string. Counting starts at 0, so text[0] is the first character.",
            "hi": "String में किसी character का position number। गिनती 0 से शुरू होती है, इसलिए text[0] पहला character है।",
            "hinglish": "String mein kisi character ka position number. Ginti 0 se shuru hoti hai, isliye text[0] pehla character hai.",
            "kn": "String ನಲ್ಲಿ ಒಂದು character ನ position number. ಎಣಿಕೆ 0 ಇಂದ ಶುರು, ಅದಕ್ಕೇ text[0] ಮೊದಲ character."}),
        ("Slice", {
            "en": "A piece of a string, written text[start:end]. It stops just before the end index.",
            "hi": "String का एक हिस्सा, text[start:end] लिखकर। यह end index से ठीक पहले रुकता है।",
            "hinglish": "String ka ek hissa, text[start:end] likhkar. Yeh end index se theek pehle rukta hai.",
            "kn": "String ನ ಒಂದು ಭಾಗ, text[start:end] ಅಂತ ಬರೆಯುತ್ತೇವೆ. ಇದು end index ಗೆ ಸ್ವಲ್ಪ ಮುಂಚೆ ನಿಲ್ಲುತ್ತೆ."}),
        ("Method", {
            "en": "A function that belongs to a value, called with a dot after it, like drug.upper().",
            "hi": "किसी value का अपना function, जिसे value के बाद dot लगाकर call करते हैं, जैसे drug.upper()।",
            "hinglish": "Kisi value ka apna function, jise value ke baad dot lagakar call karte hain, jaise drug.upper().",
            "kn": "ಒಂದು value ಗೆ ಸೇರಿದ function, value ನಂತರ dot ಹಾಕಿ call ಮಾಡುತ್ತೇವೆ, ಉದಾ: drug.upper()."}),
        ("len()", {
            "en": "Counts the characters in a string, spaces included.",
            "hi": "String के characters गिनता है, spaces भी।",
            "hinglish": "String ke characters ginta hai, spaces bhi.",
            "kn": "String ನಲ್ಲಿರುವ characters ಎಣಿಸುತ್ತೆ, spaces ಕೂಡ."}),
        ("strip()", {
            "en": "Removes spaces from both ends of a string.",
            "hi": "String के दोनों सिरों से spaces हटाता है।",
            "hinglish": "String ke dono siron se spaces hatata hai.",
            "kn": "String ನ ಎರಡೂ ತುದಿಗಳಿಂದ spaces ತೆಗೆಯುತ್ತೆ."}),
        ("replace()", {
            "en": "Gives a new string with one piece of text swapped for another: text.replace(old, new).",
            "hi": "एक text की जगह दूसरा text रखकर नई string देता है: text.replace(old, new)।",
            "hinglish": "Ek text ki jagah doosra text rakhkar nayi string deta hai: text.replace(old, new).",
            "kn": "ಒಂದು text ಬದಲು ಇನ್ನೊಂದು text ಹಾಕಿ ಹೊಸ string ಕೊಡುತ್ತೆ: text.replace(old, new)."}),
        ("split()", {
            "en": "Breaks a string into parts wherever a separator appears, such as a comma.",
            "hi": "जहाँ-जहाँ separator आए, जैसे comma, वहाँ string को हिस्सों में तोड़ता है।",
            "hinglish": "Jahan-jahan separator aaye, jaise comma, wahan string ko hisson mein todta hai.",
            "kn": "Separator ಬಂದಲ್ಲೆಲ್ಲಾ, ಉದಾ: comma, string ಅನ್ನು ಭಾಗಗಳಾಗಿ ಒಡೆಯುತ್ತೆ."}),
    ],
    "1-7": [
        ("Module", {
            "en": "A Python file of ready-made code, such as functions and values, that you can import.",
            "hi": "Ready-made code वाली एक Python file, जैसे functions और values, जिसे आप import कर सकते हैं।",
            "hinglish": "Ready-made code wali ek Python file, jaise functions aur values, jise aap import kar sakte hain.",
            "kn": "Ready-made code ಇರುವ ಒಂದು Python file, ಉದಾ: functions ಮತ್ತು values, ಇದನ್ನು import ಮಾಡಬಹುದು."}),
        ("Standard library", {
            "en": "The libraries that come with Python, such as math and datetime. Nothing to install.",
            "hi": "Python के साथ आने वाली libraries, जैसे math और datetime। कुछ install नहीं करना पड़ता।",
            "hinglish": "Python ke saath aane wali libraries, jaise math aur datetime. Kuch install nahi karna padta.",
            "kn": "Python ಜೊತೆಗೇ ಬರುವ libraries, ಉದಾ: math ಮತ್ತು datetime. ಏನೂ install ಮಾಡಬೇಕಿಲ್ಲ."}),
        ("Third-party library", {
            "en": "A library made outside the Python team, such as NumPy, installed separately with pip.",
            "hi": "Python team के बाहर बनी library, जैसे NumPy, जिसे pip से अलग से install करते हैं।",
            "hinglish": "Python team ke bahar bani library, jaise NumPy, jise pip se alag se install karte hain.",
            "kn": "Python team ಹೊರಗೆ ಮಾಡಿದ library, ಉದಾ: NumPy, ಇದನ್ನು pip ಇಂದ ಬೇರೆಯಾಗಿ install ಮಾಡುತ್ತೇವೆ."}),
        ("PyPI", {
            "en": "The Python Package Index: the free online store of third-party libraries that pip downloads from.",
            "hi": "Python Package Index: third-party libraries का free online store, जहाँ से pip download करता है।",
            "hinglish": "Python Package Index: third-party libraries ka free online store, jahan se pip download karta hai.",
            "kn": "Python Package Index: third-party libraries ನ free online store, pip ಇಲ್ಲಿಂದ download ಮಾಡುತ್ತೆ."}),
        ("pip", {
            "en": "Python's installer. Typed in the terminal: pip install to add a library, pip uninstall to remove it.",
            "hi": "Python का installer। Terminal में type करते हैं: library जोड़ने के लिए pip install, हटाने के लिए pip uninstall।",
            "hinglish": "Python ka installer. Terminal mein type karte hain: library jodne ke liye pip install, hatane ke liye pip uninstall.",
            "kn": "Python ನ installer. Terminal ನಲ್ಲಿ type ಮಾಡುತ್ತೇವೆ: library ಸೇರಿಸಲು pip install, ತೆಗೆಯಲು pip uninstall."}),
        ("import", {
            "en": "Brings a module or library into your program so you can use its tools, e.g. import math.",
            "hi": "Module या library को आपके program में लाता है, ताकि उसके tools use कर सकें, जैसे import math।",
            "hinglish": "Module ya library ko aapke program mein laata hai, taaki uske tools use kar sakein, jaise import math.",
            "kn": "Module ಅಥವಾ library ಅನ್ನು ನಿಮ್ಮ program ಗೆ ತರುತ್ತೆ, ಅದರ tools ಬಳಸಲು, ಉದಾ: import math."}),
        ("Alias (as)", {
            "en": "A short name for a library, given with as, like import numpy as np.",
            "hi": "Library का छोटा नाम, as से दिया जाता है, जैसे import numpy as np।",
            "hinglish": "Library ka chhota naam, as se diya jaata hai, jaise import numpy as np.",
            "kn": "Library ಗೆ ಕೊಡುವ ಚಿಕ್ಕ ಹೆಸರು, as ಇಂದ, ಉದಾ: import numpy as np."}),
    ],
    "2-1": [
        ("Condition", {
            "en": "An expression that is either True or False, like temp >= 38.0. It decides whether a block runs.",
            "hi": "ऐसा expression जो True या False हो, जैसे temp >= 38.0। यही तय करता है कि block चलेगा या नहीं।",
            "hinglish": "Aisa expression jo True ya False ho, jaise temp >= 38.0. Yahi tay karta hai ki block chalega ya nahi.",
            "kn": "True ಅಥವಾ False ಆಗುವ expression, ಉದಾ. temp >= 38.0. Block run ಆಗಬೇಕಾ ಬೇಡವಾ ಅಂತ ಇದೇ ತೀರ್ಮಾನಿಸುತ್ತೆ."}),
        ("if statement", {
            "en": "Runs its block only when its condition is True; otherwise Python skips the block.",
            "hi": "अपना block तभी चलाता है जब उसकी condition True हो; वरना Python block छोड़ देता है।",
            "hinglish": "Apna block tabhi chalaata hai jab uski condition True ho; warna Python block chhod deta hai.",
            "kn": "ತನ್ನ condition True ಆದಾಗ ಮಾತ್ರ block run ಮಾಡುತ್ತೆ; ಇಲ್ಲದಿದ್ದರೆ Python block ಬಿಟ್ಟುಬಿಡುತ್ತೆ."}),
        ("else", {
            "en": "The block that runs when none of the conditions above it were True. It has no condition of its own.",
            "hi": "वह block जो तब चलता है जब ऊपर की कोई condition True न हो। इसकी अपनी कोई condition नहीं होती।",
            "hinglish": "Woh block jo tab chalta hai jab upar ki koi condition True na ho. Iski apni koi condition nahi hoti.",
            "kn": "ಮೇಲಿನ ಯಾವ condition ಕೂಡ True ಆಗದಿದ್ದಾಗ run ಆಗುವ block. ಇದಕ್ಕೆ ತನ್ನದೇ condition ಇಲ್ಲ."}),
        ("elif", {
            "en": "Short for \"else if\": checks another condition when the conditions above were False.",
            "hi": "\"Else if\" का छोटा रूप: ऊपर की conditions False हों तो एक और condition जाँचता है।",
            "hinglish": "\"Else if\" ka chhota roop: upar ki conditions False hon to ek aur condition jaanchta hai.",
            "kn": "\"Else if\" ನ ಚಿಕ್ಕ ರೂಪ: ಮೇಲಿನ conditions False ಆದರೆ ಇನ್ನೊಂದು condition check ಮಾಡುತ್ತೆ."}),
        ("Block", {
            "en": "A group of indented lines that belong together, such as the lines under an if.",
            "hi": "Indent की हुई lines का group जो साथ में आती हैं, जैसे if के नीचे की lines।",
            "hinglish": "Indent ki hui lines ka group jo saath mein aati hain, jaise if ke neeche ki lines.",
            "kn": "ಒಟ್ಟಿಗೆ ಸೇರುವ indent ಮಾಡಿದ lines ನ ಗುಂಪು, ಉದಾ. if ಕೆಳಗಿನ lines."}),
        ("Indentation", {
            "en": "The spaces at the start of a line. Python uses 4 spaces to show which lines belong to a block.",
            "hi": "Line की शुरुआत के spaces। कौन-सी lines block में हैं, यह दिखाने के लिए Python 4 spaces use करता है।",
            "hinglish": "Line ki shuruaat ke spaces. Kaun-si lines block mein hain, yeh dikhaane ke liye Python 4 spaces use karta hai.",
            "kn": "Line ಶುರುವಿನ spaces. ಯಾವ lines block ಗೆ ಸೇರಿವೆ ಅಂತ ತೋರಿಸಲು Python 4 spaces ಬಳಸುತ್ತೆ."}),
        ("IndentationError", {
            "en": "The error Python gives when the indentation is missing or uneven, for example no indented line after a colon.",
            "hi": "Indentation न हो या ऊँची-नीची हो तो Python यह error देता है, जैसे colon के बाद indent की हुई line न हो।",
            "hinglish": "Indentation na ho ya oonchi-neechi ho to Python yeh error deta hai, jaise colon ke baad indent ki hui line na ho.",
            "kn": "Indentation ಇಲ್ಲದಿದ್ದಾಗ ಅಥವಾ ಸರಿಯಾಗಿ ಸಾಲಿನಲ್ಲಿ ಇಲ್ಲದಿದ್ದಾಗ Python ಕೊಡುವ error, ಉದಾ. colon ಆದಮೇಲೆ indent ಮಾಡಿದ line ಇಲ್ಲದಿದ್ದಾಗ."}),
    ],
    "2-2": [
        ("Nested if", {
            "en": "An if statement written inside the block of another if or else. Its condition is checked only when Python reaches it.",
            "hi": "किसी दूसरे if या else के block के अंदर लिखा if statement। इसकी condition तभी जाँची जाती है जब Python वहाँ पहुँचे।",
            "hinglish": "Kisi doosre if ya else ke block ke andar likha if statement. Iski condition tabhi jaanchi jaati hai jab Python wahaan pahunche.",
            "kn": "ಇನ್ನೊಂದು if ಅಥವಾ else ನ block ಒಳಗೆ ಬರೆದ if statement. Python ಅಲ್ಲಿಗೆ ತಲುಪಿದಾಗ ಮಾತ್ರ ಇದರ condition check ಆಗುತ್ತೆ."}),
        ("Outer and inner if", {
            "en": "In nested code, the outer if is asked first; the inner if sits inside its block, 4 spaces further in.",
            "hi": "Nested code में बाहर वाला if पहले पूछा जाता है; अंदर वाला if उसके block में, 4 spaces और अंदर होता है।",
            "hinglish": "Nested code mein bahar wala if pehle poochha jaata hai; andar wala if uske block mein, 4 spaces aur andar hota hai.",
            "kn": "Nested code ನಲ್ಲಿ ಹೊರಗಿನ if ಮೊದಲು ಕೇಳಲಾಗುತ್ತೆ; ಒಳಗಿನ if ಅದರ block ಒಳಗೆ, ಇನ್ನೂ 4 spaces ಒಳಗೆ ಇರುತ್ತೆ."}),
        ("Input check (validation)", {
            "en": "Checking that a value makes sense, such as weight > 0, before the program uses it.",
            "hi": "Program किसी value को use करे, उससे पहले जाँचना कि उसका मतलब बनता है, जैसे weight > 0।",
            "hinglish": "Program kisi value ko use kare, usse pehle jaanchna ki uska matlab banta hai, jaise weight > 0.",
            "kn": "Program ಒಂದು value ಬಳಸುವ ಮುಂಚೆ ಅದು ಅರ್ಥಪೂರ್ಣವಾಗಿದೆಯಾ ಅಂತ check ಮಾಡುವುದು, ಉದಾ. weight > 0."}),
        ("NameError", {
            "en": "The error Python gives when you use a name that has no value yet, for example a variable created only in a branch that didn't run.",
            "hi": "जब आप ऐसा नाम use करें जिसकी अभी कोई value नहीं, तब Python यह error देता है, जैसे ऐसी branch में बना variable जो चली ही नहीं।",
            "hinglish": "Jab aap aisa naam use karein jiski abhi koi value nahi, tab Python yeh error deta hai, jaise aisi branch mein bana variable jo chali hi nahi.",
            "kn": "ಇನ್ನೂ value ಇಲ್ಲದ ಹೆಸರನ್ನು ಬಳಸಿದಾಗ Python ಕೊಡುವ error, ಉದಾ. run ಆಗದ branch ನಲ್ಲಿ ಮಾತ್ರ ಮಾಡಿದ variable."}),
    ],
    "2-3": [
        ("Loop", {
            "en": "A block of code that runs again and again, so you don't have to copy the same lines.",
            "hi": "Code का ऐसा block जो बार-बार चलता है, ताकि वही lines copy न करनी पड़ें।",
            "hinglish": "Code ka aisa block jo baar-baar chalta hai, taaki wahi lines copy na karni padein.",
            "kn": "ಮತ್ತೆ ಮತ್ತೆ run ಆಗುವ code block, ಅದೇ lines ಅನ್ನು copy ಮಾಡಬೇಕಿಲ್ಲ."}),
        ("for loop", {
            "en": "A loop that runs its block once for each value in a sequence, such as range(), a string or a list.",
            "hi": "ऐसा loop जो sequence की हर value के लिए अपना block एक बार चलाता है, जैसे range(), string या list।",
            "hinglish": "Aisa loop jo sequence ki har value ke liye apna block ek baar chalaata hai, jaise range(), string ya list.",
            "kn": "Sequence ನ ಪ್ರತಿ value ಗೆ ತನ್ನ block ಅನ್ನು ಒಂದು ಸಲ run ಮಾಡುವ loop, ಉದಾ. range(), string ಅಥವಾ list."}),
        ("Loop variable", {
            "en": "The name after for, like day in for day in range(1, 4). It holds the current value on each iteration.",
            "hi": "for के बाद वाला नाम, जैसे for day in range(1, 4) में day। हर iteration में इसमें मौजूदा value रहती है।",
            "hinglish": "for ke baad wala naam, jaise for day in range(1, 4) mein day. Har iteration mein ismein maujooda value rehti hai.",
            "kn": "for ನಂತರದ ಹೆಸರು, ಉದಾ. for day in range(1, 4) ನಲ್ಲಿ day. ಪ್ರತಿ iteration ನಲ್ಲಿ ಇದರಲ್ಲಿ ಈಗಿನ value ಇರುತ್ತೆ."}),
        ("Iteration", {
            "en": "One run of a loop's block. A loop over range(3) has three iterations.",
            "hi": "Loop के block का एक बार चलना। range(3) वाले loop में तीन iterations होती हैं।",
            "hinglish": "Loop ke block ka ek baar chalna. range(3) wale loop mein teen iterations hoti hain.",
            "kn": "Loop ನ block ಒಂದು ಸಲ run ಆಗುವುದು. range(3) ಮೇಲಿನ loop ಗೆ ಮೂರು iterations."}),
        ("range()", {
            "en": "Makes a run of whole numbers: range(start, stop, step). The stop number is not included.",
            "hi": "पूरे numbers की लड़ी बनाता है: range(start, stop, step)। Stop number शामिल नहीं होता।",
            "hinglish": "Poore numbers ki ladi banaata hai: range(start, stop, step). Stop number shaamil nahi hota.",
            "kn": "ಪೂರ್ಣ numbers ನ ಸರಣಿ ಮಾಡುತ್ತೆ: range(start, stop, step). Stop number ಸೇರಲ್ಲ."}),
        ("List", {
            "en": "Several values kept together inside square brackets, separated by commas, like [500, 650]. More in Unit III.",
            "hi": "Square brackets के अंदर commas से अलग कई values एक साथ, जैसे [500, 650]। ज़्यादा Unit III में।",
            "hinglish": "Square brackets ke andar commas se alag kai values ek saath, jaise [500, 650]. Zyada Unit III mein.",
            "kn": "Square brackets ಒಳಗೆ commas ಇಂದ ಬೇರ್ಪಡಿಸಿದ ಹಲವು values ಒಟ್ಟಿಗೆ, ಉದಾ. [500, 650]. ಹೆಚ್ಚು Unit III ನಲ್ಲಿ."}),
        ("Accumulator", {
            "en": "A variable that collects a result across a loop, such as a total that starts at 0 and grows with +=.",
            "hi": "ऐसा variable जो loop में नतीजा जमा करता है, जैसे 0 से शुरू होकर += से बढ़ने वाला total।",
            "hinglish": "Aisa variable jo loop mein nateeja jama karta hai, jaise 0 se shuru hokar += se badhne wala total.",
            "kn": "Loop ಉದ್ದಕ್ಕೂ ಫಲಿತಾಂಶ ಸಂಗ್ರಹಿಸುವ variable, ಉದಾ. 0 ಇಂದ ಶುರುವಾಗಿ += ಇಂದ ಬೆಳೆಯುವ total."}),
    ],
    "2-4": [
        ("while loop", {
            "en": "A loop that repeats its block as long as its condition is True, checking the condition before every round.",
            "hi": "ऐसा loop जो तब तक अपना block दोहराता है जब तक condition True है, हर round से पहले condition जाँचते हुए।",
            "hinglish": "Aisa loop jo tab tak apna block dohraata hai jab tak condition True hai, har round se pehle condition jaanchte hue.",
            "kn": "Condition True ಆಗಿರುವವರೆಗೆ ತನ್ನ block ಪುನರಾವರ್ತಿಸುವ loop, ಪ್ರತಿ ಸುತ್ತಿಗೆ ಮುಂಚೆ condition check ಮಾಡುತ್ತೆ."}),
        ("Infinite loop", {
            "en": "A loop whose condition never becomes False, so it never stops. Press Stop or Ctrl + C to end it.",
            "hi": "ऐसा loop जिसकी condition कभी False नहीं होती, इसलिए वह कभी नहीं रुकता। रोकने के लिए Stop या Ctrl + C दबाइए।",
            "hinglish": "Aisa loop jiski condition kabhi False nahi hoti, isliye woh kabhi nahi rukta. Rokne ke liye Stop ya Ctrl + C dabaaiye.",
            "kn": "Condition ಯಾವತ್ತೂ False ಆಗದ loop, ಅದಕ್ಕೇ ಅದು ನಿಲ್ಲಲ್ಲ. ನಿಲ್ಲಿಸಲು Stop ಅಥವಾ Ctrl + C ಒತ್ತಿ."}),
        ("break", {
            "en": "Ends a loop immediately; the line after the loop runs next.",
            "hi": "Loop को तुरंत खत्म करता है; loop के बाद वाली line आगे चलती है।",
            "hinglish": "Loop ko turant khatam karta hai; loop ke baad wali line aage chalti hai.",
            "kn": "Loop ಅನ್ನು ತಕ್ಷಣ ಮುಗಿಸುತ್ತೆ; loop ನಂತರದ line ಮುಂದೆ run ಆಗುತ್ತೆ."}),
        ("continue", {
            "en": "Skips the rest of the block for this round only, and moves on to the next round.",
            "hi": "सिर्फ़ इस round के लिए block का बाकी हिस्सा छोड़ता है, और अगले round पर जाता है।",
            "hinglish": "Sirf is round ke liye block ka baaki hissa chhodta hai, aur agle round par jaata hai.",
            "kn": "ಈ ಸುತ್ತಿಗೆ ಮಾತ್ರ block ನ ಉಳಿದ ಭಾಗ ಬಿಟ್ಟು, ಮುಂದಿನ ಸುತ್ತಿಗೆ ಹೋಗುತ್ತೆ."}),
        ("Half-life", {
            "en": "The time it takes for the amount of a drug in the body to fall to half.",
            "hi": "शरीर में किसी दवा की मात्रा को आधा होने में लगने वाला समय।",
            "hinglish": "Shareer mein kisi dawa ki maatra ko aadha hone mein lagne wala samay.",
            "kn": "ದೇಹದಲ್ಲಿ ಔಷಧದ ಪ್ರಮಾಣ ಅರ್ಧಕ್ಕೆ ಇಳಿಯಲು ಬೇಕಾಗುವ ಸಮಯ."}),
    ],
    "2-5": [
        ("def", {
            "en": "The keyword that defines a new function: def name(parameters): followed by an indented body.",
            "hi": "नया function define करने वाला keyword: def name(parameters): और उसके नीचे indent की हुई body।",
            "hinglish": "Naya function define karne wala keyword: def name(parameters): aur uske neeche indent ki hui body.",
            "kn": "ಹೊಸ function define ಮಾಡುವ keyword: def name(parameters): ಮತ್ತು ಅದರ ಕೆಳಗೆ indent ಮಾಡಿದ body."}),
        ("Call (a function)", {
            "en": "To run a function by writing its name with brackets, like label() or mg_to_g(500).",
            "hi": "Function का नाम brackets के साथ लिखकर उसे चलाना, जैसे label() या mg_to_g(500)।",
            "hinglish": "Function ka naam brackets ke saath likhkar use chalaana, jaise label() ya mg_to_g(500).",
            "kn": "Function ನ ಹೆಸರನ್ನು brackets ಜೊತೆ ಬರೆದು ಅದನ್ನು run ಮಾಡುವುದು, ಉದಾ. label() ಅಥವಾ mg_to_g(500)."}),
        ("Parameter", {
            "en": "A name inside the brackets of def. It receives a value each time the function is called.",
            "hi": "def के brackets के अंदर का नाम। हर बार function call होने पर इसे एक value मिलती है।",
            "hinglish": "def ke brackets ke andar ka naam. Har baar function call hone par ise ek value milti hai.",
            "kn": "def ನ brackets ಒಳಗಿನ ಹೆಸರು. Function call ಆದ ಪ್ರತಿ ಸಲ ಇದಕ್ಕೆ ಒಂದು value ಸಿಗುತ್ತೆ."}),
        ("Argument", {
            "en": "The actual value passed to a function in a call, like 500 in mg_to_g(500).",
            "hi": "Call में function को दी गई असली value, जैसे mg_to_g(500) में 500।",
            "hinglish": "Call mein function ko di gayi asli value, jaise mg_to_g(500) mein 500.",
            "kn": "Call ನಲ್ಲಿ function ಗೆ ಕೊಡುವ ನಿಜವಾದ value, ಉದಾ. mg_to_g(500) ನಲ್ಲಿ 500."}),
        ("return", {
            "en": "Sends a result back to where the function was called, and ends the function.",
            "hi": "नतीजा वहाँ वापस भेजता है जहाँ function call हुआ था, और function खत्म करता है।",
            "hinglish": "Nateeja wahaan wapas bhejta hai jahaan function call hua tha, aur function khatam karta hai.",
            "kn": "Function call ಆದ ಜಾಗಕ್ಕೆ ಫಲಿತಾಂಶ ಹಿಂದೆ ಕಳಿಸಿ, function ಮುಗಿಸುತ್ತೆ."}),
        ("None", {
            "en": "Python's value for \"nothing\". A function without return gives back None.",
            "hi": "Python में \"कुछ नहीं\" की value। बिना return का function None वापस देता है।",
            "hinglish": "Python mein \"kuch nahi\" ki value. Bina return ka function None wapas deta hai.",
            "kn": "Python ನಲ್ಲಿ \"ಏನೂ ಇಲ್ಲ\" ಅನ್ನುವ value. return ಇಲ್ಲದ function None ಕೊಡುತ್ತೆ."}),
        ("Default value", {
            "en": "A value given to a parameter in def, like unit=\"mg\". It is used when the call leaves that argument out.",
            "hi": "def में parameter को दी गई value, जैसे unit=\"mg\"। Call में वह argument न हो तो यही use होती है।",
            "hinglish": "def mein parameter ko di gayi value, jaise unit=\"mg\". Call mein woh argument na ho to yahi use hoti hai.",
            "kn": "def ನಲ್ಲಿ parameter ಗೆ ಕೊಟ್ಟ value, ಉದಾ. unit=\"mg\". Call ನಲ್ಲಿ ಆ argument ಇಲ್ಲದಿದ್ದಾಗ ಇದು ಬಳಕೆಯಾಗುತ್ತೆ."}),
        ("Local variable", {
            "en": "A variable created inside a function. It exists only while the function runs.",
            "hi": "Function के अंदर बना variable। यह सिर्फ़ function चलने तक रहता है।",
            "hinglish": "Function ke andar bana variable. Yeh sirf function chalne tak rehta hai.",
            "kn": "Function ಒಳಗೆ ಮಾಡಿದ variable. Function run ಆಗುವವರೆಗೆ ಮಾತ್ರ ಇರುತ್ತೆ."}),
    ],
    "2-6": [
        ("BMI (Body Mass Index)", {
            "en": "Weight in kg divided by the square of height in metres. It is used to screen whether body weight is healthy for a person's height.",
            "hi": "kg में weight भाग metres में height का square। यह जाँचने के लिए use होता है कि height के हिसाब से weight ठीक है या नहीं।",
            "hinglish": "kg mein weight bhaag metres mein height ka square. Yeh jaanchne ke liye use hota hai ki height ke hisaab se weight theek hai ya nahi.",
            "kn": "kg ನ weight ಭಾಗಿಸು metres ನ height ನ square. Height ಗೆ ತಕ್ಕಂತೆ weight ಆರೋಗ್ಯಕರವಾಗಿದೆಯಾ ಅಂತ ನೋಡಲು ಬಳಸುತ್ತಾರೆ."}),
        ("Young's rule", {
            "en": "Child dose = age ÷ (age + 12) × adult dose, for children aged 1 to 12.",
            "hi": "Child dose = age ÷ (age + 12) × adult dose, 1 से 12 साल के बच्चों के लिए।",
            "hinglish": "Child dose = age ÷ (age + 12) × adult dose, 1 se 12 saal ke bachchon ke liye.",
            "kn": "Child dose = age ÷ (age + 12) × adult dose, 1 ರಿಂದ 12 ವರ್ಷದ ಮಕ್ಕಳಿಗೆ."}),
        ("Clark's rule", {
            "en": "Child dose = weight in kg ÷ 70 × adult dose (or weight in pounds ÷ 150 × adult dose).",
            "hi": "Child dose = kg में weight ÷ 70 × adult dose (या pounds में weight ÷ 150 × adult dose)।",
            "hinglish": "Child dose = kg mein weight ÷ 70 × adult dose (ya pounds mein weight ÷ 150 × adult dose).",
            "kn": "Child dose = kg ನಲ್ಲಿ weight ÷ 70 × adult dose (ಅಥವಾ pounds ನಲ್ಲಿ weight ÷ 150 × adult dose)."}),
        ("round()", {
            "en": "Rounds a number to the nearest whole number, or to a number of decimal places: round(142.86) is 143.",
            "hi": "Number को सबसे पास के पूरे number पर, या कुछ decimal places तक round करता है: round(142.86) है 143।",
            "hinglish": "Number ko sabse paas ke poore number par, ya kuch decimal places tak round karta hai: round(142.86) hai 143.",
            "kn": "Number ಅನ್ನು ಹತ್ತಿರದ ಪೂರ್ಣ number ಗೆ, ಅಥವಾ ಕೆಲವು decimal places ಗೆ round ಮಾಡುತ್ತೆ: round(142.86) ಅಂದರೆ 143."}),
        ("Menu-driven program", {
            "en": "A program that shows a list of choices in a loop, runs the one the user picks, and repeats until the user chooses to exit.",
            "hi": "ऐसा program जो loop में choices की list दिखाता है, user की चुनी हुई चलाता है, और exit चुनने तक दोहराता है।",
            "hinglish": "Aisa program jo loop mein choices ki list dikhaata hai, user ki chuni hui chalaata hai, aur exit chunne tak dohraata hai.",
            "kn": "Loop ನಲ್ಲಿ choices ನ list ತೋರಿಸಿ, user ಆರಿಸಿದ್ದನ್ನು run ಮಾಡಿ, user exit ಆರಿಸುವವರೆಗೆ ಪುನರಾವರ್ತಿಸುವ program."}),
    ],
    "3-1": [
        ("Dataset", {
            "en": "A collection of related data, like a week of readings or a register of patients, used for analysis.",
            "hi": "Analysis के लिए जुड़े हुए data का collection, जैसे हफ़्ते भर की readings या patients का register।",
            "hinglish": "Analysis ke liye jude hue data ka collection, jaise hafte bhar ki readings ya patients ka register.",
            "kn": "Analysis ಗಾಗಿ ಸಂಬಂಧಿತ data ಸಂಗ್ರಹ, ಒಂದು ವಾರದ readings ಅಥವಾ patients register ತರಹ."}),
        ("List", {
            "en": "An ordered collection of items in square brackets, held in one variable: [\"Aspirin\", \"Insulin\"].",
            "hi": "Square brackets में items का क्रम वाला collection, एक variable में: [\"Aspirin\", \"Insulin\"]।",
            "hinglish": "Square brackets mein items ka kram wala collection, ek variable mein: [\"Aspirin\", \"Insulin\"].",
            "kn": "Square brackets ಒಳಗಿನ items ನ ಕ್ರಮದ collection, ಒಂದೇ variable ನಲ್ಲಿ: [\"Aspirin\", \"Insulin\"]."}),
        ("Index", {
            "en": "The position number of an item in a list. Counting starts at 0, so the first item is list[0].",
            "hi": "List में किसी item का position number। गिनती 0 से शुरू होती है, इसलिए पहला item list[0] है।",
            "hinglish": "List mein kisi item ka position number. Ginti 0 se shuru hoti hai, isliye pehla item list[0] hai.",
            "kn": "List ನಲ್ಲಿ ಒಂದು item ನ position number. ಎಣಿಕೆ 0 ಇಂದ ಶುರು, ಹಾಗಾಗಿ ಮೊದಲ item list[0]."}),
        ("Negative index", {
            "en": "An index counted from the end: list[-1] is the last item, list[-2] the one before it.",
            "hi": "आखिर से गिना गया index: list[-1] आखिरी item है, list[-2] उससे पहले वाला।",
            "hinglish": "Aakhir se gina gaya index: list[-1] aakhri item hai, list[-2] usse pehle wala.",
            "kn": "ಕೊನೆಯಿಂದ ಎಣಿಸಿದ index: list[-1] ಕೊನೆಯ item, list[-2] ಅದರ ಹಿಂದಿನದು."}),
        ("Slice", {
            "en": "A part of a list, list[start:stop], from start up to but not including stop. It makes a new list.",
            "hi": "List का एक हिस्सा, list[start:stop], start से stop तक पर stop शामिल नहीं। यह नई list बनाता है।",
            "hinglish": "List ka ek hissa, list[start:stop], start se stop tak par stop shaamil nahi. Yeh nayi list banata hai.",
            "kn": "List ನ ಒಂದು ಭಾಗ, list[start:stop], start ಇಂದ stop ವರೆಗೆ ಆದರೆ stop ಸೇರಲ್ಲ. ಇದು ಹೊಸ list ಮಾಡುತ್ತೆ."}),
        ("Mutable", {
            "en": "Can be changed after it is made. Lists are mutable (stock[1] = 60 works); strings are not.",
            "hi": "बनने के बाद बदला जा सकता है। Lists mutable हैं (stock[1] = 60 चलता है); strings नहीं।",
            "hinglish": "Banne ke baad badla ja sakta hai. Lists mutable hain (stock[1] = 60 chalta hai); strings nahi.",
            "kn": "ಮಾಡಿದ ನಂತರ ಬದಲಾಯಿಸಬಹುದು. Lists mutable (stock[1] = 60 ಕೆಲಸ ಮಾಡುತ್ತೆ); strings ಅಲ್ಲ."}),
        ("IndexError", {
            "en": "The error when you ask for an index the list doesn't have, like [3] in a list of 3 items.",
            "hi": "जब list में न होने वाला index माँगें तब आने वाली error, जैसे 3 items वाली list में [3]।",
            "hinglish": "Jab list mein na hone wala index maangein tab aane wali error, jaise 3 items wali list mein [3].",
            "kn": "List ನಲ್ಲಿ ಇಲ್ಲದ index ಕೇಳಿದಾಗ ಬರುವ error, 3 items ಇರುವ list ನಲ್ಲಿ [3] ತರಹ."}),
    ],
    "3-2": [
        ("Tuple", {
            "en": "An ordered collection in round brackets, like (128, 84). It can be read like a list but never changed.",
            "hi": "Round brackets में क्रम वाला collection, जैसे (128, 84)। इसे list की तरह पढ़ सकते हैं पर कभी बदल नहीं सकते।",
            "hinglish": "Round brackets mein kram wala collection, jaise (128, 84). Ise list ki tarah padh sakte hain par kabhi badal nahi sakte.",
            "kn": "Round brackets ಒಳಗಿನ ಕ್ರಮದ collection, (128, 84) ತರಹ. List ತರಹ ಓದಬಹುದು ಆದರೆ ಯಾವತ್ತೂ ಬದಲಾಯಿಸಲು ಆಗಲ್ಲ."}),
        ("Immutable", {
            "en": "Cannot be changed after it is made. Tuples and strings are immutable.",
            "hi": "बनने के बाद बदला नहीं जा सकता। Tuples और strings immutable हैं।",
            "hinglish": "Banne ke baad badla nahi ja sakta. Tuples aur strings immutable hain.",
            "kn": "ಮಾಡಿದ ನಂತರ ಬದಲಾಯಿಸಲು ಆಗಲ್ಲ. Tuples ಮತ್ತು strings immutable."}),
        ("Unpacking", {
            "en": "Splitting a tuple into separate variables in one line: name, strength = (\"Amoxicillin\", 500).",
            "hi": "एक line में tuple को अलग variables में बाँटना: name, strength = (\"Amoxicillin\", 500)।",
            "hinglish": "Ek line mein tuple ko alag variables mein baantna: name, strength = (\"Amoxicillin\", 500).",
            "kn": "ಒಂದೇ line ನಲ್ಲಿ tuple ಅನ್ನು ಬೇರೆ variables ಆಗಿ ಒಡೆಯುವುದು: name, strength = (\"Amoxicillin\", 500)."}),
        ("Dictionary", {
            "en": "A collection of key: value pairs in curly braces. You find a value by its key, not by position.",
            "hi": "Curly braces में key: value pairs का collection। Value को position से नहीं, उसकी key से ढूँढते हैं।",
            "hinglish": "Curly braces mein key: value pairs ka collection. Value ko position se nahi, uski key se dhoondhte hain.",
            "kn": "Curly braces ಒಳಗಿನ key: value pairs ನ collection. Value ಅನ್ನು position ಇಂದ ಅಲ್ಲ, ಅದರ key ಇಂದ ಹುಡುಕುತ್ತೀರಿ."}),
        ("Key", {
            "en": "The name you look a value up by, like \"Ibuprofen\" in a dose dictionary. Each key appears only once.",
            "hi": "वह नाम जिससे value ढूँढते हैं, जैसे dose dictionary में \"Ibuprofen\"। हर key सिर्फ़ एक बार आती है।",
            "hinglish": "Woh naam jisse value dhoondhte hain, jaise dose dictionary mein \"Ibuprofen\". Har key sirf ek baar aati hai.",
            "kn": "Value ಹುಡುಕುವ ಹೆಸರು, dose dictionary ನಲ್ಲಿ \"Ibuprofen\" ತರಹ. ಪ್ರತಿ key ಒಂದೇ ಸಲ ಬರುತ್ತೆ."}),
        ("Value", {
            "en": "What is stored under a key: the 400 in \"Ibuprofen\": 400. It can be any type.",
            "hi": "Key के नीचे जो रखा है: \"Ibuprofen\": 400 में 400। यह किसी भी type का हो सकता है।",
            "hinglish": "Key ke neeche jo rakha hai: \"Ibuprofen\": 400 mein 400. Yeh kisi bhi type ka ho sakta hai.",
            "kn": "Key ಕೆಳಗೆ ಇಟ್ಟಿರುವುದು: \"Ibuprofen\": 400 ನಲ್ಲಿ 400. ಇದು ಯಾವ type ಆದರೂ ಆಗಬಹುದು."}),
        ("KeyError", {
            "en": "The error when you look up a key the dictionary doesn't have.",
            "hi": "जब dictionary में न होने वाली key ढूँढें तब आने वाली error।",
            "hinglish": "Jab dictionary mein na hone wali key dhoondhein tab aane wali error.",
            "kn": "Dictionary ನಲ್ಲಿ ಇಲ್ಲದ key ಹುಡುಕಿದಾಗ ಬರುವ error."}),
        ("get()", {
            "en": "Looks up a key safely: d.get(key, default) returns the default instead of a KeyError.",
            "hi": "Key को सुरक्षित ढूँढता है: d.get(key, default) KeyError की जगह default देता है।",
            "hinglish": "Key ko surakshit dhoondhta hai: d.get(key, default) KeyError ki jagah default deta hai.",
            "kn": "Key ಅನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ಹುಡುಕುತ್ತೆ: d.get(key, default) KeyError ಬದಲು default ಕೊಡುತ್ತೆ."}),
    ],
    "3-3": [
        ("Method", {
            "en": "A function that belongs to a value, written after a dot: queue.append(\"Anil\").",
            "hi": "किसी value का अपना function, dot के बाद लिखा जाता है: queue.append(\"Anil\")।",
            "hinglish": "Kisi value ka apna function, dot ke baad likha jaata hai: queue.append(\"Anil\").",
            "kn": "ಒಂದು value ಗೆ ಸೇರಿದ function, dot ನಂತರ ಬರೆಯುತ್ತಾರೆ: queue.append(\"Anil\")."}),
        ("append()", {
            "en": "Adds one item at the end of a list.",
            "hi": "List के आखिर में एक item जोड़ता है।",
            "hinglish": "List ke aakhir mein ek item jodta hai.",
            "kn": "List ನ ಕೊನೆಗೆ ಒಂದು item ಸೇರಿಸುತ್ತೆ."}),
        ("remove()", {
            "en": "Deletes the first item with a given value. ValueError if the value isn't there.",
            "hi": "दी गई value वाला पहला item हटाता है। Value न हो तो ValueError।",
            "hinglish": "Di gayi value wala pehla item hataata hai. Value na ho to ValueError.",
            "kn": "ಕೊಟ್ಟ value ಇರುವ ಮೊದಲ item ತೆಗೆಯುತ್ತೆ. Value ಇಲ್ಲದಿದ್ದರೆ ValueError."}),
        ("pop()", {
            "en": "Removes an item and gives it back: the last one by default, or pop(i) for index i.",
            "hi": "Item हटाकर वापस देता है: default में आखिरी, या index i के लिए pop(i)।",
            "hinglish": "Item hatakar wapas deta hai: default mein aakhri, ya index i ke liye pop(i).",
            "kn": "Item ತೆಗೆದು ಹಿಂದೆ ಕೊಡುತ್ತೆ: default ಆಗಿ ಕೊನೆಯದು, ಅಥವಾ index i ಗೆ pop(i)."}),
        ("sort()", {
            "en": "Sorts a list in place and returns None.",
            "hi": "List को उसी में sort करता है और None लौटाता है।",
            "hinglish": "List ko usi mein sort karta hai aur None lautaata hai.",
            "kn": "List ಅನ್ನು ಅದರಲ್ಲೇ sort ಮಾಡಿ None ಕೊಡುತ್ತೆ."}),
        ("sorted()", {
            "en": "Returns a new sorted list and leaves the original unchanged.",
            "hi": "नई sorted list लौटाता है और original को वैसा ही छोड़ता है।",
            "hinglish": "Nayi sorted list lautaata hai aur original ko waisa hi chhodta hai.",
            "kn": "ಹೊಸ sorted list ಕೊಡುತ್ತೆ, original ಅನ್ನು ಹಾಗೇ ಬಿಡುತ್ತೆ."}),
    ],
    "3-4": [
        ("NumPy", {
            "en": "Numerical Python: the library for fast maths on arrays. Loaded with import numpy as np.",
            "hi": "Numerical Python: arrays पर तेज़ maths की library। import numpy as np से load होती है।",
            "hinglish": "Numerical Python: arrays par tez maths ki library. import numpy as np se load hoti hai.",
            "kn": "Numerical Python: arrays ಮೇಲೆ ವೇಗದ maths ಮಾಡುವ library. import numpy as np ಇಂದ load ಆಗುತ್ತೆ."}),
        ("Array", {
            "en": "NumPy's collection of values of one type, made with np.array(). Maths on it works on every item.",
            "hi": "एक type की values का NumPy collection, np.array() से बनता है। इस पर maths हर item पर चलता है।",
            "hinglish": "Ek type ki values ka NumPy collection, np.array() se banta hai. Is par maths har item par chalta hai.",
            "kn": "ಒಂದೇ type ನ values ಇರುವ NumPy collection, np.array() ಇಂದ ಮಾಡುತ್ತಾರೆ. ಇದರ ಮೇಲಿನ maths ಪ್ರತಿ item ಮೇಲೂ ಆಗುತ್ತೆ."}),
        ("Vectorised", {
            "en": "Done on every item of an array at once, with no loop: doses / 1000.",
            "hi": "Array के हर item पर एक साथ, बिना loop के: doses / 1000।",
            "hinglish": "Array ke har item par ek saath, bina loop ke: doses / 1000.",
            "kn": "Array ನ ಪ್ರತಿ item ಮೇಲೆ ಒಂದೇ ಸಲ, loop ಇಲ್ಲದೆ: doses / 1000."}),
        ("Mean", {
            "en": "The average: the total divided by the number of values. arr.mean() in NumPy.",
            "hi": "Average: कुल जोड़ भाग values की संख्या। NumPy में arr.mean()।",
            "hinglish": "Average: kul jod bhaag values ki sankhya. NumPy mein arr.mean().",
            "kn": "Average: ಒಟ್ಟು ಮೊತ್ತ ಭಾಗಿಸು values ಸಂಖ್ಯೆ. NumPy ನಲ್ಲಿ arr.mean()."}),
        ("Standard deviation", {
            "en": "How spread out the values are around the mean. arr.std(); small means consistent readings.",
            "hi": "Values mean के आसपास कितनी फैली हैं। arr.std(); छोटा मतलब readings एक जैसी हैं।",
            "hinglish": "Values mean ke aaspaas kitni phaili hain. arr.std(); chhota matlab readings ek jaisi hain.",
            "kn": "Values mean ಸುತ್ತ ಎಷ್ಟು ಹರಡಿವೆ. arr.std(); ಕಡಿಮೆ ಅಂದ್ರೆ readings ಒಂದೇ ತರಹ ಇವೆ."}),
        ("Boolean mask", {
            "en": "An array of True and False from a condition; arr[mask] keeps the True items.",
            "hi": "Condition से बना True और False का array; arr[mask] सिर्फ़ True वाले items रखता है।",
            "hinglish": "Condition se bana True aur False ka array; arr[mask] sirf True wale items rakhta hai.",
            "kn": "Condition ಇಂದ ಬರುವ True ಮತ್ತು False ನ array; arr[mask] True items ಮಾತ್ರ ಉಳಿಸುತ್ತೆ."}),
    ],
    "3-5": [
        ("CSV", {
            "en": "Comma-Separated Values: a plain-text table, one record per line, values separated by commas.",
            "hi": "Comma-Separated Values: plain text की table, हर line में एक record, values commas से अलग।",
            "hinglish": "Comma-Separated Values: plain text ki table, har line mein ek record, values commas se alag.",
            "kn": "Comma-Separated Values: plain text table, ಪ್ರತಿ line ನಲ್ಲಿ ಒಂದು record, values commas ಇಂದ ಬೇರೆ."}),
        ("Header", {
            "en": "The first line of a CSV file, with the column names, like drug,strips.",
            "hi": "CSV file की पहली line, जिसमें columns के नाम होते हैं, जैसे drug,strips।",
            "hinglish": "CSV file ki pehli line, jismein columns ke naam hote hain, jaise drug,strips.",
            "kn": "CSV file ನ ಮೊದಲ line, columns ಹೆಸರುಗಳು ಇರುತ್ತವೆ, drug,strips ತರಹ."}),
        ("File mode", {
            "en": "How a file is opened: \"r\" to read, \"w\" to write (erases first), \"a\" to add at the end.",
            "hi": "File कैसे खुलती है: \"r\" पढ़ने, \"w\" लिखने (पहले मिटाकर), \"a\" आखिर में जोड़ने के लिए।",
            "hinglish": "File kaise khulti hai: \"r\" padhne, \"w\" likhne (pehle mitaakar), \"a\" aakhir mein jodne ke liye.",
            "kn": "File ಹೇಗೆ open ಆಗುತ್ತೆ: \"r\" ಓದಲು, \"w\" ಬರೆಯಲು (ಮೊದಲು ಅಳಿಸಿ), \"a\" ಕೊನೆಗೆ ಸೇರಿಸಲು."}),
        ("with", {
            "en": "with open(...) as f: opens a file and closes it automatically when the block ends.",
            "hi": "with open(...) as f: file खोलता है और block खत्म होते ही उसे अपने आप बंद करता है।",
            "hinglish": "with open(...) as f: file kholta hai aur block khatam hote hi use apne aap band karta hai.",
            "kn": "with open(...) as f: file open ಮಾಡಿ, block ಮುಗಿದಾಗ ತಾನಾಗೇ close ಮಾಡುತ್ತೆ."}),
        ("csv.reader", {
            "en": "Reads a CSV file and gives each row as a list of strings.",
            "hi": "CSV file पढ़कर हर row को strings की list के रूप में देता है।",
            "hinglish": "CSV file padhkar har row ko strings ki list ke roop mein deta hai.",
            "kn": "CSV file ಓದಿ ಪ್ರತಿ row ಅನ್ನು strings ನ list ಆಗಿ ಕೊಡುತ್ತೆ."}),
        ("csv.DictReader", {
            "en": "Reads a CSV file and gives each row as a dictionary, using the header names as keys.",
            "hi": "CSV file पढ़कर हर row को dictionary के रूप में देता है, header के नाम keys बनते हैं।",
            "hinglish": "CSV file padhkar har row ko dictionary ke roop mein deta hai, header ke naam keys bante hain.",
            "kn": "CSV file ಓದಿ ಪ್ರತಿ row ಅನ್ನು dictionary ಆಗಿ ಕೊಡುತ್ತೆ, header ಹೆಸರುಗಳು keys ಆಗುತ್ತವೆ."}),
    ],
    "3-6": [
        ("Structured data", {
            "en": "Data organised as records that all have the same fields, like a table.",
            "hi": "ऐसे records में रखा data जिनके fields एक जैसे हों, table की तरह।",
            "hinglish": "Aise records mein rakha data jinke fields ek jaise hon, table ki tarah.",
            "kn": "ಒಂದೇ fields ಇರುವ records ಆಗಿ ಜೋಡಿಸಿದ data, table ತರಹ."}),
        ("Record", {
            "en": "One row of a dataset: one patient, one visit or one report.",
            "hi": "Dataset की एक row: एक patient, एक visit या एक report।",
            "hinglish": "Dataset ki ek row: ek patient, ek visit ya ek report.",
            "kn": "Dataset ನ ಒಂದು row: ಒಬ್ಬ patient, ಒಂದು visit ಅಥವಾ ಒಂದು report."}),
        ("Field", {
            "en": "One column of a dataset, like age or sugar. In Python, a key of each record's dictionary.",
            "hi": "Dataset का एक column, जैसे age या sugar। Python में हर record की dictionary की एक key।",
            "hinglish": "Dataset ka ek column, jaise age ya sugar. Python mein har record ki dictionary ki ek key.",
            "kn": "Dataset ನ ಒಂದು column, age ಅಥವಾ sugar ತರಹ. Python ನಲ್ಲಿ ಪ್ರತಿ record dictionary ನ ಒಂದು key."}),
        ("Missing value", {
            "en": "A field with no data recorded: None in Python, a blank cell in Excel.",
            "hi": "जिस field में data दर्ज न हो: Python में None, Excel में खाली cell।",
            "hinglish": "Jis field mein data darj na ho: Python mein None, Excel mein khaali cell.",
            "kn": "Data ದಾಖಲಾಗದ field: Python ನಲ್ಲಿ None, Excel ನಲ್ಲಿ ಖಾಲಿ cell."}),
        ("Data dictionary", {
            "en": "A list of every field with its name, type, unit and allowed values.",
            "hi": "हर field की list, उसके नाम, type, unit और allowed values के साथ।",
            "hinglish": "Har field ki list, uske naam, type, unit aur allowed values ke saath.",
            "kn": "ಪ್ರತಿ field ನ ಹೆಸರು, type, unit ಮತ್ತು allowed values ಇರುವ list."}),
        ("De-identification", {
            "en": "Removing names, phone numbers and other identifiers so a record can't be traced to a person.",
            "hi": "नाम, phone number और दूसरी पहचान हटाना ताकि record किसी व्यक्ति तक न पहुँचे।",
            "hinglish": "Naam, phone number aur doosri pehchaan hataana taaki record kisi vyakti tak na pahunche.",
            "kn": "Record ಒಬ್ಬ ವ್ಯಕ್ತಿಗೆ ಸಂಬಂಧಿಸದಂತೆ ಹೆಸರು, phone number ಮತ್ತು ಇತರ ಗುರುತುಗಳನ್ನು ತೆಗೆಯುವುದು."}),
    ],
    "3-7": [
        ("Batch", {
            "en": "One lot of a product made together, with its own batch number, tested before release.",
            "hi": "एक साथ बना product का एक lot, अपने batch number के साथ, release से पहले test होता है।",
            "hinglish": "Ek saath bana product ka ek lot, apne batch number ke saath, release se pehle test hota hai.",
            "kn": "ಒಟ್ಟಿಗೆ ತಯಾರಾದ product ನ ಒಂದು lot, ತನ್ನದೇ batch number ಜೊತೆ, release ಮುಂಚೆ test ಆಗುತ್ತೆ."}),
        ("Assay", {
            "en": "The test of how much drug a tablet contains, as a % of the amount on the label.",
            "hi": "Tablet में कितनी drug है उसका test, label पर लिखी मात्रा के % में।",
            "hinglish": "Tablet mein kitni drug hai uska test, label par likhi maatra ke % mein.",
            "kn": "Tablet ನಲ್ಲಿ ಎಷ್ಟು drug ಇದೆ ಎಂಬ test, label ಮೇಲಿನ ಪ್ರಮಾಣದ % ಆಗಿ."}),
        ("Dissolution test", {
            "en": "Measures how much of the drug comes out of a tablet into liquid in a set time.",
            "hi": "तय समय में tablet से कितनी drug liquid में निकलती है, यह मापता है।",
            "hinglish": "Tay samay mein tablet se kitni drug liquid mein nikalti hai, yeh maapta hai.",
            "kn": "ನಿಗದಿತ ಸಮಯದಲ್ಲಿ tablet ಇಂದ ಎಷ್ಟು drug liquid ಗೆ ಬರುತ್ತೆ ಅಂತ ಅಳೆಯುತ್ತೆ."}),
        ("Specification", {
            "en": "The limits a product must meet to be released, like assay 95% to 105%.",
            "hi": "Release होने के लिए product को जो limits पूरी करनी हैं, जैसे assay 95% से 105%।",
            "hinglish": "Release hone ke liye product ko jo limits poori karni hain, jaise assay 95% se 105%.",
            "kn": "Release ಆಗಲು product ಪೂರೈಸಬೇಕಾದ limits, assay 95% ಇಂದ 105% ತರಹ."}),
        ("Data pipeline", {
            "en": "The steps data goes through: read, convert, check, summarise, report.",
            "hi": "वे steps जिनसे data गुज़रता है: पढ़ना, convert, check, सार, report।",
            "hinglish": "Woh steps jinse data guzarta hai: padhna, convert, check, saar, report.",
            "kn": "Data ಹಾದುಹೋಗುವ ಹಂತಗಳು: ಓದು, convert, check, ಸಾರಾಂಶ, report."}),
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

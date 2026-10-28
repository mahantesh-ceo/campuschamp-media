"""Lesson 1.2 translations (Hindi, Hinglish, Kannada) and voice scripts.

Run to write content/bp101t/1-2/{hi,hinglish,kn}.json and scripts/bp101t/1-2.json.
Lists keep the English order because the website merges by position.
"""
import json
import os

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
SECTIONS = ["hook", "learn", "explanation", "walkthrough", "errors", "mistakes", "tasks",
            "quiz", "exam", "mindmap", "summary", "video", "animations"]

T = {}

# ======================================================================= Hindi
T["hi"] = {
    "hook": {
        "title": "अपना coding workspace तैयार कीजिए",
        "md": "इस lesson के अंत तक आप जानेंगे कि laptop पर **Python कैसे install** करें, **कौन सा IDE चुनें** (Jupyter Notebook, PyCharm या VS Code), और **IDE, text editor से बेहतर क्यों है**, जो exam का एक favourite question है।\n\nLaptop नहीं है? कोई बात नहीं। इस course की हर चीज़ **Champ Lab** में आपके phone पर भी चलती है।",
    },
    "learn": [
        "**Python install** कैसे करें और check कैसे करें कि वह काम कर रहा है",
        "**IDE** क्या है, और तीन popular IDEs: **Jupyter Notebook, PyCharm और VS Code**",
        "**Text editors के मुकाबले IDEs के फायदे**",
    ],
    "explanation": [
        {
            "heading": "\"Python install करना\" मतलब क्या?",
            "md": "Lesson 1.1 में आपने सीखा कि **interpreter** आपका code पढ़ता और चलाता है। Python install करने का मतलब है इस interpreter को अपने computer पर रखना।\n\n**Steps (Windows):**\n1. **python.org → Downloads** पर जाइए और latest Python 3 installer download कीजिए।\n2. Installer खोलिए और पहली screen के नीचे **\"Add python.exe to PATH\" पर tick** कीजिए। यह एक checkbox बहुत सी परेशानी बचाता है।\n3. **Install Now** पर click कीजिए और पूरा होने दीजिए।\n4. **Command Prompt** खोलिए और `python --version` type कीजिए। अगर `Python 3.12.4` जैसा कुछ दिखे, तो Python तैयार है।\n\nMac पर python.org का installer use कीजिए और Terminal में `python3 --version` से check कीजिए।",
            "callout": {"title": "Tip", "md": "हमेशा **Python 3** install कीजिए। पुराने tutorials Python 2 use करते हैं, जो अब supported नहीं है।"},
        },
        {
            "heading": "Text editor बनाम IDE",
            "md": "आप Python किसी भी **text editor** में लिख सकते हैं, जैसे Notepad। लेकिन text editor सिर्फ plain text रखता है। वह आपका code न चला सकता है, न रंग दे सकता है, न गलतियाँ बता सकता है।\n\n**IDE** सब कुछ एक जगह देता है: editor, code चलाने का तरीका, error hints और bugs ढूँढने के tools।\n\nऐसे सोचिए: **सादे कागज़** पर prescription लिखना काम करता है, लेकिन **pharmacy software** spelling check करता है, interactions की warning देता है और label भी print कर देता है। Text editor कागज़ है; IDE software है।",
            "callout": {"title": "IDE", "md": "**Integrated Development Environment**: एक application जिसमें code editor, programs चलाने का तरीका, error checking और debugging tools सब एक साथ होते हैं।"},
        },
        {
            "heading": "तीन popular IDEs",
            "md": "| IDE | किसके लिए best | जानने लायक बात |\n|---|---|---|\n| **Jupyter Notebook** | Data analysis, graphs, step-by-step experiments | Code छोटे **cells** में चलता है, और हर cell का output या graph ठीक उसके नीचे दिखता है। **Anaconda** के साथ आता है, और **Google Colab** में online free चलता है। |\n| **PyCharm** | बड़े projects | **JetBrains** का full-featured Python IDE। **Community** edition free है। |\n| **VS Code** | हर तरह की coding | **Microsoft** का free, हल्का editor। **Python extension** जोड़ते ही यह powerful Python IDE बन जाता है। |\n\nइस course के लिए **Jupyter Notebook** (या Google Colab) सबसे useful है, क्योंकि pharmacy का काम ज़्यादातर data और graphs का होता है।",
            "callout": {"title": "Anaconda", "md": "एक free bundle जो Python, Jupyter Notebook और popular science libraries एक साथ install कर देता है।"},
        },
        {
            "heading": "Text editors के मुकाबले IDEs के फायदे",
            "md": "| Feature | Text editor | IDE |\n|---|---|---|\n| **Syntax highlighting** (रंगीन code) | ❌ | ✅ |\n| **Auto-completion** (type करते समय शब्द suggest करना) | ❌ | ✅ |\n| Type करते समय **error hints** | ❌ | ✅ |\n| **एक click में run** करके output देखना | ❌ | ✅ |\n| **Debugger** (bugs ढूँढने के लिए line by line चलाना) | ❌ | ✅ |\n| **Project और files संभालना** | ❌ | ✅ |\n| Libraries और extensions आसानी से **install करना** | ❌ | ✅ |\n\nसीधी बात: IDE आपकी मदद करता है **तेज़ी से लिखने, कम गलतियाँ करने और bugs जल्दी पकड़ने** में।",
        },
        {
            "heading": "Laptop नहीं है? Browser use कीजिए",
            "md": "यह course सीखने के लिए आपको कुछ भी install करने की ज़रूरत नहीं:\n\n- **Champ Lab** आपके browser में Python चलाता है, phone पर भी।\n- **Google Colab** आपके Google account से free online Jupyter Notebook देता है।\n\nजब हो सके, laptop पर Python install कीजिए, क्योंकि practical exams में laptop use हो सकता है।",
        },
    ],
    "walkthrough": {
        "intro": "Python और IDE install करने के बाद, programmers सब ठीक है या नहीं check करने के लिए एक छोटा program चलाते हैं। यह रहा हमारा।",
        "keyTerms": [
            {"meaning": "Integrated Development Environment: code लिखना, चलाना और ठीक करना, सब एक जगह।"},
            {"meaning": "आपका program चलाता है और output दिखाता है।"},
            {"meaning": "Jupyter में code का एक छोटा block, जो अलग से चलता है।"},
            {"meaning": "जगहों की वह list जहाँ Windows python जैसे programs ढूँढता है।"},
        ],
    },
    "errors": {
        "intro": "Setup की ज़्यादातर problems छोटी होती हैं, और message पहचानते ही आसानी से ठीक हो जाती हैं।",
        "examples": [
            {"title": "Python के अंदर terminal command type कर देना",
             "md": "`python --version` एक **terminal command** है। यह Command Prompt या Terminal में चलती है, लेकिन यहाँ इसे Python के अंदर ही (`>>>` prompt या code cell में) type कर दिया गया। Python `python` को एक अनजान नाम समझता है। Python prompt से बाहर निकलने के लिए `exit()` type कीजिए, फिर command terminal में चलाइए।"},
            {"title": "ऐसी library जो install नहीं है (या spelling गलत है)",
             "md": "Python ने `numpyy` नाम की library ढूँढी और उसे नहीं मिली। यहाँ बस spelling गलत है (सही है `numpy`)। अगर spelling सही है, तो library अभी install नहीं है। Libraries को **pip** से install करना आप Lesson 1.7 में सीखेंगे।",
             "callout": {"title": "Library", "md": "Ready-made code जो Python को नई क्षमताएँ देता है, जैसे numbers के लिए NumPy या graphs के लिए Matplotlib।"}},
        ],
    },
    "mistakes": [
        {"mistake": "Installation के समय **Add python.exe to PATH** पर tick न करना", "fix": "Installer फिर से चलाइए, **Modify** चुनिए (या reinstall कीजिए) और **Add python.exe to PATH** पर tick कीजिए। आप `python` की जगह `py` command भी try कर सकते हैं।"},
        {"mistake": "पुराने Python 2 tutorial से code copy करना", "fix": "Python 3 में `print` को हमेशा brackets चाहिए: `print(\"Hello\")`।"},
        {"mistake": "Notepad से file को `program.py.txt` नाम से save करना", "see": "File Python की तरह चलने के बजाय Notepad में खुलती है", "fix": "**Save as type: All Files** चुनिए और नाम `program.py` रखिए, या सीधे IDE use कीजिए।"},
        {"mistake": "Python के अंदर (`>>>`) `python --version` type करना", "fix": "पहले `exit()` type कीजिए, फिर command को Command Prompt या Terminal में चलाइए।"},
    ],
    "tasks": [
        {"title": "आपका पहला IDE message", "md": "एक program लिखिए जो बिल्कुल यही print करे:", "hints": ["print() use कीजिए और message को quotes के अंदर रखिए।"]},
        {"title": "Setup check report", "md": "एक program लिखिए जो यह report print करे। Test sum (250 + 250) Python से **calculate** करवाइए; 500 खुद type मत कीजिए।",
         "hints": ["हर line के लिए एक print() use कीजिए।", "आखिरी line के लिए try कीजिए: print(\"Test sum:\", 250 + 250)।"]},
        {"title": "पुराने tutorial का code ठीक कीजिए", "md": "यह line एक पुराने Python 2 tutorial से copy की गई है। इसे ठीक कीजिए ताकि यह `Python is ready` print करे।",
         "hints": ["Python 3 में print को brackets चाहिए।"], "solutionNote": "Python 3 में जो print करना है, उसके चारों ओर brackets चाहिए।"},
    ],
    "quiz": [
        {"q": "IDE का full form क्या है?", "why": "IDE यानी Integrated Development Environment: code लिखने, चलाने और ठीक करने की एक जगह।"},
        {"q": "कौन सा tool code को छोटे cells में चलाता है और हर cell के ठीक नीचे output या graph दिखाता है?", "why": "Jupyter Notebook code को cell by cell चलाता है और result ठीक नीचे दिखाता है, जो data और graphs के लिए बढ़िया है।"},
        {"q": "Windows पर Python install करते समय कौन सा option \"'python' is not recognized\" error से बचाता है?", "why": "python.exe को PATH में जोड़ने से Windows किसी भी folder से python command ढूँढ पाता है।"},
        {"q": "इनमें से कौन सा text editor के मुकाबले IDE का फायदा नहीं है?", "options": ["Syntax highlighting", "Auto-completion", "Debugging tools", "Python install किए बिना programs चलाना"], "why": "IDE को भी Python install चाहिए। यह code लिखना, चलाना और ठीक करना आसान बनाता है, लेकिन interpreter की जगह नहीं लेता।"},
        {"q": "Microsoft का बनाया free editor कौन सा है?", "why": "VS Code (Visual Studio Code) Microsoft का free editor है। Python extension के साथ यह पूरा Python IDE बन जाता है।"},
    ],
    "exam": {"note": "University exam English में लिखा जाता है, इसलिए model answers English में ही रखे गए हैं। ये practice के लिए important questions हैं; असली university questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 1.2 · Setup",
        "children": [
            {"label": "Python install", "children": [{"label": "python.org"}, {"label": "Add to PATH पर tick"}, {"label": "Check: python --version"}]},
            {"label": "Text editor बनाम IDE", "children": [{"label": "Editor: सिर्फ plain text"}, {"label": "IDE: सारे tools एक जगह"}]},
            {"label": "Popular IDEs", "children": [{"label": "Jupyter Notebook", "children": [{"label": "Cells + graphs"}, {"label": "Anaconda / Colab"}]}, {"label": "PyCharm", "children": [{"label": "Full-featured, JetBrains"}]}, {"label": "VS Code", "children": [{"label": "Free, Microsoft"}, {"label": "Python extension"}]}]},
            {"label": "IDE के फायदे", "children": [{"label": "Syntax highlighting"}, {"label": "Auto-completion"}, {"label": "Error hints"}, {"label": "एक click में run"}, {"label": "Debugger"}]},
            {"label": "Laptop नहीं?", "children": [{"label": "Champ Lab"}, {"label": "Google Colab"}]},
            {"label": "Setup errors", "children": [{"label": "python not recognized: PATH"}, {"label": "ModuleNotFoundError: library नहीं है"}]},
        ],
    },
    "summary": [
        "**Python install करना** मतलब interpreter को अपने computer पर रखना; Windows पर **Add python.exe to PATH** पर tick कीजिए।",
        "Installation check कीजिए: Command Prompt या Terminal में **`python --version`**।",
        "**IDE** (Integrated Development Environment) में code लिखना, चलाना और ठीक करना, सब एक जगह होता है।",
        "Popular IDEs: **Jupyter Notebook** (cells और graphs), **PyCharm** (full-featured) और **VS Code** (free, Microsoft का)।",
        "IDEs text editors से बेहतर हैं: **syntax highlighting, auto-completion, error hints, एक click में run और debugging**।",
    ],
}

# ===================================================================== Hinglish
T["hinglish"] = {
    "hook": {
        "title": "Apna coding workspace taiyaar kijiye",
        "md": "Is lesson ke end tak aap jaanenge ki laptop par **Python kaise install** karein, **kaunsa IDE chunein** (Jupyter Notebook, PyCharm ya VS Code), aur **IDE, text editor se behtar kyun hai**, jo exam ka ek favourite question hai.\n\nLaptop nahi hai? Koi baat nahi. Is course ki har cheez **Champ Lab** mein aapke phone par bhi chalti hai.",
    },
    "learn": [
        "**Python install** kaise karein aur check kaise karein ki woh kaam kar raha hai",
        "**IDE** kya hai, aur teen popular IDEs: **Jupyter Notebook, PyCharm aur VS Code**",
        "**Text editors ke mukable IDEs ke fayde**",
    ],
    "explanation": [
        {
            "heading": "\"Python install karna\" matlab kya?",
            "md": "Lesson 1.1 mein aapne seekha ki **interpreter** aapka code padhta aur chalata hai. Python install karne ka matlab hai is interpreter ko apne computer par rakhna.\n\n**Steps (Windows):**\n1. **python.org → Downloads** par jaiye aur latest Python 3 installer download kijiye.\n2. Installer kholiye aur pehli screen ke neeche **\"Add python.exe to PATH\" par tick** kijiye. Yeh ek checkbox bahut si pareshani bachata hai.\n3. **Install Now** par click kijiye aur poora hone dijiye.\n4. **Command Prompt** kholiye aur `python --version` type kijiye. Agar `Python 3.12.4` jaisa kuch dikhe, to Python taiyaar hai.\n\nMac par python.org ka installer use kijiye aur Terminal mein `python3 --version` se check kijiye.",
            "callout": {"title": "Tip", "md": "Hamesha **Python 3** install kijiye. Purane tutorials Python 2 use karte hain, jo ab supported nahi hai."},
        },
        {
            "heading": "Text editor vs IDE",
            "md": "Aap Python kisi bhi **text editor** mein likh sakte hain, jaise Notepad. Lekin text editor sirf plain text rakhta hai. Woh na aapka code chala sakta hai, na rang de sakta hai, na galtiyan bata sakta hai.\n\n**IDE** sab kuch ek jagah deta hai: editor, code chalane ka tareeka, error hints aur bugs dhoondhne ke tools.\n\nAise sochiye: **saade kaagaz** par prescription likhna kaam karta hai, lekin **pharmacy software** spelling check karta hai, interactions ki warning deta hai aur label bhi print kar deta hai. Text editor kaagaz hai; IDE software hai.",
            "callout": {"title": "IDE", "md": "**Integrated Development Environment**: ek application jisme code editor, programs chalane ka tareeka, error checking aur debugging tools sab ek saath hote hain."},
        },
        {
            "heading": "Teen popular IDEs",
            "md": "| IDE | Kiske liye best | Jaanne layak baat |\n|---|---|---|\n| **Jupyter Notebook** | Data analysis, graphs, step-by-step experiments | Code chhote **cells** mein chalta hai, aur har cell ka output ya graph theek uske neeche dikhta hai. **Anaconda** ke saath aata hai, aur **Google Colab** mein online free chalta hai. |\n| **PyCharm** | Bade projects | **JetBrains** ka full-featured Python IDE. **Community** edition free hai. |\n| **VS Code** | Har tarah ki coding | **Microsoft** ka free, halka editor. **Python extension** jodte hi yeh powerful Python IDE ban jaata hai. |\n\nIs course ke liye **Jupyter Notebook** (ya Google Colab) sabse useful hai, kyunki pharmacy ka kaam zyaadatar data aur graphs ka hota hai.",
            "callout": {"title": "Anaconda", "md": "Ek free bundle jo Python, Jupyter Notebook aur popular science libraries ek saath install kar deta hai."},
        },
        {
            "heading": "Text editors ke mukable IDEs ke fayde",
            "md": "| Feature | Text editor | IDE |\n|---|---|---|\n| **Syntax highlighting** (rangeen code) | ❌ | ✅ |\n| **Auto-completion** (type karte samay shabd suggest karna) | ❌ | ✅ |\n| Type karte samay **error hints** | ❌ | ✅ |\n| **Ek click mein run** karke output dekhna | ❌ | ✅ |\n| **Debugger** (bugs dhoondhne ke liye line by line chalana) | ❌ | ✅ |\n| **Project aur files sambhalna** | ❌ | ✅ |\n| Libraries aur extensions aasaani se **install karna** | ❌ | ✅ |\n\nSeedhi baat: IDE aapki madad karta hai **tezi se likhne, kam galtiyan karne aur bugs jaldi pakadne** mein.",
        },
        {
            "heading": "Laptop nahi hai? Browser use kijiye",
            "md": "Yeh course seekhne ke liye aapko kuch bhi install karne ki zaroorat nahi:\n\n- **Champ Lab** aapke browser mein Python chalata hai, phone par bhi.\n- **Google Colab** aapke Google account se free online Jupyter Notebook deta hai.\n\nJab ho sake, laptop par Python install kijiye, kyunki practical exams mein laptop use ho sakta hai.",
        },
    ],
    "walkthrough": {
        "intro": "Python aur IDE install karne ke baad, programmers sab theek hai ya nahi check karne ke liye ek chhota program chalate hain. Yeh raha hamara.",
        "keyTerms": [
            {"meaning": "Integrated Development Environment: code likhna, chalana aur theek karna, sab ek jagah."},
            {"meaning": "Aapka program chalata hai aur output dikhata hai."},
            {"meaning": "Jupyter mein code ka ek chhota block, jo alag se chalta hai."},
            {"meaning": "Jagahon ki woh list jahan Windows python jaise programs dhoondhta hai."},
        ],
    },
    "errors": {
        "intro": "Setup ki zyaadatar problems chhoti hoti hain, aur message pehchaante hi aasaani se theek ho jaati hain.",
        "examples": [
            {"title": "Python ke andar terminal command type kar dena",
             "md": "`python --version` ek **terminal command** hai. Yeh Command Prompt ya Terminal mein chalti hai, lekin yahan ise Python ke andar hi (`>>>` prompt ya code cell mein) type kar diya gaya. Python `python` ko ek anjaan naam samajhta hai. Python prompt se bahar nikalne ke liye `exit()` type kijiye, phir command terminal mein chalaiye."},
            {"title": "Aisi library jo install nahi hai (ya spelling galat hai)",
             "md": "Python ne `numpyy` naam ki library dhoondhi aur use nahi mili. Yahan bas spelling galat hai (sahi hai `numpy`). Agar spelling sahi hai, to library abhi install nahi hai. Libraries ko **pip** se install karna aap Lesson 1.7 mein seekhenge.",
             "callout": {"title": "Library", "md": "Ready-made code jo Python ko nayi kshamtayein deta hai, jaise numbers ke liye NumPy ya graphs ke liye Matplotlib."}},
        ],
    },
    "mistakes": [
        {"mistake": "Installation ke samay **Add python.exe to PATH** par tick na karna", "fix": "Installer phir se chalaiye, **Modify** chuniye (ya reinstall kijiye) aur **Add python.exe to PATH** par tick kijiye. Aap `python` ki jagah `py` command bhi try kar sakte hain."},
        {"mistake": "Purane Python 2 tutorial se code copy karna", "fix": "Python 3 mein `print` ko hamesha brackets chahiye: `print(\"Hello\")`."},
        {"mistake": "Notepad se file ko `program.py.txt` naam se save karna", "see": "File Python ki tarah chalne ke bajaay Notepad mein khulti hai", "fix": "**Save as type: All Files** chuniye aur naam `program.py` rakhiye, ya seedhe IDE use kijiye."},
        {"mistake": "Python ke andar (`>>>`) `python --version` type karna", "fix": "Pehle `exit()` type kijiye, phir command ko Command Prompt ya Terminal mein chalaiye."},
    ],
    "tasks": [
        {"title": "Aapka pehla IDE message", "md": "Ek program likhiye jo bilkul yahi print kare:", "hints": ["print() use kijiye aur message ko quotes ke andar rakhiye."]},
        {"title": "Setup check report", "md": "Ek program likhiye jo yeh report print kare. Test sum (250 + 250) Python se **calculate** karwaiye; 500 khud type mat kijiye.",
         "hints": ["Har line ke liye ek print() use kijiye.", "Aakhri line ke liye try kijiye: print(\"Test sum:\", 250 + 250)."]},
        {"title": "Purane tutorial ka code theek kijiye", "md": "Yeh line ek purane Python 2 tutorial se copy ki gayi hai. Ise theek kijiye taaki yeh `Python is ready` print kare.",
         "hints": ["Python 3 mein print ko brackets chahiye."], "solutionNote": "Python 3 mein jo print karna hai, uske chaaron taraf brackets chahiye."},
    ],
    "quiz": [
        {"q": "IDE ka full form kya hai?", "why": "IDE yaani Integrated Development Environment: code likhne, chalane aur theek karne ki ek jagah."},
        {"q": "Kaunsa tool code ko chhote cells mein chalata hai aur har cell ke theek neeche output ya graph dikhata hai?", "why": "Jupyter Notebook code ko cell by cell chalata hai aur result theek neeche dikhata hai, jo data aur graphs ke liye badhiya hai."},
        {"q": "Windows par Python install karte samay kaunsa option \"'python' is not recognized\" error se bachata hai?", "why": "python.exe ko PATH mein jodne se Windows kisi bhi folder se python command dhoondh paata hai."},
        {"q": "Inme se kaunsa text editor ke mukable IDE ka fayda nahi hai?", "options": ["Syntax highlighting", "Auto-completion", "Debugging tools", "Python install kiye bina programs chalana"], "why": "IDE ko bhi Python install chahiye. Yeh code likhna, chalana aur theek karna aasaan banata hai, lekin interpreter ki jagah nahi leta."},
        {"q": "Microsoft ka banaya free editor kaunsa hai?", "why": "VS Code (Visual Studio Code) Microsoft ka free editor hai. Python extension ke saath yeh poora Python IDE ban jaata hai."},
    ],
    "exam": {"note": "University exam English mein likha jaata hai, isliye model answers English mein hi rakhe gaye hain. Yeh practice ke liye important questions hain; asli university questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 1.2 · Setup",
        "children": [
            {"label": "Python install", "children": [{"label": "python.org"}, {"label": "Add to PATH par tick"}, {"label": "Check: python --version"}]},
            {"label": "Text editor vs IDE", "children": [{"label": "Editor: sirf plain text"}, {"label": "IDE: saare tools ek jagah"}]},
            {"label": "Popular IDEs", "children": [{"label": "Jupyter Notebook", "children": [{"label": "Cells + graphs"}, {"label": "Anaconda / Colab"}]}, {"label": "PyCharm", "children": [{"label": "Full-featured, JetBrains"}]}, {"label": "VS Code", "children": [{"label": "Free, Microsoft"}, {"label": "Python extension"}]}]},
            {"label": "IDE ke fayde", "children": [{"label": "Syntax highlighting"}, {"label": "Auto-completion"}, {"label": "Error hints"}, {"label": "Ek click mein run"}, {"label": "Debugger"}]},
            {"label": "Laptop nahi?", "children": [{"label": "Champ Lab"}, {"label": "Google Colab"}]},
            {"label": "Setup errors", "children": [{"label": "python not recognized: PATH"}, {"label": "ModuleNotFoundError: library nahi hai"}]},
        ],
    },
    "summary": [
        "**Python install karna** matlab interpreter ko apne computer par rakhna; Windows par **Add python.exe to PATH** par tick kijiye.",
        "Installation check kijiye: Command Prompt ya Terminal mein **`python --version`**.",
        "**IDE** (Integrated Development Environment) mein code likhna, chalana aur theek karna, sab ek jagah hota hai.",
        "Popular IDEs: **Jupyter Notebook** (cells aur graphs), **PyCharm** (full-featured) aur **VS Code** (free, Microsoft ka).",
        "IDEs text editors se behtar hain: **syntax highlighting, auto-completion, error hints, ek click mein run aur debugging**.",
    ],
}

# ===================================================================== Kannada
T["kn"] = {
    "hook": {
        "title": "ನಿಮ್ಮ coding workspace ಸಿದ್ಧ ಮಾಡಿ",
        "md": "ಈ lesson ಮುಗಿಯುವಷ್ಟರಲ್ಲಿ, laptop ನಲ್ಲಿ **Python ಹೇಗೆ install** ಮಾಡೋದು, **ಯಾವ IDE ಆಯ್ಕೆ ಮಾಡೋದು** (Jupyter Notebook, PyCharm ಅಥವಾ VS Code), ಮತ್ತು **IDE ಯಾಕೆ text editor ಗಿಂತ ಉತ್ತಮ** ಅಂತ ನಿಮಗೆ ಗೊತ್ತಾಗುತ್ತೆ. ಇದು exam ನ favourite question.\n\nLaptop ಇಲ್ವಾ? ತೊಂದರೆ ಇಲ್ಲ. ಈ course ನ ಎಲ್ಲವೂ **Champ Lab** ನಲ್ಲಿ, ನಿಮ್ಮ phone ನಲ್ಲೇ ಕೆಲಸ ಮಾಡುತ್ತೆ.",
    },
    "learn": [
        "**Python install** ಮಾಡೋದು ಮತ್ತು ಅದು ಕೆಲಸ ಮಾಡ್ತಿದೆಯಾ ಅಂತ check ಮಾಡೋದು",
        "**IDE** ಅಂದ್ರೆ ಏನು, ಮತ್ತು ಮೂರು popular IDEs: **Jupyter Notebook, PyCharm ಮತ್ತು VS Code**",
        "**Text editors ಗಿಂತ IDEs ನ ಅನುಕೂಲಗಳು**",
    ],
    "explanation": [
        {
            "heading": "\"Python install ಮಾಡೋದು\" ಅಂದ್ರೆ ಏನು?",
            "md": "Lesson 1.1 ನಲ್ಲಿ, **interpreter** ನಿಮ್ಮ code ಓದಿ run ಮಾಡುತ್ತೆ ಅಂತ ಕಲಿತಿರಿ. Python install ಮಾಡೋದು ಅಂದ್ರೆ ಈ interpreter ಅನ್ನು ನಿಮ್ಮ computer ನಲ್ಲಿ ಇಡೋದು.\n\n**Steps (Windows):**\n1. **python.org → Downloads** ಗೆ ಹೋಗಿ, latest Python 3 installer download ಮಾಡಿ.\n2. Installer open ಮಾಡಿ, ಮೊದಲ screen ನ ಕೆಳಗೆ **\"Add python.exe to PATH\" ಗೆ tick** ಮಾಡಿ. ಈ ಒಂದು checkbox ತುಂಬಾ ತೊಂದರೆ ಉಳಿಸುತ್ತೆ.\n3. **Install Now** click ಮಾಡಿ, ಮುಗಿಯುವವರೆಗೆ ಕಾಯಿರಿ.\n4. **Command Prompt** open ಮಾಡಿ `python --version` ಅಂತ type ಮಾಡಿ. `Python 3.12.4` ತರಹ ಏನಾದರೂ ಕಂಡರೆ, Python ಸಿದ್ಧ.\n\nMac ನಲ್ಲಿ python.org ನ installer use ಮಾಡಿ, Terminal ನಲ್ಲಿ `python3 --version` ಇಂದ check ಮಾಡಿ.",
            "callout": {"title": "Tip", "md": "ಯಾವಾಗಲೂ **Python 3** install ಮಾಡಿ. ಹಳೆಯ tutorials Python 2 use ಮಾಡ್ತವೆ, ಅದು ಈಗ supported ಅಲ್ಲ."},
        },
        {
            "heading": "Text editor vs IDE",
            "md": "Python ಅನ್ನು ಯಾವುದೇ **text editor** ನಲ್ಲಿ ಬರೆಯಬಹುದು, ಉದಾ: Notepad. ಆದರೆ text editor ಕೇವಲ plain text ಇಟ್ಟುಕೊಳ್ಳುತ್ತೆ. ಅದು ನಿಮ್ಮ code run ಮಾಡಲ್ಲ, ಬಣ್ಣ ಕೊಡಲ್ಲ, ತಪ್ಪುಗಳನ್ನೂ ತೋರಿಸಲ್ಲ.\n\n**IDE** ಎಲ್ಲವನ್ನೂ ಒಂದೇ ಕಡೆ ಕೊಡುತ್ತೆ: editor, code run ಮಾಡುವ ದಾರಿ, error hints ಮತ್ತು bugs ಹುಡುಕುವ tools.\n\nಹೀಗೆ ಯೋಚಿಸಿ: **ಸಾದಾ ಕಾಗದದ** ಮೇಲೆ prescription ಬರೆಯೋದು ನಡೆಯುತ್ತೆ, ಆದರೆ **pharmacy software** spelling check ಮಾಡುತ್ತೆ, interactions ಬಗ್ಗೆ warning ಕೊಡುತ್ತೆ ಮತ್ತು label ಕೂಡ print ಮಾಡುತ್ತೆ. Text editor ಕಾಗದ; IDE software.",
            "callout": {"title": "IDE", "md": "**Integrated Development Environment**: code editor, programs run ಮಾಡುವ ದಾರಿ, error checking ಮತ್ತು debugging tools ಎಲ್ಲಾ ಒಟ್ಟಿಗೆ ಇರುವ ಒಂದು application."},
        },
        {
            "heading": "ಮೂರು popular IDEs",
            "md": "| IDE | ಯಾವುದಕ್ಕೆ best | ತಿಳಿದುಕೊಳ್ಳಬೇಕಾದ ವಿಷಯ |\n|---|---|---|\n| **Jupyter Notebook** | Data analysis, graphs, step-by-step experiments | Code ಚಿಕ್ಕ **cells** ನಲ್ಲಿ run ಆಗುತ್ತೆ, ಪ್ರತಿ cell ನ output ಅಥವಾ graph ಅದರ ಕೆಳಗೇ ಕಾಣುತ್ತೆ. **Anaconda** ಜೊತೆ ಬರುತ್ತೆ, ಮತ್ತು **Google Colab** ನಲ್ಲಿ online free ಆಗಿ run ಆಗುತ್ತೆ. |\n| **PyCharm** | ದೊಡ್ಡ projects | **JetBrains** ನ full-featured Python IDE. **Community** edition free. |\n| **VS Code** | ಎಲ್ಲಾ ರೀತಿಯ coding | **Microsoft** ನ free, ಹಗುರ editor. **Python extension** ಸೇರಿಸಿದರೆ ಇದು powerful Python IDE ಆಗುತ್ತೆ. |\n\nಈ course ಗೆ **Jupyter Notebook** (ಅಥವಾ Google Colab) ಅತ್ಯಂತ useful, ಯಾಕಂದ್ರೆ pharmacy ಕೆಲಸ ಹೆಚ್ಚಾಗಿ data ಮತ್ತು graphs ಬಗ್ಗೆ.",
            "callout": {"title": "Anaconda", "md": "Python, Jupyter Notebook ಮತ್ತು popular science libraries ಅನ್ನು ಒಂದೇ ಸಲ install ಮಾಡುವ ಒಂದು free bundle."},
        },
        {
            "heading": "Text editors ಗಿಂತ IDEs ನ ಅನುಕೂಲಗಳು",
            "md": "| Feature | Text editor | IDE |\n|---|---|---|\n| **Syntax highlighting** (ಬಣ್ಣದ code) | ❌ | ✅ |\n| **Auto-completion** (type ಮಾಡುವಾಗ ಪದಗಳ suggestion) | ❌ | ✅ |\n| Type ಮಾಡುವಾಗಲೇ **error hints** | ❌ | ✅ |\n| **ಒಂದು click ನಲ್ಲಿ run** ಮಾಡಿ output ನೋಡೋದು | ❌ | ✅ |\n| **Debugger** (bugs ಹುಡುಕಲು line by line run ಮಾಡೋದು) | ❌ | ✅ |\n| **Project ಮತ್ತು files ನಿರ್ವಹಣೆ** | ❌ | ✅ |\n| Libraries ಮತ್ತು extensions ಸುಲಭವಾಗಿ **install ಮಾಡೋದು** | ❌ | ✅ |\n\nಸರಳವಾಗಿ ಹೇಳಬೇಕಂದ್ರೆ, IDE ನಿಮಗೆ **ವೇಗವಾಗಿ ಬರೆಯಲು, ಕಡಿಮೆ ತಪ್ಪು ಮಾಡಲು ಮತ್ತು bugs ಬೇಗ ಹಿಡಿಯಲು** ಸಹಾಯ ಮಾಡುತ್ತೆ.",
        },
        {
            "heading": "Laptop ಇಲ್ವಾ? Browser use ಮಾಡಿ",
            "md": "ಈ course ಕಲಿಯೋಕೆ ನೀವು ಏನನ್ನೂ install ಮಾಡಬೇಕಿಲ್ಲ:\n\n- **Champ Lab** ನಿಮ್ಮ browser ನಲ್ಲೇ Python run ಮಾಡುತ್ತೆ, phone ನಲ್ಲೂ.\n- **Google Colab** ನಿಮ್ಮ Google account ಇಂದ free online Jupyter Notebook ಕೊಡುತ್ತೆ.\n\nಸಾಧ್ಯವಾದಾಗ laptop ನಲ್ಲಿ Python install ಮಾಡಿ, ಯಾಕಂದ್ರೆ practical exams ನಲ್ಲಿ laptop use ಆಗಬಹುದು.",
        },
    ],
    "walkthrough": {
        "intro": "Python ಮತ್ತು IDE install ಮಾಡಿದ ಮೇಲೆ, ಎಲ್ಲಾ ಸರಿಯಾಗಿದೆಯಾ ಅಂತ check ಮಾಡಲು programmers ಒಂದು ಚಿಕ್ಕ program run ಮಾಡ್ತಾರೆ. ಇಲ್ಲಿದೆ ನಮ್ಮದು.",
        "keyTerms": [
            {"meaning": "Integrated Development Environment: code ಬರೆಯೋದು, run ಮಾಡೋದು, ಸರಿ ಮಾಡೋದು, ಎಲ್ಲಾ ಒಂದೇ ಕಡೆ."},
            {"meaning": "ನಿಮ್ಮ program run ಮಾಡಿ output ತೋರಿಸುತ್ತೆ."},
            {"meaning": "Jupyter ನಲ್ಲಿ ತಾನೇ ಪ್ರತ್ಯೇಕವಾಗಿ run ಆಗುವ code ನ ಚಿಕ್ಕ block."},
            {"meaning": "python ತರಹದ programs ಅನ್ನು Windows ಹುಡುಕುವ ಜಾಗಗಳ list."},
        ],
    },
    "errors": {
        "intro": "Setup ನ ಹೆಚ್ಚಿನ problems ಚಿಕ್ಕವು, message ಗುರುತಿಸಿದ ತಕ್ಷಣ ಸುಲಭವಾಗಿ ಸರಿ ಮಾಡಬಹುದು.",
        "examples": [
            {"title": "Python ಒಳಗೇ terminal command type ಮಾಡೋದು",
             "md": "`python --version` ಒಂದು **terminal command**. ಇದು Command Prompt ಅಥವಾ Terminal ನಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತೆ, ಆದರೆ ಇಲ್ಲಿ ಇದನ್ನು Python ಒಳಗೇ (`>>>` prompt ಅಥವಾ code cell ನಲ್ಲಿ) type ಮಾಡಲಾಗಿದೆ. Python `python` ಅನ್ನು ಗೊತ್ತಿಲ್ಲದ ಹೆಸರು ಅಂತ ತಿಳಿದುಕೊಳ್ಳುತ್ತೆ. Python prompt ಇಂದ ಹೊರಬರಲು `exit()` type ಮಾಡಿ, ಆಮೇಲೆ command ಅನ್ನು terminal ನಲ್ಲಿ run ಮಾಡಿ."},
            {"title": "Install ಆಗಿರದ (ಅಥವಾ spelling ತಪ್ಪಾದ) library",
             "md": "Python `numpyy` ಅನ್ನುವ library ಹುಡುಕಿತು, ಆದರೆ ಸಿಗಲಿಲ್ಲ. ಇಲ್ಲಿ spelling ತಪ್ಪಾಗಿದೆ ಅಷ್ಟೇ (ಸರಿಯಾದದ್ದು `numpy`). Spelling ಸರಿ ಇದ್ದರೆ, library ಇನ್ನೂ install ಆಗಿಲ್ಲ ಅಂತ ಅರ್ಥ. Libraries ಅನ್ನು **pip** ಇಂದ install ಮಾಡೋದು Lesson 1.7 ನಲ್ಲಿ ಕಲಿಯುತ್ತೀರಿ.",
             "callout": {"title": "Library", "md": "Python ಗೆ ಹೊಸ ಸಾಮರ್ಥ್ಯ ಕೊಡುವ ready-made code, ಉದಾ: numbers ಗಾಗಿ NumPy, graphs ಗಾಗಿ Matplotlib."}},
        ],
    },
    "mistakes": [
        {"mistake": "Installation ಸಮಯದಲ್ಲಿ **Add python.exe to PATH** ಗೆ tick ಮಾಡದೇ ಇರೋದು", "fix": "Installer ಮತ್ತೆ run ಮಾಡಿ, **Modify** ಆಯ್ಕೆ ಮಾಡಿ (ಅಥವಾ reinstall ಮಾಡಿ) ಮತ್ತು **Add python.exe to PATH** ಗೆ tick ಮಾಡಿ. `python` ಬದಲು `py` command ಕೂಡ try ಮಾಡಬಹುದು."},
        {"mistake": "ಹಳೆಯ Python 2 tutorial ಇಂದ code copy ಮಾಡೋದು", "fix": "Python 3 ನಲ್ಲಿ `print` ಗೆ ಯಾವಾಗಲೂ brackets ಬೇಕು: `print(\"Hello\")`."},
        {"mistake": "Notepad ಇಂದ file ಅನ್ನು `program.py.txt` ಅಂತ save ಮಾಡೋದು", "see": "File Python ಆಗಿ run ಆಗುವ ಬದಲು Notepad ನಲ್ಲಿ open ಆಗುತ್ತೆ", "fix": "**Save as type: All Files** ಆಯ್ಕೆ ಮಾಡಿ, ಹೆಸರನ್ನು `program.py` ಅಂತ ಇಡಿ, ಅಥವಾ ನೇರವಾಗಿ IDE use ಮಾಡಿ."},
        {"mistake": "Python ಒಳಗೇ (`>>>`) `python --version` type ಮಾಡೋದು", "fix": "ಮೊದಲು `exit()` type ಮಾಡಿ, ಆಮೇಲೆ command ಅನ್ನು Command Prompt ಅಥವಾ Terminal ನಲ್ಲಿ run ಮಾಡಿ."},
    ],
    "tasks": [
        {"title": "ನಿಮ್ಮ ಮೊದಲ IDE message", "md": "ಇದನ್ನೇ ನಿಖರವಾಗಿ print ಮಾಡುವ ಒಂದು program ಬರೆಯಿರಿ:", "hints": ["print() use ಮಾಡಿ, message ಅನ್ನು quotes ಒಳಗೆ ಹಾಕಿ."]},
        {"title": "Setup check report", "md": "ಈ report ಅನ್ನು print ಮಾಡುವ program ಬರೆಯಿರಿ. Test sum (250 + 250) ಅನ್ನು Python ಇಂದಲೇ **calculate** ಮಾಡಿಸಿ; 500 ಅನ್ನು ನೀವೇ type ಮಾಡಬೇಡಿ.",
         "hints": ["ಪ್ರತಿ line ಗೆ ಒಂದು print() use ಮಾಡಿ.", "ಕೊನೆಯ line ಗೆ ಇದನ್ನು try ಮಾಡಿ: print(\"Test sum:\", 250 + 250)."]},
        {"title": "ಹಳೆಯ tutorial ನ code ಸರಿ ಮಾಡಿ", "md": "ಈ line ಅನ್ನು ಹಳೆಯ Python 2 tutorial ಇಂದ copy ಮಾಡಲಾಗಿದೆ. ಅದು `Python is ready` ಅಂತ print ಮಾಡುವ ಹಾಗೆ ಸರಿ ಮಾಡಿ.",
         "hints": ["Python 3 ನಲ್ಲಿ print ಗೆ brackets ಬೇಕು."], "solutionNote": "Python 3 ನಲ್ಲಿ print ಮಾಡುವುದರ ಸುತ್ತ brackets ಬೇಕು."},
    ],
    "quiz": [
        {"q": "IDE ನ full form ಏನು?", "why": "IDE ಅಂದ್ರೆ Integrated Development Environment: code ಬರೆಯಲು, run ಮಾಡಲು ಮತ್ತು ಸರಿ ಮಾಡಲು ಒಂದೇ ಜಾಗ."},
        {"q": "Code ಅನ್ನು ಚಿಕ್ಕ cells ನಲ್ಲಿ run ಮಾಡಿ, ಪ್ರತಿ cell ನ ಕೆಳಗೇ output ಅಥವಾ graph ತೋರಿಸುವ tool ಯಾವುದು?", "why": "Jupyter Notebook code ಅನ್ನು cell by cell run ಮಾಡಿ, result ಅನ್ನು ಕೆಳಗೇ ತೋರಿಸುತ್ತೆ. Data ಮತ್ತು graphs ಗೆ ಇದು ಅದ್ಭುತ."},
        {"q": "Windows ನಲ್ಲಿ Python install ಮಾಡುವಾಗ, ಯಾವ option \"'python' is not recognized\" error ತಪ್ಪಿಸುತ್ತೆ?", "why": "python.exe ಅನ್ನು PATH ಗೆ ಸೇರಿಸಿದರೆ, Windows ಯಾವುದೇ folder ಇಂದ python command ಹುಡುಕಬಹುದು."},
        {"q": "ಇವುಗಳಲ್ಲಿ ಯಾವುದು text editor ಗಿಂತ IDE ನ ಅನುಕೂಲ ಅಲ್ಲ?", "options": ["Syntax highlighting", "Auto-completion", "Debugging tools", "Python install ಮಾಡದೇ programs run ಮಾಡೋದು"], "why": "IDE ಗೂ Python install ಬೇಕು. ಅದು code ಬರೆಯೋದು, run ಮಾಡೋದು ಮತ್ತು ಸರಿ ಮಾಡೋದನ್ನು ಸುಲಭ ಮಾಡುತ್ತೆ, ಆದರೆ interpreter ಬದಲಿ ಆಗಲ್ಲ."},
        {"q": "Microsoft ತಯಾರಿಸಿದ free editor ಯಾವುದು?", "why": "VS Code (Visual Studio Code) Microsoft ನ free editor. Python extension ಜೊತೆ ಇದು ಪೂರ್ಣ Python IDE ಆಗುತ್ತೆ."},
    ],
    "exam": {"note": "University exam ಅನ್ನು English ನಲ್ಲಿ ಬರೆಯುತ್ತೀರಿ, ಹಾಗಾಗಿ model answers English ನಲ್ಲೇ ಇವೆ. ಇವು practice ಗಾಗಿ important questions; ನಿಜವಾದ university questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 1.2 · Setup",
        "children": [
            {"label": "Python install", "children": [{"label": "python.org"}, {"label": "Add to PATH ಗೆ tick"}, {"label": "Check: python --version"}]},
            {"label": "Text editor vs IDE", "children": [{"label": "Editor: plain text ಮಾತ್ರ"}, {"label": "IDE: ಎಲ್ಲಾ tools ಒಂದೇ ಕಡೆ"}]},
            {"label": "Popular IDEs", "children": [{"label": "Jupyter Notebook", "children": [{"label": "Cells + graphs"}, {"label": "Anaconda / Colab"}]}, {"label": "PyCharm", "children": [{"label": "Full-featured, JetBrains"}]}, {"label": "VS Code", "children": [{"label": "Free, Microsoft"}, {"label": "Python extension"}]}]},
            {"label": "IDE ಅನುಕೂಲಗಳು", "children": [{"label": "Syntax highlighting"}, {"label": "Auto-completion"}, {"label": "Error hints"}, {"label": "ಒಂದು click ನಲ್ಲಿ run"}, {"label": "Debugger"}]},
            {"label": "Laptop ಇಲ್ವಾ?", "children": [{"label": "Champ Lab"}, {"label": "Google Colab"}]},
            {"label": "Setup errors", "children": [{"label": "python not recognized: PATH"}, {"label": "ModuleNotFoundError: library ಇಲ್ಲ"}]},
        ],
    },
    "summary": [
        "**Python install ಮಾಡೋದು** ಅಂದ್ರೆ interpreter ಅನ್ನು ನಿಮ್ಮ computer ನಲ್ಲಿ ಇಡೋದು; Windows ನಲ್ಲಿ **Add python.exe to PATH** ಗೆ tick ಮಾಡಿ.",
        "Installation check ಮಾಡಿ: Command Prompt ಅಥವಾ Terminal ನಲ್ಲಿ **`python --version`**.",
        "**IDE** (Integrated Development Environment) ನಲ್ಲಿ code ಬರೆಯೋದು, run ಮಾಡೋದು ಮತ್ತು ಸರಿ ಮಾಡೋದು ಎಲ್ಲಾ ಒಂದೇ ಕಡೆ.",
        "Popular IDEs: **Jupyter Notebook** (cells ಮತ್ತು graphs), **PyCharm** (full-featured) ಮತ್ತು **VS Code** (free, Microsoft ನದು).",
        "IDEs text editors ಗಿಂತ ಉತ್ತಮ: **syntax highlighting, auto-completion, error hints, ಒಂದು click ನಲ್ಲಿ run ಮತ್ತು debugging**.",
    ],
}

# ------------------------------------------------------------ narration captions
NARR = {
    "hi": [
        "आपने Python install कर लिया है और एक IDE खोल लिया है। चलिए, एक quick setup check चलाते हैं।",
        "पहली line एक comment है, हमारे लिए एक note। IDE में comments अलग रंग में दिखते हैं, इसलिए आसानी से पहचान में आते हैं।",
        "यह print बताता है कि Python काम कर रहा है। IDE में आप Run button दबाते हैं, और output आपके code के नीचे एक panel में दिखता है।",
        "यहाँ Python ढाई सौ और ढाई सौ जोड़ता है। अगर पाँच सौ दिखे, तो calculations भी काम कर रही हैं।",
        "आखिरी line बताती है कि हम course के लिए तैयार हैं।",
        "यही code Jupyter Notebook, PyCharm, VS Code या Champ Lab में एक जैसा चलता है। बस buttons अलग दिखते हैं।",
    ],
    "hinglish": [
        "Aapne Python install kar liya hai aur ek IDE khol liya hai. Chaliye, ek quick setup check chalate hain.",
        "Pehli line ek comment hai, hamare liye ek note. IDE mein comments alag rang mein dikhte hain, isliye aasaani se pehchaan mein aate hain.",
        "Yeh print batata hai ki Python kaam kar raha hai. IDE mein aap Run button dabaate hain, aur output aapke code ke neeche ek panel mein dikhta hai.",
        "Yahan Python dhaai sau aur dhaai sau jodta hai. Agar paanch sau dikhe, to calculations bhi kaam kar rahi hain.",
        "Aakhri line batati hai ki hum course ke liye taiyaar hain.",
        "Yahi code Jupyter Notebook, PyCharm, VS Code ya Champ Lab mein ek jaisa chalta hai. Bas buttons alag dikhte hain.",
    ],
    "kn": [
        "ನೀವು Python install ಮಾಡಿ, ಒಂದು IDE open ಮಾಡಿದ್ದೀರಿ. ಬನ್ನಿ, ಒಂದು quick setup check run ಮಾಡೋಣ.",
        "ಮೊದಲ line ಒಂದು comment, ನಮಗಾಗಿ ಒಂದು note. IDE ನಲ್ಲಿ comments ಬೇರೆ ಬಣ್ಣದಲ್ಲಿ ಕಾಣುತ್ತವೆ, ಹಾಗಾಗಿ ಸುಲಭವಾಗಿ ಗುರುತಿಸಬಹುದು.",
        "ಈ print, Python ಕೆಲಸ ಮಾಡ್ತಿದೆ ಅಂತ ಖಚಿತ ಪಡಿಸುತ್ತೆ. IDE ನಲ್ಲಿ Run button ಒತ್ತಿದರೆ, output ನಿಮ್ಮ code ನ ಕೆಳಗಿನ panel ನಲ್ಲಿ ಕಾಣುತ್ತೆ.",
        "ಇಲ್ಲಿ Python ಇನ್ನೂರ ಐವತ್ತು ಮತ್ತು ಇನ್ನೂರ ಐವತ್ತು ಕೂಡಿಸುತ್ತೆ. ಐನೂರು ಕಂಡರೆ, calculations ಕೂಡ ಕೆಲಸ ಮಾಡ್ತಿವೆ.",
        "ಕೊನೆಯ line, ನಾವು course ಗೆ ಸಿದ್ಧ ಅಂತ ಹೇಳುತ್ತೆ.",
        "ಇದೇ code Jupyter Notebook, PyCharm, VS Code ಅಥವಾ Champ Lab ನಲ್ಲಿ ಒಂದೇ ತರಹ run ಆಗುತ್ತೆ. Buttons ಮಾತ್ರ ಬೇರೆ ಕಾಣುತ್ತವೆ.",
    ],
}
ANIM = {
    "hi": [
        "Text editor, जैसे Notepad, बस एक खाली page है। यह आपका code सिर्फ plain text की तरह रखता है।",
        "IDE यानी Integrated Development Environment। यह code लिखने के लिए एक पूरा workspace है।",
        "यह आपके code को रंग देता है, type करते समय शब्द suggest करता है, गलतियों की warning देता है, और bugs ढूँढने में मदद करता है।",
        "और एक click में, यह आपका program चलाकर output वहीं दिखा देता है।",
        "इसीलिए programmers IDEs पसंद करते हैं। ये समय बचाते हैं और गलतियाँ जल्दी पकड़ते हैं।",
    ],
    "hinglish": [
        "Text editor, jaise Notepad, bas ek khaali page hai. Yeh aapka code sirf plain text ki tarah rakhta hai.",
        "IDE yaani Integrated Development Environment. Yeh code likhne ke liye ek poora workspace hai.",
        "Yeh aapke code ko rang deta hai, type karte samay shabd suggest karta hai, galtiyon ki warning deta hai, aur bugs dhoondhne mein madad karta hai.",
        "Aur ek click mein, yeh aapka program chalakar output wahin dikha deta hai.",
        "Isiliye programmers IDEs pasand karte hain. Yeh samay bachate hain aur galtiyan jaldi pakadte hain.",
    ],
    "kn": [
        "Text editor, ಉದಾ: Notepad, ಒಂದು ಖಾಲಿ page ಅಷ್ಟೇ. ಅದು ನಿಮ್ಮ code ಅನ್ನು plain text ಆಗಿ ಮಾತ್ರ ಇಡುತ್ತೆ.",
        "IDE ಅಂದ್ರೆ Integrated Development Environment. ಇದು code ಬರೆಯಲು ಒಂದು ಪೂರ್ಣ workspace.",
        "ಇದು ನಿಮ್ಮ code ಗೆ ಬಣ್ಣ ಕೊಡುತ್ತೆ, type ಮಾಡುವಾಗ ಪದಗಳನ್ನು suggest ಮಾಡುತ್ತೆ, ತಪ್ಪುಗಳ ಬಗ್ಗೆ warning ಕೊಡುತ್ತೆ, ಮತ್ತು bugs ಹುಡುಕಲು ಸಹಾಯ ಮಾಡುತ್ತೆ.",
        "ಮತ್ತು ಒಂದೇ click ನಲ್ಲಿ, ನಿಮ್ಮ program run ಮಾಡಿ output ಅನ್ನು ಅಲ್ಲೇ ತೋರಿಸುತ್ತೆ.",
        "ಅದಕ್ಕೇ programmers IDEs ಇಷ್ಟಪಡ್ತಾರೆ. ಅವು ಸಮಯ ಉಳಿಸುತ್ತವೆ ಮತ್ತು ತಪ್ಪುಗಳನ್ನು ಬೇಗ ಹಿಡಿಯುತ್ತವೆ.",
    ],
}
# Voice scripts: English words written in local script so the voice pronounces them naturally
TTS = {
    "narrator": {
        "hi": [
            "आपने पाइथन इंस्टॉल कर लिया है और एक आई डी ई खोल लिया है। चलिए, एक क्विक सेटअप चेक चलाते हैं।",
            "पहली लाइन एक कमेंट है, हमारे लिए एक नोट। आई डी ई में कमेंट्स अलग रंग में दिखते हैं, इसलिए आसानी से पहचान में आते हैं।",
            "यह प्रिंट बताता है कि पाइथन काम कर रहा है। आई डी ई में आप रन बटन दबाते हैं, और आउटपुट आपके कोड के नीचे एक पैनल में दिखता है।",
            "यहाँ पाइथन ढाई सौ और ढाई सौ जोड़ता है। अगर पाँच सौ दिखे, तो कैलकुलेशन्स भी काम कर रही हैं।",
            "आखिरी लाइन बताती है कि हम कोर्स के लिए तैयार हैं।",
            "यही कोड जुपिटर नोटबुक, पाइचार्म, वी एस कोड या चैम्प लैब में एक जैसा चलता है। बस बटन अलग दिखते हैं।",
        ],
        "kn": [
            "ನೀವು ಪೈಥಾನ್ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ, ಒಂದು ಐ ಡಿ ಇ ಓಪನ್ ಮಾಡಿದ್ದೀರಿ. ಬನ್ನಿ, ಒಂದು ಕ್ವಿಕ್ ಸೆಟಪ್ ಚೆಕ್ ರನ್ ಮಾಡೋಣ.",
            "ಮೊದಲ ಲೈನ್ ಒಂದು ಕಾಮೆಂಟ್, ನಮಗಾಗಿ ಒಂದು ನೋಟ್. ಐ ಡಿ ಇ ನಲ್ಲಿ ಕಾಮೆಂಟ್ಸ್ ಬೇರೆ ಬಣ್ಣದಲ್ಲಿ ಕಾಣುತ್ತವೆ, ಹಾಗಾಗಿ ಸುಲಭವಾಗಿ ಗುರುತಿಸಬಹುದು.",
            "ಈ ಪ್ರಿಂಟ್, ಪೈಥಾನ್ ಕೆಲಸ ಮಾಡ್ತಿದೆ ಅಂತ ಖಚಿತ ಪಡಿಸುತ್ತೆ. ಐ ಡಿ ಇ ನಲ್ಲಿ ರನ್ ಬಟನ್ ಒತ್ತಿದರೆ, ಔಟ್‌ಪುಟ್ ನಿಮ್ಮ ಕೋಡ್ ನ ಕೆಳಗಿನ ಪ್ಯಾನೆಲ್ ನಲ್ಲಿ ಕಾಣುತ್ತೆ.",
            "ಇಲ್ಲಿ ಪೈಥಾನ್ ಇನ್ನೂರ ಐವತ್ತು ಮತ್ತು ಇನ್ನೂರ ಐವತ್ತು ಕೂಡಿಸುತ್ತೆ. ಐನೂರು ಕಂಡರೆ, ಕ್ಯಾಲ್ಕುಲೇಷನ್ಸ್ ಕೂಡ ಕೆಲಸ ಮಾಡ್ತಿವೆ.",
            "ಕೊನೆಯ ಲೈನ್, ನಾವು ಕೋರ್ಸ್ ಗೆ ಸಿದ್ಧ ಅಂತ ಹೇಳುತ್ತೆ.",
            "ಇದೇ ಕೋಡ್ ಜುಪಿಟರ್ ನೋಟ್‌ಬುಕ್, ಪೈಚಾರ್ಮ್, ವಿ ಎಸ್ ಕೋಡ್ ಅಥವಾ ಚ್ಯಾಂಪ್ ಲ್ಯಾಬ್ ನಲ್ಲಿ ಒಂದೇ ತರಹ ರನ್ ಆಗುತ್ತೆ. ಬಟನ್ಸ್ ಮಾತ್ರ ಬೇರೆ ಕಾಣುತ್ತವೆ.",
        ],
    },
    "anim-ide": {
        "hi": [
            "टेक्स्ट एडिटर, जैसे नोटपैड, बस एक खाली पेज है। यह आपका कोड सिर्फ प्लेन टेक्स्ट की तरह रखता है।",
            "आई डी ई यानी इंटीग्रेटेड डेवलपमेंट एनवायरनमेंट। यह कोड लिखने के लिए एक पूरा वर्कस्पेस है।",
            "यह आपके कोड को रंग देता है, टाइप करते समय शब्द सजेस्ट करता है, गलतियों की वॉर्निंग देता है, और बग्स ढूँढने में मदद करता है।",
            "और एक क्लिक में, यह आपका प्रोग्राम चलाकर आउटपुट वहीं दिखा देता है।",
            "इसीलिए प्रोग्रामर्स आई डी ई पसंद करते हैं। ये समय बचाते हैं और गलतियाँ जल्दी पकड़ते हैं।",
        ],
        "kn": [
            "ಟೆಕ್ಸ್ಟ್ ಎಡಿಟರ್, ಉದಾಹರಣೆಗೆ ನೋಟ್‌ಪ್ಯಾಡ್, ಒಂದು ಖಾಲಿ ಪೇಜ್ ಅಷ್ಟೇ. ಅದು ನಿಮ್ಮ ಕೋಡ್ ಅನ್ನು ಪ್ಲೇನ್ ಟೆಕ್ಸ್ಟ್ ಆಗಿ ಮಾತ್ರ ಇಡುತ್ತೆ.",
            "ಐ ಡಿ ಇ ಅಂದ್ರೆ ಇಂಟಿಗ್ರೇಟೆಡ್ ಡೆವಲಪ್‌ಮೆಂಟ್ ಎನ್ವಿರಾನ್‌ಮೆಂಟ್. ಇದು ಕೋಡ್ ಬರೆಯಲು ಒಂದು ಪೂರ್ಣ ವರ್ಕ್‌ಸ್ಪೇಸ್.",
            "ಇದು ನಿಮ್ಮ ಕೋಡ್ ಗೆ ಬಣ್ಣ ಕೊಡುತ್ತೆ, ಟೈಪ್ ಮಾಡುವಾಗ ಪದಗಳನ್ನು ಸಜೆಸ್ಟ್ ಮಾಡುತ್ತೆ, ತಪ್ಪುಗಳ ಬಗ್ಗೆ ವಾರ್ನಿಂಗ್ ಕೊಡುತ್ತೆ, ಮತ್ತು ಬಗ್ಸ್ ಹುಡುಕಲು ಸಹಾಯ ಮಾಡುತ್ತೆ.",
            "ಮತ್ತು ಒಂದೇ ಕ್ಲಿಕ್ ನಲ್ಲಿ, ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಮ್ ರನ್ ಮಾಡಿ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಅಲ್ಲೇ ತೋರಿಸುತ್ತೆ.",
            "ಅದಕ್ಕೇ ಪ್ರೋಗ್ರಾಮರ್ಸ್ ಐ ಡಿ ಇ ಗಳನ್ನು ಇಷ್ಟಪಡ್ತಾರೆ. ಅವು ಸಮಯ ಉಳಿಸುತ್ತವೆ ಮತ್ತು ತಪ್ಪುಗಳನ್ನು ಬೇಗ ಹಿಡಿಯುತ್ತವೆ.",
        ],
    },
}


if __name__ == "__main__":
    en = json.load(open(os.path.join(ROOT, "content", "bp101t", "1-2", "en.json"), encoding="utf-8"))
    for lang, data in T.items():
        doc = dict(data)
        doc["walkthrough"] = dict(doc["walkthrough"], steps=[{"say": s} for s in NARR[lang]])
        doc["animations"] = [{"steps": [{"say": s} for s in ANIM[lang]]}]
        doc["translatedSections"] = SECTIONS
        path = os.path.join(ROOT, "content", "bp101t", "1-2", f"{lang}.json")
        json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("wrote", path)

    narr_en = [s["say"] for s in en["walkthrough"]["steps"]]
    anim_en = [s["say"] for s in en["animations"][0]["steps"]]
    # Spellings that make the English voice pronounce these words correctly
    say = lambda t: t.replace("an IDE", "an I D E").replace("IDEs", "I D Es").replace("VS Code", "V S Code").replace("or Champ Lab", "or our Champ lab")
    narr_en_tts, anim_en_tts = [say(t) for t in narr_en], [say(t) for t in anim_en]
    script = {
        "course": "bp101t", "lesson": "1-2",
        "voices": {"en": "Mary", "hi": "Rani", "kn": "Anu"},
        "tracks": [
            {"id": "narrator", "prefix": "step-", "lang": "en", "tts": narr_en_tts, "display": narr_en},
            {"id": "narrator", "prefix": "step-", "lang": "hi", "tts": TTS["narrator"]["hi"], "display": NARR["hi"], "displayHinglish": NARR["hinglish"]},
            {"id": "narrator", "prefix": "step-", "lang": "kn", "tts": TTS["narrator"]["kn"], "display": NARR["kn"]},
            {"id": "anim-ide", "prefix": "anim-ide-", "lang": "en", "tts": anim_en_tts, "display": anim_en},
            {"id": "anim-ide", "prefix": "anim-ide-", "lang": "hi", "tts": TTS["anim-ide"]["hi"], "display": ANIM["hi"], "displayHinglish": ANIM["hinglish"]},
            {"id": "anim-ide", "prefix": "anim-ide-", "lang": "kn", "tts": TTS["anim-ide"]["kn"], "display": ANIM["kn"]},
        ],
    }
    path = os.path.join(ROOT, "scripts", "bp101t", "1-2.json")
    json.dump(script, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", path)
    # keep the "Words to know" section after regenerating
    import subprocess, sys
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "..", "glossary_bp101t.py")], check=True)

"""Lesson 1.7 translations (Hindi, Hinglish, Kannada) and voice scripts.

Run to write content/bp101t/1-7/{hi,hinglish,kn}.json and scripts/bp101t/1-7.json.
Lists keep the English order because the website merges by position.
Voices are made with Sarvam (tools/sarvam_lessons.py), which reads English words inside
Hindi and Kannada text naturally, so the voice text is the display text with small fixes.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
LESSON = "1-7"
ANIM_ID = "anim-pip"
SECTIONS = ["hook", "learn", "explanation", "walkthrough", "errors", "mistakes", "tasks",
            "quiz", "exam", "mindmap", "summary", "animations"]

C_MOD = "```python\nimport math\nprint(math.sqrt(49))\nprint(math.pi)\n```"
O_MOD = "```\n7.0\n3.141592653589793\n```"
C_CEIL = "```python\nimport math\nprint(45 / 10)\nprint(math.ceil(45 / 10))\n```"
C_I1 = "```python\nimport math\nprint(math.ceil(4.5))\n```"
C_I2 = "```python\nfrom math import sqrt\nprint(sqrt(81))\n```"
C_I3 = "```python\nimport statistics as st\nprint(st.mean([250, 500, 375]))\n```"
C_PIP = "```\npip install numpy\npip uninstall numpy\npip list\npip show numpy\npip install --upgrade numpy\n```"

T = {}

# ======================================================================= Hindi
T["hi"] = {
    "hook": {
        "title": "हर tablet शुरू से मत बनाइए",
        "md": "Pharmacy हर tablet खुद नहीं बनाती जो वह देती है। वह भरोसेमंद companies की ready-made दवाइयाँ use करती है।\n\nPython भी ऐसे ही काम करता है। हर tool खुद लिखने की जगह आप **libraries** use करते हैं: दूसरों का लिखा और test किया हुआ ready-made code। इस lesson के अंत तक आप Python की built-in libraries use करेंगे, और **pip** से नई libraries install करना जानेंगे।",
    },
    "learn": [
        "**Module** और **library** क्या होते हैं",
        "Python के साथ आने वाली **standard library** कैसे use करें, जैसे **math**",
        "Import करने के तीन तरीके: `import math`, `from math import sqrt` और `import numpy as np`",
        "**Third-party** libraries क्या हैं, और **pip** से उन्हें install और uninstall कैसे करें",
    ],
    "explanation": [
        {"heading": "Modules और libraries",
         "md": f"**Module** ready-made code से भरी एक Python file है, जैसे functions और values। **Library** एक तरह के काम के लिए modules का collection है।\n\nइसे use करने के लिए program की शुरुआत में इसे **import** कीजिए:\n\n{C_MOD}\n\nयह print करता है:\n\n{O_MOD}\n\n`import math`, **math** module को ले आता है। फिर उसके tools dot के साथ use होते हैं: `math.sqrt()` square root निकालता है, और `math.pi` pi की value है।",
         "callout": {"title": "Library", "md": "Ready-made, test किया हुआ code, जिसे खुद लिखने की जगह आप अपने program में import करते हैं।"}},
        {"heading": "Standard library: Python के अंदर पहले से",
         "md": f"Python के साथ एक बड़ी **standard library** आती है। कुछ install नहीं करना पड़ता; बस import कीजिए। Pharmacy के काम में ये मिलेंगी:\n\n- **math**: square roots, pi, ऊपर और नीचे rounding\n- **statistics**: data का average और फैलाव\n- **random**: random numbers, जैसे sample चुनने के लिए\n- **datetime**: तारीख और समय, जैसे expiry dates\n\nDispensing में ऊपर की ओर round करना आम है। 45 tablets, हर strip में 10:\n\n{C_CEIL}\n\nयह `4.5` और फिर `5` print करता है। आधी strip नहीं दे सकते, इसलिए `math.ceil()` अगली पूरी संख्या तक **ऊपर** round करता है। `math.floor()` **नीचे** round करता है।"},
        {"heading": "Import करने के तीन तरीके",
         "md": f"**1. पूरा module import कीजिए**, फिर module के नाम के साथ dot use कीजिए:\n\n{C_I1}\n\n**2. सिर्फ़ ज़रूरी tool import कीजिए**, फिर उसे बिना dot के use कीजिए:\n\n{C_I2}\n\n**3. छोटे नाम (एक **alias**) के साथ import कीजिए**, `as` लगाकर:\n\n{C_I3}\n\nये तीनों programs `5`, `9.0` और `375` print करते हैं। बड़ी libraries के standard alias होते हैं जो सब use करते हैं, जैसे `import numpy as np` और `import pandas as pd`।",
         "callout": {"title": "Imports सबसे ऊपर लिखिए", "md": "Import वाली lines program की शुरुआत में लिखिए, ताकि नीचे की हर line उन्हें use कर सके।"}},
        {"heading": "Third-party libraries",
         "md": "**Third-party** libraries Python team के बाहर के लोग लिखते हैं और **PyPI**, यानी Python Package Index पर free में share करते हैं। आपके syllabus में इनमें से तीन हैं:\n\n- **NumPy**: बहुत सारे numbers पर तेज़ calculations (Unit IV)\n- **Pandas**: data की tables, जैसे patient results की spreadsheet (Unit IV)\n- **Matplotlib**: graphs, जैसे drug concentration curve (Unit V)\n\nये Python के साथ नहीं आतीं। इन्हें अपने computer पर एक बार **install** कीजिए, फिर किसी भी library की तरह import कीजिए।\n\n**Champ Lab में:** NumPy, Pandas और Matplotlib पहले से install हैं, इसलिए आप इन्हें सीधे import कर सकते हैं।"},
        {"heading": "pip से install और uninstall करना",
         "md": f"**pip** Python का installer है। यह PyPI से library download करके set up करता है। pip **commands** आप **terminal** (Windows पर Command Prompt) में type करते हैं, Python program के अंदर नहीं:\n\n{C_PIP}\n\n- **`pip install`** library download करके install करता है।\n- **`pip uninstall`** उसे हटाता है (confirm करने के लिए `y` type कीजिए)।\n- **`pip list`** install हुई हर library दिखाता है।\n- **`pip show`** एक library की details दिखाता है, जैसे उसका version।\n- **`pip install --upgrade`** library को नए version पर update करता है।\n\n**Jupyter Notebook** में इसे cell के अंदर percent sign के साथ चलाइए: `%pip install numpy`।",
         "callout": {"title": "pip, Python code नहीं है", "md": ".py file के अंदर या >>> prompt पर pip install numpy type करने से SyntaxError आता है। इसे terminal में type कीजिए।"}},
    ],
    "walkthrough": {
        "intro": "एक patient को 45 tablets चाहिए, और हर strip में 10 हैं। यह program बताता है कि pharmacist कितनी strips दे।",
        "keyTerms": [
            {"meaning": "math module को लाओ; उसके tools math और dot के साथ use करो।"},
            {"meaning": "अगली पूरी संख्या तक ऊपर round करो।"},
            {"meaning": "एक tool लाओ, ताकि module के नाम के बिना use हो।"},
            {"meaning": "Library install करो। Terminal में type होता है, Python में नहीं।"},
        ],
    },
    "errors": {
        "intro": "ये दो errors तब आते हैं जब Python को library नहीं मिलती, या उसके अंदर का tool नहीं मिलता।",
        "examples": [
            {"title": "Library install नहीं है, या नाम की spelling गलत है", "md": "Python ने `numpi` नाम की library ढूँढी और नहीं मिली। Spelling check कीजिए (`numpy`)। Spelling सही है तो library अभी install नहीं है: terminal में `pip install numpy` चलाइए।"},
            {"title": "Module के नाम के बिना tool use करना", "md": "`import math` module को लाता है, इसलिए उसके tools को module का नाम चाहिए: `math.sqrt(16)`। या पहले tool को ही import कीजिए: `from math import sqrt`।"},
        ],
    },
    "mistakes": [
        {"mistake": "Python program के अंदर या `>>>` prompt पर `pip install numpy` type करना", "see": "SyntaxError: invalid syntax", "fix": "इसे terminal में type कीजिए। Jupyter में `%pip install numpy` use कीजिए।"},
        {"mistake": "Import किए बिना module use करना, जैसे बिना import के `math.ceil(4.5)`", "see": "NameError: name 'math' is not defined", "fix": "सबसे ऊपर `import math` जोड़िए।"},
        {"mistake": "Alias से import करके पूरा नाम use करना, जैसे `import numpy as np` फिर `numpy.mean(...)`", "see": "NameError: name 'numpy' is not defined", "fix": "Alias use कीजिए: `np.mean(...)`।"},
        {"mistake": "अपनी file का नाम `math.py` या `numpy.py` रखना", "see": "Import errors, क्योंकि Python library की जगह आपकी file import करता है", "fix": "File का नाम बदलिए, जैसे `strips.py`।"},
    ],
    "tasks": [
        {"title": "Strips ऊपर round कीजिए", "md": "एक patient को **23 tablets** चाहिए, और हर strip में **10** हैं। **math.ceil()** use करके strips की संख्या print कीजिए, बिल्कुल ऐसे:", "hints": ["23 / 10 है 2.3। इसे ऊपर round कीजिए।", "print(\"Strips:\", math.ceil(23 / 10))"]},
        {"title": "सिर्फ़ एक tool import कीजिए", "md": "math module से सिर्फ़ **sqrt** import कीजिए, और 144 का square root print कीजिए, बिल्कुल ऐसे:", "hints": ["Import वाली line from math import ... से शुरू होती है।", "from math import sqrt, फिर print(sqrt(144))"]},
        {"title": "pi use कीजिए", "md": "एक गोल tablet की radius **4 mm** है। उसकी face area है pi × radius × radius। **math.pi** और दो decimal places वाली f-string use करके बिल्कुल यह print कीजिए:", "hints": ["Area है math.pi * radius_mm * radius_mm।", "print(f\"Area: {math.pi * radius_mm * radius_mm:.2f} sq mm\")"]},
        {"title": "Bug ढूँढिए", "md": "यह program 45 tablets के लिए strips की संख्या print करना चाहिए, पर NameError पर रुक जाता है। इसे ठीक कीजिए ताकि output बिल्कुल यह हो:", "hints": ["Program ने math import किया है, ceil नहीं।", "ceil की जगह math.ceil लिखिए।"],
         "solutionNote": "import math module को लाता है, इसलिए उसके tools को module का नाम और dot चाहिए: math.ceil।"},
    ],
    "quiz": [
        {"q": "कौन सा command NumPy install करता है?", "why": "pip install library download करके install करता है। import सिर्फ़ पहले से install library use करता है।"},
        {"q": "इनमें से कौन Python के साथ आती है, बिना कुछ install किए?", "why": "math, standard library का हिस्सा है। बाकी third-party libraries हैं।"},
        {"q": "import math। print(math.ceil(4.1)) क्या दिखाता है?", "why": "ceil अगली पूरी संख्या तक ऊपर round करता है।"},
        {"q": "import numpy as np के बाद NumPy कैसे use करते हैं?", "why": "Alias np, नाम numpy की जगह ले लेता है।"},
        {"q": "कौन सा command library हटाता है?", "why": "pip uninstall library हटाता है।"},
        {"q": "pip install numpy कहाँ type करते हैं?", "why": "pip terminal का command है, Python code नहीं।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 1.7 · Libraries & pip",
        "children": [
            {"label": "Library", "children": [{"label": "Ready-made, test किया code"}, {"label": "Module = एक file"}]},
            {"label": "Standard", "children": [{"label": "math, statistics"}, {"label": "random, datetime"}, {"label": "कुछ install नहीं"}]},
            {"label": "Third-party", "children": [{"label": "NumPy, Pandas, Matplotlib"}, {"label": "PyPI से"}]},
            {"label": "import", "children": [{"label": "import math"}, {"label": "from math import sqrt"}, {"label": "import numpy as np"}]},
            {"label": "pip (terminal)", "children": [{"label": "pip install"}, {"label": "pip uninstall"}, {"label": "pip list / show"}]},
            {"label": "Errors", "children": [{"label": "ModuleNotFoundError"}, {"label": "NameError: sqrt"}]},
        ],
    },
    "summary": [
        "**Library** ready-made, test किया हुआ code है; **module** उसकी एक file है। इसे **import** से लाते हैं।",
        "**Standard library** Python के साथ आती है, जैसे **math**: `math.ceil()` ऊपर round करता है, `math.sqrt()` square root निकालता है।",
        "पूरा module (`import math`), एक tool (`from math import sqrt`) import कीजिए, या छोटा **alias** use कीजिए (`import numpy as np`)।",
        "**NumPy**, **Pandas** और **Matplotlib** जैसी **third-party** libraries **PyPI** से आती हैं और **pip** से install होती हैं।",
        "**pip install**, **pip uninstall**, **pip list** और **pip show** **terminal** में type होते हैं, Python के अंदर नहीं।",
    ],
}

# ==================================================================== Hinglish
T["hinglish"] = {
    "hook": {
        "title": "Har tablet shuru se mat banaiye",
        "md": "Pharmacy har tablet khud nahi banati jo woh deti hai. Woh bharosemand companies ki ready-made dawaiyaan use karti hai.\n\nPython bhi aise hi kaam karta hai. Har tool khud likhne ki jagah aap **libraries** use karte hain: doosron ka likha aur test kiya hua ready-made code. Is lesson ke ant tak aap Python ki built-in libraries use karenge, aur **pip** se nayi libraries install karna jaanenge.",
    },
    "learn": [
        "**Module** aur **library** kya hote hain",
        "Python ke saath aane wali **standard library** kaise use karein, jaise **math**",
        "Import karne ke teen tareeke: `import math`, `from math import sqrt` aur `import numpy as np`",
        "**Third-party** libraries kya hain, aur **pip** se unhe install aur uninstall kaise karein",
    ],
    "explanation": [
        {"heading": "Modules aur libraries",
         "md": f"**Module** ready-made code se bhari ek Python file hai, jaise functions aur values. **Library** ek tarah ke kaam ke liye modules ka collection hai.\n\nIse use karne ke liye program ki shuruaat mein ise **import** kijiye:\n\n{C_MOD}\n\nYeh print karta hai:\n\n{O_MOD}\n\n`import math`, **math** module ko le aata hai. Phir uske tools dot ke saath use hote hain: `math.sqrt()` square root nikaalta hai, aur `math.pi` pi ki value hai.",
         "callout": {"title": "Library", "md": "Ready-made, test kiya hua code, jise khud likhne ki jagah aap apne program mein import karte hain."}},
        {"heading": "Standard library: Python ke andar pehle se",
         "md": f"Python ke saath ek badi **standard library** aati hai. Kuch install nahi karna padta; bas import kijiye. Pharmacy ke kaam mein yeh milengi:\n\n- **math**: square roots, pi, upar aur neeche rounding\n- **statistics**: data ka average aur phailaav\n- **random**: random numbers, jaise sample chunne ke liye\n- **datetime**: taareekh aur samay, jaise expiry dates\n\nDispensing mein upar ki or round karna aam hai. 45 tablets, har strip mein 10:\n\n{C_CEIL}\n\nYeh `4.5` aur phir `5` print karta hai. Aadhi strip nahi de sakte, isliye `math.ceil()` agli poori sankhya tak **upar** round karta hai. `math.floor()` **neeche** round karta hai."},
        {"heading": "Import karne ke teen tareeke",
         "md": f"**1. Poora module import kijiye**, phir module ke naam ke saath dot use kijiye:\n\n{C_I1}\n\n**2. Sirf zaroori tool import kijiye**, phir use bina dot ke use kijiye:\n\n{C_I2}\n\n**3. Chhote naam (ek **alias**) ke saath import kijiye**, `as` lagakar:\n\n{C_I3}\n\nYeh teeno programs `5`, `9.0` aur `375` print karte hain. Badi libraries ke standard alias hote hain jo sab use karte hain, jaise `import numpy as np` aur `import pandas as pd`.",
         "callout": {"title": "Imports sabse upar likhiye", "md": "Import wali lines program ki shuruaat mein likhiye, taaki neeche ki har line unhe use kar sake."}},
        {"heading": "Third-party libraries",
         "md": "**Third-party** libraries Python team ke bahar ke log likhte hain aur **PyPI**, yaani Python Package Index par free mein share karte hain. Aapke syllabus mein inme se teen hain:\n\n- **NumPy**: bahut saare numbers par tez calculations (Unit IV)\n- **Pandas**: data ki tables, jaise patient results ki spreadsheet (Unit IV)\n- **Matplotlib**: graphs, jaise drug concentration curve (Unit V)\n\nYeh Python ke saath nahi aatin. Inhe apne computer par ek baar **install** kijiye, phir kisi bhi library ki tarah import kijiye.\n\n**Champ Lab mein:** NumPy, Pandas aur Matplotlib pehle se install hain, isliye aap inhe seedhe import kar sakte hain."},
        {"heading": "pip se install aur uninstall karna",
         "md": f"**pip** Python ka installer hai. Yeh PyPI se library download karke set up karta hai. pip **commands** aap **terminal** (Windows par Command Prompt) mein type karte hain, Python program ke andar nahi:\n\n{C_PIP}\n\n- **`pip install`** library download karke install karta hai.\n- **`pip uninstall`** use hataata hai (confirm karne ke liye `y` type kijiye).\n- **`pip list`** install hui har library dikhata hai.\n- **`pip show`** ek library ki details dikhata hai, jaise uska version.\n- **`pip install --upgrade`** library ko naye version par update karta hai.\n\n**Jupyter Notebook** mein ise cell ke andar percent sign ke saath chalaiye: `%pip install numpy`.",
         "callout": {"title": "pip, Python code nahi hai", "md": ".py file ke andar ya >>> prompt par pip install numpy type karne se SyntaxError aata hai. Ise terminal mein type kijiye."}},
    ],
    "walkthrough": {
        "intro": "Ek patient ko 45 tablets chahiye, aur har strip mein 10 hain. Yeh program batata hai ki pharmacist kitni strips de.",
        "keyTerms": [
            {"meaning": "math module ko lao; uske tools math aur dot ke saath use karo."},
            {"meaning": "Agli poori sankhya tak upar round karo."},
            {"meaning": "Ek tool lao, taaki module ke naam ke bina use ho."},
            {"meaning": "Library install karo. Terminal mein type hota hai, Python mein nahi."},
        ],
    },
    "errors": {
        "intro": "Yeh do errors tab aate hain jab Python ko library nahi milti, ya uske andar ka tool nahi milta.",
        "examples": [
            {"title": "Library install nahi hai, ya naam ki spelling galat hai", "md": "Python ne `numpi` naam ki library dhoondhi aur nahi mili. Spelling check kijiye (`numpy`). Spelling sahi hai to library abhi install nahi hai: terminal mein `pip install numpy` chalaiye."},
            {"title": "Module ke naam ke bina tool use karna", "md": "`import math` module ko laata hai, isliye uske tools ko module ka naam chahiye: `math.sqrt(16)`. Ya pehle tool ko hi import kijiye: `from math import sqrt`."},
        ],
    },
    "mistakes": [
        {"mistake": "Python program ke andar ya `>>>` prompt par `pip install numpy` type karna", "see": "SyntaxError: invalid syntax", "fix": "Ise terminal mein type kijiye. Jupyter mein `%pip install numpy` use kijiye."},
        {"mistake": "Import kiye bina module use karna, jaise bina import ke `math.ceil(4.5)`", "see": "NameError: name 'math' is not defined", "fix": "Sabse upar `import math` jodiye."},
        {"mistake": "Alias se import karke poora naam use karna, jaise `import numpy as np` phir `numpy.mean(...)`", "see": "NameError: name 'numpy' is not defined", "fix": "Alias use kijiye: `np.mean(...)`."},
        {"mistake": "Apni file ka naam `math.py` ya `numpy.py` rakhna", "see": "Import errors, kyunki Python library ki jagah aapki file import karta hai", "fix": "File ka naam badaliye, jaise `strips.py`."},
    ],
    "tasks": [
        {"title": "Strips upar round kijiye", "md": "Ek patient ko **23 tablets** chahiye, aur har strip mein **10** hain. **math.ceil()** use karke strips ki sankhya print kijiye, bilkul aise:", "hints": ["23 / 10 hai 2.3. Ise upar round kijiye.", "print(\"Strips:\", math.ceil(23 / 10))"]},
        {"title": "Sirf ek tool import kijiye", "md": "math module se sirf **sqrt** import kijiye, aur 144 ka square root print kijiye, bilkul aise:", "hints": ["Import wali line from math import ... se shuru hoti hai.", "from math import sqrt, phir print(sqrt(144))"]},
        {"title": "pi use kijiye", "md": "Ek gol tablet ki radius **4 mm** hai. Uski face area hai pi × radius × radius. **math.pi** aur do decimal places wali f-string use karke bilkul yeh print kijiye:", "hints": ["Area hai math.pi * radius_mm * radius_mm.", "print(f\"Area: {math.pi * radius_mm * radius_mm:.2f} sq mm\")"]},
        {"title": "Bug dhoondhiye", "md": "Yeh program 45 tablets ke liye strips ki sankhya print karna chahiye, par NameError par ruk jaata hai. Ise theek kijiye taaki output bilkul yeh ho:", "hints": ["Program ne math import kiya hai, ceil nahi.", "ceil ki jagah math.ceil likhiye."],
         "solutionNote": "import math module ko laata hai, isliye uske tools ko module ka naam aur dot chahiye: math.ceil."},
    ],
    "quiz": [
        {"q": "Kaun sa command NumPy install karta hai?", "why": "pip install library download karke install karta hai. import sirf pehle se install library use karta hai."},
        {"q": "Inme se kaun Python ke saath aati hai, bina kuch install kiye?", "why": "math, standard library ka hissa hai. Baaki third-party libraries hain."},
        {"q": "import math. print(math.ceil(4.1)) kya dikhata hai?", "why": "ceil agli poori sankhya tak upar round karta hai."},
        {"q": "import numpy as np ke baad NumPy kaise use karte hain?", "why": "Alias np, naam numpy ki jagah le leta hai."},
        {"q": "Kaun sa command library hataata hai?", "why": "pip uninstall library hataata hai."},
        {"q": "pip install numpy kahan type karte hain?", "why": "pip terminal ka command hai, Python code nahi."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 1.7 · Libraries & pip",
        "children": [
            {"label": "Library", "children": [{"label": "Ready-made, test kiya code"}, {"label": "Module = ek file"}]},
            {"label": "Standard", "children": [{"label": "math, statistics"}, {"label": "random, datetime"}, {"label": "Kuch install nahi"}]},
            {"label": "Third-party", "children": [{"label": "NumPy, Pandas, Matplotlib"}, {"label": "PyPI se"}]},
            {"label": "import", "children": [{"label": "import math"}, {"label": "from math import sqrt"}, {"label": "import numpy as np"}]},
            {"label": "pip (terminal)", "children": [{"label": "pip install"}, {"label": "pip uninstall"}, {"label": "pip list / show"}]},
            {"label": "Errors", "children": [{"label": "ModuleNotFoundError"}, {"label": "NameError: sqrt"}]},
        ],
    },
    "summary": [
        "**Library** ready-made, test kiya hua code hai; **module** uski ek file hai. Ise **import** se laate hain.",
        "**Standard library** Python ke saath aati hai, jaise **math**: `math.ceil()` upar round karta hai, `math.sqrt()` square root nikaalta hai.",
        "Poora module (`import math`), ek tool (`from math import sqrt`) import kijiye, ya chhota **alias** use kijiye (`import numpy as np`).",
        "**NumPy**, **Pandas** aur **Matplotlib** jaisi **third-party** libraries **PyPI** se aati hain aur **pip** se install hoti hain.",
        "**pip install**, **pip uninstall**, **pip list** aur **pip show** **terminal** mein type hote hain, Python ke andar nahi.",
    ],
}

# ===================================================================== Kannada
T["kn"] = {
    "hook": {
        "title": "ಪ್ರತಿ tablet ಅನ್ನು ಶುರುವಿನಿಂದ ಮಾಡಬೇಡಿ",
        "md": "Pharmacy ತಾನು ಕೊಡುವ ಪ್ರತಿ tablet ಅನ್ನೂ ತಾನೇ ತಯಾರಿಸಲ್ಲ. ನಂಬಿಕೆಯ companies ಮಾಡಿದ ready-made ಔಷಧಿಗಳನ್ನು ಬಳಸುತ್ತೆ.\n\nPython ಕೂಡ ಹಾಗೇ ಕೆಲಸ ಮಾಡುತ್ತೆ. ಪ್ರತಿ tool ಅನ್ನೂ ನೀವೇ ಬರೆಯುವ ಬದಲು **libraries** ಬಳಸುತ್ತೀರಿ: ಬೇರೆಯವರು ಬರೆದು test ಮಾಡಿದ ready-made code. ಈ lesson ಮುಗಿಯುವಷ್ಟರಲ್ಲಿ, Python ನ built-in libraries ಬಳಸುತ್ತೀರಿ, ಮತ್ತು **pip** ಇಂದ ಹೊಸ libraries install ಮಾಡೋದು ಗೊತ್ತಾಗುತ್ತೆ.",
    },
    "learn": [
        "**Module** ಮತ್ತು **library** ಅಂದ್ರೆ ಏನು",
        "Python ಜೊತೆ ಬರುವ **standard library** ಹೇಗೆ ಬಳಸೋದು, ಉದಾ: **math**",
        "Import ಮಾಡುವ ಮೂರು ವಿಧಾನಗಳು: `import math`, `from math import sqrt` ಮತ್ತು `import numpy as np`",
        "**Third-party** libraries ಅಂದ್ರೆ ಏನು, ಮತ್ತು **pip** ಇಂದ ಅವನ್ನು install, uninstall ಮಾಡೋದು ಹೇಗೆ",
    ],
    "explanation": [
        {"heading": "Modules ಮತ್ತು libraries",
         "md": f"**Module** ಅಂದ್ರೆ ready-made code ತುಂಬಿರುವ ಒಂದು Python file, ಉದಾ: functions ಮತ್ತು values. **Library** ಒಂದು ರೀತಿಯ ಕೆಲಸಕ್ಕೆ ಬೇಕಾದ modules ನ collection.\n\nಇದನ್ನು ಬಳಸಲು program ನ ಶುರುವಿನಲ್ಲಿ **import** ಮಾಡಿ:\n\n{C_MOD}\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n{O_MOD}\n\n`import math`, **math** module ಅನ್ನು ತರುತ್ತೆ. ಆಮೇಲೆ ಅದರ tools ಅನ್ನು dot ಜೊತೆ ಬಳಸುತ್ತೇವೆ: `math.sqrt()` square root ಕೊಡುತ್ತೆ, ಮತ್ತು `math.pi` pi ನ value.",
         "callout": {"title": "Library", "md": "ನೀವೇ ಬರೆಯುವ ಬದಲು ನಿಮ್ಮ program ಗೆ import ಮಾಡಿಕೊಳ್ಳುವ ready-made, test ಆದ code."}},
        {"heading": "Standard library: Python ಒಳಗೇ ಇದೆ",
         "md": f"Python ಜೊತೆ ಒಂದು ದೊಡ್ಡ **standard library** ಬರುತ್ತೆ. ಏನೂ install ಮಾಡಬೇಕಿಲ್ಲ; import ಮಾಡಿದ್ರೆ ಸಾಕು. Pharmacy ಕೆಲಸದಲ್ಲಿ ಇವು ಸಿಗುತ್ತವೆ:\n\n- **math**: square roots, pi, ಮೇಲೆ ಮತ್ತು ಕೆಳಗೆ rounding\n- **statistics**: data ನ average ಮತ್ತು ಹರಡುವಿಕೆ\n- **random**: random numbers, ಉದಾ: sample ಆರಿಸಲು\n- **datetime**: ದಿನಾಂಕ ಮತ್ತು ಸಮಯ, ಉದಾ: expiry dates\n\nDispensing ನಲ್ಲಿ ಮೇಲಕ್ಕೆ round ಮಾಡೋದು ಸಾಮಾನ್ಯ. 45 tablets, ಪ್ರತಿ strip ನಲ್ಲಿ 10:\n\n{C_CEIL}\n\nಇದು `4.5` ಮತ್ತು ನಂತರ `5` print ಮಾಡುತ್ತೆ. ಅರ್ಧ strip ಕೊಡೋಕೆ ಆಗಲ್ಲ, ಅದಕ್ಕೇ `math.ceil()` ಮುಂದಿನ ಪೂರ್ಣ ಸಂಖ್ಯೆಗೆ **ಮೇಲಕ್ಕೆ** round ಮಾಡುತ್ತೆ. `math.floor()` **ಕೆಳಕ್ಕೆ** round ಮಾಡುತ್ತೆ."},
        {"heading": "Import ಮಾಡುವ ಮೂರು ವಿಧಾನಗಳು",
         "md": f"**1. ಪೂರ್ತಿ module import ಮಾಡಿ**, ಆಮೇಲೆ module ಹೆಸರು ಮತ್ತು dot ಬಳಸಿ:\n\n{C_I1}\n\n**2. ಬೇಕಾದ tool ಮಾತ್ರ import ಮಾಡಿ**, ಆಮೇಲೆ dot ಇಲ್ಲದೆ ಬಳಸಿ:\n\n{C_I2}\n\n**3. ಚಿಕ್ಕ ಹೆಸರು (ಒಂದು **alias**) ಜೊತೆ import ಮಾಡಿ**, `as` ಹಾಕಿ:\n\n{C_I3}\n\nಈ ಮೂರು programs `5`, `9.0` ಮತ್ತು `375` print ಮಾಡುತ್ತವೆ. ದೊಡ್ಡ libraries ಗೆ ಎಲ್ಲರೂ ಬಳಸುವ standard aliases ಇವೆ, ಉದಾ: `import numpy as np` ಮತ್ತು `import pandas as pd`.",
         "callout": {"title": "Imports ಮೇಲ್ಗಡೆ ಬರೆಯಿರಿ", "md": "Import lines ಅನ್ನು program ನ ಶುರುವಿನಲ್ಲಿ ಬರೆಯಿರಿ, ಕೆಳಗಿನ ಪ್ರತಿ line ಅವನ್ನು ಬಳಸಲು."}},
        {"heading": "Third-party libraries",
         "md": "**Third-party** libraries ಅನ್ನು Python team ಹೊರಗಿನವರು ಬರೆದು **PyPI**, ಅಂದ್ರೆ Python Package Index ನಲ್ಲಿ free ಆಗಿ share ಮಾಡುತ್ತಾರೆ. ನಿಮ್ಮ syllabus ನಲ್ಲಿ ಇವುಗಳಲ್ಲಿ ಮೂರು ಇವೆ:\n\n- **NumPy**: ತುಂಬಾ numbers ಮೇಲೆ ವೇಗದ calculations (Unit IV)\n- **Pandas**: data tables, ಉದಾ: patient results ನ spreadsheet (Unit IV)\n- **Matplotlib**: graphs, ಉದಾ: drug concentration curve (Unit V)\n\nಇವು Python ಜೊತೆ ಬರಲ್ಲ. ನಿಮ್ಮ computer ನಲ್ಲಿ ಒಮ್ಮೆ **install** ಮಾಡಿ, ಆಮೇಲೆ ಬೇರೆ libraries ತರಹಾನೇ import ಮಾಡಿ.\n\n**Champ Lab ನಲ್ಲಿ:** NumPy, Pandas ಮತ್ತು Matplotlib ಈಗಾಗಲೇ install ಆಗಿವೆ, ಅದಕ್ಕೇ ನೇರವಾಗಿ import ಮಾಡಬಹುದು."},
        {"heading": "pip ಇಂದ install ಮತ್ತು uninstall",
         "md": f"**pip** Python ನ installer. ಇದು PyPI ಇಂದ library download ಮಾಡಿ set up ಮಾಡುತ್ತೆ. pip **commands** ಅನ್ನು **terminal** (Windows ನಲ್ಲಿ Command Prompt) ನಲ್ಲಿ type ಮಾಡುತ್ತೀರಿ, Python program ಒಳಗೆ ಅಲ್ಲ:\n\n{C_PIP}\n\n- **`pip install`** library download ಮಾಡಿ install ಮಾಡುತ್ತೆ.\n- **`pip uninstall`** ಅದನ್ನು ತೆಗೆಯುತ್ತೆ (confirm ಮಾಡಲು `y` type ಮಾಡಿ).\n- **`pip list`** install ಆಗಿರುವ ಎಲ್ಲಾ libraries ತೋರಿಸುತ್ತೆ.\n- **`pip show`** ಒಂದು library ನ details ತೋರಿಸುತ್ತೆ, ಉದಾ: version.\n- **`pip install --upgrade`** library ಅನ್ನು ಹೊಸ version ಗೆ update ಮಾಡುತ್ತೆ.\n\n**Jupyter Notebook** ನಲ್ಲಿ cell ಒಳಗೆ percent sign ಜೊತೆ run ಮಾಡಿ: `%pip install numpy`.",
         "callout": {"title": "pip, Python code ಅಲ್ಲ", "md": ".py file ಒಳಗೆ ಅಥವಾ >>> prompt ನಲ್ಲಿ pip install numpy type ಮಾಡಿದ್ರೆ SyntaxError ಬರುತ್ತೆ. ಇದನ್ನು terminal ನಲ್ಲಿ type ಮಾಡಿ."}},
    ],
    "walkthrough": {
        "intro": "ಒಬ್ಬ patient ಗೆ 45 tablets ಬೇಕು, ಮತ್ತು ಪ್ರತಿ strip ನಲ್ಲಿ 10 ಇವೆ. Pharmacist ಎಷ್ಟು strips ಕೊಡಬೇಕು ಅಂತ ಈ program ಲೆಕ್ಕ ಹಾಕುತ್ತೆ.",
        "keyTerms": [
            {"meaning": "math module ತಾ; ಅದರ tools ಅನ್ನು math ಮತ್ತು dot ಜೊತೆ ಬಳಸು."},
            {"meaning": "ಮುಂದಿನ ಪೂರ್ಣ ಸಂಖ್ಯೆಗೆ ಮೇಲಕ್ಕೆ round ಮಾಡು."},
            {"meaning": "ಒಂದು tool ತಾ, module ಹೆಸರಿಲ್ಲದೆ ಬಳಸಲು."},
            {"meaning": "Library install ಮಾಡು. Terminal ನಲ್ಲಿ type ಮಾಡೋದು, Python ನಲ್ಲಿ ಅಲ್ಲ."},
        ],
    },
    "errors": {
        "intro": "Python ಗೆ library ಸಿಗದಿದ್ದಾಗ, ಅಥವಾ ಅದರ ಒಳಗಿನ tool ಸಿಗದಿದ್ದಾಗ ಈ ಎರಡು errors ಬರುತ್ತವೆ.",
        "examples": [
            {"title": "Library install ಆಗಿಲ್ಲ, ಅಥವಾ ಹೆಸರಿನ spelling ತಪ್ಪು", "md": "Python `numpi` ಅನ್ನೋ library ಹುಡುಕಿತು, ಸಿಗಲಿಲ್ಲ. Spelling check ಮಾಡಿ (`numpy`). Spelling ಸರಿ ಇದ್ರೆ, library ಇನ್ನೂ install ಆಗಿಲ್ಲ: terminal ನಲ್ಲಿ `pip install numpy` run ಮಾಡಿ."},
            {"title": "Module ಹೆಸರಿಲ್ಲದೆ tool ಬಳಸೋದು", "md": "`import math` module ಅನ್ನು ತರುತ್ತೆ, ಅದಕ್ಕೇ ಅದರ tools ಗೆ module ಹೆಸರು ಬೇಕು: `math.sqrt(16)`. ಅಥವಾ ಮೊದಲು tool ಅನ್ನೇ import ಮಾಡಿ: `from math import sqrt`."},
        ],
    },
    "mistakes": [
        {"mistake": "Python program ಒಳಗೆ ಅಥವಾ `>>>` prompt ನಲ್ಲಿ `pip install numpy` type ಮಾಡೋದು", "see": "SyntaxError: invalid syntax", "fix": "ಇದನ್ನು terminal ನಲ್ಲಿ type ಮಾಡಿ. Jupyter ನಲ್ಲಿ `%pip install numpy` ಬಳಸಿ."},
        {"mistake": "Import ಮಾಡದೆ module ಬಳಸೋದು, ಉದಾ: import ಇಲ್ಲದೆ `math.ceil(4.5)`", "see": "NameError: name 'math' is not defined", "fix": "ಮೇಲ್ಗಡೆ `import math` ಸೇರಿಸಿ."},
        {"mistake": "Alias ಜೊತೆ import ಮಾಡಿ ಪೂರ್ತಿ ಹೆಸರು ಬಳಸೋದು, ಉದಾ: `import numpy as np` ಆಮೇಲೆ `numpy.mean(...)`", "see": "NameError: name 'numpy' is not defined", "fix": "Alias ಬಳಸಿ: `np.mean(...)`."},
        {"mistake": "ನಿಮ್ಮ file ಗೆ `math.py` ಅಥವಾ `numpy.py` ಅಂತ ಹೆಸರಿಡೋದು", "see": "Import errors, ಯಾಕಂದ್ರೆ Python library ಬದಲು ನಿಮ್ಮ file ಅನ್ನು import ಮಾಡುತ್ತೆ", "fix": "File ಹೆಸರು ಬದಲಾಯಿಸಿ, ಉದಾ: `strips.py`."},
    ],
    "tasks": [
        {"title": "Strips ಅನ್ನು ಮೇಲಕ್ಕೆ round ಮಾಡಿ", "md": "ಒಬ್ಬ patient ಗೆ **23 tablets** ಬೇಕು, ಮತ್ತು ಪ್ರತಿ strip ನಲ್ಲಿ **10** ಇವೆ. **math.ceil()** ಬಳಸಿ strips ಸಂಖ್ಯೆ print ಮಾಡಿ, ಹೀಗೇ:", "hints": ["23 / 10 ಅಂದ್ರೆ 2.3. ಇದನ್ನು ಮೇಲಕ್ಕೆ round ಮಾಡಿ.", "print(\"Strips:\", math.ceil(23 / 10))"]},
        {"title": "ಒಂದೇ tool import ಮಾಡಿ", "md": "math module ಇಂದ **sqrt** ಮಾತ್ರ import ಮಾಡಿ, ಮತ್ತು 144 ರ square root print ಮಾಡಿ, ಹೀಗೇ:", "hints": ["Import line from math import ... ಇಂದ ಶುರು ಆಗುತ್ತೆ.", "from math import sqrt, ಆಮೇಲೆ print(sqrt(144))"]},
        {"title": "pi ಬಳಸಿ", "md": "ಒಂದು ದುಂಡು tablet ನ radius **4 mm**. ಅದರ face area = pi × radius × radius. **math.pi** ಮತ್ತು ಎರಡು decimal places ಇರುವ f-string ಬಳಸಿ ಹೀಗೇ print ಮಾಡಿ:", "hints": ["Area ಅಂದ್ರೆ math.pi * radius_mm * radius_mm.", "print(f\"Area: {math.pi * radius_mm * radius_mm:.2f} sq mm\")"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "ಈ program 45 tablets ಗೆ strips ಸಂಖ್ಯೆ print ಮಾಡಬೇಕು, ಆದ್ರೆ NameError ನಲ್ಲಿ ನಿಂತುಬಿಡುತ್ತೆ. Output ಹೀಗೇ ಬರುವ ಹಾಗೆ ಸರಿ ಮಾಡಿ:", "hints": ["Program math ಅನ್ನು import ಮಾಡಿದೆ, ceil ಅನ್ನು ಅಲ್ಲ.", "ceil ಬದಲು math.ceil ಬರೆಯಿರಿ."],
         "solutionNote": "import math module ಅನ್ನು ತರುತ್ತೆ, ಅದಕ್ಕೇ ಅದರ tools ಗೆ module ಹೆಸರು ಮತ್ತು dot ಬೇಕು: math.ceil."},
    ],
    "quiz": [
        {"q": "ಯಾವ command NumPy install ಮಾಡುತ್ತೆ?", "why": "pip install library download ಮಾಡಿ install ಮಾಡುತ್ತೆ. import ಈಗಾಗಲೇ install ಆದ library ಅನ್ನು ಮಾತ್ರ ಬಳಸುತ್ತೆ."},
        {"q": "ಇವುಗಳಲ್ಲಿ ಯಾವುದು Python ಜೊತೆಗೇ ಬರುತ್ತೆ, ಏನೂ install ಮಾಡದೆ?", "why": "math standard library ನ ಭಾಗ. ಉಳಿದವು third-party libraries."},
        {"q": "import math. print(math.ceil(4.1)) ಏನು ತೋರಿಸುತ್ತೆ?", "why": "ceil ಮುಂದಿನ ಪೂರ್ಣ ಸಂಖ್ಯೆಗೆ ಮೇಲಕ್ಕೆ round ಮಾಡುತ್ತೆ."},
        {"q": "import numpy as np ನಂತರ NumPy ಹೇಗೆ ಬಳಸೋದು?", "why": "Alias np, numpy ಹೆಸರಿನ ಜಾಗ ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ."},
        {"q": "ಯಾವ command library ತೆಗೆಯುತ್ತೆ?", "why": "pip uninstall library ತೆಗೆಯುತ್ತೆ."},
        {"q": "pip install numpy ಎಲ್ಲಿ type ಮಾಡೋದು?", "why": "pip terminal ನ command, Python code ಅಲ್ಲ."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 1.7 · Libraries & pip",
        "children": [
            {"label": "Library", "children": [{"label": "Ready-made, test ಆದ code"}, {"label": "Module = ಒಂದು file"}]},
            {"label": "Standard", "children": [{"label": "math, statistics"}, {"label": "random, datetime"}, {"label": "Install ಬೇಕಿಲ್ಲ"}]},
            {"label": "Third-party", "children": [{"label": "NumPy, Pandas, Matplotlib"}, {"label": "PyPI ಇಂದ"}]},
            {"label": "import", "children": [{"label": "import math"}, {"label": "from math import sqrt"}, {"label": "import numpy as np"}]},
            {"label": "pip (terminal)", "children": [{"label": "pip install"}, {"label": "pip uninstall"}, {"label": "pip list / show"}]},
            {"label": "Errors", "children": [{"label": "ModuleNotFoundError"}, {"label": "NameError: sqrt"}]},
        ],
    },
    "summary": [
        "**Library** ಅಂದ್ರೆ ready-made, test ಆದ code; **module** ಅದರ ಒಂದು file. ಇದನ್ನು **import** ಇಂದ ತರುತ್ತೇವೆ.",
        "**Standard library** Python ಜೊತೆ ಬರುತ್ತೆ, ಉದಾ: **math**: `math.ceil()` ಮೇಲಕ್ಕೆ round ಮಾಡುತ್ತೆ, `math.sqrt()` square root ಕೊಡುತ್ತೆ.",
        "ಪೂರ್ತಿ module (`import math`), ಒಂದು tool (`from math import sqrt`) import ಮಾಡಿ, ಅಥವಾ ಚಿಕ್ಕ **alias** ಬಳಸಿ (`import numpy as np`).",
        "**NumPy**, **Pandas** ಮತ್ತು **Matplotlib** ತರಹದ **third-party** libraries **PyPI** ಇಂದ ಬರುತ್ತವೆ, **pip** ಇಂದ install ಆಗುತ್ತವೆ.",
        "**pip install**, **pip uninstall**, **pip list** ಮತ್ತು **pip show** ಅನ್ನು **terminal** ನಲ್ಲಿ type ಮಾಡುತ್ತೇವೆ, Python ಒಳಗೆ ಅಲ್ಲ.",
    ],
}

# Walkthrough narration, one line per step (same order as English)
NARR = {
    "hi": [
        "यह program, Python की math library से बताता है कि कितनी strips देनी हैं।",
        "Comment बताता है कि program क्या करता है।",
        "import math, Python का math module ले आता है। यह Python के साथ आता है, इसलिए कुछ install नहीं करना।",
        "Patient को पैंतालीस tablets चाहिए।",
        "हर strip में दस tablets हैं।",
        "पैंतालीस को दस से भाग दें तो चार दशमलव पाँच। पर आधी strip नहीं दे सकते।",
        "math dot ceil अगली पूरी संख्या तक ऊपर round करता है। इसलिए pharmacist पाँच strips देता है।",
        "यह line सिर्फ़ square root वाला tool import करती है, ताकि उसे math और dot लिखे बिना use किया जा सके।",
        "इक्यासी का square root नौ है। Python इसे नौ दशमलव zero दिखाता है।",
    ],
    "hinglish": [
        "Yeh program, Python ki math library se batata hai ki kitni strips deni hain.",
        "Comment batata hai ki program kya karta hai.",
        "import math, Python ka math module le aata hai. Yeh Python ke saath aata hai, isliye kuch install nahi karna.",
        "Patient ko paintaalees tablets chahiye.",
        "Har strip mein das tablets hain.",
        "Paintaalees ko das se bhaag dein to chaar dashamlav paanch. Par aadhi strip nahi de sakte.",
        "math dot ceil agli poori sankhya tak upar round karta hai. Isliye pharmacist paanch strips deta hai.",
        "Yeh line sirf square root wala tool import karti hai, taaki use math aur dot likhe bina use kiya ja sake.",
        "Ikyaasi ka square root nau hai. Python ise nau dashamlav zero dikhata hai.",
    ],
    "kn": [
        "ಈ program Python ನ math library ಬಳಸಿ ಎಷ್ಟು strips ಕೊಡಬೇಕು ಅಂತ ಲೆಕ್ಕ ಹಾಕುತ್ತೆ.",
        "Comment ಈ program ಏನು ಮಾಡುತ್ತೆ ಅಂತ ಹೇಳುತ್ತೆ.",
        "import math, Python ನ math module ಅನ್ನು ತರುತ್ತೆ. ಇದು Python ಜೊತೆಗೇ ಬರುತ್ತೆ, ಅದಕ್ಕೇ ಏನೂ install ಮಾಡಬೇಕಿಲ್ಲ.",
        "Patient ಗೆ ನಲವತ್ತೈದು tablets ಬೇಕು.",
        "ಪ್ರತಿ strip ನಲ್ಲಿ ಹತ್ತು tablets ಇವೆ.",
        "ನಲವತ್ತೈದನ್ನು ಹತ್ತರಿಂದ ಭಾಗಿಸಿದ್ರೆ ನಾಲ್ಕು ಪಾಯಿಂಟ್ ಐದು. ಆದ್ರೆ ಅರ್ಧ strip ಕೊಡೋಕೆ ಆಗಲ್ಲ.",
        "math dot ceil ಮುಂದಿನ ಪೂರ್ಣ ಸಂಖ್ಯೆಗೆ ಮೇಲಕ್ಕೆ round ಮಾಡುತ್ತೆ. ಅದಕ್ಕೇ pharmacist ಐದು strips ಕೊಡುತ್ತಾರೆ.",
        "ಈ line square root tool ಅನ್ನು ಮಾತ್ರ import ಮಾಡುತ್ತೆ, math ಮತ್ತು dot ಬರೆಯದೆ ಬಳಸಲು.",
        "ಎಂಬತ್ತೊಂದರ square root ಒಂಬತ್ತು. Python ಇದನ್ನು ಒಂಬತ್ತು ಪಾಯಿಂಟ್ zero ಅಂತ ತೋರಿಸುತ್ತೆ.",
    ],
}

# Animation narration
ANIM = {
    "hi": [
        "Terminal में student type करता है: pip install numpy।",
        "pip, NumPy को PyPI पर ढूँढता है, जो Python packages की online library है।",
        "यह NumPy download करके computer पर install कर देता है।",
        "अब इस computer का कोई भी program इसे use कर सकता है, import numpy as np से।",
        "और pip uninstall numpy इसे फिर से हटा देता है।",
    ],
    "hinglish": [
        "Terminal mein student type karta hai: pip install numpy.",
        "pip, NumPy ko PyPI par dhoondhta hai, jo Python packages ki online library hai.",
        "Yeh NumPy download karke computer par install kar deta hai.",
        "Ab is computer ka koi bhi program ise use kar sakta hai, import numpy as np se.",
        "Aur pip uninstall numpy ise phir se hata deta hai.",
    ],
    "kn": [
        "Terminal ನಲ್ಲಿ student type ಮಾಡುತ್ತಾರೆ: pip install numpy.",
        "pip, NumPy ಅನ್ನು PyPI ನಲ್ಲಿ ಹುಡುಕುತ್ತೆ, ಇದು Python packages ನ online library.",
        "ಇದು NumPy ಅನ್ನು download ಮಾಡಿ computer ನಲ್ಲಿ install ಮಾಡುತ್ತೆ.",
        "ಈಗ ಈ computer ನ ಯಾವ program ಬೇಕಾದ್ರೂ ಇದನ್ನು ಬಳಸಬಹುದು, import numpy as np ಇಂದ.",
        "ಮತ್ತು pip uninstall numpy ಇದನ್ನು ಮತ್ತೆ ತೆಗೆಯುತ್ತೆ.",
    ],
}


def say_en(text):
    """English voice text: read code names naturally."""
    return text.replace("math dot ceil", "math dot seal")


def say_native(text, lang):
    """Hindi/Kannada voice text: Sarvam reads English words inside native script; only Python needs native spelling."""
    return text.replace("Python", {"hi": "पाइथन", "kn": "ಪೈಥಾನ್"}[lang])


if __name__ == "__main__":
    en = json.load(open(os.path.join(ROOT, "content", "bp101t", LESSON, "en.json"), encoding="utf-8"))
    n_steps, n_anim = len(en["walkthrough"]["steps"]), len(en["animations"][0]["steps"])
    for lang, data in T.items():
        assert len(NARR[lang]) == n_steps and len(ANIM[lang]) == n_anim, lang
        assert len(data["explanation"]) == len(en["explanation"]) and len(data["tasks"]) == len(en["tasks"]), lang
        assert len(data["quiz"]) == len(en["quiz"]) and len(data["mistakes"]) == len(en["mistakes"]), lang
        doc = dict(data)
        doc["walkthrough"] = dict(doc["walkthrough"], steps=[{"say": s} for s in NARR[lang]])
        doc["animations"] = [{"steps": [{"say": s} for s in ANIM[lang]]}]
        doc["translatedSections"] = SECTIONS
        path = os.path.join(ROOT, "content", "bp101t", LESSON, f"{lang}.json")
        json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("wrote", path)

    narr_en = [s["say"] for s in en["walkthrough"]["steps"]]
    anim_en = [s["say"] for s in en["animations"][0]["steps"]]
    tracks = []
    for tid, prefix, en_lines, native in (("narrator", "step-", narr_en, NARR), (ANIM_ID, ANIM_ID + "-", anim_en, ANIM)):
        tracks.append({"id": tid, "prefix": prefix, "lang": "en", "tts": [say_en(t) for t in en_lines], "display": en_lines})
        tracks.append({"id": tid, "prefix": prefix, "lang": "hi", "tts": [say_native(t, "hi") for t in native["hi"]], "display": native["hi"], "displayHinglish": native["hinglish"]})
        tracks.append({"id": tid, "prefix": prefix, "lang": "kn", "tts": [say_native(t, "kn") for t in native["kn"]], "display": native["kn"]})
    script = {"course": "bp101t", "lesson": LESSON, "voices": {"en": "Ritu", "hi": "Ritu", "kn": "Chaitra"}, "tracks": tracks}
    path = os.path.join(ROOT, "scripts", "bp101t", f"{LESSON}.json")
    json.dump(script, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", path)
    # keep the "Words to know" section after regenerating
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "..", "glossary_bp101t.py")], check=True)

"""Lesson 1.5 translations (Hindi, Hinglish, Kannada) and voice scripts.

Run to write content/bp101t/1-5/{hi,hinglish,kn}.json and scripts/bp101t/1-5.json.
Lists keep the English order because the website merges by position.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
SECTIONS = ["hook", "learn", "explanation", "walkthrough", "errors", "mistakes", "tasks",
            "quiz", "exam", "mindmap", "summary", "video", "animations"]

C_ASK = "```python\nname = input(\"Patient name: \")\nprint(\"Hello,\", name)\n```"
O_ASK = "```\nPatient name: Ravi\nHello, Ravi\n```"
C_TEXT = "```python\nweight = input(\"Weight (kg): \")\nprint(weight * 2)\n```"
C_FLOAT = "```python\nweight = float(input(\"Weight (kg): \"))\nprint(weight * 2)\n```"
C_SEP = "```python\nprint(\"12\", \"05\", \"2026\", sep=\"/\")\nprint(\"Dose\", end=\": \")\nprint(\"500 mg\")\n```"
O_SEP = "```\n12/05/2026\nDose: 500 mg\n```"
C_F = "```python\ndrug = \"Amoxicillin\"\ndose_mg = 500\nprint(f\"{drug}: {dose_mg} mg, three times a day\")\nprint(f\"Daily total: {dose_mg * 3} mg\")\n```"
O_F = "```\nAmoxicillin: 500 mg, three times a day\nDaily total: 1500 mg\n```"
C_LONG = "```python\ndose_mg = 16.1 * 15\nprint(dose_mg)\n```"
C_DEC = "```python\nprint(f\"Dose: {dose_mg:.1f} mg\")\n```"

T = {}

# ======================================================================= Hindi
T["hi"] = {
    "hook": {
        "title": "सवाल पूछने वाला dose calculator",
        "md": "अब तक आपके programs हर बार वही numbers use करते थे। असली pharmacy tool को **पूछना** पड़ता है: *Patient का नाम क्या है? वज़न कितना है?*\n\nइस lesson के अंत तक आप एक छोटा dose calculator बनाएँगे, जो ये details पूछता है, dose calculate करता है और एक साफ़ label print करता है।",
    },
    "learn": [
        "**input()** से user से जानकारी कैसे पूछें",
        "input() हमेशा **text** क्यों देता है, और उसे number कैसे बनाएँ",
        "**sep**, **end** और **f-strings** से साफ़ output कैसे print करें",
        "Number को तय **decimal places** के साथ कैसे दिखाएँ",
    ],
    "explanation": [
        {"heading": "input() से सवाल पूछना",
         "md": f"`input()` user से सवाल पूछता है और तब तक **इंतज़ार** करता है जब तक वो answer type करके Enter न दबाए। Brackets के अंदर का text **prompt** है, यानी screen पर दिखने वाला सवाल:\n\n{C_ASK}\n\nअगर user `Ravi` type करे, तो screen पर दिखता है:\n\n{O_ASK}\n\nAnswer, variable `name` में रख लिया जाता है, ताकि program उसे बाद में use कर सके।\n\n**Champ Lab में:** पीछे कोई keyboard इंतज़ार नहीं कर रहा, इसलिए पहले **Input** box में अपने answers type कीजिए, हर line में एक, फिर Run दबाइए।",
         "callout": {"title": "Prompt के आखिर में space रखिए", "md": "input(\"Weight (kg): \") लिखिए, closing quote से पहले space के साथ, ताकि answer सवाल से चिपके नहीं।"}},
        {"heading": "input() हमेशा text देता है",
         "md": f"User जो भी type करे, `input()` उसे **string** के रूप में देता है, चाहे वो number जैसा दिखे:\n\n{C_TEXT}\n\nअगर user `20` type करे, तो यह `2020` print करता है, 40 नहीं। Text `\"20\"` दोहराया गया, जैसा आपने Lesson 1.3 में देखा था।\n\nइसका fix है Lesson 1.4 वाला **type casting**। Answer को तुरंत बदलिए:\n\n{C_FLOAT}\n\nअब `20` type करने पर `40.0` print होता है। पूरी संख्या के लिए `int()` use कीजिए, जैसे tablets की गिनती, और दशमलव वाली संख्या के लिए `float()`, जैसे वज़न।",
         "callout": {"title": "input() से आए numbers को हमेशा बदलिए", "md": "input() से पढ़ा गया वज़न या dose तब तक text है, जब तक आप उसे int() या float() से न बदलें।"}},
        {"heading": "sep और end के साथ print करना",
         "md": f"आप जानते हैं कि `print()` items के बीच space लगाता है। दो settings इसे बदलती हैं:\n\n- **`sep`** तय करता है कि items के **बीच** क्या आए (default में space)।\n- **`end`** तय करता है कि **आखिर** में क्या आए (default में नई line)।\n\n{C_SEP}\n\nयह print करता है:\n\n{O_SEP}\n\nदूसरा `print()` उसी line पर आगे लिखता है, क्योंकि पहला नई line की जगह `\": \"` पर खत्म हुआ।"},
        {"heading": "f-strings: text के अंदर values",
         "md": f"**f-string** वह string है जिसकी opening quote से पहले `f` लिखा हो। Curly brackets `{{ }}` के अंदर लिखी हर चीज़ की जगह उसकी value आ जाती है:\n\n{C_F}\n\nयह print करता है:\n\n{O_F}\n\nन commas, न `str()`, और हर space आप खुद तय करते हैं।",
         "callout": {"title": "f-string", "md": "Quotes से पहले f वाली string, जिसमें {name} की जगह name की value आ जाती है।"}},
        {"heading": "Decimal places तय करना",
         "md": f"Calculations से कभी-कभी लंबे decimals आते हैं। 16.1 kg का बच्चा, 15 mg प्रति kg के हिसाब से:\n\n{C_LONG}\n\n`241.50000000000003` print करता है। Computer decimals को बहुत छोटे rounding फ़र्क के साथ रखता है, इसलिए यह normal है।\n\nCurly brackets के अंदर `:.1f` लगाइए, ताकि **एक** decimal place दिखे:\n\n{C_DEC}\n\nयह `Dose: 241.5 mg` print करता है। दो decimal places के लिए `:.2f` use कीजिए, जैसे `f\"{{100 / 3:.2f}}\"` देता है `33.33`।"},
    ],
    "walkthrough": {
        "intro": "यह program patient का नाम और वज़न पूछता है, और 15 mg प्रति kg के हिसाब से dose print करता है। इस example में pharmacist Ravi और 16.1 type करता है।",
        "keyTerms": [
            {"meaning": "सवाल दिखाओ और user के answer का इंतज़ार करो। Answer text होता है।"},
            {"meaning": "Value पूछो और answer को number बनाओ।"},
            {"meaning": "Variable की value को text के अंदर रखो।"},
            {"meaning": "एक decimal place दिखाओ।"},
        ],
    },
    "errors": {
        "intro": "ये दो errors तब आते हैं जब input() के answer को सही से handle नहीं किया जाता।",
        "examples": [
            {"title": "input() के text से calculate करना",
             "md": "`weight` में text है, और text को दशमलव वाली संख्या से गुणा नहीं किया जा सकता। पहले answer को बदलिए: `weight = float(input(\"Weight (kg): \"))`।"},
            {"title": "User ने number नहीं, कुछ और type किया",
             "md": "User ने `52 kg` type किया। `float()` सिर्फ number बदल सकता है, इसलिए unit की वजह से error आया। Prompt में ही unit पूछिए, जैसे `\"Weight (kg): \"`, ताकि user सिर्फ number type करे।"},
        ],
    },
    "mistakes": [
        {"mistake": "Answer को बदलना भूल जाना, जैसे `weight = input(\"Weight: \")` फिर `weight * 2`", "see": "कोई error नहीं, लेकिन 20 type करने पर 2020 आता है", "fix": "बदलिए: `weight = float(input(\"Weight: \"))`।"},
        {"mistake": "f-string से पहले `f` भूल जाना, जैसे `print(\"Dose: {dose} mg\")`", "see": "कोई error नहीं, लेकिन Dose: {dose} mg print होता है", "fix": "Quote से पहले f लगाइए: `print(f\"Dose: {dose} mg\")`।"},
        {"mistake": "Prompt के आखिर में space न रखना, जैसे `input(\"Weight:\")`", "see": "कोई error नहीं, लेकिन answer सवाल से चिपक जाता है: Weight:52", "fix": "Space लगाइए: `input(\"Weight: \")`।"},
        {"mistake": "Text और number को `+` से जोड़ना, जैसे `print(\"Dose: \" + dose)`", "fix": "f-string use कीजिए: `print(f\"Dose: {dose}\")`।"},
    ],
    "tasks": [
        {"title": "Patient का स्वागत कीजिए", "md": "Program patient का नाम पूछता है। एक line जोड़िए जो उनका स्वागत करे। नाम **Ananya** type होने पर output बिल्कुल यह होना चाहिए:",
         "hints": ["print() \"Hello,\" और variable name को comma से अलग करके दिखा सकता है।", "Try कीजिए: print(\"Hello,\", name) या print(f\"Hello, {name}\")।"]},
        {"title": "Answer को बदलिए", "md": "Program पूछता है कि patient कितनी strips ले रहा है। हर strip में **10 tablets** हैं। Answer को पूरी संख्या में बदलकर कुल tablets print कीजिए। **4** type होने पर output बिल्कुल यह होना चाहिए:",
         "hints": ["strips में text है। int(strips) उसे number बनाता है।", "print(\"Tablets:\", int(strips) * 10)"]},
        {"title": "दो decimal places", "md": "100 ml syrup 3 बच्चों में बराबर बाँटा जाता है। **f-string** और **`:.2f`** से हर बच्चे का volume print कीजिए, बिल्कुल ऐसे:",
         "hints": ["Quote से पहले f लगाइए: f\"Volume: ...\"", "Curly brackets के अंदर लिखिए: volume_ml:.2f"]},
        {"title": "Bug ढूँढिए", "md": "यह program 15 mg प्रति kg के हिसाब से dose print करना चाहिए। **20** type होने पर output बिल्कुल नीचे वाला होना चाहिए, लेकिन dose 20s की लंबी string बनकर आती है। इसे ठीक कीजिए।",
         "hints": ["input() कौन सा data type देता है?", "input(...) को float(...) के अंदर रखिए।"],
         "solutionNote": "input() text देता है, इसलिए \"20\" * 15 text को दोहराता है। float() पहले उसे number 20.0 बनाता है।"},
    ],
    "quiz": [
        {"q": "input() हमेशा कौन सा data type देता है?", "why": "input() हमेशा text (string) देता है, चाहे user number type करे।"},
        {"q": "x = input(\"Number: \") और user 20 type करता है। print(x * 2) क्या दिखाता है?", "why": "x में text \"20\" है, और * text को दोहराता है।"},
        {"q": "print(\"A\", \"B\", sep=\"\") क्या दिखाता है?", "why": "sep=\"\" items के बीच कुछ नहीं रखता।"},
        {"q": "dose = 500। कौन सी line Dose: 500 mg print करती है?", "why": "सिर्फ {dose} वाली f-string ही value को text के अंदर रखती है।"},
        {"q": "print(f\"{2 / 3:.2f}\") क्या दिखाता है?", "why": ":.2f दो decimal places दिखाता है, round करके: 0.67।"},
        {"q": "print(\"Hi\", end=\"!\") क्या दिखाता है?", "why": "end=\"!\" नई line की जगह आखिर में ! print करता है।"},
    ],
    "exam": {"note": "University exam English में लिखा जाता है, इसलिए model answers English में ही रखे गए हैं। ये practice के लिए important questions हैं; असली university questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 1.5 · Input और output",
        "children": [
            {"label": "input()", "children": [{"label": "Prompt दिखाता है"}, {"label": "Enter का इंतज़ार"}, {"label": "हमेशा str देता है"}]},
            {"label": "बदलना", "children": [{"label": "int(input(...))"}, {"label": "float(input(...))"}, {"label": "\"20\" * 2 = 2020"}]},
            {"label": "print()", "children": [{"label": "sep: items के बीच"}, {"label": "end: आखिर में"}]},
            {"label": "f-strings", "children": [{"label": "f\"{name}\""}, {"label": "{x:.1f} एक decimal"}, {"label": "{x:.2f} दो decimals"}]},
            {"label": "Errors", "children": [{"label": "TypeError: text × number"}, {"label": "ValueError: '52 kg'"}]},
        ],
    },
    "summary": [
        "**`input()`** एक **prompt** दिखाता है और user के answer type करके Enter दबाने का इंतज़ार करता है।",
        "Answer हमेशा **string** होता है, इसलिए numbers को **`int()`** या **`float()`** से बदलिए: `float(input(\"Weight (kg): \"))`।",
        "**`sep`** तय करता है कि printed items के बीच क्या आए; **`end`** तय करता है कि line के आखिर में क्या आए।",
        "**f-strings** values को text के अंदर रखती हैं: `f\"Dose: {dose} mg\"`।",
        "**`:.1f`** और **`:.2f`** एक या दो decimal places दिखाते हैं, और 241.50000000000003 जैसे छोटे rounding फ़र्क छिपा देते हैं।",
    ],
}

# ===================================================================== Hinglish
T["hinglish"] = {
    "hook": {
        "title": "Sawaal poochne wala dose calculator",
        "md": "Ab tak aapke programs har baar wahi numbers use karte the. Asli pharmacy tool ko **poochna** padta hai: *Patient ka naam kya hai? Wazan kitna hai?*\n\nIs lesson ke end tak aap ek chhota dose calculator banayenge, jo yeh details poochta hai, dose calculate karta hai aur ek saaf label print karta hai.",
    },
    "learn": [
        "**input()** se user se jaankari kaise poochein",
        "input() hamesha **text** kyon deta hai, aur use number kaise banayein",
        "**sep**, **end** aur **f-strings** se saaf output kaise print karein",
        "Number ko tay **decimal places** ke saath kaise dikhayein",
    ],
    "explanation": [
        {"heading": "input() se sawaal poochna",
         "md": f"`input()` user se sawaal poochta hai aur tab tak **intezaar** karta hai jab tak woh answer type karke Enter na dabaye. Brackets ke andar ka text **prompt** hai, yaani screen par dikhne wala sawaal:\n\n{C_ASK}\n\nAgar user `Ravi` type kare, to screen par dikhta hai:\n\n{O_ASK}\n\nAnswer, variable `name` mein rakh liya jaata hai, taaki program use baad mein use kar sake.\n\n**Champ Lab mein:** peechhe koi keyboard intezaar nahi kar raha, isliye pehle **Input** box mein apne answers type kijiye, har line mein ek, phir Run dabaiye.",
         "callout": {"title": "Prompt ke aakhir mein space rakhiye", "md": "input(\"Weight (kg): \") likhiye, closing quote se pehle space ke saath, taaki answer sawaal se chipke nahi."}},
        {"heading": "input() hamesha text deta hai",
         "md": f"User jo bhi type kare, `input()` use **string** ke roop mein deta hai, chahe woh number jaisa dikhe:\n\n{C_TEXT}\n\nAgar user `20` type kare, to yeh `2020` print karta hai, 40 nahi. Text `\"20\"` dohraya gaya, jaisa aapne Lesson 1.3 mein dekha tha.\n\nIska fix hai Lesson 1.4 wala **type casting**. Answer ko turant badliye:\n\n{C_FLOAT}\n\nAb `20` type karne par `40.0` print hota hai. Poori sankhya ke liye `int()` use kijiye, jaise tablets ki ginti, aur dashamlav wali sankhya ke liye `float()`, jaise wazan.",
         "callout": {"title": "input() se aaye numbers ko hamesha badliye", "md": "input() se padha gaya wazan ya dose tab tak text hai, jab tak aap use int() ya float() se na badlein."}},
        {"heading": "sep aur end ke saath print karna",
         "md": f"Aap jaante hain ki `print()` items ke beech space lagata hai. Do settings ise badalti hain:\n\n- **`sep`** tay karta hai ki items ke **beech** kya aaye (default mein space).\n- **`end`** tay karta hai ki **aakhir** mein kya aaye (default mein nayi line).\n\n{C_SEP}\n\nYeh print karta hai:\n\n{O_SEP}\n\nDoosra `print()` usi line par aage likhta hai, kyunki pehla nayi line ki jagah `\": \"` par khatam hua."},
        {"heading": "f-strings: text ke andar values",
         "md": f"**f-string** woh string hai jiski opening quote se pehle `f` likha ho. Curly brackets `{{ }}` ke andar likhi har cheez ki jagah uski value aa jaati hai:\n\n{C_F}\n\nYeh print karta hai:\n\n{O_F}\n\nNa commas, na `str()`, aur har space aap khud tay karte hain.",
         "callout": {"title": "f-string", "md": "Quotes se pehle f wali string, jisme {name} ki jagah name ki value aa jaati hai."}},
        {"heading": "Decimal places tay karna",
         "md": f"Calculations se kabhi-kabhi lambe decimals aate hain. 16.1 kg ka bachcha, 15 mg per kg ke hisaab se:\n\n{C_LONG}\n\n`241.50000000000003` print karta hai. Computer decimals ko bahut chhote rounding farak ke saath rakhta hai, isliye yeh normal hai.\n\nCurly brackets ke andar `:.1f` lagaiye, taaki **ek** decimal place dikhe:\n\n{C_DEC}\n\nYeh `Dose: 241.5 mg` print karta hai. Do decimal places ke liye `:.2f` use kijiye, jaise `f\"{{100 / 3:.2f}}\"` deta hai `33.33`."},
    ],
    "walkthrough": {
        "intro": "Yeh program patient ka naam aur wazan poochta hai, aur 15 mg per kg ke hisaab se dose print karta hai. Is example mein pharmacist Ravi aur 16.1 type karta hai.",
        "keyTerms": [
            {"meaning": "Sawaal dikhao aur user ke answer ka intezaar karo. Answer text hota hai."},
            {"meaning": "Value poochho aur answer ko number banao."},
            {"meaning": "Variable ki value ko text ke andar rakho."},
            {"meaning": "Ek decimal place dikhao."},
        ],
    },
    "errors": {
        "intro": "Yeh do errors tab aate hain jab input() ke answer ko sahi se handle nahi kiya jaata.",
        "examples": [
            {"title": "input() ke text se calculate karna",
             "md": "`weight` mein text hai, aur text ko dashamlav wali sankhya se guna nahi kiya ja sakta. Pehle answer ko badliye: `weight = float(input(\"Weight (kg): \"))`."},
            {"title": "User ne number nahi, kuch aur type kiya",
             "md": "User ne `52 kg` type kiya. `float()` sirf number badal sakta hai, isliye unit ki wajah se error aaya. Prompt mein hi unit poochhiye, jaise `\"Weight (kg): \"`, taaki user sirf number type kare."},
        ],
    },
    "mistakes": [
        {"mistake": "Answer ko badalna bhool jaana, jaise `weight = input(\"Weight: \")` phir `weight * 2`", "see": "Koi error nahi, lekin 20 type karne par 2020 aata hai", "fix": "Badliye: `weight = float(input(\"Weight: \"))`."},
        {"mistake": "f-string se pehle `f` bhool jaana, jaise `print(\"Dose: {dose} mg\")`", "see": "Koi error nahi, lekin Dose: {dose} mg print hota hai", "fix": "Quote se pehle f lagaiye: `print(f\"Dose: {dose} mg\")`."},
        {"mistake": "Prompt ke aakhir mein space na rakhna, jaise `input(\"Weight:\")`", "see": "Koi error nahi, lekin answer sawaal se chipak jaata hai: Weight:52", "fix": "Space lagaiye: `input(\"Weight: \")`."},
        {"mistake": "Text aur number ko `+` se jodna, jaise `print(\"Dose: \" + dose)`", "fix": "f-string use kijiye: `print(f\"Dose: {dose}\")`."},
    ],
    "tasks": [
        {"title": "Patient ka swagat kijiye", "md": "Program patient ka naam poochta hai. Ek line jodiye jo unka swagat kare. Naam **Ananya** type hone par output bilkul yeh hona chahiye:",
         "hints": ["print() \"Hello,\" aur variable name ko comma se alag karke dikha sakta hai.", "Try kijiye: print(\"Hello,\", name) ya print(f\"Hello, {name}\")."]},
        {"title": "Answer ko badliye", "md": "Program poochta hai ki patient kitni strips le raha hai. Har strip mein **10 tablets** hain. Answer ko poori sankhya mein badalkar kul tablets print kijiye. **4** type hone par output bilkul yeh hona chahiye:",
         "hints": ["strips mein text hai. int(strips) use number banata hai.", "print(\"Tablets:\", int(strips) * 10)"]},
        {"title": "Do decimal places", "md": "100 ml syrup 3 bachchon mein barabar baanta jaata hai. **f-string** aur **`:.2f`** se har bachche ka volume print kijiye, bilkul aise:",
         "hints": ["Quote se pehle f lagaiye: f\"Volume: ...\"", "Curly brackets ke andar likhiye: volume_ml:.2f"]},
        {"title": "Bug dhoondhiye", "md": "Yeh program 15 mg per kg ke hisaab se dose print karna chahiye. **20** type hone par output bilkul neeche wala hona chahiye, lekin dose 20s ki lambi string bankar aati hai. Ise theek kijiye.",
         "hints": ["input() kaun sa data type deta hai?", "input(...) ko float(...) ke andar rakhiye."],
         "solutionNote": "input() text deta hai, isliye \"20\" * 15 text ko dohraata hai. float() pehle use number 20.0 banata hai."},
    ],
    "quiz": [
        {"q": "input() hamesha kaun sa data type deta hai?", "why": "input() hamesha text (string) deta hai, chahe user number type kare."},
        {"q": "x = input(\"Number: \") aur user 20 type karta hai. print(x * 2) kya dikhata hai?", "why": "x mein text \"20\" hai, aur * text ko dohraata hai."},
        {"q": "print(\"A\", \"B\", sep=\"\") kya dikhata hai?", "why": "sep=\"\" items ke beech kuch nahi rakhta."},
        {"q": "dose = 500. Kaun si line Dose: 500 mg print karti hai?", "why": "Sirf {dose} wali f-string hi value ko text ke andar rakhti hai."},
        {"q": "print(f\"{2 / 3:.2f}\") kya dikhata hai?", "why": ":.2f do decimal places dikhata hai, round karke: 0.67."},
        {"q": "print(\"Hi\", end=\"!\") kya dikhata hai?", "why": "end=\"!\" nayi line ki jagah aakhir mein ! print karta hai."},
    ],
    "exam": {"note": "University exam English mein likha jaata hai, isliye model answers English mein hi rakhe gaye hain. Yeh practice ke liye important questions hain; asli university questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 1.5 · Input aur output",
        "children": [
            {"label": "input()", "children": [{"label": "Prompt dikhata hai"}, {"label": "Enter ka intezaar"}, {"label": "Hamesha str deta hai"}]},
            {"label": "Badalna", "children": [{"label": "int(input(...))"}, {"label": "float(input(...))"}, {"label": "\"20\" * 2 = 2020"}]},
            {"label": "print()", "children": [{"label": "sep: items ke beech"}, {"label": "end: aakhir mein"}]},
            {"label": "f-strings", "children": [{"label": "f\"{name}\""}, {"label": "{x:.1f} ek decimal"}, {"label": "{x:.2f} do decimals"}]},
            {"label": "Errors", "children": [{"label": "TypeError: text × number"}, {"label": "ValueError: '52 kg'"}]},
        ],
    },
    "summary": [
        "**`input()`** ek **prompt** dikhata hai aur user ke answer type karke Enter dabane ka intezaar karta hai.",
        "Answer hamesha **string** hota hai, isliye numbers ko **`int()`** ya **`float()`** se badliye: `float(input(\"Weight (kg): \"))`.",
        "**`sep`** tay karta hai ki printed items ke beech kya aaye; **`end`** tay karta hai ki line ke aakhir mein kya aaye.",
        "**f-strings** values ko text ke andar rakhti hain: `f\"Dose: {dose} mg\"`.",
        "**`:.1f`** aur **`:.2f`** ek ya do decimal places dikhate hain, aur 241.50000000000003 jaise chhote rounding farak chhipa dete hain.",
    ],
}

# ===================================================================== Kannada
T["kn"] = {
    "hook": {
        "title": "ಪ್ರಶ್ನೆ ಕೇಳುವ dose calculator",
        "md": "ಇಲ್ಲಿಯವರೆಗೆ ನಿಮ್ಮ programs ಪ್ರತಿ ಸಲ ಅದೇ numbers use ಮಾಡುತ್ತಿದ್ದವು. ನಿಜವಾದ pharmacy tool **ಕೇಳಬೇಕು**: *Patient ನ ಹೆಸರೇನು? ತೂಕ ಎಷ್ಟು?*\n\nಈ lesson ಮುಗಿಯುವಷ್ಟರಲ್ಲಿ ಈ details ಕೇಳಿ, dose ಲೆಕ್ಕ ಹಾಕಿ, ಒಂದು ಚೆನ್ನಾಗಿರುವ label print ಮಾಡುವ ಚಿಕ್ಕ dose calculator ಅನ್ನು ನೀವು ಮಾಡುತ್ತೀರಿ.",
    },
    "learn": [
        "**input()** ಇಂದ user ಹತ್ತಿರ ಮಾಹಿತಿ ಕೇಳೋದು ಹೇಗೆ",
        "input() ಯಾವಾಗಲೂ **text** ಯಾಕೆ ಕೊಡುತ್ತೆ, ಅದನ್ನು number ಮಾಡೋದು ಹೇಗೆ",
        "**sep**, **end** ಮತ್ತು **f-strings** ಇಂದ ಚೆನ್ನಾಗಿ print ಮಾಡೋದು ಹೇಗೆ",
        "Number ಅನ್ನು ನಿಗದಿತ **decimal places** ಜೊತೆ ತೋರಿಸೋದು ಹೇಗೆ",
    ],
    "explanation": [
        {"heading": "input() ಇಂದ ಪ್ರಶ್ನೆ ಕೇಳೋದು",
         "md": f"`input()` user ಗೆ ಪ್ರಶ್ನೆ ಕೇಳಿ, ಅವರು answer type ಮಾಡಿ Enter ಒತ್ತುವವರೆಗೆ **ಕಾಯುತ್ತೆ**. Brackets ಒಳಗಿನ text **prompt**, ಅಂದ್ರೆ screen ಮೇಲೆ ಕಾಣುವ ಪ್ರಶ್ನೆ:\n\n{C_ASK}\n\nUser `Ravi` ಅಂತ type ಮಾಡಿದರೆ, screen ಮೇಲೆ ಕಾಣೋದು:\n\n{O_ASK}\n\nAnswer ಅನ್ನು variable `name` ನಲ್ಲಿ ಇಡಲಾಗುತ್ತೆ, ಆಮೇಲೆ program ಅದನ್ನು use ಮಾಡಬಹುದು.\n\n**Champ Lab ನಲ್ಲಿ:** ಹಿಂದೆ ಯಾವ keyboard ಕೂಡ ಕಾಯುತ್ತಿಲ್ಲ, ಹಾಗಾಗಿ ಮೊದಲು **Input** box ನಲ್ಲಿ ನಿಮ್ಮ answers type ಮಾಡಿ, ಪ್ರತಿ line ಗೆ ಒಂದು, ನಂತರ Run ಒತ್ತಿ.",
         "callout": {"title": "Prompt ಕೊನೆಯಲ್ಲಿ space ಇಡಿ", "md": "input(\"Weight (kg): \") ಅಂತ, closing quote ಮುಂಚೆ space ಜೊತೆ ಬರೆಯಿರಿ, ಆಗ answer ಪ್ರಶ್ನೆಗೆ ಅಂಟಿಕೊಳ್ಳಲ್ಲ."}},
        {"heading": "input() ಯಾವಾಗಲೂ text ಕೊಡುತ್ತೆ",
         "md": f"User ಏನೇ type ಮಾಡಿದರೂ, `input()` ಅದನ್ನು **string** ಆಗಿ ಕೊಡುತ್ತೆ, number ತರಹ ಕಂಡರೂ ಕೂಡ:\n\n{C_TEXT}\n\nUser `20` type ಮಾಡಿದರೆ, ಇದು `2020` print ಮಾಡುತ್ತೆ, 40 ಅಲ್ಲ. Lesson 1.3 ನಲ್ಲಿ ನೋಡಿದ ಹಾಗೆ, text `\"20\"` ಪುನರಾವರ್ತನೆ ಆಯ್ತು.\n\nಇದಕ್ಕೆ fix Lesson 1.4 ನ **type casting**. Answer ಅನ್ನು ತಕ್ಷಣ ಬದಲಾಯಿಸಿ:\n\n{C_FLOAT}\n\nಈಗ `20` type ಮಾಡಿದರೆ `40.0` print ಆಗುತ್ತೆ. Tablets ಸಂಖ್ಯೆ ತರಹದ ಪೂರ್ಣ ಸಂಖ್ಯೆಗೆ `int()`, ತೂಕದ ತರಹ ದಶಮಾಂಶ ಇರಬಹುದಾದ ಸಂಖ್ಯೆಗೆ `float()` use ಮಾಡಿ.",
         "callout": {"title": "input() ಇಂದ ಬಂದ numbers ಅನ್ನು ಯಾವಾಗಲೂ ಬದಲಾಯಿಸಿ", "md": "input() ಇಂದ ಓದಿದ ತೂಕ ಅಥವಾ dose, int() ಅಥವಾ float() ಇಂದ ಬದಲಾಯಿಸುವವರೆಗೆ text."}},
        {"heading": "sep ಮತ್ತು end ಜೊತೆ print ಮಾಡೋದು",
         "md": f"`print()` items ನಡುವೆ space ಹಾಕುತ್ತೆ ಅಂತ ನಿಮಗೆ ಗೊತ್ತು. ಎರಡು settings ಇದನ್ನು ಬದಲಾಯಿಸುತ್ತವೆ:\n\n- **`sep`** items **ನಡುವೆ** ಏನು ಬರಬೇಕು ಅಂತ ಹೇಳುತ್ತೆ (default space).\n- **`end`** **ಕೊನೆಯಲ್ಲಿ** ಏನು ಬರಬೇಕು ಅಂತ ಹೇಳುತ್ತೆ (default ಹೊಸ line).\n\n{C_SEP}\n\nಇದು print ಮಾಡೋದು:\n\n{O_SEP}\n\nಮೊದಲನೆಯದು ಹೊಸ line ಬದಲು `\": \"` ಇಂದ ಮುಗಿದಿದ್ದರಿಂದ, ಎರಡನೇ `print()` ಅದೇ line ನಲ್ಲಿ ಮುಂದುವರಿಯುತ್ತೆ."},
        {"heading": "f-strings: text ಒಳಗೆ values",
         "md": f"**f-string** ಅಂದ್ರೆ opening quote ಮುಂದೆ `f` ಇರುವ string. Curly brackets `{{ }}` ಒಳಗೆ ಬರೆದ ಪ್ರತಿಯೊಂದರ ಜಾಗಕ್ಕೆ ಅದರ value ಬರುತ್ತೆ:\n\n{C_F}\n\nಇದು print ಮಾಡೋದು:\n\n{O_F}\n\nCommas ಬೇಡ, `str()` ಬೇಡ, ಪ್ರತಿ space ಅನ್ನು ನೀವೇ ನಿರ್ಧರಿಸುತ್ತೀರಿ.",
         "callout": {"title": "f-string", "md": "Quotes ಮುಂದೆ f ಇರುವ string, ಅದರಲ್ಲಿ {name} ಜಾಗಕ್ಕೆ name ನ value ಬರುತ್ತೆ."}},
        {"heading": "Decimal places ನಿಗದಿ ಮಾಡೋದು",
         "md": f"ಲೆಕ್ಕಗಳಿಂದ ಕೆಲವೊಮ್ಮೆ ಉದ್ದದ decimals ಬರುತ್ತವೆ. 16.1 kg ತೂಕದ ಮಗು, kg ಗೆ 15 mg ಪ್ರಕಾರ:\n\n{C_LONG}\n\n`241.50000000000003` print ಮಾಡುತ್ತೆ. Computer decimals ಅನ್ನು ತುಂಬಾ ಚಿಕ್ಕ rounding ವ್ಯತ್ಯಾಸದೊಂದಿಗೆ ಇಡುತ್ತೆ, ಹಾಗಾಗಿ ಇದು normal.\n\n**ಒಂದು** decimal place ತೋರಿಸಲು curly brackets ಒಳಗೆ `:.1f` ಹಾಕಿ:\n\n{C_DEC}\n\nಇದು `Dose: 241.5 mg` print ಮಾಡುತ್ತೆ. ಎರಡು decimal places ಗೆ `:.2f` use ಮಾಡಿ, ಉದಾ: `f\"{{100 / 3:.2f}}\"` ಕೊಡೋದು `33.33`."},
    ],
    "walkthrough": {
        "intro": "ಈ program patient ನ ಹೆಸರು ಮತ್ತು ತೂಕ ಕೇಳಿ, kg ಗೆ 15 mg ಪ್ರಕಾರ dose print ಮಾಡುತ್ತೆ. ಈ example ನಲ್ಲಿ pharmacist Ravi ಮತ್ತು 16.1 type ಮಾಡುತ್ತಾರೆ.",
        "keyTerms": [
            {"meaning": "ಪ್ರಶ್ನೆ ತೋರಿಸಿ user ನ answer ಗಾಗಿ ಕಾಯಿ. Answer text."},
            {"meaning": "Value ಕೇಳಿ answer ಅನ್ನು number ಮಾಡು."},
            {"meaning": "Variable ನ value ಅನ್ನು text ಒಳಗೆ ಇಡು."},
            {"meaning": "ಒಂದು decimal place ತೋರಿಸು."},
        ],
    },
    "errors": {
        "intro": "input() ನ answer ಅನ್ನು ಸರಿಯಾಗಿ handle ಮಾಡದಿದ್ದಾಗ ಈ ಎರಡು errors ಬರುತ್ತವೆ.",
        "examples": [
            {"title": "input() ನ text ಇಂದ ಲೆಕ್ಕ ಮಾಡೋದು",
             "md": "`weight` ನಲ್ಲಿ text ಇದೆ, text ಅನ್ನು ದಶಮಾಂಶ ಸಂಖ್ಯೆಯಿಂದ ಗುಣಿಸಲು ಆಗಲ್ಲ. ಮೊದಲು answer ಅನ್ನು ಬದಲಾಯಿಸಿ: `weight = float(input(\"Weight (kg): \"))`."},
            {"title": "User number ಅಲ್ಲದ್ದು type ಮಾಡಿದಾಗ",
             "md": "User `52 kg` ಅಂತ type ಮಾಡಿದರು. `float()` number ಅನ್ನು ಮಾತ್ರ ಬದಲಾಯಿಸಬಹುದು, ಹಾಗಾಗಿ unit ಇಂದ error ಬಂತು. Prompt ನಲ್ಲೇ unit ಕೇಳಿ, ಉದಾ: `\"Weight (kg): \"`, ಆಗ user number ಮಾತ್ರ type ಮಾಡುತ್ತಾರೆ."},
        ],
    },
    "mistakes": [
        {"mistake": "Answer ಅನ್ನು ಬದಲಾಯಿಸಲು ಮರೆಯೋದು, ಉದಾ: `weight = input(\"Weight: \")` ನಂತರ `weight * 2`", "see": "Error ಇಲ್ಲ, ಆದರೆ 20 type ಮಾಡಿದರೆ 2020 ಬರುತ್ತೆ", "fix": "ಬದಲಾಯಿಸಿ: `weight = float(input(\"Weight: \"))`."},
        {"mistake": "f-string ಮುಂದೆ `f` ಮರೆಯೋದು, ಉದಾ: `print(\"Dose: {dose} mg\")`", "see": "Error ಇಲ್ಲ, ಆದರೆ Dose: {dose} mg ಅಂತಲೇ print ಆಗುತ್ತೆ", "fix": "Quote ಮುಂದೆ f ಹಾಕಿ: `print(f\"Dose: {dose} mg\")`."},
        {"mistake": "Prompt ಕೊನೆಯಲ್ಲಿ space ಇಡದಿರೋದು, ಉದಾ: `input(\"Weight:\")`", "see": "Error ಇಲ್ಲ, ಆದರೆ answer ಪ್ರಶ್ನೆಗೆ ಅಂಟಿಕೊಳ್ಳುತ್ತೆ: Weight:52", "fix": "Space ಹಾಕಿ: `input(\"Weight: \")`."},
        {"mistake": "Text ಮತ್ತು number ಅನ್ನು `+` ಇಂದ ಜೋಡಿಸೋದು, ಉದಾ: `print(\"Dose: \" + dose)`", "fix": "f-string use ಮಾಡಿ: `print(f\"Dose: {dose}\")`."},
    ],
    "tasks": [
        {"title": "Patient ಅನ್ನು ಸ್ವಾಗತಿಸಿ", "md": "Program patient ನ ಹೆಸರು ಕೇಳುತ್ತೆ. ಅವರನ್ನು ಸ್ವಾಗತಿಸುವ ಒಂದು line ಸೇರಿಸಿ. ಹೆಸರು **Ananya** type ಆದಾಗ output ಸರಿಯಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["print() \"Hello,\" ಮತ್ತು variable name ಅನ್ನು comma ಇಂದ ಬೇರ್ಪಡಿಸಿ ತೋರಿಸಬಹುದು.", "Try ಮಾಡಿ: print(\"Hello,\", name) ಅಥವಾ print(f\"Hello, {name}\")."]},
        {"title": "Answer ಅನ್ನು ಬದಲಾಯಿಸಿ", "md": "Patient ಎಷ್ಟು strips ತಗೊಳ್ತಿದ್ದಾರೆ ಅಂತ program ಕೇಳುತ್ತೆ. ಪ್ರತಿ strip ನಲ್ಲಿ **10 tablets**. Answer ಅನ್ನು ಪೂರ್ಣ ಸಂಖ್ಯೆಯಾಗಿ ಬದಲಾಯಿಸಿ ಒಟ್ಟು tablets print ಮಾಡಿ. **4** type ಆದಾಗ output ಸರಿಯಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["strips ನಲ್ಲಿ text ಇದೆ. int(strips) ಅದನ್ನು number ಮಾಡುತ್ತೆ.", "print(\"Tablets:\", int(strips) * 10)"]},
        {"title": "ಎರಡು decimal places", "md": "100 ml syrup ಅನ್ನು 3 ಮಕ್ಕಳಿಗೆ ಸಮವಾಗಿ ಹಂಚಲಾಗುತ್ತೆ. **f-string** ಮತ್ತು **`:.2f`** ಇಂದ ಪ್ರತಿ ಮಗುವಿನ volume ಅನ್ನು ಸರಿಯಾಗಿ ಹೀಗೆ print ಮಾಡಿ:",
         "hints": ["Quote ಮುಂದೆ f ಹಾಕಿ: f\"Volume: ...\"", "Curly brackets ಒಳಗೆ ಬರೆಯಿರಿ: volume_ml:.2f"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "ಈ program kg ಗೆ 15 mg ಪ್ರಕಾರ dose print ಮಾಡಬೇಕು. **20** type ಆದಾಗ output ಸರಿಯಾಗಿ ಕೆಳಗಿನದು ಆಗಬೇಕು, ಆದರೆ dose 20 ಗಳ ಉದ್ದದ string ಆಗಿ ಬರುತ್ತೆ. ಸರಿ ಮಾಡಿ.",
         "hints": ["input() ಯಾವ data type ಕೊಡುತ್ತೆ?", "input(...) ಅನ್ನು float(...) ಒಳಗೆ ಇಡಿ."],
         "solutionNote": "input() text ಕೊಡುತ್ತೆ, ಹಾಗಾಗಿ \"20\" * 15 text ಅನ್ನು ಪುನರಾವರ್ತಿಸುತ್ತೆ. float() ಮೊದಲು ಅದನ್ನು number 20.0 ಮಾಡುತ್ತೆ."},
    ],
    "quiz": [
        {"q": "input() ಯಾವಾಗಲೂ ಯಾವ data type ಕೊಡುತ್ತೆ?", "why": "User number type ಮಾಡಿದರೂ, input() ಯಾವಾಗಲೂ text (string) ಕೊಡುತ್ತೆ."},
        {"q": "x = input(\"Number: \") ಮತ್ತು user 20 type ಮಾಡುತ್ತಾರೆ. print(x * 2) ಏನು ತೋರಿಸುತ್ತೆ?", "why": "x ನಲ್ಲಿ text \"20\" ಇದೆ, ಮತ್ತು * text ಅನ್ನು ಪುನರಾವರ್ತಿಸುತ್ತೆ."},
        {"q": "print(\"A\", \"B\", sep=\"\") ಏನು ತೋರಿಸುತ್ತೆ?", "why": "sep=\"\" items ನಡುವೆ ಏನೂ ಇಡಲ್ಲ."},
        {"q": "dose = 500. ಯಾವ line Dose: 500 mg print ಮಾಡುತ್ತೆ?", "why": "{dose} ಇರುವ f-string ಮಾತ್ರ value ಅನ್ನು text ಒಳಗೆ ಇಡುತ್ತೆ."},
        {"q": "print(f\"{2 / 3:.2f}\") ಏನು ತೋರಿಸುತ್ತೆ?", "why": ":.2f round ಮಾಡಿ ಎರಡು decimal places ತೋರಿಸುತ್ತೆ: 0.67."},
        {"q": "print(\"Hi\", end=\"!\") ಏನು ತೋರಿಸುತ್ತೆ?", "why": "end=\"!\" ಹೊಸ line ಬದಲು ಕೊನೆಯಲ್ಲಿ ! print ಮಾಡುತ್ತೆ."},
    ],
    "exam": {"note": "University exam English ನಲ್ಲಿ ಬರೆಯುವುದರಿಂದ model answers English ನಲ್ಲೇ ಇವೆ. ಇವು practice ಗಾಗಿ important questions; ನಿಜವಾದ university questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 1.5 · Input ಮತ್ತು output",
        "children": [
            {"label": "input()", "children": [{"label": "Prompt ತೋರಿಸುತ್ತೆ"}, {"label": "Enter ಗಾಗಿ ಕಾಯುತ್ತೆ"}, {"label": "ಯಾವಾಗಲೂ str"}]},
            {"label": "ಬದಲಾಯಿಸು", "children": [{"label": "int(input(...))"}, {"label": "float(input(...))"}, {"label": "\"20\" * 2 = 2020"}]},
            {"label": "print()", "children": [{"label": "sep: items ನಡುವೆ"}, {"label": "end: ಕೊನೆಯಲ್ಲಿ"}]},
            {"label": "f-strings", "children": [{"label": "f\"{name}\""}, {"label": "{x:.1f} ಒಂದು decimal"}, {"label": "{x:.2f} ಎರಡು decimals"}]},
            {"label": "Errors", "children": [{"label": "TypeError: text × number"}, {"label": "ValueError: '52 kg'"}]},
        ],
    },
    "summary": [
        "**`input()`** ಒಂದು **prompt** ತೋರಿಸಿ, user answer type ಮಾಡಿ Enter ಒತ್ತುವವರೆಗೆ ಕಾಯುತ್ತೆ.",
        "Answer ಯಾವಾಗಲೂ **string**, ಹಾಗಾಗಿ numbers ಅನ್ನು **`int()`** ಅಥವಾ **`float()`** ಇಂದ ಬದಲಾಯಿಸಿ: `float(input(\"Weight (kg): \"))`.",
        "**`sep`** print ಆಗುವ items ನಡುವೆ ಏನು ಬರಬೇಕು, **`end`** line ಕೊನೆಯಲ್ಲಿ ಏನು ಬರಬೇಕು ಅಂತ ನಿರ್ಧರಿಸುತ್ತೆ.",
        "**f-strings** values ಅನ್ನು text ಒಳಗೆ ಇಡುತ್ತವೆ: `f\"Dose: {dose} mg\"`.",
        "**`:.1f`** ಮತ್ತು **`:.2f`** ಒಂದು ಅಥವಾ ಎರಡು decimal places ತೋರಿಸಿ, 241.50000000000003 ತರಹದ ಚಿಕ್ಕ rounding ವ್ಯತ್ಯಾಸಗಳನ್ನು ಮರೆಮಾಡುತ್ತವೆ.",
    ],
}

NARR = {
    "hi": [
        "यह program patient का नाम और वज़न पूछता है, और फिर dose print करता है। देखिए answers variables में कैसे जाते हैं।",
        "Comment बताता है कि program क्या करता है।",
        "input सवाल दिखाता है, Patient name, और इंतज़ार करता है। Pharmacist Ravi type करके Enter दबाता है। Ravi, variable name में रख लिया जाता है।",
        "फिर input वज़न पूछता है। Answer text है, इसलिए float सोलह दशमलव एक को number बना देता है।",
        "Python पंद्रह से गुणा करता है। Variables panel देखिए: answer के पीछे decimals की लंबी पूँछ है। यह बहुत छोटा rounding फ़र्क है।",
        "यह f-string, name की value को text के अंदर रखती है।",
        "Colon, point एक, f ठीक एक decimal place दिखाता है। इसलिए label पढ़ता है, दो सौ इकतालीस दशमलव पाँच milligrams।",
    ],
    "hinglish": [
        "Yeh program patient ka naam aur wazan poochta hai, aur phir dose print karta hai. Dekhiye answers variables mein kaise jaate hain.",
        "Comment batata hai ki program kya karta hai.",
        "input sawaal dikhata hai, Patient name, aur intezaar karta hai. Pharmacist Ravi type karke Enter dabata hai. Ravi, variable name mein rakh liya jaata hai.",
        "Phir input wazan poochta hai. Answer text hai, isliye float solah dashamlav ek ko number bana deta hai.",
        "Python pandrah se guna karta hai. Variables panel dekhiye: answer ke peechhe decimals ki lambi poonchh hai. Yeh bahut chhota rounding farak hai.",
        "Yeh f-string, name ki value ko text ke andar rakhti hai.",
        "Colon, point ek, f theek ek decimal place dikhata hai. Isliye label padhta hai, do sau iktaalees dashamlav paanch milligrams.",
    ],
    "kn": [
        "ಈ program patient ನ ಹೆಸರು ಮತ್ತು ತೂಕ ಕೇಳಿ, ನಂತರ dose print ಮಾಡುತ್ತೆ. Answers variables ಒಳಗೆ ಹೇಗೆ ಹೋಗುತ್ತವೆ ನೋಡಿ.",
        "Program ಏನು ಮಾಡುತ್ತೆ ಅಂತ comment ಹೇಳುತ್ತೆ.",
        "input, Patient name ಅನ್ನುವ ಪ್ರಶ್ನೆ ತೋರಿಸಿ ಕಾಯುತ್ತೆ. Pharmacist Ravi ಅಂತ type ಮಾಡಿ Enter ಒತ್ತುತ್ತಾರೆ. Ravi, variable name ನಲ್ಲಿ ಇಡಲಾಗುತ್ತೆ.",
        "ನಂತರ input ತೂಕ ಕೇಳುತ್ತೆ. Answer text, ಹಾಗಾಗಿ float ಹದಿನಾರು ದಶಮಾಂಶ ಒಂದನ್ನು number ಮಾಡುತ್ತೆ.",
        "Python ಹದಿನೈದರಿಂದ ಗುಣಿಸುತ್ತೆ. Variables panel ನೋಡಿ: answer ಹಿಂದೆ decimals ನ ಉದ್ದದ ಬಾಲ ಇದೆ. ಅದು ತುಂಬಾ ಚಿಕ್ಕ rounding ವ್ಯತ್ಯಾಸ.",
        "ಈ f-string, name ನ value ಅನ್ನು text ಒಳಗೆ ಇಡುತ್ತೆ.",
        "Colon, point ಒಂದು, f ಸರಿಯಾಗಿ ಒಂದು decimal place ತೋರಿಸುತ್ತೆ. ಹಾಗಾಗಿ label, ಇನ್ನೂರ ನಲವತ್ತೊಂದು ದಶಮಾಂಶ ಐದು milligrams ಅಂತ ಓದುತ್ತೆ.",
    ],
}
ANIM = {
    "hi": [
        "Program सवाल दिखाकर इंतज़ार करता है। Pharmacist सोलह दशमलव एक type करके Enter दबाता है।",
        "input हमेशा text देता है। इसलिए पहले box में string सोलह दशमलव एक है, quotes के साथ।",
        "float text को number बना देता है। अब quotes चले गए।",
        "अब Python dose calculate कर सकता है: सोलह दशमलव एक गुणा पंद्रह, एक छोटी rounding पूँछ के साथ।",
        "Colon, point एक, f वाली f-string इसे साफ़-साफ़, एक decimal place के साथ print करती है।",
    ],
    "hinglish": [
        "Program sawaal dikhakar intezaar karta hai. Pharmacist solah dashamlav ek type karke Enter dabata hai.",
        "input hamesha text deta hai. Isliye pehle box mein string solah dashamlav ek hai, quotes ke saath.",
        "float text ko number bana deta hai. Ab quotes chale gaye.",
        "Ab Python dose calculate kar sakta hai: solah dashamlav ek guna pandrah, ek chhoti rounding poonchh ke saath.",
        "Colon, point ek, f wali f-string ise saaf-saaf, ek decimal place ke saath print karti hai.",
    ],
    "kn": [
        "Program ಪ್ರಶ್ನೆ ತೋರಿಸಿ ಕಾಯುತ್ತೆ. Pharmacist ಹದಿನಾರು ದಶಮಾಂಶ ಒಂದು ಅಂತ type ಮಾಡಿ Enter ಒತ್ತುತ್ತಾರೆ.",
        "input ಯಾವಾಗಲೂ text ಕೊಡುತ್ತೆ. ಹಾಗಾಗಿ ಮೊದಲು box ನಲ್ಲಿ quotes ಜೊತೆ string ಹದಿನಾರು ದಶಮಾಂಶ ಒಂದು ಇದೆ.",
        "float text ಅನ್ನು number ಮಾಡುತ್ತೆ. ಈಗ quotes ಹೋದವು.",
        "ಈಗ Python dose ಲೆಕ್ಕ ಹಾಕಬಹುದು: ಹದಿನಾರು ದಶಮಾಂಶ ಒಂದು ಗುಣಿಸು ಹದಿನೈದು, ಒಂದು ಚಿಕ್ಕ rounding ಬಾಲದ ಜೊತೆ.",
        "Colon, point ಒಂದು, f ಇರುವ f-string ಇದನ್ನು ಒಂದು decimal place ಜೊತೆ ಚೆನ್ನಾಗಿ print ಮಾಡುತ್ತೆ.",
    ],
}
TTS = {
    "narrator": {
        "hi": [
            "यह प्रोग्राम पेशेंट का नाम और वज़न पूछता है, और फिर डोज़ प्रिंट करता है। देखिए आंसर्स वेरिएबल्स में कैसे जाते हैं।",
            "कमेंट बताता है कि प्रोग्राम क्या करता है।",
            "इनपुट सवाल दिखाता है, पेशेंट नेम, और इंतज़ार करता है। फार्मासिस्ट रवि टाइप करके एंटर दबाता है। रवि, वेरिएबल नेम में रख लिया जाता है।",
            "फिर इनपुट वज़न पूछता है। आंसर टेक्स्ट है, इसलिए फ्लोट सोलह दशमलव एक को नंबर बना देता है।",
            "पाइथन पंद्रह से गुणा करता है। वेरिएबल्स पैनल देखिए: आंसर के पीछे डेसिमल्स की लंबी पूँछ है। यह बहुत छोटा राउंडिंग फ़र्क है।",
            "यह एफ स्ट्रिंग, नेम की वैल्यू को टेक्स्ट के अंदर रखती है।",
            "कोलन, पॉइंट वन, एफ, ठीक एक डेसिमल प्लेस दिखाता है। इसलिए लेबल पढ़ता है, दो सौ इकतालीस दशमलव पाँच मिलीग्राम।",
        ],
        "kn": [
            "ಈ ಪ್ರೋಗ್ರಾಮ್ ಪೇಷೆಂಟ್ ನ ಹೆಸರು ಮತ್ತು ತೂಕ ಕೇಳಿ, ನಂತರ ಡೋಸ್ ಪ್ರಿಂಟ್ ಮಾಡುತ್ತೆ. ಆನ್ಸರ್ಸ್ ವೇರಿಯಬಲ್ಸ್ ಒಳಗೆ ಹೇಗೆ ಹೋಗುತ್ತವೆ ನೋಡಿ.",
            "ಪ್ರೋಗ್ರಾಮ್ ಏನು ಮಾಡುತ್ತೆ ಅಂತ ಕಾಮೆಂಟ್ ಹೇಳುತ್ತೆ.",
            "ಇನ್ಪುಟ್, ಪೇಷೆಂಟ್ ನೇಮ್ ಅನ್ನುವ ಪ್ರಶ್ನೆ ತೋರಿಸಿ ಕಾಯುತ್ತೆ. ಫಾರ್ಮಸಿಸ್ಟ್ ರವಿ ಅಂತ ಟೈಪ್ ಮಾಡಿ ಎಂಟರ್ ಒತ್ತುತ್ತಾರೆ. ರವಿ, ವೇರಿಯಬಲ್ ನೇಮ್ ನಲ್ಲಿ ಇಡಲಾಗುತ್ತೆ.",
            "ನಂತರ ಇನ್ಪುಟ್ ತೂಕ ಕೇಳುತ್ತೆ. ಆನ್ಸರ್ ಟೆಕ್ಸ್ಟ್, ಹಾಗಾಗಿ ಫ್ಲೋಟ್ ಹದಿನಾರು ದಶಮಾಂಶ ಒಂದನ್ನು ನಂಬರ್ ಮಾಡುತ್ತೆ.",
            "ಪೈಥಾನ್ ಹದಿನೈದರಿಂದ ಗುಣಿಸುತ್ತೆ. ವೇರಿಯಬಲ್ಸ್ ಪ್ಯಾನೆಲ್ ನೋಡಿ: ಆನ್ಸರ್ ಹಿಂದೆ ಡೆಸಿಮಲ್ಸ್ ನ ಉದ್ದದ ಬಾಲ ಇದೆ. ಅದು ತುಂಬಾ ಚಿಕ್ಕ ರೌಂಡಿಂಗ್ ವ್ಯತ್ಯಾಸ.",
            "ಈ ಎಫ್ ಸ್ಟ್ರಿಂಗ್, ನೇಮ್ ನ ವ್ಯಾಲ್ಯೂ ಅನ್ನು ಟೆಕ್ಸ್ಟ್ ಒಳಗೆ ಇಡುತ್ತೆ.",
            "ಕೋಲನ್, ಪಾಯಿಂಟ್ ಒನ್, ಎಫ್, ಸರಿಯಾಗಿ ಒಂದು ಡೆಸಿಮಲ್ ಪ್ಲೇಸ್ ತೋರಿಸುತ್ತೆ. ಹಾಗಾಗಿ ಲೇಬಲ್, ಇನ್ನೂರ ನಲವತ್ತೊಂದು ದಶಮಾಂಶ ಐದು ಮಿಲಿಗ್ರಾಂ ಅಂತ ಓದುತ್ತೆ.",
        ],
    },
    "anim-input": {
        "hi": [
            "प्रोग्राम सवाल दिखाकर इंतज़ार करता है। फार्मासिस्ट सोलह दशमलव एक टाइप करके एंटर दबाता है।",
            "इनपुट हमेशा टेक्स्ट देता है। इसलिए पहले बॉक्स में स्ट्रिंग सोलह दशमलव एक है, कोट्स के साथ।",
            "फ्लोट टेक्स्ट को नंबर बना देता है। अब कोट्स चले गए।",
            "अब पाइथन डोज़ कैलकुलेट कर सकता है: सोलह दशमलव एक गुणा पंद्रह, एक छोटी राउंडिंग पूँछ के साथ।",
            "कोलन, पॉइंट वन, एफ वाली एफ स्ट्रिंग इसे साफ़-साफ़, एक डेसिमल प्लेस के साथ प्रिंट करती है।",
        ],
        "kn": [
            "ಪ್ರೋಗ್ರಾಮ್ ಪ್ರಶ್ನೆ ತೋರಿಸಿ ಕಾಯುತ್ತೆ. ಫಾರ್ಮಸಿಸ್ಟ್ ಹದಿನಾರು ದಶಮಾಂಶ ಒಂದು ಅಂತ ಟೈಪ್ ಮಾಡಿ ಎಂಟರ್ ಒತ್ತುತ್ತಾರೆ.",
            "ಇನ್ಪುಟ್ ಯಾವಾಗಲೂ ಟೆಕ್ಸ್ಟ್ ಕೊಡುತ್ತೆ. ಹಾಗಾಗಿ ಮೊದಲು ಬಾಕ್ಸ್ ನಲ್ಲಿ ಕೋಟ್ಸ್ ಜೊತೆ ಸ್ಟ್ರಿಂಗ್ ಹದಿನಾರು ದಶಮಾಂಶ ಒಂದು ಇದೆ.",
            "ಫ್ಲೋಟ್ ಟೆಕ್ಸ್ಟ್ ಅನ್ನು ನಂಬರ್ ಮಾಡುತ್ತೆ. ಈಗ ಕೋಟ್ಸ್ ಹೋದವು.",
            "ಈಗ ಪೈಥಾನ್ ಡೋಸ್ ಲೆಕ್ಕ ಹಾಕಬಹುದು: ಹದಿನಾರು ದಶಮಾಂಶ ಒಂದು ಗುಣಿಸು ಹದಿನೈದು, ಒಂದು ಚಿಕ್ಕ ರೌಂಡಿಂಗ್ ಬಾಲದ ಜೊತೆ.",
            "ಕೋಲನ್, ಪಾಯಿಂಟ್ ಒನ್, ಎಫ್ ಇರುವ ಎಫ್ ಸ್ಟ್ರಿಂಗ್ ಇದನ್ನು ಒಂದು ಡೆಸಿಮಲ್ ಪ್ಲೇಸ್ ಜೊತೆ ಚೆನ್ನಾಗಿ ಪ್ರಿಂಟ್ ಮಾಡುತ್ತೆ.",
        ],
    },
}


def say_en(text):
    """English voice script: spell out code names so the voice reads them naturally."""
    text = re.sub(r"([Cc]olon, point one,) f\b", r"\1 F", text).replace("f-string", "F string")
    text = re.sub(r"\b(\w+)_mg\b", r"\1 M G", text)
    text = re.sub(r"\b(\w+)_kg\b", r"\1 K G", text)
    return re.sub(r"\b([a-z]+)_([a-z]+)\b", r"\1 \2", text)


if __name__ == "__main__":
    en = json.load(open(os.path.join(ROOT, "content", "bp101t", "1-5", "en.json"), encoding="utf-8"))
    n_steps, n_anim = len(en["walkthrough"]["steps"]), len(en["animations"][0]["steps"])
    for lang, data in T.items():
        assert len(NARR[lang]) == n_steps and len(ANIM[lang]) == n_anim, lang
        doc = dict(data)
        doc["walkthrough"] = dict(doc["walkthrough"], steps=[{"say": s} for s in NARR[lang]])
        doc["animations"] = [{"steps": [{"say": s} for s in ANIM[lang]]}]
        doc["translatedSections"] = SECTIONS
        path = os.path.join(ROOT, "content", "bp101t", "1-5", f"{lang}.json")
        json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("wrote", path)

    for lang in ("hi", "kn"):
        assert len(TTS["narrator"][lang]) == n_steps and len(TTS["anim-input"][lang]) == n_anim, lang
    narr_en = [s["say"] for s in en["walkthrough"]["steps"]]
    anim_en = [s["say"] for s in en["animations"][0]["steps"]]
    script = {
        "course": "bp101t", "lesson": "1-5",
        "voices": {"en": "Mary", "hi": "Rani", "kn": "Anu"},
        "tracks": [
            {"id": "narrator", "prefix": "step-", "lang": "en", "tts": [say_en(t) for t in narr_en], "display": narr_en},
            {"id": "narrator", "prefix": "step-", "lang": "hi", "tts": TTS["narrator"]["hi"], "display": NARR["hi"], "displayHinglish": NARR["hinglish"]},
            {"id": "narrator", "prefix": "step-", "lang": "kn", "tts": TTS["narrator"]["kn"], "display": NARR["kn"]},
            {"id": "anim-input", "prefix": "anim-input-", "lang": "en", "tts": [say_en(t) for t in anim_en], "display": anim_en},
            {"id": "anim-input", "prefix": "anim-input-", "lang": "hi", "tts": TTS["anim-input"]["hi"], "display": ANIM["hi"], "displayHinglish": ANIM["hinglish"]},
            {"id": "anim-input", "prefix": "anim-input-", "lang": "kn", "tts": TTS["anim-input"]["kn"], "display": ANIM["kn"]},
        ],
    }
    path = os.path.join(ROOT, "scripts", "bp101t", "1-5.json")
    json.dump(script, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", path)
    # keep the "Words to know" section after regenerating
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "..", "glossary_bp101t.py")], check=True)

"""Lesson 1.3 translations (Hindi, Hinglish, Kannada) and voice scripts.

Run to write content/bp101t/1-3/{hi,hinglish,kn}.json and scripts/bp101t/1-3.json.
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

CODE_DOSE = "```python\ndose_mg = 500\n```"
CODE_CHANGE = "```python\ndose_mg = 500\ndose_mg = 650\nprint(\"Dose:\", dose_mg, \"mg\")\n```"
CODE_TYPE = "```python\nprint(type(500))\nprint(type(52.5))\nprint(type(\"500\"))\nprint(type(True))\n```"
OUT_TYPE = "```\n<class 'int'>\n<class 'float'>\n<class 'str'>\n<class 'bool'>\n```"
CODE_NUM = "```python\ndose = 500\nprint(dose * 3)\n```"
CODE_TXT = "```python\ndose = \"500\"\nprint(dose * 3)\n```"

T = {}

# ======================================================================= Hindi
T["hi"] = {
    "hook": {
        "title": "Patient की details को label लगे boxes में रखिए",
        "md": "Pharmacist दवाइयों को **label लगे boxes** में रखता है, ताकि सही दवा तुरंत मिल जाए। Python भी जानकारी ऐसे ही रखता है, **variables** में।\n\nइस lesson के अंत तक आप एक patient का नाम, वज़न और dose variables में रखेंगे, और उनसे dose calculate करेंगे।",
    },
    "learn": [
        "**Variable** क्या है, और value कैसे रखें और बदलें",
        "**Variables के नाम** रखने के नियम",
        "चार basic **data types**: integers, floats, strings और booleans",
    ],
    "explanation": [
        {"heading": "Variable क्या है?",
         "md": f"Pharmacy की shelf पर रखे एक **label लगे box** के बारे में सोचिए। Label बताता है कि अंदर क्या है; box उस चीज़ को रखता है।\n\n**Variable** भी ऐसे ही काम करता है। इसका एक **नाम** (label) होता है और यह एक **value** (अंदर की चीज़) रखता है:\n\n{CODE_DOSE}\n\n`=` को **\"रखो\"** पढ़िए: *500 को `dose_mg` नाम के box में रखो*। इसे **assignment** कहते हैं। इसका मतलब गणित वाला \"बराबर\" नहीं है।\n\nValue रखने के बाद आप उसे नाम से use कर सकते हैं, और कभी भी बदल सकते हैं:\n\n{CODE_CHANGE}\n\nयह `Dose: 650 mg` print करता है, क्योंकि box में अब 650 है।",
         "callout": {"title": "Variable", "md": "Computer की memory में एक नाम वाली जगह जो एक value रखती है, जैसे shelf पर label लगा box।"}},
        {"heading": "Variables के नाम रखना",
         "md": "Variable के नाम कुछ नियम मानते हैं:\n\n- सिर्फ **letters, numbers और underscores** (`_`) use करें, जैसे `dose_mg`, `patient2`।\n- **Number से शुरू न करें**: `2nd_dose` नहीं चलेगा; `dose_2` ठीक है।\n- **Spaces नहीं**: `patient weight` नहीं, `patient_weight` लिखें।\n- नाम **case-sensitive** होते हैं: `weight` और `Weight` दो अलग variables हैं।\n- **Python के अपने शब्द use न करें**, जैसे `True`, `if` या `for`। ये खास मतलब वाले **keywords** हैं।\n\n**अच्छी आदत:** ऐसे नाम चुनें जो बताएँ कि अंदर क्या है, small letters और underscores के साथ, जैसे `patient_weight_kg`। `x` या `a1` जैसे नाम code को बाद में समझना मुश्किल बना देते हैं।"},
        {"heading": "चार basic data types",
         "md": "हर value का एक **data type** होता है, जो Python को बताता है कि value किस तरह की है।\n\n| Data type | Python नाम | क्या रखता है | Pharmacy example |\n|---|---|---|---|\n| **Integer** | `int` | पूरी संख्याएँ | `tablets = 30` |\n| **Float** | `float` | दशमलव वाली संख्याएँ | `weight_kg = 52.5` |\n| **String** | `str` | Quotes के अंदर text | `drug = \"Amoxicillin\"` |\n| **Boolean** | `bool` | सिर्फ `True` या `False` | `in_stock = True` |\n\nध्यान दीजिए: `True` और `False` **capital letter** से शुरू होते हैं, और इनमें **quotes नहीं** होते।",
         "callout": {"title": "Data type", "md": "Value किस तरह की है: पूरी संख्या (int), दशमलव वाली संख्या (float), text (str) या True/False (bool)।"}},
        {"heading": "type() से type check करना",
         "md": f"पक्का नहीं कि value का type क्या है? `type()` से Python से पूछिए:\n\n{CODE_TYPE}\n\nयह print करता है:\n\n{OUT_TYPE}\n\nतीसरी line ध्यान से देखिए: `\"500\"` **quotes** में है, इसलिए यह **text** है, number नहीं।"},
        {"heading": "Data types क्यों ज़रूरी हैं",
         "md": f"Python numbers और text के साथ बिल्कुल अलग तरह से काम करता है। इन्हें compare कीजिए:\n\n{CODE_NUM}\n\n`1500` print करता है, लेकिन\n\n{CODE_TXT}\n\n`500500500` print करता है। Text के साथ `*` गुणा करने के बजाय text को **दोहराता** है।",
         "callout": {"title": "Pharmacy में यह बहुत मायने रखता है", "md": "गलती से text के रूप में रखा गया number, 1500 mg की dose को बेमतलब 500500500 बना सकता है। हमेशा check कीजिए कि doses और वज़न numbers हों, strings नहीं।"}},
    ],
    "walkthrough": {
        "intro": "यह program एक patient की details variables में रखता है और फिर उन्हें use करता है। हर line चलते समय Variables panel देखिए।",
        "keyTerms": [
            {"meaning": "दाईं तरफ की value को बाईं तरफ के variable में रखो।"},
            {"meaning": "पूरी संख्या / दशमलव वाली संख्या।"},
            {"meaning": "Quotes के अंदर text।"},
            {"meaning": "True या False।"},
        ],
    },
    "errors": {
        "intro": "Variables use करना शुरू करते समय ये दो errors सबसे आम हैं।",
        "examples": [
            {"title": "ऐसा नाम use करना जो मौजूद ही नहीं",
             "md": "Variable का नाम `dose_mg` है, लेकिन line 2 `dose` माँग रही है। Python सिर्फ वही नाम जानता है जो आपने बनाए हैं। Spelling check कीजिए, capital letters भी।"},
            {"title": "Text और number को + से जोड़ना",
             "md": "`+` दो strings को जोड़ सकता है, लेकिन **string** और **integer** को नहीं। सबसे आसान fix है + की जगह comma लगाना: `print(\"Dose:\", 500)`। दूसरा fix आप Lesson 1.4 में सीखेंगे।",
             "callout": {"title": "TypeError", "md": "Error जिसका मतलब है कि उस काम के लिए गलत data type की value use की गई।"}},
        ],
    },
    "mistakes": [
        {"mistake": "Variable के नाम में space डालना, जैसे `patient weight = 52`", "fix": "Underscore use कीजिए: `patient_weight = 52`।"},
        {"mistake": "नाम number से शुरू करना, जैसे `2nd_dose = 250`", "fix": "Number बाद में लगाइए: `dose_2 = 250`।"},
        {"mistake": "नाम में hyphen use करना, जैसे `dose-mg = 500`", "fix": "Python `-` को minus समझता है। Underscore use कीजिए: `dose_mg = 500`।"},
        {"mistake": "`true` small letters में लिखना", "fix": "Booleans capital letter से शुरू होते हैं: `True`, `False`।"},
        {"mistake": "Number को quotes में रखना, जैसे `dose = \"500\"`", "see": "कोई error नहीं, लेकिन `dose * 3` देता है 500500500", "fix": "Numbers को बिना quotes के लिखिए: `dose = 500`।"},
    ],
    "tasks": [
        {"title": "Variables से label print कीजिए", "md": "Variables तैयार हैं। एक line जोड़िए जो **variables use करके** दवा और उसकी strength print करे, ताकि output बिल्कुल यह हो:",
         "hints": ["print() commas से अलग किए कई items दिखा सकता है।", "Try कीजिए: print(drug, strength_mg, \"mg\")।"]},
        {"title": "बच्चे की dose calculate कीजिए", "md": "Rohan का वज़न **18 kg** है, और dose **15 mg प्रति kg** है। नाम, वज़न और dose प्रति kg को `patient`, `weight_kg` और `dose_mg_per_kg` नाम के variables में रखिए, फिर print कीजिए:\n\n*(सिर्फ सीखने के लिए: असली doses clinical guidelines के अनुसार ही होनी चाहिए।)*",
         "hints": ["patient = \"Rohan\" नाम रखता है। weight_kg और dose_mg_per_kg के लिए भी ऐसा ही कीजिए।", "Python से गुणा करवाइए: print(patient, \"needs\", weight_kg * dose_mg_per_kg, \"mg\")।"]},
        {"title": "यह कौन सा type है?", "md": "`type()` use करके value `52.5` का data type print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["Value को type() के अंदर रखिए, और type() को print() के अंदर।"]},
        {"title": "Bug ढूँढिए", "md": "यह program `In stock: True` print करना चाहिए, लेकिन इसमें error है। इसे ठीक कीजिए।",
         "hints": ["Python case-sensitive है।"], "solutionNote": "Booleans True और False लिखे जाते हैं, capital letter के साथ।"},
    ],
    "quiz": [
        {"q": "52.5 का data type क्या है?", "why": "52.5 में दशमलव है, इसलिए यह float है।"},
        {"q": "इनमें से कौन सा सही variable नाम है?", "why": "नाम में letters, numbers और underscores हो सकते हैं, spaces या hyphens नहीं, और नाम number से शुरू नहीं हो सकता।"},
        {"q": "dose_mg = 500 क्या करता है?", "options": ["Check करता है कि dose_mg, 500 के बराबर है या नहीं", "500 को dose_mg नाम के variable में रखता है", "500 print करता है", "dose_mg में 500 जोड़ता है"], "why": "= मतलब रखो: दाईं तरफ की value बाईं तरफ के variable में जाती है।"},
        {"q": "print(type(\"500\")) क्या दिखाता है?", "why": "\"500\" quotes में है, इसलिए यह text (string) है, number नहीं।"},
        {"q": "in_stock = True। in_stock का data type क्या है?", "why": "True और False booleans (bool) हैं।"},
    ],
    "exam": {"note": "University exam English में लिखा जाता है, इसलिए model answers English में ही रखे गए हैं। ये practice के लिए important questions हैं; असली university questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 1.3 · Variables और data types",
        "children": [
            {"label": "Variable", "children": [{"label": "Label लगा box"}, {"label": "name = value"}, {"label": "= मतलब रखो"}, {"label": "Value बदल सकती है"}]},
            {"label": "नाम के नियम", "children": [{"label": "Letters, numbers, _"}, {"label": "Number से शुरू नहीं"}, {"label": "Spaces नहीं"}, {"label": "Case-sensitive"}, {"label": "Keywords नहीं"}]},
            {"label": "Data types", "children": [{"label": "int: 30 tablets"}, {"label": "float: 52.5 kg"}, {"label": "str: \"Amoxicillin\""}, {"label": "bool: True / False"}]},
            {"label": "type()", "children": [{"label": "Data type दिखाता है"}, {"label": "\"500\" एक str है"}]},
            {"label": "क्यों ज़रूरी", "children": [{"label": "500 * 3 = 1500"}, {"label": "\"500\" * 3 = 500500500"}]},
            {"label": "Errors", "children": [{"label": "NameError: गलत नाम"}, {"label": "TypeError: text + number"}]},
        ],
    },
    "summary": [
        "**Variable** एक label लगा box है जो **value** रखता है; `=` का मतलब **रखो** है, बराबर नहीं।",
        "नामों में **letters, numbers और underscores** होते हैं, ये number से शुरू नहीं होते, इनमें spaces नहीं होते, और ये **case-sensitive** होते हैं।",
        "चार basic **data types** हैं **int** (30), **float** (52.5), **str** (\"Amoxicillin\") और **bool** (True / False)।",
        "**`type()`** value का data type दिखाता है; quotes में लिखी हर चीज़ **string** है, \"500\" भी।",
        "Data types से result बदलता है: `500 * 3` है 1500, लेकिन `\"500\" * 3` है 500500500।",
    ],
}

# ===================================================================== Hinglish
T["hinglish"] = {
    "hook": {
        "title": "Patient ki details ko label lage boxes mein rakhiye",
        "md": "Pharmacist dawaiyon ko **label lage boxes** mein rakhta hai, taaki sahi dawa turant mil jaaye. Python bhi jaankari aise hi rakhta hai, **variables** mein.\n\nIs lesson ke end tak aap ek patient ka naam, wazan aur dose variables mein rakhenge, aur unse dose calculate karenge.",
    },
    "learn": [
        "**Variable** kya hai, aur value kaise rakhein aur badlein",
        "**Variables ke naam** rakhne ke niyam",
        "Chaar basic **data types**: integers, floats, strings aur booleans",
    ],
    "explanation": [
        {"heading": "Variable kya hai?",
         "md": f"Pharmacy ki shelf par rakhe ek **label lage box** ke baare mein sochiye. Label batata hai ki andar kya hai; box us cheez ko rakhta hai.\n\n**Variable** bhi aise hi kaam karta hai. Iska ek **naam** (label) hota hai aur yeh ek **value** (andar ki cheez) rakhta hai:\n\n{CODE_DOSE}\n\n`=` ko **\"rakho\"** padhiye: *500 ko `dose_mg` naam ke box mein rakho*. Ise **assignment** kehte hain. Iska matlab ganit wala \"barabar\" nahi hai.\n\nValue rakhne ke baad aap use naam se use kar sakte hain, aur kabhi bhi badal sakte hain:\n\n{CODE_CHANGE}\n\nYeh `Dose: 650 mg` print karta hai, kyunki box mein ab 650 hai.",
         "callout": {"title": "Variable", "md": "Computer ki memory mein ek naam wali jagah jo ek value rakhti hai, jaise shelf par label laga box."}},
        {"heading": "Variables ke naam rakhna",
         "md": "Variable ke naam kuch niyam maante hain:\n\n- Sirf **letters, numbers aur underscores** (`_`) use karein, jaise `dose_mg`, `patient2`.\n- **Number se shuru na karein**: `2nd_dose` nahi chalega; `dose_2` theek hai.\n- **Spaces nahi**: `patient weight` nahi, `patient_weight` likhein.\n- Naam **case-sensitive** hote hain: `weight` aur `Weight` do alag variables hain.\n- **Python ke apne shabd use na karein**, jaise `True`, `if` ya `for`. Yeh khaas matlab wale **keywords** hain.\n\n**Achhi aadat:** aise naam chuniye jo bataayein ki andar kya hai, small letters aur underscores ke saath, jaise `patient_weight_kg`. `x` ya `a1` jaise naam code ko baad mein samajhna mushkil bana dete hain."},
        {"heading": "Chaar basic data types",
         "md": "Har value ka ek **data type** hota hai, jo Python ko batata hai ki value kis tarah ki hai.\n\n| Data type | Python naam | Kya rakhta hai | Pharmacy example |\n|---|---|---|---|\n| **Integer** | `int` | Poori sankhyayein | `tablets = 30` |\n| **Float** | `float` | Dashamlav wali sankhyayein | `weight_kg = 52.5` |\n| **String** | `str` | Quotes ke andar text | `drug = \"Amoxicillin\"` |\n| **Boolean** | `bool` | Sirf `True` ya `False` | `in_stock = True` |\n\nDhyaan dijiye: `True` aur `False` **capital letter** se shuru hote hain, aur inme **quotes nahi** hote.",
         "callout": {"title": "Data type", "md": "Value kis tarah ki hai: poori sankhya (int), dashamlav wali sankhya (float), text (str) ya True/False (bool)."}},
        {"heading": "type() se type check karna",
         "md": f"Pakka nahi ki value ka type kya hai? `type()` se Python se poochiye:\n\n{CODE_TYPE}\n\nYeh print karta hai:\n\n{OUT_TYPE}\n\nTeesri line dhyaan se dekhiye: `\"500\"` **quotes** mein hai, isliye yeh **text** hai, number nahi."},
        {"heading": "Data types kyun zaroori hain",
         "md": f"Python numbers aur text ke saath bilkul alag tarah se kaam karta hai. Inhe compare kijiye:\n\n{CODE_NUM}\n\n`1500` print karta hai, lekin\n\n{CODE_TXT}\n\n`500500500` print karta hai. Text ke saath `*` guna karne ke bajaay text ko **dohraata** hai.",
         "callout": {"title": "Pharmacy mein yeh bahut maayne rakhta hai", "md": "Galti se text ke roop mein rakha gaya number, 1500 mg ki dose ko bematlab 500500500 bana sakta hai. Hamesha check kijiye ki doses aur wazan numbers hon, strings nahi."}},
    ],
    "walkthrough": {
        "intro": "Yeh program ek patient ki details variables mein rakhta hai aur phir unhe use karta hai. Har line chalte samay Variables panel dekhiye.",
        "keyTerms": [
            {"meaning": "Daayin taraf ki value ko baayin taraf ke variable mein rakho."},
            {"meaning": "Poori sankhya / dashamlav wali sankhya."},
            {"meaning": "Quotes ke andar text."},
            {"meaning": "True ya False."},
        ],
    },
    "errors": {
        "intro": "Variables use karna shuru karte samay yeh do errors sabse aam hain.",
        "examples": [
            {"title": "Aisa naam use karna jo maujood hi nahi",
             "md": "Variable ka naam `dose_mg` hai, lekin line 2 `dose` maang rahi hai. Python sirf wahi naam jaanta hai jo aapne banaye hain. Spelling check kijiye, capital letters bhi."},
            {"title": "Text aur number ko + se jodna",
             "md": "`+` do strings ko jod sakta hai, lekin **string** aur **integer** ko nahi. Sabse aasaan fix hai + ki jagah comma lagana: `print(\"Dose:\", 500)`. Doosra fix aap Lesson 1.4 mein seekhenge.",
             "callout": {"title": "TypeError", "md": "Error jiska matlab hai ki us kaam ke liye galat data type ki value use ki gayi."}},
        ],
    },
    "mistakes": [
        {"mistake": "Variable ke naam mein space daalna, jaise `patient weight = 52`", "fix": "Underscore use kijiye: `patient_weight = 52`."},
        {"mistake": "Naam number se shuru karna, jaise `2nd_dose = 250`", "fix": "Number baad mein lagaiye: `dose_2 = 250`."},
        {"mistake": "Naam mein hyphen use karna, jaise `dose-mg = 500`", "fix": "Python `-` ko minus samajhta hai. Underscore use kijiye: `dose_mg = 500`."},
        {"mistake": "`true` small letters mein likhna", "fix": "Booleans capital letter se shuru hote hain: `True`, `False`."},
        {"mistake": "Number ko quotes mein rakhna, jaise `dose = \"500\"`", "see": "Koi error nahi, lekin `dose * 3` deta hai 500500500", "fix": "Numbers ko bina quotes ke likhiye: `dose = 500`."},
    ],
    "tasks": [
        {"title": "Variables se label print kijiye", "md": "Variables taiyaar hain. Ek line jodiye jo **variables use karke** dawa aur uski strength print kare, taaki output bilkul yeh ho:",
         "hints": ["print() commas se alag kiye kai items dikha sakta hai.", "Try kijiye: print(drug, strength_mg, \"mg\")."]},
        {"title": "Bachche ki dose calculate kijiye", "md": "Rohan ka wazan **18 kg** hai, aur dose **15 mg prati kg** hai. Naam, wazan aur dose prati kg ko `patient`, `weight_kg` aur `dose_mg_per_kg` naam ke variables mein rakhiye, phir print kijiye:\n\n*(Sirf seekhne ke liye: asli doses clinical guidelines ke anusaar hi honi chahiye.)*",
         "hints": ["patient = \"Rohan\" naam rakhta hai. weight_kg aur dose_mg_per_kg ke liye bhi aisa hi kijiye.", "Python se guna karwaiye: print(patient, \"needs\", weight_kg * dose_mg_per_kg, \"mg\")."]},
        {"title": "Yeh kaunsa type hai?", "md": "`type()` use karke value `52.5` ka data type print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["Value ko type() ke andar rakhiye, aur type() ko print() ke andar."]},
        {"title": "Bug dhoondhiye", "md": "Yeh program `In stock: True` print karna chahiye, lekin isme error hai. Ise theek kijiye.",
         "hints": ["Python case-sensitive hai."], "solutionNote": "Booleans True aur False likhe jaate hain, capital letter ke saath."},
    ],
    "quiz": [
        {"q": "52.5 ka data type kya hai?", "why": "52.5 mein dashamlav hai, isliye yeh float hai."},
        {"q": "Inme se kaunsa sahi variable naam hai?", "why": "Naam mein letters, numbers aur underscores ho sakte hain, spaces ya hyphens nahi, aur naam number se shuru nahi ho sakta."},
        {"q": "dose_mg = 500 kya karta hai?", "options": ["Check karta hai ki dose_mg, 500 ke barabar hai ya nahi", "500 ko dose_mg naam ke variable mein rakhta hai", "500 print karta hai", "dose_mg mein 500 jodta hai"], "why": "= matlab rakho: daayin taraf ki value baayin taraf ke variable mein jaati hai."},
        {"q": "print(type(\"500\")) kya dikhata hai?", "why": "\"500\" quotes mein hai, isliye yeh text (string) hai, number nahi."},
        {"q": "in_stock = True. in_stock ka data type kya hai?", "why": "True aur False booleans (bool) hain."},
    ],
    "exam": {"note": "University exam English mein likha jaata hai, isliye model answers English mein hi rakhe gaye hain. Yeh practice ke liye important questions hain; asli university questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 1.3 · Variables aur data types",
        "children": [
            {"label": "Variable", "children": [{"label": "Label laga box"}, {"label": "name = value"}, {"label": "= matlab rakho"}, {"label": "Value badal sakti hai"}]},
            {"label": "Naam ke niyam", "children": [{"label": "Letters, numbers, _"}, {"label": "Number se shuru nahi"}, {"label": "Spaces nahi"}, {"label": "Case-sensitive"}, {"label": "Keywords nahi"}]},
            {"label": "Data types", "children": [{"label": "int: 30 tablets"}, {"label": "float: 52.5 kg"}, {"label": "str: \"Amoxicillin\""}, {"label": "bool: True / False"}]},
            {"label": "type()", "children": [{"label": "Data type dikhata hai"}, {"label": "\"500\" ek str hai"}]},
            {"label": "Kyun zaroori", "children": [{"label": "500 * 3 = 1500"}, {"label": "\"500\" * 3 = 500500500"}]},
            {"label": "Errors", "children": [{"label": "NameError: galat naam"}, {"label": "TypeError: text + number"}]},
        ],
    },
    "summary": [
        "**Variable** ek label laga box hai jo **value** rakhta hai; `=` ka matlab **rakho** hai, barabar nahi.",
        "Naamon mein **letters, numbers aur underscores** hote hain, yeh number se shuru nahi hote, inme spaces nahi hote, aur yeh **case-sensitive** hote hain.",
        "Chaar basic **data types** hain **int** (30), **float** (52.5), **str** (\"Amoxicillin\") aur **bool** (True / False).",
        "**`type()`** value ka data type dikhata hai; quotes mein likhi har cheez **string** hai, \"500\" bhi.",
        "Data types se result badalta hai: `500 * 3` hai 1500, lekin `\"500\" * 3` hai 500500500.",
    ],
}

# ===================================================================== Kannada
T["kn"] = {
    "hook": {
        "title": "Patient ನ details ಅನ್ನು label ಇರುವ boxes ನಲ್ಲಿ ಇಡಿ",
        "md": "Pharmacist ಔಷಧಿಗಳನ್ನು **label ಇರುವ boxes** ನಲ್ಲಿ ಇಡ್ತಾರೆ, ಸರಿಯಾದ ಔಷಧಿ ತಕ್ಷಣ ಸಿಗಲಿ ಅಂತ. Python ಕೂಡ ಮಾಹಿತಿಯನ್ನು ಹೀಗೇ ಇಡುತ್ತೆ, **variables** ನಲ್ಲಿ.\n\nಈ lesson ಮುಗಿಯುವಷ್ಟರಲ್ಲಿ, ನೀವು ಒಬ್ಬ patient ನ ಹೆಸರು, ತೂಕ ಮತ್ತು dose ಅನ್ನು variables ನಲ್ಲಿ ಇಟ್ಟು, ಅವುಗಳಿಂದ dose calculate ಮಾಡ್ತೀರಿ.",
    },
    "learn": [
        "**Variable** ಅಂದ್ರೆ ಏನು, ಮತ್ತು value ಅನ್ನು ಹೇಗೆ ಇಡೋದು, ಬದಲಾಯಿಸೋದು",
        "**Variables ಗೆ ಹೆಸರು** ಇಡುವ ನಿಯಮಗಳು",
        "ನಾಲ್ಕು basic **data types**: integers, floats, strings ಮತ್ತು booleans",
    ],
    "explanation": [
        {"heading": "Variable ಅಂದ್ರೆ ಏನು?",
         "md": f"Pharmacy shelf ಮೇಲಿನ ಒಂದು **label ಇರುವ box** ಬಗ್ಗೆ ಯೋಚಿಸಿ. Label ಒಳಗೆ ಏನಿದೆ ಅಂತ ಹೇಳುತ್ತೆ; box ಆ ವಸ್ತುವನ್ನು ಇಟ್ಟುಕೊಳ್ಳುತ್ತೆ.\n\n**Variable** ಕೂಡ ಹೀಗೇ ಕೆಲಸ ಮಾಡುತ್ತೆ. ಅದಕ್ಕೆ ಒಂದು **ಹೆಸರು** (label) ಇರುತ್ತೆ, ಮತ್ತು ಅದು ಒಂದು **value** (ಒಳಗಿನ ವಸ್ತು) ಇಟ್ಟುಕೊಳ್ಳುತ್ತೆ:\n\n{CODE_DOSE}\n\n`=` ಅನ್ನು **\"ಇಡು\"** ಅಂತ ಓದಿ: *500 ಅನ್ನು `dose_mg` ಅನ್ನುವ box ನಲ್ಲಿ ಇಡು*. ಇದನ್ನು **assignment** ಅಂತಾರೆ. ಇದು ಗಣಿತದ \"ಸಮ\" ಅಲ್ಲ.\n\nValue ಇಟ್ಟ ಮೇಲೆ, ಅದನ್ನು ಹೆಸರಿನಿಂದ use ಮಾಡಬಹುದು, ಮತ್ತು ಯಾವಾಗ ಬೇಕಾದರೂ ಬದಲಾಯಿಸಬಹುದು:\n\n{CODE_CHANGE}\n\nಇದು `Dose: 650 mg` ಅಂತ print ಮಾಡುತ್ತೆ, ಯಾಕಂದ್ರೆ box ನಲ್ಲಿ ಈಗ 650 ಇದೆ.",
         "callout": {"title": "Variable", "md": "Computer memory ಯಲ್ಲಿ ಒಂದು value ಇಡುವ ಹೆಸರಿರುವ ಜಾಗ, shelf ಮೇಲಿನ label ಇರುವ box ತರಹ."}},
        {"heading": "Variables ಗೆ ಹೆಸರು ಇಡೋದು",
         "md": "Variable ಹೆಸರುಗಳು ಕೆಲವು ನಿಯಮ ಪಾಲಿಸುತ್ತವೆ:\n\n- **Letters, numbers ಮತ್ತು underscores** (`_`) ಮಾತ್ರ use ಮಾಡಿ, ಉದಾ: `dose_mg`, `patient2`.\n- **Number ಇಂದ ಶುರು ಮಾಡಬೇಡಿ**: `2nd_dose` ಆಗಲ್ಲ; `dose_2` ಸರಿ.\n- **Spaces ಬೇಡ**: `patient weight` ಅಲ್ಲ, `patient_weight` ಅಂತ ಬರೆಯಿರಿ.\n- ಹೆಸರುಗಳು **case-sensitive**: `weight` ಮತ್ತು `Weight` ಎರಡು ಬೇರೆ variables.\n- **Python ನ ಸ್ವಂತ ಪದಗಳನ್ನು use ಮಾಡಬೇಡಿ**, ಉದಾ: `True`, `if`, `for`. ಇವು ವಿಶೇಷ ಅರ್ಥ ಇರುವ **keywords**.\n\n**ಒಳ್ಳೆ ಅಭ್ಯಾಸ:** ಒಳಗೆ ಏನಿದೆ ಅಂತ ಹೇಳುವ ಹೆಸರುಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಿ, small letters ಮತ್ತು underscores ಜೊತೆ, ಉದಾ: `patient_weight_kg`. `x` ಅಥವಾ `a1` ತರಹದ ಹೆಸರುಗಳು code ಅನ್ನು ಆಮೇಲೆ ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳೋದನ್ನು ಕಷ್ಟ ಮಾಡುತ್ತವೆ."},
        {"heading": "ನಾಲ್ಕು basic data types",
         "md": "ಪ್ರತಿ value ಗೂ ಒಂದು **data type** ಇರುತ್ತೆ, ಅದು value ಯಾವ ರೀತಿಯದು ಅಂತ Python ಗೆ ಹೇಳುತ್ತೆ.\n\n| Data type | Python ಹೆಸರು | ಏನು ಇಡುತ್ತೆ | Pharmacy example |\n|---|---|---|---|\n| **Integer** | `int` | ಪೂರ್ಣ ಸಂಖ್ಯೆಗಳು | `tablets = 30` |\n| **Float** | `float` | ದಶಮಾಂಶ ಇರುವ ಸಂಖ್ಯೆಗಳು | `weight_kg = 52.5` |\n| **String** | `str` | Quotes ಒಳಗಿನ text | `drug = \"Amoxicillin\"` |\n| **Boolean** | `bool` | `True` ಅಥವಾ `False` ಮಾತ್ರ | `in_stock = True` |\n\nಗಮನಿಸಿ: `True` ಮತ್ತು `False` **capital letter** ಇಂದ ಶುರುವಾಗುತ್ತವೆ, ಮತ್ತು ಅವಕ್ಕೆ **quotes ಇಲ್ಲ**.",
         "callout": {"title": "Data type", "md": "Value ಯಾವ ರೀತಿಯದು: ಪೂರ್ಣ ಸಂಖ್ಯೆ (int), ದಶಮಾಂಶ ಸಂಖ್ಯೆ (float), text (str) ಅಥವಾ True/False (bool)."}},
        {"heading": "type() ಇಂದ type check ಮಾಡೋದು",
         "md": f"Value ನ type ಏನು ಅಂತ ಖಚಿತ ಇಲ್ವಾ? `type()` ಇಂದ Python ಅನ್ನೇ ಕೇಳಿ:\n\n{CODE_TYPE}\n\nಇದು print ಮಾಡೋದು:\n\n{OUT_TYPE}\n\nಮೂರನೇ line ಅನ್ನು ಗಮನವಿಟ್ಟು ನೋಡಿ: `\"500\"` **quotes** ನಲ್ಲಿದೆ, ಹಾಗಾಗಿ ಅದು **text**, number ಅಲ್ಲ."},
        {"heading": "Data types ಯಾಕೆ ಮುಖ್ಯ",
         "md": f"Python numbers ಮತ್ತು text ಜೊತೆ ತುಂಬಾ ಬೇರೆ ರೀತಿ ಕೆಲಸ ಮಾಡುತ್ತೆ. ಇವನ್ನು ಹೋಲಿಸಿ:\n\n{CODE_NUM}\n\n`1500` ಅಂತ print ಮಾಡುತ್ತೆ, ಆದರೆ\n\n{CODE_TXT}\n\n`500500500` ಅಂತ print ಮಾಡುತ್ತೆ. Text ಜೊತೆ `*` ಗುಣಿಸುವ ಬದಲು text ಅನ್ನು **ಮತ್ತೆ ಮತ್ತೆ ಬರೆಯುತ್ತೆ**.",
         "callout": {"title": "Pharmacy ಯಲ್ಲಿ ಇದು ತುಂಬಾ ಮುಖ್ಯ", "md": "ತಪ್ಪಾಗಿ text ಆಗಿ ಇಟ್ಟ number, 1500 mg dose ಅನ್ನು ಅರ್ಥವಿಲ್ಲದ 500500500 ಮಾಡಬಹುದು. Doses ಮತ್ತು ತೂಕಗಳು numbers ಆಗಿವೆಯಾ, strings ಅಲ್ಲವಾ ಅಂತ ಯಾವಾಗಲೂ check ಮಾಡಿ."}},
    ],
    "walkthrough": {
        "intro": "ಈ program ಒಬ್ಬ patient ನ details ಅನ್ನು variables ನಲ್ಲಿ ಇಟ್ಟು, ಆಮೇಲೆ ಅವನ್ನು use ಮಾಡುತ್ತೆ. ಪ್ರತಿ line run ಆಗುವಾಗ Variables panel ನೋಡಿ.",
        "keyTerms": [
            {"meaning": "ಬಲಭಾಗದ value ಅನ್ನು ಎಡಭಾಗದ variable ನಲ್ಲಿ ಇಡು."},
            {"meaning": "ಪೂರ್ಣ ಸಂಖ್ಯೆ / ದಶಮಾಂಶ ಇರುವ ಸಂಖ್ಯೆ."},
            {"meaning": "Quotes ಒಳಗಿನ text."},
            {"meaning": "True ಅಥವಾ False."},
        ],
    },
    "errors": {
        "intro": "Variables use ಮಾಡಲು ಶುರು ಮಾಡಿದಾಗ ಈ ಎರಡು errors ತುಂಬಾ ಸಾಮಾನ್ಯ.",
        "examples": [
            {"title": "ಇಲ್ಲದ ಹೆಸರನ್ನು use ಮಾಡೋದು",
             "md": "Variable ನ ಹೆಸರು `dose_mg`, ಆದರೆ line 2 `dose` ಅನ್ನು ಕೇಳುತ್ತಿದೆ. ನೀವು ತಯಾರಿಸಿದ ನಿಖರ ಹೆಸರುಗಳು ಮಾತ್ರ Python ಗೆ ಗೊತ್ತು. Spelling check ಮಾಡಿ, capital letters ಕೂಡ."},
            {"title": "Text ಮತ್ತು number ಅನ್ನು + ಇಂದ ಸೇರಿಸೋದು",
             "md": "`+` ಎರಡು strings ಅನ್ನು ಸೇರಿಸಬಹುದು, ಆದರೆ **string** ಮತ್ತು **integer** ಅನ್ನು ಅಲ್ಲ. ಸುಲಭದ fix: + ಬದಲು comma ಹಾಕಿ: `print(\"Dose:\", 500)`. ಇನ್ನೊಂದು fix ಅನ್ನು Lesson 1.4 ನಲ್ಲಿ ಕಲಿಯುತ್ತೀರಿ.",
             "callout": {"title": "TypeError", "md": "ಆ ಕೆಲಸಕ್ಕೆ ತಪ್ಪು data type ನ value use ಮಾಡಿದ್ದೀರಿ ಅನ್ನುವ error."}},
        ],
    },
    "mistakes": [
        {"mistake": "Variable ಹೆಸರಿನಲ್ಲಿ space ಹಾಕೋದು, ಉದಾ: `patient weight = 52`", "fix": "Underscore use ಮಾಡಿ: `patient_weight = 52`."},
        {"mistake": "ಹೆಸರನ್ನು number ಇಂದ ಶುರು ಮಾಡೋದು, ಉದಾ: `2nd_dose = 250`", "fix": "Number ಅನ್ನು ಆಮೇಲೆ ಹಾಕಿ: `dose_2 = 250`."},
        {"mistake": "ಹೆಸರಿನಲ್ಲಿ hyphen use ಮಾಡೋದು, ಉದಾ: `dose-mg = 500`", "fix": "Python `-` ಅನ್ನು minus ಅಂತ ಓದುತ್ತೆ. Underscore use ಮಾಡಿ: `dose_mg = 500`."},
        {"mistake": "`true` ಅನ್ನು small letters ನಲ್ಲಿ ಬರೆಯೋದು", "fix": "Booleans capital letter ಇಂದ ಶುರುವಾಗುತ್ತವೆ: `True`, `False`."},
        {"mistake": "Number ಅನ್ನು quotes ನಲ್ಲಿ ಇಡೋದು, ಉದಾ: `dose = \"500\"`", "see": "Error ಇಲ್ಲ, ಆದರೆ `dose * 3` ಕೊಡೋದು 500500500", "fix": "Numbers ಅನ್ನು quotes ಇಲ್ಲದೆ ಬರೆಯಿರಿ: `dose = 500`."},
    ],
    "tasks": [
        {"title": "Variables ಇಂದ label print ಮಾಡಿ", "md": "Variables ಸಿದ್ಧ ಇವೆ. **Variables use ಮಾಡಿ** ಔಷಧಿ ಮತ್ತು ಅದರ strength ಅನ್ನು print ಮಾಡುವ ಒಂದು line ಸೇರಿಸಿ, output ನಿಖರವಾಗಿ ಇದು ಆಗಬೇಕು:",
         "hints": ["print() commas ಇಂದ ಬೇರ್ಪಡಿಸಿದ ಹಲವು items ತೋರಿಸಬಹುದು.", "ಇದನ್ನು try ಮಾಡಿ: print(drug, strength_mg, \"mg\")."]},
        {"title": "ಮಗುವಿನ dose calculate ಮಾಡಿ", "md": "Rohan ನ ತೂಕ **18 kg**, ಮತ್ತು dose **ಪ್ರತಿ kg ಗೆ 15 mg**. ಹೆಸರು, ತೂಕ ಮತ್ತು ಪ್ರತಿ kg dose ಅನ್ನು `patient`, `weight_kg` ಮತ್ತು `dose_mg_per_kg` ಅನ್ನುವ variables ನಲ್ಲಿ ಇಟ್ಟು, ಆಮೇಲೆ print ಮಾಡಿ:\n\n*(ಕಲಿಕೆಗಾಗಿ ಮಾತ್ರ: ನಿಜವಾದ doses clinical guidelines ಪ್ರಕಾರವೇ ಇರಬೇಕು.)*",
         "hints": ["patient = \"Rohan\" ಹೆಸರನ್ನು ಇಡುತ್ತೆ. weight_kg ಮತ್ತು dose_mg_per_kg ಗೂ ಹೀಗೇ ಮಾಡಿ.", "Python ಇಂದಲೇ ಗುಣಿಸಿ: print(patient, \"needs\", weight_kg * dose_mg_per_kg, \"mg\")."]},
        {"title": "ಇದು ಯಾವ type?", "md": "`type()` use ಮಾಡಿ value `52.5` ನ data type ಅನ್ನು print ಮಾಡಿ. Output ನಿಖರವಾಗಿ ಇದು ಆಗಬೇಕು:",
         "hints": ["Value ಅನ್ನು type() ಒಳಗೆ, ಮತ್ತು type() ಅನ್ನು print() ಒಳಗೆ ಹಾಕಿ."]},
        {"title": "Bug ಹುಡುಕಿ", "md": "ಈ program `In stock: True` ಅಂತ print ಮಾಡಬೇಕು, ಆದರೆ ಇದರಲ್ಲಿ error ಇದೆ. ಸರಿ ಮಾಡಿ.",
         "hints": ["Python case-sensitive."], "solutionNote": "Booleans ಅನ್ನು True ಮತ್ತು False ಅಂತ, capital letter ಜೊತೆ ಬರೆಯುತ್ತಾರೆ."},
    ],
    "quiz": [
        {"q": "52.5 ನ data type ಏನು?", "why": "52.5 ನಲ್ಲಿ ದಶಮಾಂಶ ಇದೆ, ಹಾಗಾಗಿ ಅದು float."},
        {"q": "ಇವುಗಳಲ್ಲಿ ಯಾವುದು ಸರಿಯಾದ variable ಹೆಸರು?", "why": "ಹೆಸರಿನಲ್ಲಿ letters, numbers ಮತ್ತು underscores ಇರಬಹುದು, spaces ಅಥವಾ hyphens ಇರಬಾರದು, ಮತ್ತು number ಇಂದ ಶುರುವಾಗಬಾರದು."},
        {"q": "dose_mg = 500 ಏನು ಮಾಡುತ್ತೆ?", "options": ["dose_mg, 500 ಗೆ ಸಮವಾ ಅಂತ check ಮಾಡುತ್ತೆ", "500 ಅನ್ನು dose_mg ಅನ್ನುವ variable ನಲ್ಲಿ ಇಡುತ್ತೆ", "500 ಅನ್ನು print ಮಾಡುತ್ತೆ", "dose_mg ಗೆ 500 ಸೇರಿಸುತ್ತೆ"], "why": "= ಅಂದ್ರೆ ಇಡು: ಬಲಭಾಗದ value ಎಡಭಾಗದ variable ಗೆ ಹೋಗುತ್ತೆ."},
        {"q": "print(type(\"500\")) ಏನು ತೋರಿಸುತ್ತೆ?", "why": "\"500\" quotes ನಲ್ಲಿದೆ, ಹಾಗಾಗಿ ಅದು text (string), number ಅಲ್ಲ."},
        {"q": "in_stock = True. in_stock ನ data type ಏನು?", "why": "True ಮತ್ತು False booleans (bool)."},
    ],
    "exam": {"note": "University exam ಅನ್ನು English ನಲ್ಲಿ ಬರೆಯುತ್ತೀರಿ, ಹಾಗಾಗಿ model answers English ನಲ್ಲೇ ಇವೆ. ಇವು practice ಗಾಗಿ important questions; ನಿಜವಾದ university questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 1.3 · Variables ಮತ್ತು data types",
        "children": [
            {"label": "Variable", "children": [{"label": "Label ಇರುವ box"}, {"label": "name = value"}, {"label": "= ಅಂದ್ರೆ ಇಡು"}, {"label": "Value ಬದಲಾಗಬಹುದು"}]},
            {"label": "ಹೆಸರಿನ ನಿಯಮಗಳು", "children": [{"label": "Letters, numbers, _"}, {"label": "Number ಇಂದ ಶುರು ಬೇಡ"}, {"label": "Spaces ಬೇಡ"}, {"label": "Case-sensitive"}, {"label": "Keywords ಬೇಡ"}]},
            {"label": "Data types", "children": [{"label": "int: 30 tablets"}, {"label": "float: 52.5 kg"}, {"label": "str: \"Amoxicillin\""}, {"label": "bool: True / False"}]},
            {"label": "type()", "children": [{"label": "Data type ತೋರಿಸುತ್ತೆ"}, {"label": "\"500\" ಒಂದು str"}]},
            {"label": "ಯಾಕೆ ಮುಖ್ಯ", "children": [{"label": "500 * 3 = 1500"}, {"label": "\"500\" * 3 = 500500500"}]},
            {"label": "Errors", "children": [{"label": "NameError: ತಪ್ಪು ಹೆಸರು"}, {"label": "TypeError: text + number"}]},
        ],
    },
    "summary": [
        "**Variable** ಅಂದ್ರೆ **value** ಇಡುವ label ಇರುವ box; `=` ಅಂದ್ರೆ **ಇಡು**, ಸಮ ಅಲ್ಲ.",
        "ಹೆಸರುಗಳಲ್ಲಿ **letters, numbers ಮತ್ತು underscores** ಇರುತ್ತವೆ, number ಇಂದ ಶುರುವಾಗಲ್ಲ, spaces ಇರಲ್ಲ, ಮತ್ತು ಅವು **case-sensitive**.",
        "ನಾಲ್ಕು basic **data types**: **int** (30), **float** (52.5), **str** (\"Amoxicillin\") ಮತ್ತು **bool** (True / False).",
        "**`type()`** value ನ data type ತೋರಿಸುತ್ತೆ; quotes ನಲ್ಲಿರುವ ಎಲ್ಲವೂ **string**, \"500\" ಕೂಡ.",
        "Data types result ಅನ್ನು ಬದಲಾಯಿಸುತ್ತವೆ: `500 * 3` ಅಂದ್ರೆ 1500, ಆದರೆ `\"500\" * 3` ಅಂದ್ರೆ 500500500.",
    ],
}

# ------------------------------------------------------------ narration captions
NARR = {
    "hi": [
        "यह program एक patient की details variables में रखता है, और फिर उन्हें use करता है। हर line चलते समय Variables panel देखिए।",
        "पहली line एक comment है। यह बताती है कि program किस बारे में है।",
        "यहाँ equals sign का मतलब है रखो। Python, text Ananya को patient_name नाम के box में रखता है। यह quotes में है, इसलिए यह string है।",
        "weight_kg में बावन दशमलव पाँच रखा गया है। इसमें दशमलव है, इसलिए इसका data type float है।",
        "dose_mg_per_kg में दस रखा गया है, एक पूरी संख्या। इसका data type int है, यानी integer।",
        "in_stock में True रखा गया है, capital T के साथ। जो values सिर्फ True या False होती हैं, उन्हें booleans कहते हैं।",
        "अब print variables use करता है। Python हर box के अंदर देखकर values दिखाता है।",
        "Python बावन दशमलव पाँच को दस से गुणा करता है। इनमें से एक float है, इसलिए answer भी float है: पाँच सौ पच्चीस दशमलव शून्य।",
        "आखिर में Python boolean दिखाता है। आपने अभी चार अलग-अलग data types रखकर use किए।",
    ],
    "hinglish": [
        "Yeh program ek patient ki details variables mein rakhta hai, aur phir unhe use karta hai. Har line chalte samay Variables panel dekhiye.",
        "Pehli line ek comment hai. Yeh batati hai ki program kis baare mein hai.",
        "Yahan equals sign ka matlab hai rakho. Python, text Ananya ko patient_name naam ke box mein rakhta hai. Yeh quotes mein hai, isliye yeh string hai.",
        "weight_kg mein baavan dashamlav paanch rakha gaya hai. Isme dashamlav hai, isliye iska data type float hai.",
        "dose_mg_per_kg mein das rakha gaya hai, ek poori sankhya. Iska data type int hai, yaani integer.",
        "in_stock mein True rakha gaya hai, capital T ke saath. Jo values sirf True ya False hoti hain, unhe booleans kehte hain.",
        "Ab print variables use karta hai. Python har box ke andar dekhkar values dikhata hai.",
        "Python baavan dashamlav paanch ko das se guna karta hai. Inme se ek float hai, isliye answer bhi float hai: paanch sau pachchees dashamlav shoonya.",
        "Aakhir mein Python boolean dikhata hai. Aapne abhi chaar alag-alag data types rakhkar use kiye.",
    ],
    "kn": [
        "ಈ program ಒಬ್ಬ patient ನ details ಅನ್ನು variables ನಲ್ಲಿ ಇಟ್ಟು, ಆಮೇಲೆ ಅವನ್ನು use ಮಾಡುತ್ತೆ. ಪ್ರತಿ line run ಆಗುವಾಗ Variables panel ನೋಡಿ.",
        "ಮೊದಲ line ಒಂದು comment. Program ಯಾವುದರ ಬಗ್ಗೆ ಅಂತ ಅದು ಹೇಳುತ್ತೆ.",
        "ಇಲ್ಲಿ equals sign ಅಂದ್ರೆ ಇಡು. Python, Ananya ಅನ್ನುವ text ಅನ್ನು patient_name ಅನ್ನುವ box ನಲ್ಲಿ ಇಡುತ್ತೆ. ಅದು quotes ನಲ್ಲಿದೆ, ಹಾಗಾಗಿ ಅದು string.",
        "weight_kg ನಲ್ಲಿ ಐವತ್ತೆರಡು ದಶಮಾಂಶ ಐದು ಇಡಲಾಗಿದೆ. ಅದರಲ್ಲಿ ದಶಮಾಂಶ ಇದೆ, ಹಾಗಾಗಿ ಅದರ data type float.",
        "dose_mg_per_kg ನಲ್ಲಿ ಹತ್ತು ಇಡಲಾಗಿದೆ, ಒಂದು ಪೂರ್ಣ ಸಂಖ್ಯೆ. ಅದರ data type int, ಅಂದ್ರೆ integer.",
        "in_stock ನಲ್ಲಿ True ಇಡಲಾಗಿದೆ, capital T ಜೊತೆ. True ಅಥವಾ False ಮಾತ್ರ ಆಗಿರುವ values ಗೆ booleans ಅಂತಾರೆ.",
        "ಈಗ print variables ಅನ್ನು use ಮಾಡುತ್ತೆ. Python ಪ್ರತಿ box ಒಳಗೆ ನೋಡಿ values ತೋರಿಸುತ್ತೆ.",
        "Python ಐವತ್ತೆರಡು ದಶಮಾಂಶ ಐದನ್ನು ಹತ್ತರಿಂದ ಗುಣಿಸುತ್ತೆ. ಅದರಲ್ಲಿ ಒಂದು float, ಹಾಗಾಗಿ answer ಕೂಡ float: ಐನೂರ ಇಪ್ಪತ್ತೈದು ದಶಮಾಂಶ ಸೊನ್ನೆ.",
        "ಕೊನೆಗೆ Python boolean ತೋರಿಸುತ್ತೆ. ನೀವು ಈಗಷ್ಟೇ ನಾಲ್ಕು ಬೇರೆ ಬೇರೆ data types ಅನ್ನು ಇಟ್ಟು use ಮಾಡಿದ್ದೀರಿ.",
    ],
}
ANIM = {
    "hi": [
        "Variable, pharmacy की shelf पर रखे label लगे box जैसा है। Label उसका नाम है, और अंदर value है।",
        "अलग-अलग boxes अलग तरह की values रख सकते हैं: text, दशमलव वाली संख्या, या True या False।",
        "Python याद रखता है कि हर box में किस तरह की value है। इसे data type कहते हैं: int, str, float और bool।",
        "आप अंदर की चीज़ बदल सकते हैं। अब dose_mg box में पाँच सौ नहीं, साढ़े छह सौ है।",
        "जब आप नाम use करते हैं, Python box के अंदर देखकर अभी वाली value use करता है।",
    ],
    "hinglish": [
        "Variable, pharmacy ki shelf par rakhe label lage box jaisa hai. Label uska naam hai, aur andar value hai.",
        "Alag-alag boxes alag tarah ki values rakh sakte hain: text, dashamlav wali sankhya, ya True ya False.",
        "Python yaad rakhta hai ki har box mein kis tarah ki value hai. Ise data type kehte hain: int, str, float aur bool.",
        "Aap andar ki cheez badal sakte hain. Ab dose_mg box mein paanch sau nahi, saadhe chhe sau hai.",
        "Jab aap naam use karte hain, Python box ke andar dekhkar abhi wali value use karta hai.",
    ],
    "kn": [
        "Variable, pharmacy shelf ಮೇಲಿನ label ಇರುವ box ತರಹ. Label ಅದರ ಹೆಸರು, ಮತ್ತು ಒಳಗಿರೋದು value.",
        "ಬೇರೆ ಬೇರೆ boxes ಬೇರೆ ರೀತಿಯ values ಇಡಬಹುದು: text, ದಶಮಾಂಶ ಸಂಖ್ಯೆ, ಅಥವಾ True ಅಥವಾ False.",
        "ಪ್ರತಿ box ನಲ್ಲಿ ಯಾವ ರೀತಿಯ value ಇದೆ ಅಂತ Python ನೆನಪಿಟ್ಟುಕೊಳ್ಳುತ್ತೆ. ಇದನ್ನು data type ಅಂತಾರೆ: int, str, float ಮತ್ತು bool.",
        "ಒಳಗಿರುವುದನ್ನು ಬದಲಾಯಿಸಬಹುದು. ಈಗ dose_mg box ನಲ್ಲಿ ಐನೂರು ಅಲ್ಲ, ಆರುನೂರ ಐವತ್ತು ಇದೆ.",
        "ನೀವು ಹೆಸರು use ಮಾಡಿದಾಗ, Python box ಒಳಗೆ ನೋಡಿ ಈಗ ಇರುವ value ಅನ್ನು use ಮಾಡುತ್ತೆ.",
    ],
}
# Voice scripts: English words and code names in local script so the voices read them naturally
TTS = {
    "narrator": {
        "hi": [
            "यह प्रोग्राम एक पेशेंट की डिटेल्स वेरिएबल्स में रखता है, और फिर उन्हें यूज़ करता है। हर लाइन चलते समय वेरिएबल्स पैनल देखिए।",
            "पहली लाइन एक कमेंट है। यह बताती है कि प्रोग्राम किस बारे में है।",
            "यहाँ इक्वल्स साइन का मतलब है रखो। पाइथन, टेक्स्ट अनन्या को पेशेंट नेम नाम के बॉक्स में रखता है। यह कोट्स में है, इसलिए यह स्ट्रिंग है।",
            "वेट के जी में बावन दशमलव पाँच रखा गया है। इसमें दशमलव है, इसलिए इसका डेटा टाइप फ्लोट है।",
            "डोज़ एम जी पर के जी में दस रखा गया है, एक पूरी संख्या। इसका डेटा टाइप इंट है, यानी इंटीजर।",
            "इन स्टॉक में ट्रू रखा गया है, कैपिटल टी के साथ। जो वैल्यूज़ सिर्फ ट्रू या फॉल्स होती हैं, उन्हें बूलियन्स कहते हैं।",
            "अब प्रिंट वेरिएबल्स यूज़ करता है। पाइथन हर बॉक्स के अंदर देखकर वैल्यूज़ दिखाता है।",
            "पाइथन बावन दशमलव पाँच को दस से गुणा करता है। इनमें से एक फ्लोट है, इसलिए आंसर भी फ्लोट है: पाँच सौ पच्चीस दशमलव शून्य।",
            "आखिर में पाइथन बूलियन दिखाता है। आपने अभी चार अलग-अलग डेटा टाइप्स रखकर यूज़ किए।",
        ],
        "kn": [
            "ಈ ಪ್ರೋಗ್ರಾಮ್ ಒಬ್ಬ ಪೇಷೆಂಟ್ ನ ಡೀಟೇಲ್ಸ್ ಅನ್ನು ವೇರಿಯಬಲ್ಸ್ ನಲ್ಲಿ ಇಟ್ಟು, ಆಮೇಲೆ ಅವನ್ನು ಯೂಸ್ ಮಾಡುತ್ತೆ. ಪ್ರತಿ ಲೈನ್ ರನ್ ಆಗುವಾಗ ವೇರಿಯಬಲ್ಸ್ ಪ್ಯಾನೆಲ್ ನೋಡಿ.",
            "ಮೊದಲ ಲೈನ್ ಒಂದು ಕಾಮೆಂಟ್. ಪ್ರೋಗ್ರಾಮ್ ಯಾವುದರ ಬಗ್ಗೆ ಅಂತ ಅದು ಹೇಳುತ್ತೆ.",
            "ಇಲ್ಲಿ ಈಕ್ವಲ್ಸ್ ಸೈನ್ ಅಂದ್ರೆ ಇಡು. ಪೈಥಾನ್, ಅನನ್ಯಾ ಅನ್ನುವ ಟೆಕ್ಸ್ಟ್ ಅನ್ನು ಪೇಷೆಂಟ್ ನೇಮ್ ಅನ್ನುವ ಬಾಕ್ಸ್ ನಲ್ಲಿ ಇಡುತ್ತೆ. ಅದು ಕೋಟ್ಸ್ ನಲ್ಲಿದೆ, ಹಾಗಾಗಿ ಅದು ಸ್ಟ್ರಿಂಗ್.",
            "ವೇಟ್ ಕೆ ಜಿ ನಲ್ಲಿ ಐವತ್ತೆರಡು ದಶಮಾಂಶ ಐದು ಇಡಲಾಗಿದೆ. ಅದರಲ್ಲಿ ದಶಮಾಂಶ ಇದೆ, ಹಾಗಾಗಿ ಅದರ ಡೇಟಾ ಟೈಪ್ ಫ್ಲೋಟ್.",
            "ಡೋಸ್ ಎಮ್ ಜಿ ಪರ್ ಕೆ ಜಿ ನಲ್ಲಿ ಹತ್ತು ಇಡಲಾಗಿದೆ, ಒಂದು ಪೂರ್ಣ ಸಂಖ್ಯೆ. ಅದರ ಡೇಟಾ ಟೈಪ್ ಇಂಟ್, ಅಂದ್ರೆ ಇಂಟಿಜರ್.",
            "ಇನ್ ಸ್ಟಾಕ್ ನಲ್ಲಿ ಟ್ರೂ ಇಡಲಾಗಿದೆ, ಕ್ಯಾಪಿಟಲ್ ಟಿ ಜೊತೆ. ಟ್ರೂ ಅಥವಾ ಫಾಲ್ಸ್ ಮಾತ್ರ ಆಗಿರುವ ವ್ಯಾಲ್ಯೂಸ್ ಗೆ ಬೂಲಿಯನ್ಸ್ ಅಂತಾರೆ.",
            "ಈಗ ಪ್ರಿಂಟ್ ವೇರಿಯಬಲ್ಸ್ ಅನ್ನು ಯೂಸ್ ಮಾಡುತ್ತೆ. ಪೈಥಾನ್ ಪ್ರತಿ ಬಾಕ್ಸ್ ಒಳಗೆ ನೋಡಿ ವ್ಯಾಲ್ಯೂಸ್ ತೋರಿಸುತ್ತೆ.",
            "ಪೈಥಾನ್ ಐವತ್ತೆರಡು ದಶಮಾಂಶ ಐದನ್ನು ಹತ್ತರಿಂದ ಗುಣಿಸುತ್ತೆ. ಅದರಲ್ಲಿ ಒಂದು ಫ್ಲೋಟ್, ಹಾಗಾಗಿ ಆನ್ಸರ್ ಕೂಡ ಫ್ಲೋಟ್: ಐನೂರ ಇಪ್ಪತ್ತೈದು ದಶಮಾಂಶ ಸೊನ್ನೆ.",
            "ಕೊನೆಗೆ ಪೈಥಾನ್ ಬೂಲಿಯನ್ ತೋರಿಸುತ್ತೆ. ನೀವು ಈಗಷ್ಟೇ ನಾಲ್ಕು ಬೇರೆ ಬೇರೆ ಡೇಟಾ ಟೈಪ್ಸ್ ಅನ್ನು ಇಟ್ಟು ಯೂಸ್ ಮಾಡಿದ್ದೀರಿ.",
        ],
    },
    "anim-boxes": {
        "hi": [
            "वेरिएबल, फार्मेसी की शेल्फ पर रखे लेबल लगे बॉक्स जैसा है। लेबल उसका नाम है, और अंदर वैल्यू है।",
            "अलग-अलग बॉक्स अलग तरह की वैल्यूज़ रख सकते हैं: टेक्स्ट, दशमलव वाली संख्या, या ट्रू या फॉल्स।",
            "पाइथन याद रखता है कि हर बॉक्स में किस तरह की वैल्यू है। इसे डेटा टाइप कहते हैं: इंट, स्ट्र, फ्लोट और बूल।",
            "आप अंदर की चीज़ बदल सकते हैं। अब डोज़ एम जी बॉक्स में पाँच सौ नहीं, साढ़े छह सौ है।",
            "जब आप नाम यूज़ करते हैं, पाइथन बॉक्स के अंदर देखकर अभी वाली वैल्यू यूज़ करता है।",
        ],
        "kn": [
            "ವೇರಿಯಬಲ್, ಫಾರ್ಮಸಿ ಶೆಲ್ಫ್ ಮೇಲಿನ ಲೇಬಲ್ ಇರುವ ಬಾಕ್ಸ್ ತರಹ. ಲೇಬಲ್ ಅದರ ಹೆಸರು, ಮತ್ತು ಒಳಗಿರೋದು ವ್ಯಾಲ್ಯೂ.",
            "ಬೇರೆ ಬೇರೆ ಬಾಕ್ಸ್ ಗಳು ಬೇರೆ ರೀತಿಯ ವ್ಯಾಲ್ಯೂಸ್ ಇಡಬಹುದು: ಟೆಕ್ಸ್ಟ್, ದಶಮಾಂಶ ಸಂಖ್ಯೆ, ಅಥವಾ ಟ್ರೂ ಅಥವಾ ಫಾಲ್ಸ್.",
            "ಪ್ರತಿ ಬಾಕ್ಸ್ ನಲ್ಲಿ ಯಾವ ರೀತಿಯ ವ್ಯಾಲ್ಯೂ ಇದೆ ಅಂತ ಪೈಥಾನ್ ನೆನಪಿಟ್ಟುಕೊಳ್ಳುತ್ತೆ. ಇದನ್ನು ಡೇಟಾ ಟೈಪ್ ಅಂತಾರೆ: ಇಂಟ್, ಸ್ಟ್ರ್, ಫ್ಲೋಟ್ ಮತ್ತು ಬೂಲ್.",
            "ಒಳಗಿರುವುದನ್ನು ಬದಲಾಯಿಸಬಹುದು. ಈಗ ಡೋಸ್ ಎಮ್ ಜಿ ಬಾಕ್ಸ್ ನಲ್ಲಿ ಐನೂರು ಅಲ್ಲ, ಆರುನೂರ ಐವತ್ತು ಇದೆ.",
            "ನೀವು ಹೆಸರು ಯೂಸ್ ಮಾಡಿದಾಗ, ಪೈಥಾನ್ ಬಾಕ್ಸ್ ಒಳಗೆ ನೋಡಿ ಈಗ ಇರುವ ವ್ಯಾಲ್ಯೂ ಅನ್ನು ಯೂಸ್ ಮಾಡುತ್ತೆ.",
        ],
    },
}


def say_en(text):
    """English voice script: spell out code names so the voice reads them naturally."""
    text = re.sub(r"\b(\w+)_mg_per_kg\b", r"\1 M G per K G", text)
    text = re.sub(r"\b(\w+)_kg\b", r"\1 K G", text)
    text = re.sub(r"\b(\w+)_mg\b", r"\1 M G", text)
    text = re.sub(r"\b([a-z]+)_([a-z]+)\b", r"\1 \2", text)
    return text.replace("int, str, float", "int, string, float")


if __name__ == "__main__":
    en = json.load(open(os.path.join(ROOT, "content", "bp101t", "1-3", "en.json"), encoding="utf-8"))
    for lang, data in T.items():
        doc = dict(data)
        doc["walkthrough"] = dict(doc["walkthrough"], steps=[{"say": s} for s in NARR[lang]])
        doc["animations"] = [{"steps": [{"say": s} for s in ANIM[lang]]}]
        doc["translatedSections"] = SECTIONS
        path = os.path.join(ROOT, "content", "bp101t", "1-3", f"{lang}.json")
        json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("wrote", path)

    narr_en = [s["say"] for s in en["walkthrough"]["steps"]]
    anim_en = [s["say"] for s in en["animations"][0]["steps"]]
    script = {
        "course": "bp101t", "lesson": "1-3",
        "voices": {"en": "Mary", "hi": "Rani", "kn": "Anu"},
        "tracks": [
            {"id": "narrator", "prefix": "step-", "lang": "en", "tts": [say_en(t) for t in narr_en], "display": narr_en},
            {"id": "narrator", "prefix": "step-", "lang": "hi", "tts": TTS["narrator"]["hi"], "display": NARR["hi"], "displayHinglish": NARR["hinglish"]},
            {"id": "narrator", "prefix": "step-", "lang": "kn", "tts": TTS["narrator"]["kn"], "display": NARR["kn"]},
            {"id": "anim-boxes", "prefix": "anim-boxes-", "lang": "en", "tts": [say_en(t) for t in anim_en], "display": anim_en},
            {"id": "anim-boxes", "prefix": "anim-boxes-", "lang": "hi", "tts": TTS["anim-boxes"]["hi"], "display": ANIM["hi"], "displayHinglish": ANIM["hinglish"]},
            {"id": "anim-boxes", "prefix": "anim-boxes-", "lang": "kn", "tts": TTS["anim-boxes"]["kn"], "display": ANIM["kn"]},
        ],
    }
    path = os.path.join(ROOT, "scripts", "bp101t", "1-3.json")
    json.dump(script, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", path)
    # keep the "Words to know" section after regenerating
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "..", "glossary_bp101t.py")], check=True)

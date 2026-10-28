"""Lesson 1.4 translations (Hindi, Hinglish, Kannada) and voice scripts.

Run to write content/bp101t/1-4/{hi,hinglish,kn}.json and scripts/bp101t/1-4.json.
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

TABLE_CAST = {
    "hi": "| क्या चाहिए | लिखिए | Result |\n|---|---|---|\n| integer | `int(\"500\")` | `500` |\n| float | `float(\"52.5\")` | `52.5` |\n| string | `str(500)` | `\"500\"` |",
    "hinglish": "| Kya chahiye | Likhiye | Result |\n|---|---|---|\n| integer | `int(\"500\")` | `500` |\n| float | `float(\"52.5\")` | `52.5` |\n| string | `str(500)` | `\"500\"` |",
    "kn": "| ಏನು ಬೇಕು | ಬರೆಯಿರಿ | Result |\n|---|---|---|\n| integer | `int(\"500\")` | `500` |\n| float | `float(\"52.5\")` | `52.5` |\n| string | `str(500)` | `\"500\"` |",
}
CODE_CAST = "```python\nstrength = \"500\"\nprint(int(strength) * 3)\n```"
CODE_STR = "```python\nprint(\"Dose: \" + str(500) + \" mg\")\n```"
CODE_INT = "```python\nprint(int(2.9))\n```"
CODE_MIX = "```python\nprint(10 + 2.5)\n```"
CODE_STRIPS = "```python\nprint(25 // 10)\nprint(25 % 10)\n```"
CODE_CMP = "```python\ndaily_dose_mg = 4500\nprint(daily_dose_mg > 4000)\n```"
CODE_LOGIC = "```python\nage = 16\nweight_kg = 52\nprint(age >= 18 and weight_kg >= 50)\nprint(age >= 18 or weight_kg >= 50)\n```"
CODE_SHORT = "```python\nstock = 100\nstock -= 30\nprint(stock)\n```"
CODE_ORDER = "```python\nprint(98 + 102 / 2)\nprint((98 + 102) / 2)\n```"


def arith_table(meaning):
    rows = [("+", "500 + 250", "750"), ("-", "30 - 12", "18"), ("*", "500 * 3", "1500"), ("/", "10 / 4", "2.5"),
            ("//", "25 // 10", "2"), ("%", "25 % 10", "5"), ("**", "2 ** 3", "8")]
    head = meaning["head"]
    out = f"| Operator | {head[0]} | {head[1]} | Result |\n|---|---|---|---|\n"
    return out + "\n".join(f"| `{o}` | {m} | `{e}` | `{r}` |" for (o, e, r), m in zip(rows, meaning["rows"]))


def cmp_table(head, questions):
    ops = ["==", "!=", ">", "<", ">=", "<="]
    return f"| Operator | {head} |\n|---|---|\n" + "\n".join(f"| `{o}` | {q} |" for o, q in zip(ops, questions))


T = {}

# ======================================================================= Hindi
T["hi"] = {
    "hook": {
        "title": "इस patient को कितनी strips चाहिए?",
        "md": "Doctor ने लिखा है: **2 tablets, दिन में 3 बार, 7 दिन तक**। Tablets 10 की strip में आती हैं। आप कितनी strips देंगे?\n\nइस lesson के अंत तक Python आपके लिए यह answer निकालेगा। आप values को एक data type से दूसरे में **बदलना** सीखेंगे, और Python के **operators** से calculate और compare करना सीखेंगे।",
    },
    "learn": [
        "किसी value को एक data type से दूसरे में **बदलना**, जिसे **type casting** कहते हैं",
        "Calculation के लिए **arithmetic operators**, `//` और `%` के साथ",
        "**Comparison** और **logical** operators, जो **True** या **False** answer देते हैं",
        "Python किस **क्रम** में calculate करता है, और **brackets** उसे कैसे बदलते हैं",
    ],
    "explanation": [
        {"heading": "Data types के बीच बदलना",
         "md": f"Values अक्सर **text** के रूप में आती हैं, जैसे label से पढ़ी गई strength: `\"500\"`। Python text से calculate नहीं कर सकता, इसलिए पहले उसे number में **बदलना** पड़ता है। इसे **type casting** कहते हैं।\n\n{TABLE_CAST['hi']}\n\n{CODE_CAST}\n\nयह `1500` print करता है। `int()` के बिना आपको `500500500` मिलता।\n\nLesson 1.3 वाला error याद है, जहाँ `+` text और number को नहीं जोड़ पाया था? `str()` उसे ठीक करता है:\n\n{CODE_STR}\n\nयह `Dose: 500 mg` print करता है।",
         "callout": {"title": "Type casting", "md": "किसी value को एक data type से दूसरे में बदलना, int(), float() या str() से।"}},
        {"heading": "बदलते समय दो बातें ध्यान रखिए",
         "md": f"**1. `int()` दशमलव वाला हिस्सा काट देता है। Round नहीं करता।**\n\n{CODE_INT}\n\nयह `2` print करता है, 3 नहीं।\n\n**2. Python कभी-कभी खुद बदल देता है।** जब आप integer और float मिलाते हैं, तो answer float होता है:\n\n{CODE_MIX}\n\nयह `12.5` print करता है। ऐसे अपने-आप बदलने को **implicit conversion** कहते हैं। `int()`, `float()` या `str()` से खुद बदलना **explicit conversion** है।"},
        {"heading": "Arithmetic operators",
         "md": "**Operator** एक symbol है जो values के साथ कुछ करता है, जैसे `+` या `*`। ये Python के **arithmetic operators** हैं:\n\n"
               + arith_table({"head": ["मतलब", "Example"], "rows": ["जोड़ना", "घटाना", "गुणा", "भाग", "भाग, सिर्फ पूरी संख्या", "शेषफल (remainder)", "घात (power)"]})
               + f"\n\nPharmacy में `//` और `%` बहुत काम आते हैं। **25 tablets** और **10 प्रति strip** के साथ:\n\n{CODE_STRIPS}\n\nयह `2` (पूरी strips) और `5` (खुली tablets) print करता है।\n\nध्यान दीजिए: `/` हमेशा float देता है, पूरा भाग होने पर भी: `10 / 2` है `5.0`।",
         "callout": {"title": "Operator", "md": "एक symbol जो values के साथ कुछ करता है, जैसे + (जोड़ना) या > (बड़ा है)।"}},
        {"heading": "Comparison operators: हाँ-या-ना वाले सवाल",
         "md": "**Comparison operators** दो values की तुलना करते हैं। Answer हमेशा boolean होता है: `True` या `False`।\n\n"
               + cmp_table("कौन सा सवाल पूछता है", ["बराबर?", "बराबर नहीं?", "बड़ा है?", "छोटा है?", "बड़ा या बराबर?", "छोटा या बराबर?"])
               + f"\n\n{CODE_CMP}\n\nयह `True` print करता है: dose 4000 mg से ज़्यादा है।",
         "callout": {"title": "= और == अलग हैं", "md": "एक = value रखता है। दो == दो values की तुलना करते हैं। इन्हें मिला देना beginners की सबसे आम गलतियों में से एक है।"}},
        {"heading": "Logical operators: and, or, not",
         "md": f"**Logical operators** True/False answers को जोड़ते हैं:\n\n- `and`: **True** सिर्फ तब, जब **दोनों** तरफ True हो\n- `or`: **True** तब, जब **कम से कम एक** तरफ True हो\n- `not`: True को False, और False को True कर देता है\n\n{CODE_LOGIC}\n\nयह पहले `False` print करता है (patient 18 या उससे ज़्यादा का नहीं है), फिर `True` (वज़न 50 kg या उससे ज़्यादा है)।"},
        {"heading": "Shortcuts, और calculation का क्रम",
         "md": f"**Shortcut operators** किसी variable को उसकी अपनी value से बदलते हैं:\n\n{CODE_SHORT}\n\nयह `70` print करता है। `stock -= 30`, `stock = stock - 30` लिखने का छोटा तरीका है। इसी तरह `+=` जोड़ता है और `*=` गुणा करता है।\n\n**Calculation का क्रम:** गणित की तरह, Python पहले `**` करता है, फिर `*`, `/`, `//` और `%`, फिर `+` और `-`। **Brackets सबसे पहले।**\n\n{CODE_ORDER}\n\nयह पहले `149.0`, फिर `100.0` print करता है। सिर्फ दूसरा ही दो readings, 98 और 102, का average है।",
         "callout": {"title": "शक हो तो brackets लगाइए", "md": "Brackets से dose formulas पढ़ने वाले हर किसी को साफ़ समझ आते हैं, और Python उस क्रम में calculate नहीं करता जो आप नहीं चाहते थे।"}},
    ],
    "walkthrough": {
        "intro": "यह program निकालता है कि 7 दिन के course में कितनी tablets लगेंगी, और कितनी strips देनी हैं। हर line चलते समय Variables panel देखिए।",
        "keyTerms": [
            {"meaning": "Text \"2\" को number 2 में बदलो।"},
            {"meaning": "भाग देकर सिर्फ पूरी संख्या रखो।"},
            {"meaning": "भाग देने के बाद बचा हुआ।"},
            {"meaning": "बड़ा या बराबर। True या False देता है।"},
        ],
    },
    "errors": {
        "intro": "Values बदलते और calculate करते समय ये दो errors आम हैं।",
        "examples": [
            {"title": "ऐसा text बदलना जो पूरी संख्या नहीं है",
             "md": "`int()` सिर्फ उसी text को बदल सकता है जो **पूरी संख्या** जैसा दिखे। `\"52.5\"` में दशमलव है, इसलिए `float(\"52.5\")` use कीजिए। `\"fifty\"` जैसा text तो बदला ही नहीं जा सकता।",
             "callout": {"title": "ValueError", "md": "Error जिसका मतलब है कि value का data type सही है, लेकिन उसे use नहीं किया जा सकता, जैसे int(\"52.5\")।"}},
            {"title": "शून्य से भाग देना",
             "md": "किसी भी चीज़ को शून्य से भाग नहीं दिया जा सकता, न गणित में, न Python में। Check कीजिए कि जिस number से आप भाग दे रहे हैं, वो कभी 0 न हो, जैसे दिनों की संख्या।"},
        ],
    },
    "mistakes": [
        {"mistake": "Compare करने के लिए `=` use करना, जैसे `print(dose = 500)`", "fix": "दो equals signs से compare कीजिए: `print(dose == 500)`।"},
        {"mistake": "Text और number को `+` से जोड़ना, जैसे `\"Total: \" + 42`", "fix": "पहले number को बदलिए: `\"Total: \" + str(42)`।"},
        {"mistake": "`int()` से round होने की उम्मीद करना, जैसे `int(2.9)`", "see": "कोई error नहीं, लेकिन result 2 है", "fix": "`int()` दशमलव वाला हिस्सा काट देता है। Round करने के लिए `round(2.9)` use कीजिए, जो 3 देता है।"},
        {"mistake": "`/` से पूरी संख्या की उम्मीद करना, जैसे `10 / 2`", "see": "कोई error नहीं, लेकिन result 5.0 है", "fix": "पूरी संख्या चाहिए तो `//` use कीजिए: `10 // 2` देता है 5।"},
        {"mistake": "Average में brackets भूल जाना, जैसे `98 + 102 / 2`", "see": "कोई error नहीं, लेकिन result 149.0 है", "fix": "Brackets लगाइए: `(98 + 102) / 2` देता है 100.0।"},
    ],
    "tasks": [
        {"title": "पहले बदलिए, फिर calculate कीजिए", "md": "Strength label से पढ़ी गई है, इसलिए यह text है। इसे number में बदलिए और strength का **दोगुना** print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["int(strength) text को number बनाता है।", "Try कीजिए: print(int(strength) * 2)।"]},
        {"title": "Strips और खुली tablets", "md": "**45 tablets** हैं, और हर strip में **10** आती हैं। `//` और `%` use करके print कीजिए:",
         "hints": ["total // 10 पूरी strips देता है।", "total % 10 बची हुई tablets देता है।", "print(\"Strips:\", total // 10, \"Loose:\", total % 10)"]},
        {"title": "क्या dose limit से ज़्यादा है?", "md": "Maximum daily dose **4000 mg** है। Print कीजिए कि `daily_dose_mg` limit से **बड़ा** है या नहीं। Output बिल्कुल यह होना चाहिए:\n\n*(सिर्फ सीखने के लिए: असली limits clinical guidelines के अनुसार ही होनी चाहिए।)*",
         "hints": ["> पूछता है \"बड़ा है?\" और True या False देता है।", "print(\"Over the limit:\", daily_dose_mg > limit_mg)"]},
        {"title": "Bug ढूँढिए", "md": "यह program `Total: 42` print करना चाहिए, लेकिन इसमें error है। इसे **`str()` use करके** ठीक कीजिए।",
         "hints": ["+ text और number को नहीं जोड़ सकता।", "str(total) से number को text में बदलिए।"],
         "solutionNote": "str(total), 42 को text \"42\" बना देता है, इसलिए + दोनों strings को जोड़ पाता है।"},
    ],
    "quiz": [
        {"q": "print(int(\"500\") + 5) क्या दिखाता है?", "why": "int(\"500\") text को number 500 बनाता है, इसलिए answer 505 है।"},
        {"q": "17 // 5 कितना है?", "why": "// भाग देकर सिर्फ पूरी संख्या रखता है: 17 में 5 तीन बार जाता है, कुछ बच जाता है।"},
        {"q": "17 % 5 कितना है?", "why": "% शेषफल देता है: 17 में 5 तीन बार (15) जाता है, 2 बचता है।"},
        {"q": "print(4500 > 4000) क्या दिखाता है?", "why": "4500, 4000 से बड़ा है, इसलिए comparison True देता है।"},
        {"q": "age = 16। print(age >= 18 and age <= 60) क्या दिखाता है?", "why": "and में दोनों तरफ True होना ज़रूरी है। 16, 18 या उससे ज़्यादा नहीं है, इसलिए answer False है।"},
        {"q": "98 और 102 का average कौन सा देता है?", "why": "Brackets की वजह से Python पहले जोड़ता है, फिर भाग देता है: 200 / 2 = 100.0।"},
    ],
    "exam": {"note": "University exam English में लिखा जाता है, इसलिए model answers English में ही रखे गए हैं। ये practice के लिए important questions हैं; असली university questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 1.4 · Type casting और operators",
        "children": [
            {"label": "Type casting", "children": [{"label": "int(\"500\") → 500"}, {"label": "float(\"52.5\") → 52.5"}, {"label": "str(500) → \"500\""}, {"label": "int(2.9) → 2"}]},
            {"label": "Arithmetic", "children": [{"label": "+  -  *  /"}, {"label": "// पूरी संख्या"}, {"label": "% शेषफल"}, {"label": "** घात"}]},
            {"label": "Comparison", "children": [{"label": "==  !="}, {"label": ">  <  >=  <="}, {"label": "True / False देता है"}]},
            {"label": "Logical", "children": [{"label": "and: दोनों True"}, {"label": "or: कम से कम एक"}, {"label": "not: उलट देता है"}]},
            {"label": "क्रम", "children": [{"label": "Brackets पहले"}, {"label": "** फिर * / // %"}, {"label": "फिर + -"}]},
            {"label": "Errors", "children": [{"label": "ValueError: int(\"52.5\")"}, {"label": "ZeroDivisionError"}]},
        ],
    },
    "summary": [
        "**Type casting** values बदलता है: `int(\"500\")` देता है 500, `float(\"52.5\")` देता है 52.5 और `str(500)` देता है \"500\"।",
        "`int()` दशमलव वाला हिस्सा **काट** देता है (round नहीं करता), और int के साथ float मिलाने पर answer **float** होता है।",
        "**Arithmetic operators** calculate करते हैं: `//` पूरी संख्या रखता है और `%` शेषफल देता है, strips और खुली tablets के लिए एकदम सही।",
        "**Comparison operators** (`==`, `!=`, `>`, `<`, `>=`, `<=`) और **logical operators** (`and`, `or`, `not`) **True** या **False** देते हैं।",
        "Python पहले `**`, फिर `* / // %`, फिर `+ -` करता है; **brackets** सबसे पहले।",
    ],
}

# ===================================================================== Hinglish
T["hinglish"] = {
    "hook": {
        "title": "Is patient ko kitni strips chahiye?",
        "md": "Doctor ne likha hai: **2 tablets, din mein 3 baar, 7 din tak**. Tablets 10 ki strip mein aati hain. Aap kitni strips denge?\n\nIs lesson ke end tak Python aapke liye yeh answer nikalega. Aap values ko ek data type se doosre mein **badalna** seekhenge, aur Python ke **operators** se calculate aur compare karna seekhenge.",
    },
    "learn": [
        "Kisi value ko ek data type se doosre mein **badalna**, jise **type casting** kehte hain",
        "Calculation ke liye **arithmetic operators**, `//` aur `%` ke saath",
        "**Comparison** aur **logical** operators, jo **True** ya **False** answer dete hain",
        "Python kis **kram** mein calculate karta hai, aur **brackets** use kaise badalte hain",
    ],
    "explanation": [
        {"heading": "Data types ke beech badalna",
         "md": f"Values aksar **text** ke roop mein aati hain, jaise label se padhi gayi strength: `\"500\"`. Python text se calculate nahi kar sakta, isliye pehle use number mein **badalna** padta hai. Ise **type casting** kehte hain.\n\n{TABLE_CAST['hinglish']}\n\n{CODE_CAST}\n\nYeh `1500` print karta hai. `int()` ke bina aapko `500500500` milta.\n\nLesson 1.3 wala error yaad hai, jahan `+` text aur number ko nahi jod paaya tha? `str()` use theek karta hai:\n\n{CODE_STR}\n\nYeh `Dose: 500 mg` print karta hai.",
         "callout": {"title": "Type casting", "md": "Kisi value ko ek data type se doosre mein badalna, int(), float() ya str() se."}},
        {"heading": "Badalte samay do baatein dhyan rakhiye",
         "md": f"**1. `int()` dashamlav wala hissa kaat deta hai. Round nahi karta.**\n\n{CODE_INT}\n\nYeh `2` print karta hai, 3 nahi.\n\n**2. Python kabhi-kabhi khud badal deta hai.** Jab aap integer aur float milaate hain, to answer float hota hai:\n\n{CODE_MIX}\n\nYeh `12.5` print karta hai. Aise apne-aap badalne ko **implicit conversion** kehte hain. `int()`, `float()` ya `str()` se khud badalna **explicit conversion** hai."},
        {"heading": "Arithmetic operators",
         "md": "**Operator** ek symbol hai jo values ke saath kuch karta hai, jaise `+` ya `*`. Yeh Python ke **arithmetic operators** hain:\n\n"
               + arith_table({"head": ["Matlab", "Example"], "rows": ["Jodna", "Ghatana", "Guna", "Bhaag", "Bhaag, sirf poori sankhya", "Sheshphal (remainder)", "Ghaat (power)"]})
               + f"\n\nPharmacy mein `//` aur `%` bahut kaam aate hain. **25 tablets** aur **10 per strip** ke saath:\n\n{CODE_STRIPS}\n\nYeh `2` (poori strips) aur `5` (khuli tablets) print karta hai.\n\nDhyan dijiye: `/` hamesha float deta hai, poora bhaag hone par bhi: `10 / 2` hai `5.0`.",
         "callout": {"title": "Operator", "md": "Ek symbol jo values ke saath kuch karta hai, jaise + (jodna) ya > (bada hai)."}},
        {"heading": "Comparison operators: haan-ya-na wale sawaal",
         "md": "**Comparison operators** do values ki tulna karte hain. Answer hamesha boolean hota hai: `True` ya `False`.\n\n"
               + cmp_table("Kaun sa sawaal poochta hai", ["Barabar?", "Barabar nahi?", "Bada hai?", "Chhota hai?", "Bada ya barabar?", "Chhota ya barabar?"])
               + f"\n\n{CODE_CMP}\n\nYeh `True` print karta hai: dose 4000 mg se zyada hai.",
         "callout": {"title": "= aur == alag hain", "md": "Ek = value rakhta hai. Do == do values ki tulna karte hain. Inhe mila dena beginners ki sabse aam galtiyon mein se ek hai."}},
        {"heading": "Logical operators: and, or, not",
         "md": f"**Logical operators** True/False answers ko jodte hain:\n\n- `and`: **True** sirf tab, jab **dono** taraf True ho\n- `or`: **True** tab, jab **kam se kam ek** taraf True ho\n- `not`: True ko False, aur False ko True kar deta hai\n\n{CODE_LOGIC}\n\nYeh pehle `False` print karta hai (patient 18 ya usse zyada ka nahi hai), phir `True` (wazan 50 kg ya usse zyada hai)."},
        {"heading": "Shortcuts, aur calculation ka kram",
         "md": f"**Shortcut operators** kisi variable ko uski apni value se badalte hain:\n\n{CODE_SHORT}\n\nYeh `70` print karta hai. `stock -= 30`, `stock = stock - 30` likhne ka chhota tareeka hai. Isi tarah `+=` jodta hai aur `*=` guna karta hai.\n\n**Calculation ka kram:** maths ki tarah, Python pehle `**` karta hai, phir `*`, `/`, `//` aur `%`, phir `+` aur `-`. **Brackets sabse pehle.**\n\n{CODE_ORDER}\n\nYeh pehle `149.0`, phir `100.0` print karta hai. Sirf doosra hi do readings, 98 aur 102, ka average hai.",
         "callout": {"title": "Shak ho to brackets lagaiye", "md": "Brackets se dose formulas padhne wale har kisi ko saaf samajh aate hain, aur Python us kram mein calculate nahi karta jo aap nahi chahte the."}},
    ],
    "walkthrough": {
        "intro": "Yeh program nikalta hai ki 7 din ke course mein kitni tablets lagengi, aur kitni strips deni hain. Har line chalte samay Variables panel dekhiye.",
        "keyTerms": [
            {"meaning": "Text \"2\" ko number 2 mein badlo."},
            {"meaning": "Bhaag dekar sirf poori sankhya rakho."},
            {"meaning": "Bhaag dene ke baad bacha hua."},
            {"meaning": "Bada ya barabar. True ya False deta hai."},
        ],
    },
    "errors": {
        "intro": "Values badalte aur calculate karte samay yeh do errors aam hain.",
        "examples": [
            {"title": "Aisa text badalna jo poori sankhya nahi hai",
             "md": "`int()` sirf usi text ko badal sakta hai jo **poori sankhya** jaisa dikhe. `\"52.5\"` mein dashamlav hai, isliye `float(\"52.5\")` use kijiye. `\"fifty\"` jaisa text to badla hi nahi ja sakta.",
             "callout": {"title": "ValueError", "md": "Error jiska matlab hai ki value ka data type sahi hai, lekin use use nahi kiya ja sakta, jaise int(\"52.5\")."}},
            {"title": "Shoonya se bhaag dena",
             "md": "Kisi bhi cheez ko shoonya se bhaag nahi diya ja sakta, na maths mein, na Python mein. Check kijiye ki jis number se aap bhaag de rahe hain, woh kabhi 0 na ho, jaise dinon ki sankhya."},
        ],
    },
    "mistakes": [
        {"mistake": "Compare karne ke liye `=` use karna, jaise `print(dose = 500)`", "fix": "Do equals signs se compare kijiye: `print(dose == 500)`."},
        {"mistake": "Text aur number ko `+` se jodna, jaise `\"Total: \" + 42`", "fix": "Pehle number ko badliye: `\"Total: \" + str(42)`."},
        {"mistake": "`int()` se round hone ki ummeed karna, jaise `int(2.9)`", "see": "Koi error nahi, lekin result 2 hai", "fix": "`int()` dashamlav wala hissa kaat deta hai. Round karne ke liye `round(2.9)` use kijiye, jo 3 deta hai."},
        {"mistake": "`/` se poori sankhya ki ummeed karna, jaise `10 / 2`", "see": "Koi error nahi, lekin result 5.0 hai", "fix": "Poori sankhya chahiye to `//` use kijiye: `10 // 2` deta hai 5."},
        {"mistake": "Average mein brackets bhool jaana, jaise `98 + 102 / 2`", "see": "Koi error nahi, lekin result 149.0 hai", "fix": "Brackets lagaiye: `(98 + 102) / 2` deta hai 100.0."},
    ],
    "tasks": [
        {"title": "Pehle badliye, phir calculate kijiye", "md": "Strength label se padhi gayi hai, isliye yeh text hai. Ise number mein badliye aur strength ka **dogna** print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["int(strength) text ko number banata hai.", "Try kijiye: print(int(strength) * 2)."]},
        {"title": "Strips aur khuli tablets", "md": "**45 tablets** hain, aur har strip mein **10** aati hain. `//` aur `%` use karke print kijiye:",
         "hints": ["total // 10 poori strips deta hai.", "total % 10 bachi hui tablets deta hai.", "print(\"Strips:\", total // 10, \"Loose:\", total % 10)"]},
        {"title": "Kya dose limit se zyada hai?", "md": "Maximum daily dose **4000 mg** hai. Print kijiye ki `daily_dose_mg` limit se **bada** hai ya nahi. Output bilkul yeh hona chahiye:\n\n*(Sirf seekhne ke liye: asli limits clinical guidelines ke anusaar hi honi chahiye.)*",
         "hints": ["> poochta hai \"bada hai?\" aur True ya False deta hai.", "print(\"Over the limit:\", daily_dose_mg > limit_mg)"]},
        {"title": "Bug dhoondhiye", "md": "Yeh program `Total: 42` print karna chahiye, lekin isme error hai. Ise **`str()` use karke** theek kijiye.",
         "hints": ["+ text aur number ko nahi jod sakta.", "str(total) se number ko text mein badliye."],
         "solutionNote": "str(total), 42 ko text \"42\" bana deta hai, isliye + dono strings ko jod paata hai."},
    ],
    "quiz": [
        {"q": "print(int(\"500\") + 5) kya dikhata hai?", "why": "int(\"500\") text ko number 500 banata hai, isliye answer 505 hai."},
        {"q": "17 // 5 kitna hai?", "why": "// bhaag dekar sirf poori sankhya rakhta hai: 17 mein 5 teen baar jaata hai, kuch bach jaata hai."},
        {"q": "17 % 5 kitna hai?", "why": "% sheshphal deta hai: 17 mein 5 teen baar (15) jaata hai, 2 bachta hai."},
        {"q": "print(4500 > 4000) kya dikhata hai?", "why": "4500, 4000 se bada hai, isliye comparison True deta hai."},
        {"q": "age = 16. print(age >= 18 and age <= 60) kya dikhata hai?", "why": "and mein dono taraf True hona zaroori hai. 16, 18 ya usse zyada nahi hai, isliye answer False hai."},
        {"q": "98 aur 102 ka average kaun sa deta hai?", "why": "Brackets ki wajah se Python pehle jodta hai, phir bhaag deta hai: 200 / 2 = 100.0."},
    ],
    "exam": {"note": "University exam English mein likha jaata hai, isliye model answers English mein hi rakhe gaye hain. Yeh practice ke liye important questions hain; asli university questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 1.4 · Type casting aur operators",
        "children": [
            {"label": "Type casting", "children": [{"label": "int(\"500\") → 500"}, {"label": "float(\"52.5\") → 52.5"}, {"label": "str(500) → \"500\""}, {"label": "int(2.9) → 2"}]},
            {"label": "Arithmetic", "children": [{"label": "+  -  *  /"}, {"label": "// poori sankhya"}, {"label": "% sheshphal"}, {"label": "** ghaat"}]},
            {"label": "Comparison", "children": [{"label": "==  !="}, {"label": ">  <  >=  <="}, {"label": "True / False deta hai"}]},
            {"label": "Logical", "children": [{"label": "and: dono True"}, {"label": "or: kam se kam ek"}, {"label": "not: ulat deta hai"}]},
            {"label": "Kram", "children": [{"label": "Brackets pehle"}, {"label": "** phir * / // %"}, {"label": "phir + -"}]},
            {"label": "Errors", "children": [{"label": "ValueError: int(\"52.5\")"}, {"label": "ZeroDivisionError"}]},
        ],
    },
    "summary": [
        "**Type casting** values badalta hai: `int(\"500\")` deta hai 500, `float(\"52.5\")` deta hai 52.5 aur `str(500)` deta hai \"500\".",
        "`int()` dashamlav wala hissa **kaat** deta hai (round nahi karta), aur int ke saath float milaane par answer **float** hota hai.",
        "**Arithmetic operators** calculate karte hain: `//` poori sankhya rakhta hai aur `%` sheshphal deta hai, strips aur khuli tablets ke liye ekdum sahi.",
        "**Comparison operators** (`==`, `!=`, `>`, `<`, `>=`, `<=`) aur **logical operators** (`and`, `or`, `not`) **True** ya **False** dete hain.",
        "Python pehle `**`, phir `* / // %`, phir `+ -` karta hai; **brackets** sabse pehle.",
    ],
}

# ===================================================================== Kannada
T["kn"] = {
    "hook": {
        "title": "ಈ patient ಗೆ ಎಷ್ಟು strips ಬೇಕು?",
        "md": "Doctor ಬರೆದಿದ್ದಾರೆ: **2 tablets, ದಿನಕ್ಕೆ 3 ಸಲ, 7 ದಿನ**. Tablets 10 ರ strip ನಲ್ಲಿ ಬರುತ್ತವೆ. ನೀವು ಎಷ್ಟು strips ಕೊಡುತ್ತೀರಿ?\n\nಈ lesson ಮುಗಿಯುವಷ್ಟರಲ್ಲಿ Python ನಿಮಗಾಗಿ ಈ answer ಕಂಡುಹಿಡಿಯುತ್ತೆ. Values ಅನ್ನು ಒಂದು data type ಇಂದ ಇನ್ನೊಂದಕ್ಕೆ **ಬದಲಾಯಿಸೋದು**, ಮತ್ತು Python ನ **operators** ಇಂದ calculate ಮತ್ತು compare ಮಾಡೋದನ್ನು ಕಲಿಯುತ್ತೀರಿ.",
    },
    "learn": [
        "ಒಂದು value ಅನ್ನು ಒಂದು data type ಇಂದ ಇನ್ನೊಂದಕ್ಕೆ **ಬದಲಾಯಿಸೋದು**, ಇದಕ್ಕೆ **type casting** ಅಂತಾರೆ",
        "ಲೆಕ್ಕಕ್ಕಾಗಿ **arithmetic operators**, `//` ಮತ್ತು `%` ಜೊತೆ",
        "**True** ಅಥವಾ **False** ಉತ್ತರ ಕೊಡುವ **comparison** ಮತ್ತು **logical** operators",
        "Python ಯಾವ **ಕ್ರಮದಲ್ಲಿ** ಲೆಕ್ಕ ಮಾಡುತ್ತೆ, ಮತ್ತು **brackets** ಅದನ್ನು ಹೇಗೆ ಬದಲಾಯಿಸುತ್ತವೆ",
    ],
    "explanation": [
        {"heading": "Data types ನಡುವೆ ಬದಲಾಯಿಸೋದು",
         "md": f"Values ಹೆಚ್ಚಾಗಿ **text** ಆಗಿ ಬರುತ್ತವೆ, ಉದಾ: label ಇಂದ ಓದಿದ strength: `\"500\"`. Python text ಇಂದ ಲೆಕ್ಕ ಮಾಡಲು ಆಗಲ್ಲ, ಹಾಗಾಗಿ ಮೊದಲು ಅದನ್ನು number ಆಗಿ **ಬದಲಾಯಿಸಬೇಕು**. ಇದಕ್ಕೆ **type casting** ಅಂತಾರೆ.\n\n{TABLE_CAST['kn']}\n\n{CODE_CAST}\n\nಇದು `1500` print ಮಾಡುತ್ತೆ. `int()` ಇಲ್ಲದಿದ್ದರೆ ನಿಮಗೆ `500500500` ಸಿಗುತ್ತಿತ್ತು.\n\nLesson 1.3 ರ error ನೆನಪಿದೆಯಾ, `+` text ಮತ್ತು number ಅನ್ನು ಜೋಡಿಸಲು ಆಗಿರಲಿಲ್ಲ? `str()` ಅದನ್ನು ಸರಿ ಮಾಡುತ್ತೆ:\n\n{CODE_STR}\n\nಇದು `Dose: 500 mg` print ಮಾಡುತ್ತೆ.",
         "callout": {"title": "Type casting", "md": "ಒಂದು value ಅನ್ನು ಒಂದು data type ಇಂದ ಇನ್ನೊಂದಕ್ಕೆ ಬದಲಾಯಿಸೋದು, int(), float() ಅಥವಾ str() ಇಂದ."}},
        {"heading": "ಬದಲಾಯಿಸುವಾಗ ಗಮನಿಸಬೇಕಾದ ಎರಡು ವಿಷಯ",
         "md": f"**1. `int()` ದಶಮಾಂಶ ಭಾಗವನ್ನು ಕತ್ತರಿಸುತ್ತೆ. Round ಮಾಡಲ್ಲ.**\n\n{CODE_INT}\n\nಇದು `2` print ಮಾಡುತ್ತೆ, 3 ಅಲ್ಲ.\n\n**2. Python ಕೆಲವೊಮ್ಮೆ ತಾನೇ ಬದಲಾಯಿಸುತ್ತೆ.** Integer ಮತ್ತು float ಸೇರಿಸಿದಾಗ ಉತ್ತರ float ಆಗುತ್ತೆ:\n\n{CODE_MIX}\n\nಇದು `12.5` print ಮಾಡುತ್ತೆ. ಹೀಗೆ ತಾನಾಗಿಯೇ ಬದಲಾಗೋದಕ್ಕೆ **implicit conversion** ಅಂತಾರೆ. `int()`, `float()` ಅಥವಾ `str()` ಇಂದ ನಾವೇ ಬದಲಾಯಿಸೋದು **explicit conversion**."},
        {"heading": "Arithmetic operators",
         "md": "**Operator** ಅಂದ್ರೆ values ಜೊತೆ ಏನಾದರೂ ಮಾಡುವ symbol, ಉದಾ: `+` ಅಥವಾ `*`. ಇವು Python ನ **arithmetic operators**:\n\n"
               + arith_table({"head": ["ಅರ್ಥ", "Example"], "rows": ["ಕೂಡಿಸು", "ಕಳೆ", "ಗುಣಿಸು", "ಭಾಗಿಸು", "ಭಾಗಿಸಿ, ಪೂರ್ಣ ಸಂಖ್ಯೆ ಮಾತ್ರ", "ಶೇಷ (remainder)", "ಘಾತ (power)"]})
               + f"\n\nPharmacy ಯಲ್ಲಿ `//` ಮತ್ತು `%` ತುಂಬಾ ಉಪಯೋಗ. **25 tablets** ಮತ್ತು **ಒಂದು strip ಗೆ 10** ಇದ್ದರೆ:\n\n{CODE_STRIPS}\n\nಇದು `2` (ಪೂರ್ತಿ strips) ಮತ್ತು `5` (ಬಿಡಿ tablets) print ಮಾಡುತ್ತೆ.\n\nಗಮನಿಸಿ: `/` ಯಾವಾಗಲೂ float ಕೊಡುತ್ತೆ, ಸರಿಯಾಗಿ ಭಾಗ ಆದರೂ ಕೂಡ: `10 / 2` ಅಂದ್ರೆ `5.0`.",
         "callout": {"title": "Operator", "md": "Values ಜೊತೆ ಏನಾದರೂ ಮಾಡುವ symbol, ಉದಾ: + (ಕೂಡಿಸು) ಅಥವಾ > (ದೊಡ್ಡದು)."}},
        {"heading": "Comparison operators: ಹೌದು-ಅಥವಾ-ಇಲ್ಲ ಪ್ರಶ್ನೆಗಳು",
         "md": "**Comparison operators** ಎರಡು values ಅನ್ನು ಹೋಲಿಸುತ್ತವೆ. ಉತ್ತರ ಯಾವಾಗಲೂ boolean: `True` ಅಥವಾ `False`.\n\n"
               + cmp_table("ಕೇಳುವ ಪ್ರಶ್ನೆ", ["ಸಮವಾ?", "ಸಮ ಅಲ್ವಾ?", "ದೊಡ್ಡದಾ?", "ಚಿಕ್ಕದಾ?", "ದೊಡ್ಡದು ಅಥವಾ ಸಮವಾ?", "ಚಿಕ್ಕದು ಅಥವಾ ಸಮವಾ?"])
               + f"\n\n{CODE_CMP}\n\nಇದು `True` print ಮಾಡುತ್ತೆ: dose 4000 mg ಗಿಂತ ಜಾಸ್ತಿ ಇದೆ.",
         "callout": {"title": "= ಮತ್ತು == ಬೇರೆ ಬೇರೆ", "md": "ಒಂದು = value ಇಡುತ್ತೆ. ಎರಡು == ಎರಡು values ಅನ್ನು ಹೋಲಿಸುತ್ತೆ. ಇವನ್ನು mix ಮಾಡೋದು beginners ಮಾಡುವ ಅತಿ ಸಾಮಾನ್ಯ ತಪ್ಪುಗಳಲ್ಲಿ ಒಂದು."}},
        {"heading": "Logical operators: and, or, not",
         "md": f"**Logical operators** True/False ಉತ್ತರಗಳನ್ನು ಜೋಡಿಸುತ್ತವೆ:\n\n- `and`: **ಎರಡೂ** ಕಡೆ True ಇದ್ದಾಗ ಮಾತ್ರ **True**\n- `or`: **ಕನಿಷ್ಠ ಒಂದು** ಕಡೆ True ಇದ್ದರೆ **True**\n- `not`: True ಅನ್ನು False, False ಅನ್ನು True ಮಾಡುತ್ತೆ\n\n{CODE_LOGIC}\n\nಇದು ಮೊದಲು `False` print ಮಾಡುತ್ತೆ (patient ಗೆ 18 ಅಥವಾ ಹೆಚ್ಚು ವಯಸ್ಸಾಗಿಲ್ಲ), ನಂತರ `True` (ತೂಕ 50 kg ಅಥವಾ ಹೆಚ್ಚು ಇದೆ)."},
        {"heading": "Shortcuts, ಮತ್ತು ಲೆಕ್ಕದ ಕ್ರಮ",
         "md": f"**Shortcut operators** ಒಂದು variable ಅನ್ನು ಅದರದೇ value ಬಳಸಿ ಬದಲಾಯಿಸುತ್ತವೆ:\n\n{CODE_SHORT}\n\nಇದು `70` print ಮಾಡುತ್ತೆ. `stock -= 30` ಅಂದ್ರೆ `stock = stock - 30` ಅನ್ನು ಚಿಕ್ಕದಾಗಿ ಬರೆಯೋ ರೀತಿ. ಹಾಗೆಯೇ `+=` ಕೂಡಿಸುತ್ತೆ, `*=` ಗುಣಿಸುತ್ತೆ.\n\n**ಲೆಕ್ಕದ ಕ್ರಮ:** ಗಣಿತದ ಹಾಗೆ, Python ಮೊದಲು `**`, ನಂತರ `*`, `/`, `//` ಮತ್ತು `%`, ನಂತರ `+` ಮತ್ತು `-` ಮಾಡುತ್ತೆ. **Brackets ಎಲ್ಲಕ್ಕಿಂತ ಮೊದಲು.**\n\n{CODE_ORDER}\n\nಇದು ಮೊದಲು `149.0`, ನಂತರ `100.0` print ಮಾಡುತ್ತೆ. ಎರಡನೆಯದು ಮಾತ್ರ 98 ಮತ್ತು 102 ಅನ್ನುವ ಎರಡು readings ನ average.",
         "callout": {"title": "ಸಂಶಯ ಇದ್ದರೆ brackets ಹಾಕಿ", "md": "Brackets ಇಂದ dose formulas ಓದುವ ಎಲ್ಲರಿಗೂ ಸ್ಪಷ್ಟವಾಗಿ ಅರ್ಥ ಆಗುತ್ತೆ, ಮತ್ತು ನೀವು ಬಯಸದ ಕ್ರಮದಲ್ಲಿ Python ಲೆಕ್ಕ ಮಾಡಲ್ಲ."}},
    ],
    "walkthrough": {
        "intro": "ಈ program 7 ದಿನದ course ಗೆ ಎಷ್ಟು tablets ಬೇಕು, ಮತ್ತು ಎಷ್ಟು strips ಕೊಡಬೇಕು ಅಂತ ಲೆಕ್ಕ ಹಾಕುತ್ತೆ. ಪ್ರತಿ line run ಆಗುವಾಗ Variables panel ನೋಡಿ.",
        "keyTerms": [
            {"meaning": "Text \"2\" ಅನ್ನು number 2 ಆಗಿ ಬದಲಾಯಿಸು."},
            {"meaning": "ಭಾಗಿಸಿ ಪೂರ್ಣ ಸಂಖ್ಯೆ ಮಾತ್ರ ಇಡು."},
            {"meaning": "ಭಾಗಿಸಿದ ನಂತರ ಉಳಿದದ್ದು."},
            {"meaning": "ದೊಡ್ಡದು ಅಥವಾ ಸಮ. True ಅಥವಾ False ಕೊಡುತ್ತೆ."},
        ],
    },
    "errors": {
        "intro": "Values ಬದಲಾಯಿಸುವಾಗ ಮತ್ತು ಲೆಕ್ಕ ಮಾಡುವಾಗ ಈ ಎರಡು errors ಸಾಮಾನ್ಯ.",
        "examples": [
            {"title": "ಪೂರ್ಣ ಸಂಖ್ಯೆ ಅಲ್ಲದ text ಅನ್ನು ಬದಲಾಯಿಸೋದು",
             "md": "`int()` **ಪೂರ್ಣ ಸಂಖ್ಯೆ** ತರಹ ಕಾಣುವ text ಅನ್ನು ಮಾತ್ರ ಬದಲಾಯಿಸಬಹುದು. `\"52.5\"` ನಲ್ಲಿ ದಶಮಾಂಶ ಇದೆ, ಹಾಗಾಗಿ `float(\"52.5\")` use ಮಾಡಿ. `\"fifty\"` ತರಹದ text ಅನ್ನು ಬದಲಾಯಿಸಲು ಆಗೋದೇ ಇಲ್ಲ.",
             "callout": {"title": "ValueError", "md": "Value ನ data type ಸರಿ ಇದೆ, ಆದರೆ ಅದನ್ನು use ಮಾಡಲು ಆಗಲ್ಲ ಅನ್ನುವ error, ಉದಾ: int(\"52.5\")."}},
            {"title": "ಸೊನ್ನೆಯಿಂದ ಭಾಗಿಸೋದು",
             "md": "ಯಾವುದನ್ನೂ ಸೊನ್ನೆಯಿಂದ ಭಾಗಿಸಲು ಆಗಲ್ಲ, ಗಣಿತದಲ್ಲೂ ಇಲ್ಲ, Python ನಲ್ಲೂ ಇಲ್ಲ. ನೀವು ಭಾಗಿಸುವ number ಯಾವತ್ತೂ 0 ಆಗಬಾರದು ಅಂತ check ಮಾಡಿ, ಉದಾ: ದಿನಗಳ ಸಂಖ್ಯೆ."},
        ],
    },
    "mistakes": [
        {"mistake": "Compare ಮಾಡಲು `=` use ಮಾಡೋದು, ಉದಾ: `print(dose = 500)`", "fix": "ಎರಡು equals signs ಇಂದ compare ಮಾಡಿ: `print(dose == 500)`."},
        {"mistake": "Text ಮತ್ತು number ಅನ್ನು `+` ಇಂದ ಜೋಡಿಸೋದು, ಉದಾ: `\"Total: \" + 42`", "fix": "ಮೊದಲು number ಅನ್ನು ಬದಲಾಯಿಸಿ: `\"Total: \" + str(42)`."},
        {"mistake": "`int()` round ಮಾಡುತ್ತೆ ಅಂತ ಅಂದುಕೊಳ್ಳೋದು, ಉದಾ: `int(2.9)`", "see": "Error ಇಲ್ಲ, ಆದರೆ result 2", "fix": "`int()` ದಶಮಾಂಶ ಭಾಗ ಕತ್ತರಿಸುತ್ತೆ. Round ಮಾಡಲು `round(2.9)` use ಮಾಡಿ, ಅದು 3 ಕೊಡುತ್ತೆ."},
        {"mistake": "`/` ಪೂರ್ಣ ಸಂಖ್ಯೆ ಕೊಡುತ್ತೆ ಅಂತ ಅಂದುಕೊಳ್ಳೋದು, ಉದಾ: `10 / 2`", "see": "Error ಇಲ್ಲ, ಆದರೆ result 5.0", "fix": "ಪೂರ್ಣ ಸಂಖ್ಯೆ ಬೇಕಾದರೆ `//` use ಮಾಡಿ: `10 // 2` ಕೊಡೋದು 5."},
        {"mistake": "Average ನಲ್ಲಿ brackets ಮರೆಯೋದು, ಉದಾ: `98 + 102 / 2`", "see": "Error ಇಲ್ಲ, ಆದರೆ result 149.0", "fix": "Brackets ಹಾಕಿ: `(98 + 102) / 2` ಕೊಡೋದು 100.0."},
    ],
    "tasks": [
        {"title": "ಮೊದಲು ಬದಲಾಯಿಸಿ, ನಂತರ ಲೆಕ್ಕ ಮಾಡಿ", "md": "Strength ಅನ್ನು label ಇಂದ ಓದಲಾಗಿದೆ, ಹಾಗಾಗಿ ಅದು text. ಅದನ್ನು number ಆಗಿ ಬದಲಾಯಿಸಿ, strength ನ **ಎರಡರಷ್ಟು** print ಮಾಡಿ. Output ಸರಿಯಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["int(strength) text ಅನ್ನು number ಮಾಡುತ್ತೆ.", "Try ಮಾಡಿ: print(int(strength) * 2)."]},
        {"title": "Strips ಮತ್ತು ಬಿಡಿ tablets", "md": "**45 tablets** ಇವೆ, ಪ್ರತಿ strip ನಲ್ಲಿ **10**. `//` ಮತ್ತು `%` use ಮಾಡಿ print ಮಾಡಿ:",
         "hints": ["total // 10 ಪೂರ್ತಿ strips ಕೊಡುತ್ತೆ.", "total % 10 ಉಳಿದ tablets ಕೊಡುತ್ತೆ.", "print(\"Strips:\", total // 10, \"Loose:\", total % 10)"]},
        {"title": "Dose limit ಗಿಂತ ಜಾಸ್ತಿ ಇದೆಯಾ?", "md": "Maximum daily dose **4000 mg**. `daily_dose_mg` limit ಗಿಂತ **ದೊಡ್ಡದಾ** ಅಂತ print ಮಾಡಿ. Output ಸರಿಯಾಗಿ ಹೀಗಿರಬೇಕು:\n\n*(ಕಲಿಯಲು ಮಾತ್ರ: ನಿಜವಾದ limits clinical guidelines ಪ್ರಕಾರವೇ ಇರಬೇಕು.)*",
         "hints": ["> \"ದೊಡ್ಡದಾ?\" ಅಂತ ಕೇಳಿ True ಅಥವಾ False ಕೊಡುತ್ತೆ.", "print(\"Over the limit:\", daily_dose_mg > limit_mg)"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "ಈ program `Total: 42` print ಮಾಡಬೇಕು, ಆದರೆ ಇದರಲ್ಲಿ error ಇದೆ. **`str()` use ಮಾಡಿ** ಸರಿ ಮಾಡಿ.",
         "hints": ["+ text ಮತ್ತು number ಅನ್ನು ಜೋಡಿಸಲು ಆಗಲ್ಲ.", "str(total) ಇಂದ number ಅನ್ನು text ಆಗಿ ಬದಲಾಯಿಸಿ."],
         "solutionNote": "str(total), 42 ಅನ್ನು text \"42\" ಮಾಡುತ್ತೆ, ಹಾಗಾಗಿ + ಎರಡೂ strings ಅನ್ನು ಜೋಡಿಸುತ್ತೆ."},
    ],
    "quiz": [
        {"q": "print(int(\"500\") + 5) ಏನು ತೋರಿಸುತ್ತೆ?", "why": "int(\"500\") text ಅನ್ನು number 500 ಮಾಡುತ್ತೆ, ಹಾಗಾಗಿ ಉತ್ತರ 505."},
        {"q": "17 // 5 ಎಷ್ಟು?", "why": "// ಭಾಗಿಸಿ ಪೂರ್ಣ ಸಂಖ್ಯೆ ಮಾತ್ರ ಇಡುತ್ತೆ: 17 ರಲ್ಲಿ 5 ಮೂರು ಸಲ ಹೋಗುತ್ತೆ, ಸ್ವಲ್ಪ ಉಳಿಯುತ್ತೆ."},
        {"q": "17 % 5 ಎಷ್ಟು?", "why": "% ಶೇಷ ಕೊಡುತ್ತೆ: 17 ರಲ್ಲಿ 5 ಮೂರು ಸಲ (15) ಹೋಗುತ್ತೆ, 2 ಉಳಿಯುತ್ತೆ."},
        {"q": "print(4500 > 4000) ಏನು ತೋರಿಸುತ್ತೆ?", "why": "4500, 4000 ಗಿಂತ ದೊಡ್ಡದು, ಹಾಗಾಗಿ comparison True ಕೊಡುತ್ತೆ."},
        {"q": "age = 16. print(age >= 18 and age <= 60) ಏನು ತೋರಿಸುತ್ತೆ?", "why": "and ಗೆ ಎರಡೂ ಕಡೆ True ಬೇಕು. 16, 18 ಅಥವಾ ಹೆಚ್ಚು ಅಲ್ಲ, ಹಾಗಾಗಿ ಉತ್ತರ False."},
        {"q": "98 ಮತ್ತು 102 ರ average ಯಾವುದು ಕೊಡುತ್ತೆ?", "why": "Brackets ಇರುವುದರಿಂದ Python ಮೊದಲು ಕೂಡಿಸಿ, ನಂತರ ಭಾಗಿಸುತ್ತೆ: 200 / 2 = 100.0."},
    ],
    "exam": {"note": "University exam English ನಲ್ಲಿ ಬರೆಯುವುದರಿಂದ model answers English ನಲ್ಲೇ ಇವೆ. ಇವು practice ಗಾಗಿ important questions; ನಿಜವಾದ university questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 1.4 · Type casting ಮತ್ತು operators",
        "children": [
            {"label": "Type casting", "children": [{"label": "int(\"500\") → 500"}, {"label": "float(\"52.5\") → 52.5"}, {"label": "str(500) → \"500\""}, {"label": "int(2.9) → 2"}]},
            {"label": "Arithmetic", "children": [{"label": "+  -  *  /"}, {"label": "// ಪೂರ್ಣ ಸಂಖ್ಯೆ"}, {"label": "% ಶೇಷ"}, {"label": "** ಘಾತ"}]},
            {"label": "Comparison", "children": [{"label": "==  !="}, {"label": ">  <  >=  <="}, {"label": "True / False ಕೊಡುತ್ತೆ"}]},
            {"label": "Logical", "children": [{"label": "and: ಎರಡೂ True"}, {"label": "or: ಕನಿಷ್ಠ ಒಂದು"}, {"label": "not: ತಿರುಗಿಸುತ್ತೆ"}]},
            {"label": "ಕ್ರಮ", "children": [{"label": "Brackets ಮೊದಲು"}, {"label": "** ನಂತರ * / // %"}, {"label": "ನಂತರ + -"}]},
            {"label": "Errors", "children": [{"label": "ValueError: int(\"52.5\")"}, {"label": "ZeroDivisionError"}]},
        ],
    },
    "summary": [
        "**Type casting** values ಅನ್ನು ಬದಲಾಯಿಸುತ್ತೆ: `int(\"500\")` ಕೊಡೋದು 500, `float(\"52.5\")` ಕೊಡೋದು 52.5, `str(500)` ಕೊಡೋದು \"500\".",
        "`int()` ದಶಮಾಂಶ ಭಾಗವನ್ನು **ಕತ್ತರಿಸುತ್ತೆ** (round ಮಾಡಲ್ಲ), ಮತ್ತು int ಜೊತೆ float ಸೇರಿಸಿದರೆ ಉತ್ತರ **float**.",
        "**Arithmetic operators** ಲೆಕ್ಕ ಮಾಡುತ್ತವೆ: `//` ಪೂರ್ಣ ಸಂಖ್ಯೆ ಇಡುತ್ತೆ, `%` ಶೇಷ ಕೊಡುತ್ತೆ, strips ಮತ್ತು ಬಿಡಿ tablets ಗೆ ಸರಿಯಾದದ್ದು.",
        "**Comparison operators** (`==`, `!=`, `>`, `<`, `>=`, `<=`) ಮತ್ತು **logical operators** (`and`, `or`, `not`) **True** ಅಥವಾ **False** ಕೊಡುತ್ತವೆ.",
        "Python ಮೊದಲು `**`, ನಂತರ `* / // %`, ನಂತರ `+ -` ಮಾಡುತ್ತೆ; **brackets** ಎಲ್ಲಕ್ಕಿಂತ ಮೊದಲು.",
    ],
}

# Walkthrough narration shown on screen (code names as written)
NARR = {
    "hi": [
        "यह program निकालता है कि सात दिन के course में कितनी tablets लगेंगी, और कितनी strips देनी हैं। Variables panel देखिए।",
        "Comment बताता है कि program क्या करता है।",
        "int, text दो को number दो में बदलता है, ताकि Python उससे calculate कर सके।",
        "doses_per_day में तीन रखा गया है।",
        "days में सात रखा गया है।",
        "Star गुणा करता है। दो गुणा तीन गुणा सात, यानी बयालीस tablets।",
        "दो slashes भाग देकर सिर्फ पूरी संख्या रखते हैं। बयालीस को दस से भाग देने पर चार पूरी strips।",
        "Percent sign शेषफल देता है। बयालीस को दस से भाग देने पर दो खुली tablets बचती हैं।",
        "Print कुल tablets दिखाता है।",
        "फिर strips और खुली tablets।",
        "आखिर में एक comparison। चार strips में चालीस tablets आती हैं। चालीस, बयालीस से बड़ा या बराबर नहीं है, इसलिए answer False है। Patient को एक और strip चाहिए।",
    ],
    "hinglish": [
        "Yeh program nikalta hai ki saat din ke course mein kitni tablets lagengi, aur kitni strips deni hain. Variables panel dekhiye.",
        "Comment batata hai ki program kya karta hai.",
        "int, text do ko number do mein badalta hai, taaki Python usse calculate kar sake.",
        "doses_per_day mein teen rakha gaya hai.",
        "days mein saat rakha gaya hai.",
        "Star guna karta hai. Do guna teen guna saat, yaani bayaalees tablets.",
        "Do slashes bhaag dekar sirf poori sankhya rakhte hain. Bayaalees ko das se bhaag dene par chaar poori strips.",
        "Percent sign sheshphal deta hai. Bayaalees ko das se bhaag dene par do khuli tablets bachti hain.",
        "Print kul tablets dikhata hai.",
        "Phir strips aur khuli tablets.",
        "Aakhir mein ek comparison. Chaar strips mein chaalees tablets aati hain. Chaalees, bayaalees se bada ya barabar nahi hai, isliye answer False hai. Patient ko ek aur strip chahiye.",
    ],
    "kn": [
        "ಈ program ಏಳು ದಿನದ course ಗೆ ಎಷ್ಟು tablets ಬೇಕು, ಮತ್ತು ಎಷ್ಟು strips ಕೊಡಬೇಕು ಅಂತ ಲೆಕ್ಕ ಹಾಕುತ್ತೆ. Variables panel ನೋಡಿ.",
        "Program ಏನು ಮಾಡುತ್ತೆ ಅಂತ comment ಹೇಳುತ್ತೆ.",
        "int, ಎರಡು ಅನ್ನುವ text ಅನ್ನು ಎರಡು ಅನ್ನುವ number ಆಗಿ ಬದಲಾಯಿಸುತ್ತೆ, ಆಗ Python ಅದರಿಂದ ಲೆಕ್ಕ ಮಾಡಬಹುದು.",
        "doses_per_day ನಲ್ಲಿ ಮೂರು ಇಡಲಾಗಿದೆ.",
        "days ನಲ್ಲಿ ಏಳು ಇಡಲಾಗಿದೆ.",
        "Star ಗುಣಿಸುತ್ತೆ. ಎರಡು ಗುಣಿಸು ಮೂರು ಗುಣಿಸು ಏಳು, ಅಂದ್ರೆ ನಲವತ್ತೆರಡು tablets.",
        "ಎರಡು slashes ಭಾಗಿಸಿ ಪೂರ್ಣ ಸಂಖ್ಯೆ ಮಾತ್ರ ಇಡುತ್ತವೆ. ನಲವತ್ತೆರಡನ್ನು ಹತ್ತರಿಂದ ಭಾಗಿಸಿದರೆ ನಾಲ್ಕು ಪೂರ್ತಿ strips.",
        "Percent sign ಶೇಷ ಕೊಡುತ್ತೆ. ನಲವತ್ತೆರಡನ್ನು ಹತ್ತರಿಂದ ಭಾಗಿಸಿದರೆ ಎರಡು ಬಿಡಿ tablets ಉಳಿಯುತ್ತವೆ.",
        "Print ಒಟ್ಟು tablets ತೋರಿಸುತ್ತೆ.",
        "ನಂತರ strips ಮತ್ತು ಬಿಡಿ tablets.",
        "ಕೊನೆಗೆ ಒಂದು comparison. ನಾಲ್ಕು strips ನಲ್ಲಿ ನಲವತ್ತು tablets ಇರುತ್ತವೆ. ನಲವತ್ತು, ನಲವತ್ತೆರಡಕ್ಕಿಂತ ದೊಡ್ಡದು ಅಥವಾ ಸಮ ಅಲ್ಲ, ಹಾಗಾಗಿ ಉತ್ತರ False. Patient ಗೆ ಇನ್ನೊಂದು strip ಬೇಕು.",
    ],
}
ANIM = {
    "hi": [
        "बयालीस tablets को दस-दस की strips में pack करना है।",
        "दो slashes पूरी strips गिनते हैं। बयालीस को दस से भाग देकर, सिर्फ पूरी संख्या रखने पर, चार।",
        "Percent sign बचा हुआ गिनता है: दो खुली tablets।",
        "चार strips में सिर्फ चालीस tablets आती हैं, इसलिए comparison कहता है कि ये काफी नहीं हैं। Patient को पाँच strips चाहिए।",
    ],
    "hinglish": [
        "Bayaalees tablets ko das-das ki strips mein pack karna hai.",
        "Do slashes poori strips ginte hain. Bayaalees ko das se bhaag dekar, sirf poori sankhya rakhne par, chaar.",
        "Percent sign bacha hua ginta hai: do khuli tablets.",
        "Chaar strips mein sirf chaalees tablets aati hain, isliye comparison kehta hai ki yeh kaafi nahi hain. Patient ko paanch strips chahiye.",
    ],
    "kn": [
        "ನಲವತ್ತೆರಡು tablets ಅನ್ನು ಹತ್ತು ಹತ್ತರ strips ನಲ್ಲಿ pack ಮಾಡಬೇಕು.",
        "ಎರಡು slashes ಪೂರ್ತಿ strips ಎಣಿಸುತ್ತವೆ. ನಲವತ್ತೆರಡನ್ನು ಹತ್ತರಿಂದ ಭಾಗಿಸಿ, ಪೂರ್ಣ ಸಂಖ್ಯೆ ಮಾತ್ರ ಇಟ್ಟರೆ, ನಾಲ್ಕು.",
        "Percent sign ಉಳಿದದ್ದನ್ನು ಎಣಿಸುತ್ತೆ: ಎರಡು ಬಿಡಿ tablets.",
        "ನಾಲ್ಕು strips ನಲ್ಲಿ ನಲವತ್ತು tablets ಮಾತ್ರ ಇರುತ್ತವೆ, ಹಾಗಾಗಿ ಅವು ಸಾಕಾಗಲ್ಲ ಅಂತ comparison ಹೇಳುತ್ತೆ. Patient ಗೆ ಐದು strips ಬೇಕು.",
    ],
}
# Voice scripts: English words and code names in local script so the voices read them naturally
TTS = {
    "narrator": {
        "hi": [
            "यह प्रोग्राम निकालता है कि सात दिन के कोर्स में कितनी टैबलेट्स लगेंगी, और कितनी स्ट्रिप्स देनी हैं। वेरिएबल्स पैनल देखिए।",
            "कमेंट बताता है कि प्रोग्राम क्या करता है।",
            "इंट, टेक्स्ट दो को नंबर दो में बदलता है, ताकि पाइथन उससे कैलकुलेट कर सके।",
            "डोज़ेस पर डे में तीन रखा गया है।",
            "डेज़ में सात रखा गया है।",
            "स्टार गुणा करता है। दो गुणा तीन गुणा सात, यानी बयालीस टैबलेट्स।",
            "दो स्लैशेस भाग देकर सिर्फ पूरी संख्या रखते हैं। बयालीस को दस से भाग देने पर चार पूरी स्ट्रिप्स।",
            "परसेंट साइन शेषफल देता है। बयालीस को दस से भाग देने पर दो खुली टैबलेट्स बचती हैं।",
            "प्रिंट कुल टैबलेट्स दिखाता है।",
            "फिर स्ट्रिप्स और खुली टैबलेट्स।",
            "आखिर में एक कम्पैरिज़न। चार स्ट्रिप्स में चालीस टैबलेट्स आती हैं। चालीस, बयालीस से बड़ा या बराबर नहीं है, इसलिए आंसर फॉल्स है। पेशेंट को एक और स्ट्रिप चाहिए।",
        ],
        "kn": [
            "ಈ ಪ್ರೋಗ್ರಾಮ್ ಏಳು ದಿನದ ಕೋರ್ಸ್ ಗೆ ಎಷ್ಟು ಟ್ಯಾಬ್ಲೆಟ್ಸ್ ಬೇಕು, ಮತ್ತು ಎಷ್ಟು ಸ್ಟ್ರಿಪ್ಸ್ ಕೊಡಬೇಕು ಅಂತ ಲೆಕ್ಕ ಹಾಕುತ್ತೆ. ವೇರಿಯಬಲ್ಸ್ ಪ್ಯಾನೆಲ್ ನೋಡಿ.",
            "ಪ್ರೋಗ್ರಾಮ್ ಏನು ಮಾಡುತ್ತೆ ಅಂತ ಕಾಮೆಂಟ್ ಹೇಳುತ್ತೆ.",
            "ಇಂಟ್, ಎರಡು ಅನ್ನುವ ಟೆಕ್ಸ್ಟ್ ಅನ್ನು ಎರಡು ಅನ್ನುವ ನಂಬರ್ ಆಗಿ ಬದಲಾಯಿಸುತ್ತೆ, ಆಗ ಪೈಥಾನ್ ಅದರಿಂದ ಲೆಕ್ಕ ಮಾಡಬಹುದು.",
            "ಡೋಸಸ್ ಪರ್ ಡೇ ನಲ್ಲಿ ಮೂರು ಇಡಲಾಗಿದೆ.",
            "ಡೇಸ್ ನಲ್ಲಿ ಏಳು ಇಡಲಾಗಿದೆ.",
            "ಸ್ಟಾರ್ ಗುಣಿಸುತ್ತೆ. ಎರಡು ಗುಣಿಸು ಮೂರು ಗುಣಿಸು ಏಳು, ಅಂದ್ರೆ ನಲವತ್ತೆರಡು ಟ್ಯಾಬ್ಲೆಟ್ಸ್.",
            "ಎರಡು ಸ್ಲ್ಯಾಶಸ್ ಭಾಗಿಸಿ ಪೂರ್ಣ ಸಂಖ್ಯೆ ಮಾತ್ರ ಇಡುತ್ತವೆ. ನಲವತ್ತೆರಡನ್ನು ಹತ್ತರಿಂದ ಭಾಗಿಸಿದರೆ ನಾಲ್ಕು ಪೂರ್ತಿ ಸ್ಟ್ರಿಪ್ಸ್.",
            "ಪರ್ಸೆಂಟ್ ಸೈನ್ ಶೇಷ ಕೊಡುತ್ತೆ. ನಲವತ್ತೆರಡನ್ನು ಹತ್ತರಿಂದ ಭಾಗಿಸಿದರೆ ಎರಡು ಬಿಡಿ ಟ್ಯಾಬ್ಲೆಟ್ಸ್ ಉಳಿಯುತ್ತವೆ.",
            "ಪ್ರಿಂಟ್ ಒಟ್ಟು ಟ್ಯಾಬ್ಲೆಟ್ಸ್ ತೋರಿಸುತ್ತೆ.",
            "ನಂತರ ಸ್ಟ್ರಿಪ್ಸ್ ಮತ್ತು ಬಿಡಿ ಟ್ಯಾಬ್ಲೆಟ್ಸ್.",
            "ಕೊನೆಗೆ ಒಂದು ಕಂಪ್ಯಾರಿಸನ್. ನಾಲ್ಕು ಸ್ಟ್ರಿಪ್ಸ್ ನಲ್ಲಿ ನಲವತ್ತು ಟ್ಯಾಬ್ಲೆಟ್ಸ್ ಇರುತ್ತವೆ. ನಲವತ್ತು, ನಲವತ್ತೆರಡಕ್ಕಿಂತ ದೊಡ್ಡದು ಅಥವಾ ಸಮ ಅಲ್ಲ, ಹಾಗಾಗಿ ಉತ್ತರ ಫಾಲ್ಸ್. ಪೇಷೆಂಟ್ ಗೆ ಇನ್ನೊಂದು ಸ್ಟ್ರಿಪ್ ಬೇಕು.",
        ],
    },
    "anim-strips": {
        "hi": [
            "बयालीस टैबलेट्स को दस-दस की स्ट्रिप्स में पैक करना है।",
            "दो स्लैशेस पूरी स्ट्रिप्स गिनते हैं। बयालीस को दस से भाग देकर, सिर्फ पूरी संख्या रखने पर, चार।",
            "परसेंट साइन बचा हुआ गिनता है: दो खुली टैबलेट्स।",
            "चार स्ट्रिप्स में सिर्फ चालीस टैबलेट्स आती हैं, इसलिए कम्पैरिज़न कहता है कि ये काफी नहीं हैं। पेशेंट को पाँच स्ट्रिप्स चाहिए।",
        ],
        "kn": [
            "ನಲವತ್ತೆರಡು ಟ್ಯಾಬ್ಲೆಟ್ಸ್ ಅನ್ನು ಹತ್ತು ಹತ್ತರ ಸ್ಟ್ರಿಪ್ಸ್ ನಲ್ಲಿ ಪ್ಯಾಕ್ ಮಾಡಬೇಕು.",
            "ಎರಡು ಸ್ಲ್ಯಾಶಸ್ ಪೂರ್ತಿ ಸ್ಟ್ರಿಪ್ಸ್ ಎಣಿಸುತ್ತವೆ. ನಲವತ್ತೆರಡನ್ನು ಹತ್ತರಿಂದ ಭಾಗಿಸಿ, ಪೂರ್ಣ ಸಂಖ್ಯೆ ಮಾತ್ರ ಇಟ್ಟರೆ, ನಾಲ್ಕು.",
            "ಪರ್ಸೆಂಟ್ ಸೈನ್ ಉಳಿದದ್ದನ್ನು ಎಣಿಸುತ್ತೆ: ಎರಡು ಬಿಡಿ ಟ್ಯಾಬ್ಲೆಟ್ಸ್.",
            "ನಾಲ್ಕು ಸ್ಟ್ರಿಪ್ಸ್ ನಲ್ಲಿ ನಲವತ್ತು ಟ್ಯಾಬ್ಲೆಟ್ಸ್ ಮಾತ್ರ ಇರುತ್ತವೆ, ಹಾಗಾಗಿ ಅವು ಸಾಕಾಗಲ್ಲ ಅಂತ ಕಂಪ್ಯಾರಿಸನ್ ಹೇಳುತ್ತೆ. ಪೇಷೆಂಟ್ ಗೆ ಐದು ಸ್ಟ್ರಿಪ್ಸ್ ಬೇಕು.",
        ],
    },
}


def say_en(text):
    """English voice script: spell out code names so the voice reads them naturally."""
    text = re.sub(r"\b([a-z]+)_([a-z]+)_([a-z]+)\b", r"\1 \2 \3", text)
    return re.sub(r"\b([a-z]+)_([a-z]+)\b", r"\1 \2", text)


if __name__ == "__main__":
    en = json.load(open(os.path.join(ROOT, "content", "bp101t", "1-4", "en.json"), encoding="utf-8"))
    n_steps, n_anim = len(en["walkthrough"]["steps"]), len(en["animations"][0]["steps"])
    for lang, data in T.items():
        assert len(NARR[lang]) == n_steps and len(ANIM[lang]) == n_anim, lang
        doc = dict(data)
        doc["walkthrough"] = dict(doc["walkthrough"], steps=[{"say": s} for s in NARR[lang]])
        doc["animations"] = [{"steps": [{"say": s} for s in ANIM[lang]]}]
        doc["translatedSections"] = SECTIONS
        path = os.path.join(ROOT, "content", "bp101t", "1-4", f"{lang}.json")
        json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("wrote", path)

    narr_en = [s["say"] for s in en["walkthrough"]["steps"]]
    anim_en = [s["say"] for s in en["animations"][0]["steps"]]
    for track in TTS.values():
        for lang in ("hi", "kn"):
            assert len(track[lang]) in (n_steps, n_anim)
    script = {
        "course": "bp101t", "lesson": "1-4",
        "voices": {"en": "Mary", "hi": "Rani", "kn": "Anu"},
        "tracks": [
            {"id": "narrator", "prefix": "step-", "lang": "en", "tts": [say_en(t) for t in narr_en], "display": narr_en},
            {"id": "narrator", "prefix": "step-", "lang": "hi", "tts": TTS["narrator"]["hi"], "display": NARR["hi"], "displayHinglish": NARR["hinglish"]},
            {"id": "narrator", "prefix": "step-", "lang": "kn", "tts": TTS["narrator"]["kn"], "display": NARR["kn"]},
            {"id": "anim-strips", "prefix": "anim-strips-", "lang": "en", "tts": [say_en(t) for t in anim_en], "display": anim_en},
            {"id": "anim-strips", "prefix": "anim-strips-", "lang": "hi", "tts": TTS["anim-strips"]["hi"], "display": ANIM["hi"], "displayHinglish": ANIM["hinglish"]},
            {"id": "anim-strips", "prefix": "anim-strips-", "lang": "kn", "tts": TTS["anim-strips"]["kn"], "display": ANIM["kn"]},
        ],
    }
    path = os.path.join(ROOT, "scripts", "bp101t", "1-4.json")
    json.dump(script, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", path)
    # keep the "Words to know" section after regenerating
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "..", "glossary_bp101t.py")], check=True)

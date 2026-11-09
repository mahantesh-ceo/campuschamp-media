"""Lesson 3.2 translations (Hindi, Hinglish, Kannada) and voice scripts."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import build  # noqa: E402

_spec = importlib.util.spec_from_file_location("en32", os.path.join(os.path.dirname(__file__), "..", "lessons", "bp101t_3-2_en.py"))
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)

T = {}

T["hi"] = {
    "hook": {
        "title": "नाम से ढूँढो, number से नहीं",
        "md": "Pharmacist यह नहीं कहता कि \"formulary की तीसरी drug दो\"। वह पूछता है \"**Ibuprofen** का adult dose क्या है?\" Patient की file भी position से नहीं पढ़ी जाती: आप **age**, **blood group**, **allergies** ढूँढते हैं।\n\nक्रम वाली readings के लिए lists बढ़िया हैं। पर जो जानकारी **नाम से** ढूँढी जाती है, उसके लिए Python के पास **dictionary** है। और छोटे records के लिए जो कभी नहीं बदलने चाहिए, जैसे 128 over 84 का blood pressure, उसके पास **tuple** है।",
    },
    "learn": [
        "**Tuple** एक fixed record कैसे रखता है, और उसे क्यों नहीं बदल सकते",
        "Tuple को अलग variables में **unpack** करना",
        "**Dictionary** **key: value** pairs कैसे रखती है, जो key से ढूँढे जाते हैं",
        "Values जोड़ना, बदलना, **get()** से सुरक्षित ढूँढना, और dictionary पर loop चलाना",
    ],
    "explanation": [
        {
            "heading": "Tuples: records जो नहीं बदलते",
            "md": "**Tuple** list जैसा है, पर **round brackets** से लिखा जाता है, और बनने के बाद **बदला नहीं जा सकता**:\n\n" + E.C_TUPLE + "\n\nयह print करता है:\n\n" + E.O_TUPLE + "\n\nIndexing, slicing और `len()` बिल्कुल lists की तरह काम करते हैं। पर `bp[0] = 130` error देता है, क्योंकि tuples **immutable** हैं। यह खूबी है: दर्ज की गई reading, या drug का (name, strength) pair, गलती से नहीं बदलना चाहिए।",
            "callout": {"title": "Tuple", "md": "Round brackets में क्रम वाला collection, जैसे (128, 84)। इसे list की तरह पढ़ सकते हैं पर कभी बदल नहीं सकते।"},
        },
        {
            "heading": "Tuple को unpack करना",
            "md": "एक line में tuple को अलग-अलग variables में बाँट सकते हैं। इसे **unpacking** कहते हैं:\n\n" + E.C_UNPACK + "\n\nयह print करता है:\n\n" + E.O_UNPACK + "\n\nबाईं ओर variables की संख्या tuple के items की संख्या के बराबर होनी चाहिए। एक बात और: एक item वाले tuple को comma चाहिए, `(\"Aspirin\",)`, क्योंकि `(\"Aspirin\")` brackets में सिर्फ़ एक string है।",
        },
        {
            "heading": "Dictionaries: key और value",
            "md": "**Dictionary** **curly braces** के अंदर **key: value** के pairs रखती है। Value को उसकी key से square brackets में ढूँढते हैं:\n\n" + E.C_DICT + "\n\nयह print करता है:\n\n" + E.O_DICT + "\n\nKeys आमतौर पर strings होती हैं, जैसे `\"name\"` या किसी drug का नाम। Values कुछ भी हो सकती हैं: numbers, strings, यहाँ तक कि lists भी। `len()` pairs गिनता है।",
            "callout": {"title": "Dictionary", "md": "Curly braces में key: value pairs का collection, जैसे {\"name\": \"Ravi\", \"age\": 54}। Value को position से नहीं, key से ढूँढते हैं।"},
        },
        {
            "heading": "बदलना और जोड़ना",
            "md": "Dictionaries mutable हैं। पहले से मौजूद key को value देने पर वह **update** होती है; नई key को value देने पर नया pair **जुड़ता** है:\n\n" + E.C_CHANGE + "\n\nयह print करता है:\n\n" + E.O_CHANGE + "\n\nDictionary में हर key सिर्फ़ एक बार आती है, इसलिए age बदली गई, दोहराई नहीं गई।",
        },
        {
            "heading": "सुरक्षित lookup और loop",
            "md": "जो key नहीं है उसे माँगने पर `KeyError` आता है। `get()` इससे बचाता है: वह उसकी जगह default value देता है। `in` keys check करता है, और `.items()` loop के लिए हर key और value देता है:\n\n" + E.C_GET + "\n\nयह print करता है:\n\n" + E.O_GET + "\n\nAspirin stock में नहीं है, इसलिए `get` ने default, 0, लौटाया।",
            "callout": {"title": "List, tuple या dictionary?", "md": "क्रम वाली readings जो बढ़ सकती हैं, उनके लिए list। Fixed record के लिए tuple। जब नाम से ढूँढना हो, तब dictionary।"},
        },
    ],
    "walkthrough": {
        "intro": "यह program adult doses एक dictionary में रखता है, drug के नाम से एक dose ढूँढता है, फिर एक नई drug जोड़ता है।",
        "keyTerms": [
            {"meaning": "key: value pairs वाली dictionary।"},
            {"meaning": "drug में रखी key की value ढूँढो।"},
            {"meaning": "नया pair जोड़ो (key पहले से हो तो update करो)।"},
            {"meaning": "True, अगर Aspirin keys में से एक है।"},
        ],
    },
    "errors": {
        "intro": "एक error न होने वाली key से आती है, दूसरी tuple बदलने की कोशिश से।",
        "examples": [
            {"title": "ऐसी key ढूँढना जो है ही नहीं", "md": "`\"Aspirin\"` नाम की कोई key नहीं है। पहले `\"Aspirin\" in doses` से check कीजिए, या error की जगह default पाने के लिए `doses.get(\"Aspirin\", 0)` use कीजिए। Keys case-sensitive भी हैं: `\"paracetamol\"` और `\"Paracetamol\"` एक नहीं।"},
            {"title": "Tuple का item बदलना", "md": "Tuples बदले नहीं जा सकते। उसकी जगह नया tuple बनाइए, `bp = (130, 84)`, या अगर values सच में बदलनी हैं तो list use कीजिए।"},
        ],
    },
    "mistakes": [
        {"mistake": "Dictionary पर index लगाना: `patient[0]`", "see": "KeyError: 0", "fix": "Dictionaries key से ढूँढी जाती हैं: `patient[\"name\"]`।"},
        {"mistake": "एक item का tuple बिना comma के लिखना: `(\"Aspirin\")`", "see": "कोई error नहीं, पर यह tuple नहीं, string है", "fix": "Comma लगाइए: `(\"Aspirin\",)`।"},
        {"mistake": "Key में अलग case लिखना: `doses[\"paracetamol\"]`", "see": "KeyError: 'paracetamol'", "fix": "Keys बिल्कुल मिलनी चाहिए, capital letters समेत।"},
        {"mistake": "गलत संख्या के variables में unpack करना: `name, strength = (\"Amoxicillin\", 500, \"mg\")`", "see": "ValueError: too many values to unpack", "fix": "हर item के लिए एक variable: `name, strength, unit = ...`।"},
    ],
    "tasks": [
        {"title": "Tuple पढ़िए", "md": "एक blood pressure reading tuple में रखी है। **Indexing** से दोनों values print कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["पहली value bp[0] है, दूसरी bp[1]।", "print(\"Systolic:\", bp[0])"]},
        {"title": "Patient की जानकारी ढूँढिए", "md": "Dictionary **patient** से patient का नाम और वज़न print कीजिए, ताकि output बिल्कुल यह हो:",
         "hints": ["patient[\"name\"] से \"Meena\" मिलता है।", "print(patient[\"name\"], \"weighs\", patient[\"weight\"], \"kg\")"]},
        {"title": "Stock update कीजिए", "md": "Cetirizine की पाँच strips बिकीं, इसलिए उसका stock अब **40** है। Azithromycin भी आई: **30** strips। Dictionary में इन्हें update और add कीजिए, फिर उसे print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["stock[\"Cetirizine\"] = 40 मौजूदा key को update करता है।", "stock[\"Azithromycin\"] = 30 नया pair जोड़ता है।"]},
        {"title": "Bug ढूँढिए", "md": "यह program patient की allergy check करता है, पर Anil की कोई allergy दर्ज नहीं, और program KeyError के साथ crash हो जाता है। **get()** से इसे ठीक कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["get() key और एक default value लेता है।", "print(allergies.get(\"Anil\", \"None recorded\"))"],
         "solutionNote": "allergies[\"Anil\"] fail होता है क्योंकि वह key है ही नहीं। get() KeyError देने की जगह default value लौटाता है।"},
    ],
    "quiz": [
        {"q": "कौन-से brackets dictionary बनाते हैं?", "why": "Dictionaries key: value pairs के साथ curly braces use करती हैं।"},
        {"q": "t = (5, 10)\nt[0] = 7\n\nक्या होता है?", "why": "Tuples immutable हैं, इसलिए item assignment से TypeError आता है।"},
        {"q": "d = {\"a\": 1, \"b\": 2}\nprint(d[\"b\"])\n\nयह क्या print करता है?", "why": "Key \"b\" की value 2 है।"},
        {"q": "जब \"x\" key न हो तो d[\"x\"] क्या देता है?", "why": "न होने वाली key KeyError देती है; get() इससे बचाता है।"},
        {"q": "stock = {\"Aspirin\": 20}\nprint(stock.get(\"Insulin\", 0))\n\nयह क्या print करता है?", "why": "Insulin key नहीं है, इसलिए get() default, 0, लौटाता है।"},
        {"q": "Patient की details field के नाम से (name, age, blood group) रखने के लिए सबसे अच्छा क्या है?", "why": "Dictionary से हर detail उसके नाम से ढूँढी जा सकती है।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 3.2 · Tuples और dictionaries",
        "children": [
            {"label": "Tuple", "children": [{"label": "(a, b) round brackets"}, {"label": "Immutable"}, {"label": "Fixed records"}]},
            {"label": "Unpack", "children": [{"label": "a, b = t"}, {"label": "संख्या मिलनी चाहिए"}, {"label": "(x,) एक item"}]},
            {"label": "Dictionary", "children": [{"label": "{key: value}"}, {"label": "d[key]"}, {"label": "Keys unique"}]},
            {"label": "बदलना", "children": [{"label": "d[key] = new"}, {"label": "नई key जुड़ती है"}, {"label": "Tuples नहीं"}]},
            {"label": "सुरक्षित use", "children": [{"label": "d.get(key, default)"}, {"label": "key in d"}, {"label": "for k, v in d.items()"}]},
            {"label": "Errors", "children": [{"label": "KeyError: key नहीं"}, {"label": "TypeError: tuple assignment"}]},
        ],
    },
    "summary": [
        "**Tuple** round brackets में लिखा जाता है, `(128, 84)`; उसे list की तरह पढ़ते हैं पर **बदल नहीं सकते**।",
        "**Unpacking** tuple को variables में बाँटता है: `name, strength = (\"Amoxicillin\", 500)`।",
        "**Dictionary** curly braces में **key: value** pairs रखती है और key से ढूँढी जाती है: `doses[\"Ibuprofen\"]`।",
        "`d[key] = value` मौजूदा key को update करता है या नई जोड़ता है; keys unique और case-sensitive हैं।",
        "न होने वाली key **KeyError** देती है; `d.get(key, default)` और `key in d` इससे बचाते हैं, और `d.items()` pairs पर loop चलाता है।",
    ],
}

T["hinglish"] = {
    "hook": {
        "title": "Naam se dhoondho, number se nahi",
        "md": "Pharmacist yeh nahi kehta ki \"formulary ki teesri drug do\". Woh poochhta hai \"**Ibuprofen** ka adult dose kya hai?\" Patient ki file bhi position se nahi padhi jaati: aap **age**, **blood group**, **allergies** dhoondhte hain.\n\nKram wali readings ke liye lists badhiya hain. Par jo jaankari **naam se** dhoondhi jaati hai, uske liye Python ke paas **dictionary** hai. Aur chhote records ke liye jo kabhi nahi badalne chahiye, jaise 128 over 84 ka blood pressure, uske paas **tuple** hai.",
    },
    "learn": [
        "**Tuple** ek fixed record kaise rakhta hai, aur use kyun nahi badal sakte",
        "Tuple ko alag variables mein **unpack** karna",
        "**Dictionary** **key: value** pairs kaise rakhti hai, jo key se dhoondhe jaate hain",
        "Values jodna, badalna, **get()** se surakshit dhoondhna, aur dictionary par loop chalana",
    ],
    "explanation": [
        {
            "heading": "Tuples: records jo nahi badalte",
            "md": "**Tuple** list jaisa hai, par **round brackets** se likha jaata hai, aur banne ke baad **badla nahi ja sakta**:\n\n" + E.C_TUPLE + "\n\nYeh print karta hai:\n\n" + E.O_TUPLE + "\n\nIndexing, slicing aur `len()` bilkul lists ki tarah kaam karte hain. Par `bp[0] = 130` error deta hai, kyunki tuples **immutable** hain. Yeh khoobi hai: darj ki gayi reading, ya drug ka (name, strength) pair, galti se nahi badalna chahiye.",
            "callout": {"title": "Tuple", "md": "Round brackets mein kram wala collection, jaise (128, 84). Ise list ki tarah padh sakte hain par kabhi badal nahi sakte."},
        },
        {
            "heading": "Tuple ko unpack karna",
            "md": "Ek line mein tuple ko alag-alag variables mein baant sakte hain. Ise **unpacking** kehte hain:\n\n" + E.C_UNPACK + "\n\nYeh print karta hai:\n\n" + E.O_UNPACK + "\n\nBaayin taraf variables ki sankhya tuple ke items ki sankhya ke barabar honi chahiye. Ek baat aur: ek item wale tuple ko comma chahiye, `(\"Aspirin\",)`, kyunki `(\"Aspirin\")` brackets mein sirf ek string hai.",
        },
        {
            "heading": "Dictionaries: key aur value",
            "md": "**Dictionary** **curly braces** ke andar **key: value** ke pairs rakhti hai. Value ko uski key se square brackets mein dhoondhte hain:\n\n" + E.C_DICT + "\n\nYeh print karta hai:\n\n" + E.O_DICT + "\n\nKeys aam taur par strings hoti hain, jaise `\"name\"` ya kisi drug ka naam. Values kuch bhi ho sakti hain: numbers, strings, yahaan tak ki lists bhi. `len()` pairs ginta hai.",
            "callout": {"title": "Dictionary", "md": "Curly braces mein key: value pairs ka collection, jaise {\"name\": \"Ravi\", \"age\": 54}. Value ko position se nahi, key se dhoondhte hain."},
        },
        {
            "heading": "Badalna aur jodna",
            "md": "Dictionaries mutable hain. Pehle se maujood key ko value dene par woh **update** hoti hai; nayi key ko value dene par naya pair **judta** hai:\n\n" + E.C_CHANGE + "\n\nYeh print karta hai:\n\n" + E.O_CHANGE + "\n\nDictionary mein har key sirf ek baar aati hai, isliye age badli gayi, dohraayi nahi gayi.",
        },
        {
            "heading": "Surakshit lookup aur loop",
            "md": "Jo key nahi hai use maangne par `KeyError` aata hai. `get()` isse bachaata hai: woh uski jagah default value deta hai. `in` keys check karta hai, aur `.items()` loop ke liye har key aur value deta hai:\n\n" + E.C_GET + "\n\nYeh print karta hai:\n\n" + E.O_GET + "\n\nAspirin stock mein nahi hai, isliye `get` ne default, 0, lautaaya.",
            "callout": {"title": "List, tuple ya dictionary?", "md": "Kram wali readings jo badh sakti hain, unke liye list. Fixed record ke liye tuple. Jab naam se dhoondhna ho, tab dictionary."},
        },
    ],
    "walkthrough": {
        "intro": "Yeh program adult doses ek dictionary mein rakhta hai, drug ke naam se ek dose dhoondhta hai, phir ek nayi drug jodta hai.",
        "keyTerms": [
            {"meaning": "key: value pairs wali dictionary."},
            {"meaning": "drug mein rakhi key ki value dhoondho."},
            {"meaning": "Naya pair jodo (key pehle se ho to update karo)."},
            {"meaning": "True, agar Aspirin keys mein se ek hai."},
        ],
    },
    "errors": {
        "intro": "Ek error na hone wali key se aati hai, doosri tuple badalne ki koshish se.",
        "examples": [
            {"title": "Aisi key dhoondhna jo hai hi nahi", "md": "`\"Aspirin\"` naam ki koi key nahi hai. Pehle `\"Aspirin\" in doses` se check kijiye, ya error ki jagah default paane ke liye `doses.get(\"Aspirin\", 0)` use kijiye. Keys case-sensitive bhi hain: `\"paracetamol\"` aur `\"Paracetamol\"` ek nahi."},
            {"title": "Tuple ka item badalna", "md": "Tuples badle nahi ja sakte. Uski jagah naya tuple banaiye, `bp = (130, 84)`, ya agar values sach mein badalni hain to list use kijiye."},
        ],
    },
    "mistakes": [
        {"mistake": "Dictionary par index lagaana: `patient[0]`", "see": "KeyError: 0", "fix": "Dictionaries key se dhoondhi jaati hain: `patient[\"name\"]`."},
        {"mistake": "Ek item ka tuple bina comma ke likhna: `(\"Aspirin\")`", "see": "Koi error nahi, par yeh tuple nahi, string hai", "fix": "Comma lagaiye: `(\"Aspirin\",)`."},
        {"mistake": "Key mein alag case likhna: `doses[\"paracetamol\"]`", "see": "KeyError: 'paracetamol'", "fix": "Keys bilkul milni chahiye, capital letters samet."},
        {"mistake": "Galat sankhya ke variables mein unpack karna: `name, strength = (\"Amoxicillin\", 500, \"mg\")`", "see": "ValueError: too many values to unpack", "fix": "Har item ke liye ek variable: `name, strength, unit = ...`."},
    ],
    "tasks": [
        {"title": "Tuple padhiye", "md": "Ek blood pressure reading tuple mein rakhi hai. **Indexing** se dono values print kijiye taaki output bilkul yeh ho:",
         "hints": ["Pehli value bp[0] hai, doosri bp[1].", "print(\"Systolic:\", bp[0])"]},
        {"title": "Patient ki jaankari dhoondhiye", "md": "Dictionary **patient** se patient ka naam aur wazan print kijiye, taaki output bilkul yeh ho:",
         "hints": ["patient[\"name\"] se \"Meena\" milta hai.", "print(patient[\"name\"], \"weighs\", patient[\"weight\"], \"kg\")"]},
        {"title": "Stock update kijiye", "md": "Cetirizine ki paanch strips biki, isliye uska stock ab **40** hai. Azithromycin bhi aayi: **30** strips. Dictionary mein inhe update aur add kijiye, phir use print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["stock[\"Cetirizine\"] = 40 maujooda key ko update karta hai.", "stock[\"Azithromycin\"] = 30 naya pair jodta hai."]},
        {"title": "Bug dhoondhiye", "md": "Yeh program patient ki allergy check karta hai, par Anil ki koi allergy darj nahi, aur program KeyError ke saath crash ho jaata hai. **get()** se ise theek kijiye taaki output bilkul yeh ho:",
         "hints": ["get() key aur ek default value leta hai.", "print(allergies.get(\"Anil\", \"None recorded\"))"],
         "solutionNote": "allergies[\"Anil\"] fail hota hai kyunki woh key hai hi nahi. get() KeyError dene ki jagah default value lautaata hai."},
    ],
    "quiz": [
        {"q": "Kaun-se brackets dictionary banaate hain?", "why": "Dictionaries key: value pairs ke saath curly braces use karti hain."},
        {"q": "t = (5, 10)\nt[0] = 7\n\nKya hota hai?", "why": "Tuples immutable hain, isliye item assignment se TypeError aata hai."},
        {"q": "d = {\"a\": 1, \"b\": 2}\nprint(d[\"b\"])\n\nYeh kya print karta hai?", "why": "Key \"b\" ki value 2 hai."},
        {"q": "Jab \"x\" key na ho to d[\"x\"] kya deta hai?", "why": "Na hone wali key KeyError deti hai; get() isse bachaata hai."},
        {"q": "stock = {\"Aspirin\": 20}\nprint(stock.get(\"Insulin\", 0))\n\nYeh kya print karta hai?", "why": "Insulin key nahi hai, isliye get() default, 0, lautaata hai."},
        {"q": "Patient ki details field ke naam se (name, age, blood group) rakhne ke liye sabse achha kya hai?", "why": "Dictionary se har detail uske naam se dhoondhi ja sakti hai."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 3.2 · Tuples aur dictionaries",
        "children": [
            {"label": "Tuple", "children": [{"label": "(a, b) round brackets"}, {"label": "Immutable"}, {"label": "Fixed records"}]},
            {"label": "Unpack", "children": [{"label": "a, b = t"}, {"label": "Sankhya milni chahiye"}, {"label": "(x,) ek item"}]},
            {"label": "Dictionary", "children": [{"label": "{key: value}"}, {"label": "d[key]"}, {"label": "Keys unique"}]},
            {"label": "Badalna", "children": [{"label": "d[key] = new"}, {"label": "Nayi key judti hai"}, {"label": "Tuples nahi"}]},
            {"label": "Surakshit use", "children": [{"label": "d.get(key, default)"}, {"label": "key in d"}, {"label": "for k, v in d.items()"}]},
            {"label": "Errors", "children": [{"label": "KeyError: key nahi"}, {"label": "TypeError: tuple assignment"}]},
        ],
    },
    "summary": [
        "**Tuple** round brackets mein likha jaata hai, `(128, 84)`; use list ki tarah padhte hain par **badal nahi sakte**.",
        "**Unpacking** tuple ko variables mein baantta hai: `name, strength = (\"Amoxicillin\", 500)`.",
        "**Dictionary** curly braces mein **key: value** pairs rakhti hai aur key se dhoondhi jaati hai: `doses[\"Ibuprofen\"]`.",
        "`d[key] = value` maujooda key ko update karta hai ya nayi jodta hai; keys unique aur case-sensitive hain.",
        "Na hone wali key **KeyError** deti hai; `d.get(key, default)` aur `key in d` isse bachaate hain, aur `d.items()` pairs par loop chalaata hai.",
    ],
}

T["kn"] = {
    "hook": {
        "title": "Number ಇಂದ ಅಲ್ಲ, ಹೆಸರಿನಿಂದ ಹುಡುಕಿ",
        "md": "Pharmacist \"formulary ನ ಮೂರನೇ drug ಕೊಡಿ\" ಅಂತ ಹೇಳಲ್ಲ. \"**Ibuprofen** ನ adult dose ಎಷ್ಟು?\" ಅಂತ ಕೇಳ್ತಾರೆ. Patient file ಕೂಡ position ಇಂದ ಓದಲ್ಲ: ನೀವು **age**, **blood group**, **allergies** ಹುಡುಕುತ್ತೀರಿ.\n\nಕ್ರಮದ readings ಗೆ lists ಚೆನ್ನಾಗಿವೆ. ಆದರೆ **ಹೆಸರಿನಿಂದ** ಹುಡುಕುವ ಮಾಹಿತಿಗೆ Python ನಲ್ಲಿ **dictionary** ಇದೆ. ಯಾವತ್ತೂ ಬದಲಾಗಬಾರದ ಸಣ್ಣ records ಗೆ, 128 over 84 ಎಂಬ blood pressure ತರಹ, **tuple** ಇದೆ.",
    },
    "learn": [
        "**Tuple** ಒಂದು fixed record ಅನ್ನು ಹೇಗೆ ಇಡುತ್ತೆ, ಮತ್ತು ಅದನ್ನು ಯಾಕೆ ಬದಲಾಯಿಸಲು ಆಗಲ್ಲ",
        "Tuple ಅನ್ನು ಬೇರೆ variables ಆಗಿ **unpack** ಮಾಡುವುದು",
        "**Dictionary** **key: value** pairs ಅನ್ನು ಹೇಗೆ ಇಡುತ್ತೆ, key ಇಂದ ಹುಡುಕುವುದು",
        "Values ಸೇರಿಸುವುದು, ಬದಲಾಯಿಸುವುದು, **get()** ಇಂದ ಸುರಕ್ಷಿತವಾಗಿ ಹುಡುಕುವುದು, dictionary ಮೇಲೆ loop",
    ],
    "explanation": [
        {
            "heading": "Tuples: ಬದಲಾಗದ records",
            "md": "**Tuple** list ತರಹವೇ, ಆದರೆ **round brackets** ಇಂದ ಬರೆಯುತ್ತಾರೆ, ಮತ್ತು ಮಾಡಿದ ಮೇಲೆ **ಬದಲಾಯಿಸಲು ಆಗಲ್ಲ**:\n\n" + E.C_TUPLE + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_TUPLE + "\n\nIndexing, slicing ಮತ್ತು `len()` lists ತರಹವೇ ಕೆಲಸ ಮಾಡುತ್ತವೆ. ಆದರೆ `bp[0] = 130` error ಕೊಡುತ್ತೆ, ಯಾಕಂದ್ರೆ tuples **immutable**. ಇದು ಒಳ್ಳೆಯದೇ: ದಾಖಲಾದ reading, ಅಥವಾ drug ನ (name, strength) pair, ತಪ್ಪಿ ಬದಲಾಗಬಾರದು.",
            "callout": {"title": "Tuple", "md": "Round brackets ಒಳಗಿನ ಕ್ರಮದ collection, (128, 84) ತರಹ. List ತರಹ ಓದಬಹುದು ಆದರೆ ಯಾವತ್ತೂ ಬದಲಾಯಿಸಲು ಆಗಲ್ಲ."},
        },
        {
            "heading": "Tuple ಅನ್ನು unpack ಮಾಡುವುದು",
            "md": "ಒಂದೇ line ನಲ್ಲಿ tuple ಅನ್ನು ಬೇರೆ ಬೇರೆ variables ಆಗಿ ಒಡೆಯಬಹುದು. ಇದನ್ನು **unpacking** ಅಂತಾರೆ:\n\n" + E.C_UNPACK + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_UNPACK + "\n\nಎಡಗಡೆ ಇರುವ variables ಸಂಖ್ಯೆ tuple ನ items ಸಂಖ್ಯೆಗೆ ಸಮ ಇರಬೇಕು. ಇನ್ನೊಂದು ವಿಷಯ: ಒಂದೇ item ಇರುವ tuple ಗೆ comma ಬೇಕು, `(\"Aspirin\",)`, ಯಾಕಂದ್ರೆ `(\"Aspirin\")` brackets ಒಳಗಿನ ಒಂದು string ಅಷ್ಟೇ.",
        },
        {
            "heading": "Dictionaries: key ಮತ್ತು value",
            "md": "**Dictionary** **curly braces** ಒಳಗೆ **key: value** pairs ಇಡುತ್ತೆ. Value ಅನ್ನು ಅದರ key ಇಂದ square brackets ನಲ್ಲಿ ಹುಡುಕುತ್ತೀರಿ:\n\n" + E.C_DICT + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_DICT + "\n\nKeys ಸಾಮಾನ್ಯವಾಗಿ strings, `\"name\"` ಅಥವಾ ಒಂದು drug ನ ಹೆಸರು ತರಹ. Values ಏನಾದರೂ ಆಗಬಹುದು: numbers, strings, lists ಕೂಡ. `len()` pairs ಎಣಿಸುತ್ತೆ.",
            "callout": {"title": "Dictionary", "md": "Curly braces ಒಳಗಿನ key: value pairs ನ collection, {\"name\": \"Ravi\", \"age\": 54} ತರಹ. Value ಅನ್ನು position ಇಂದ ಅಲ್ಲ, key ಇಂದ ಹುಡುಕುತ್ತೀರಿ."},
        },
        {
            "heading": "ಬದಲಾಯಿಸುವುದು ಮತ್ತು ಸೇರಿಸುವುದು",
            "md": "Dictionaries mutable. ಇರುವ key ಗೆ value ಕೊಟ್ಟರೆ ಅದು **update** ಆಗುತ್ತೆ; ಹೊಸ key ಗೆ value ಕೊಟ್ಟರೆ ಹೊಸ pair **ಸೇರುತ್ತೆ**:\n\n" + E.C_CHANGE + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_CHANGE + "\n\nDictionary ನಲ್ಲಿ ಪ್ರತಿ key ಒಂದೇ ಸಲ ಇರುತ್ತೆ, ಹಾಗಾಗಿ age ಬದಲಾಯಿತು, ಎರಡು ಸಲ ಬರಲಿಲ್ಲ.",
        },
        {
            "heading": "ಸುರಕ್ಷಿತ lookup ಮತ್ತು loop",
            "md": "ಇಲ್ಲದ key ಕೇಳಿದರೆ `KeyError` ಬರುತ್ತೆ. `get()` ಇದನ್ನು ತಪ್ಪಿಸುತ್ತೆ: ಅದರ ಬದಲು default value ಕೊಡುತ್ತೆ. `in` keys check ಮಾಡುತ್ತೆ, ಮತ್ತು `.items()` loop ಗಾಗಿ ಪ್ರತಿ key ಮತ್ತು value ಕೊಡುತ್ತೆ:\n\n" + E.C_GET + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_GET + "\n\nAspirin stock ನಲ್ಲಿ ಇಲ್ಲ, ಹಾಗಾಗಿ `get` default, 0, ಕೊಟ್ಟಿತು.",
            "callout": {"title": "List, tuple ಅಥವಾ dictionary?", "md": "ಬೆಳೆಯಬಹುದಾದ ಕ್ರಮದ readings ಗೆ list. Fixed record ಗೆ tuple. ಹೆಸರಿನಿಂದ ಹುಡುಕುವಾಗ dictionary."},
        },
    ],
    "walkthrough": {
        "intro": "ಈ program adult doses ಅನ್ನು ಒಂದು dictionary ನಲ್ಲಿ ಇಡುತ್ತೆ, drug ಹೆಸರಿನಿಂದ ಒಂದು dose ಹುಡುಕುತ್ತೆ, ನಂತರ ಹೊಸ drug ಸೇರಿಸುತ್ತೆ.",
        "keyTerms": [
            {"meaning": "key: value pairs ಇರುವ dictionary."},
            {"meaning": "drug ನಲ್ಲಿರುವ key ಯ value ಹುಡುಕು."},
            {"meaning": "ಹೊಸ pair ಸೇರಿಸು (key ಇದ್ದರೆ update ಮಾಡು)."},
            {"meaning": "Aspirin keys ನಲ್ಲಿ ಒಂದಾಗಿದ್ದರೆ True."},
        ],
    },
    "errors": {
        "intro": "ಒಂದು error ಇಲ್ಲದ key ಇಂದ, ಇನ್ನೊಂದು tuple ಬದಲಾಯಿಸಲು ಪ್ರಯತ್ನಿಸುವುದರಿಂದ ಬರುತ್ತೆ.",
        "examples": [
            {"title": "ಇಲ್ಲದ key ಹುಡುಕುವುದು", "md": "`\"Aspirin\"` ಎಂಬ key ಇಲ್ಲ. ಮೊದಲು `\"Aspirin\" in doses` ಇಂದ check ಮಾಡಿ, ಅಥವಾ error ಬದಲು default ಪಡೆಯಲು `doses.get(\"Aspirin\", 0)` ಬಳಸಿ. Keys case-sensitive ಕೂಡ: `\"paracetamol\"` ಮತ್ತು `\"Paracetamol\"` ಒಂದೇ ಅಲ್ಲ."},
            {"title": "Tuple ನ item ಬದಲಾಯಿಸುವುದು", "md": "Tuples ಬದಲಾಯಿಸಲು ಆಗಲ್ಲ. ಅದರ ಬದಲು ಹೊಸ tuple ಮಾಡಿ, `bp = (130, 84)`, ಅಥವಾ values ನಿಜವಾಗಿ ಬದಲಾಗಬೇಕಾದರೆ list ಬಳಸಿ."},
        ],
    },
    "mistakes": [
        {"mistake": "Dictionary ಗೆ index ಹಾಕುವುದು: `patient[0]`", "see": "KeyError: 0", "fix": "Dictionaries ಅನ್ನು key ಇಂದ ಹುಡುಕುತ್ತಾರೆ: `patient[\"name\"]`."},
        {"mistake": "ಒಂದು item ನ tuple ಅನ್ನು comma ಇಲ್ಲದೆ ಬರೆಯುವುದು: `(\"Aspirin\")`", "see": "Error ಇಲ್ಲ, ಆದರೆ ಇದು tuple ಅಲ್ಲ, string", "fix": "Comma ಹಾಕಿ: `(\"Aspirin\",)`."},
        {"mistake": "Key ನಲ್ಲಿ ಬೇರೆ case ಬರೆಯುವುದು: `doses[\"paracetamol\"]`", "see": "KeyError: 'paracetamol'", "fix": "Keys ನಿಖರವಾಗಿ ಹೊಂದಬೇಕು, capital letters ಸಹಿತ."},
        {"mistake": "ತಪ್ಪು ಸಂಖ್ಯೆಯ variables ಗೆ unpack ಮಾಡುವುದು: `name, strength = (\"Amoxicillin\", 500, \"mg\")`", "see": "ValueError: too many values to unpack", "fix": "ಪ್ರತಿ item ಗೆ ಒಂದು variable: `name, strength, unit = ...`."},
    ],
    "tasks": [
        {"title": "Tuple ಓದಿ", "md": "ಒಂದು blood pressure reading tuple ನಲ್ಲಿ ಇದೆ. **Indexing** ಇಂದ ಎರಡೂ values print ಮಾಡಿ, output ನಿಖರವಾಗಿ ಹೀಗಿರಲಿ:",
         "hints": ["ಮೊದಲ value bp[0], ಎರಡನೇದು bp[1].", "print(\"Systolic:\", bp[0])"]},
        {"title": "Patient ಮಾಹಿತಿ ಹುಡುಕಿ", "md": "**patient** dictionary ಇಂದ patient ನ ಹೆಸರು ಮತ್ತು ತೂಕ print ಮಾಡಿ, output ನಿಖರವಾಗಿ ಹೀಗಿರಲಿ:",
         "hints": ["patient[\"name\"] ಇಂದ \"Meena\" ಸಿಗುತ್ತೆ.", "print(patient[\"name\"], \"weighs\", patient[\"weight\"], \"kg\")"]},
        {"title": "Stock update ಮಾಡಿ", "md": "Cetirizine ನ ಐದು strips ಮಾರಾಟ ಆದವು, ಹಾಗಾಗಿ ಈಗ stock **40**. Azithromycin ಕೂಡ ಬಂತು: **30** strips. Dictionary ನಲ್ಲಿ ಇವನ್ನು update ಮತ್ತು add ಮಾಡಿ, ನಂತರ print ಮಾಡಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["stock[\"Cetirizine\"] = 40 ಇರುವ key ಅನ್ನು update ಮಾಡುತ್ತೆ.", "stock[\"Azithromycin\"] = 30 ಹೊಸ pair ಸೇರಿಸುತ್ತೆ."]},
        {"title": "Bug ಹುಡುಕಿ", "md": "ಈ program patient ನ allergy check ಮಾಡುತ್ತೆ, ಆದರೆ Anil ಗೆ ಯಾವ allergy ದಾಖಲಾಗಿಲ್ಲ, program KeyError ಜೊತೆ crash ಆಗುತ್ತೆ. **get()** ಇಂದ ಸರಿ ಮಾಡಿ, output ನಿಖರವಾಗಿ ಹೀಗಿರಲಿ:",
         "hints": ["get() key ಮತ್ತು ಒಂದು default value ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ.", "print(allergies.get(\"Anil\", \"None recorded\"))"],
         "solutionNote": "allergies[\"Anil\"] fail ಆಗುತ್ತೆ ಯಾಕಂದ್ರೆ ಆ key ಇಲ್ಲ. get() KeyError ಬದಲು default value ಕೊಡುತ್ತೆ."},
    ],
    "quiz": [
        {"q": "ಯಾವ brackets dictionary ಮಾಡುತ್ತವೆ?", "why": "Dictionaries key: value pairs ಜೊತೆ curly braces ಬಳಸುತ್ತವೆ."},
        {"q": "t = (5, 10)\nt[0] = 7\n\nಏನಾಗುತ್ತೆ?", "why": "Tuples immutable, ಹಾಗಾಗಿ item assignment ಇಂದ TypeError ಬರುತ್ತೆ."},
        {"q": "d = {\"a\": 1, \"b\": 2}\nprint(d[\"b\"])\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "Key \"b\" ಯ value 2."},
        {"q": "\"x\" key ಇಲ್ಲದಿದ್ದಾಗ d[\"x\"] ಏನು ಕೊಡುತ್ತೆ?", "why": "ಇಲ್ಲದ key KeyError ಕೊಡುತ್ತೆ; get() ಅದನ್ನು ತಪ್ಪಿಸುತ್ತೆ."},
        {"q": "stock = {\"Aspirin\": 20}\nprint(stock.get(\"Insulin\", 0))\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "Insulin key ಅಲ್ಲ, ಹಾಗಾಗಿ get() default, 0, ಕೊಡುತ್ತೆ."},
        {"q": "Patient details ಅನ್ನು field ಹೆಸರಿನಿಂದ (name, age, blood group) ಇಡಲು ಯಾವುದು ಉತ್ತಮ?", "why": "Dictionary ಇಂದ ಪ್ರತಿ detail ಅನ್ನು ಅದರ ಹೆಸರಿನಿಂದ ಹುಡುಕಬಹುದು."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 3.2 · Tuples ಮತ್ತು dictionaries",
        "children": [
            {"label": "Tuple", "children": [{"label": "(a, b) round brackets"}, {"label": "Immutable"}, {"label": "Fixed records"}]},
            {"label": "Unpack", "children": [{"label": "a, b = t"}, {"label": "ಸಂಖ್ಯೆ ಹೊಂದಬೇಕು"}, {"label": "(x,) ಒಂದು item"}]},
            {"label": "Dictionary", "children": [{"label": "{key: value}"}, {"label": "d[key]"}, {"label": "Keys unique"}]},
            {"label": "ಬದಲಾವಣೆ", "children": [{"label": "d[key] = new"}, {"label": "ಹೊಸ key ಸೇರುತ್ತೆ"}, {"label": "Tuples ಅಲ್ಲ"}]},
            {"label": "ಸುರಕ್ಷಿತ ಬಳಕೆ", "children": [{"label": "d.get(key, default)"}, {"label": "key in d"}, {"label": "for k, v in d.items()"}]},
            {"label": "Errors", "children": [{"label": "KeyError: key ಇಲ್ಲ"}, {"label": "TypeError: tuple assignment"}]},
        ],
    },
    "summary": [
        "**Tuple** round brackets ನಲ್ಲಿ, `(128, 84)`; list ತರಹ ಓದಬಹುದು ಆದರೆ **ಬದಲಾಯಿಸಲು ಆಗಲ್ಲ**.",
        "**Unpacking** tuple ಅನ್ನು variables ಆಗಿ ಒಡೆಯುತ್ತೆ: `name, strength = (\"Amoxicillin\", 500)`.",
        "**Dictionary** curly braces ನಲ್ಲಿ **key: value** pairs ಇಡುತ್ತೆ, key ಇಂದ ಹುಡುಕುತ್ತಾರೆ: `doses[\"Ibuprofen\"]`.",
        "`d[key] = value` ಇರುವ key update ಮಾಡುತ್ತೆ ಅಥವಾ ಹೊಸದು ಸೇರಿಸುತ್ತೆ; keys unique ಮತ್ತು case-sensitive.",
        "ಇಲ್ಲದ key **KeyError** ಕೊಡುತ್ತೆ; `d.get(key, default)` ಮತ್ತು `key in d` ಅದನ್ನು ತಪ್ಪಿಸುತ್ತವೆ, `d.items()` pairs ಮೇಲೆ loop.",
    ],
}

NARR = {
    "hi": [
        "यह program एक छोटी formulary है। यह drug के नाम से dose ढूँढता है, और फिर एक नई drug जोड़ता है।",
        "Comment बताता है कि doses milligrams में हैं और drug के नाम से ढूँढे जाते हैं।",
        "Curly braces dictionary बनाते हैं। हर drug का नाम key है, और उसका dose value है। तीन pairs हैं।",
        "drug में वह नाम है जो हमें ढूँढना है: Ibuprofen।",
        "doses of drug, key Ibuprofen ढूँढता है और उसकी value देता है, चार सौ। कोई position नहीं गिननी।",
        "Amoxicillin अभी key नहीं है, इसलिए यह line नया pair जोड़ती है: Amoxicillin, पाँच सौ।",
        "len pairs गिनता है। अब चार drugs हैं।",
        "in keys check करता है। Aspirin उनमें नहीं है, इसलिए False print होता है।",
    ],
    "hinglish": [
        "Yeh program ek chhoti formulary hai. Yeh drug ke naam se dose dhoondhta hai, aur phir ek nayi drug jodta hai.",
        "Comment batata hai ki doses milligrams mein hain aur drug ke naam se dhoondhe jaate hain.",
        "Curly braces dictionary banaate hain. Har drug ka naam key hai, aur uska dose value hai. Teen pairs hain.",
        "drug mein woh naam hai jo humein dhoondhna hai: Ibuprofen.",
        "doses of drug, key Ibuprofen dhoondhta hai aur uski value deta hai, chaar sau. Koi position nahi ginni.",
        "Amoxicillin abhi key nahi hai, isliye yeh line naya pair jodti hai: Amoxicillin, paanch sau.",
        "len pairs ginta hai. Ab chaar drugs hain.",
        "in keys check karta hai. Aspirin unmein nahi hai, isliye False print hota hai.",
    ],
    "kn": [
        "ಈ program ಒಂದು ಸಣ್ಣ formulary. ಇದು drug ಹೆಸರಿನಿಂದ dose ಹುಡುಕುತ್ತೆ, ನಂತರ ಹೊಸ drug ಸೇರಿಸುತ್ತೆ.",
        "Comment doses milligrams ನಲ್ಲಿವೆ, drug ಹೆಸರಿನಿಂದ ಹುಡುಕುತ್ತಾರೆ ಅಂತ ಹೇಳುತ್ತೆ.",
        "Curly braces dictionary ಮಾಡುತ್ತವೆ. ಪ್ರತಿ drug ಹೆಸರು key, ಅದರ dose value. ಮೂರು pairs ಇವೆ.",
        "drug ನಲ್ಲಿ ನಾವು ಹುಡುಕಬೇಕಾದ ಹೆಸರು ಇದೆ: Ibuprofen.",
        "doses of drug, key Ibuprofen ಹುಡುಕಿ ಅದರ value ಕೊಡುತ್ತೆ, ನಾನೂರು. ಯಾವ position ಎಣಿಸುವ ಅಗತ್ಯ ಇಲ್ಲ.",
        "Amoxicillin ಇನ್ನೂ key ಅಲ್ಲ, ಹಾಗಾಗಿ ಈ line ಹೊಸ pair ಸೇರಿಸುತ್ತೆ: Amoxicillin, ಐನೂರು.",
        "len pairs ಎಣಿಸುತ್ತೆ. ಈಗ ನಾಲ್ಕು drugs.",
        "in keys check ಮಾಡುತ್ತೆ. Aspirin ಅದರಲ್ಲಿ ಇಲ್ಲ, ಹಾಗಾಗಿ False print ಆಗುತ್ತೆ.",
    ],
}

ANIM = {
    "hi": [
        "Dictionary pairs रखती है। हर drug का नाम key है, और उसका dose value।",
        "Python सीधे key Ibuprofen पर जाता है और उसकी value लौटाता है, चार सौ। कोई position नहीं गिननी पड़ती।",
        "नई key को value देने से नया pair जुड़ता है: Amoxicillin, पाँच सौ।",
        "in keys check करता है। Aspirin उनमें नहीं है, इसलिए जवाब False है।",
    ],
    "hinglish": [
        "Dictionary pairs rakhti hai. Har drug ka naam key hai, aur uska dose value.",
        "Python seedhe key Ibuprofen par jaata hai aur uski value lautaata hai, chaar sau. Koi position nahi ginni padti.",
        "Nayi key ko value dene se naya pair judta hai: Amoxicillin, paanch sau.",
        "in keys check karta hai. Aspirin unmein nahi hai, isliye jawaab False hai.",
    ],
    "kn": [
        "Dictionary pairs ಇಡುತ್ತೆ. ಪ್ರತಿ drug ಹೆಸರು key, ಅದರ dose value.",
        "Python ನೇರವಾಗಿ key Ibuprofen ಗೆ ಹೋಗಿ ಅದರ value ಕೊಡುತ್ತೆ, ನಾನೂರು. ಯಾವ position ಎಣಿಸಬೇಕಿಲ್ಲ.",
        "ಹೊಸ key ಗೆ value ಕೊಟ್ಟರೆ ಹೊಸ pair ಸೇರುತ್ತೆ: Amoxicillin, ಐನೂರು.",
        "in keys check ಮಾಡುತ್ತೆ. Aspirin ಅದರಲ್ಲಿ ಇಲ್ಲ, ಹಾಗಾಗಿ ಉತ್ತರ False.",
    ],
}

if __name__ == "__main__":
    build("3-2", "anim-lookup", T, NARR, ANIM)

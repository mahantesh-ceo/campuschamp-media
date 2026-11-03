"""Lesson 2.1 translations (Hindi, Hinglish, Kannada) and voice scripts.

Run to write content/bp101t/2-1/{hi,hinglish,kn}.json and scripts/bp101t/2-1.json.
"""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import build  # noqa: E402

_spec = importlib.util.spec_from_file_location("en21", os.path.join(os.path.dirname(__file__), "..", "lessons", "bp101t_2-1_en.py"))
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)
C_IF, C_ELSE, C_ELIF, C_AND = E.C_IF, E.C_ELSE, E.C_ELIF, E.C_AND
O_IF = "```\nFever\nCheck done\n```"
ELIF_SYNTAX = "```python\nif condition1:\n    block1\nelif condition2:\n    block2\nelse:\n    block3\n```"

T = {}

# ======================================================================= Hindi
T["hi"] = {
    "hook": {
        "title": "क्या यह बुखार है?",
        "md": "Nurse thermometer पढ़ती है: **38.6 °C**। क्या यह बुखार है? तेज़ बुखार? या normal?\n\nPharmacist दिन भर ऐसे फ़ैसले लेता है: stock कम है क्या, dose ज़्यादा है क्या, patient बच्चा है क्या? अब तक आपके programs हर line ऊपर से नीचे चलाते थे। इस lesson में आपका program **तय करेगा** कि कौन-सी lines चलानी हैं।",
    },
    "learn": [
        "**if** कुछ lines तभी कैसे चलाता है जब condition **True** हो",
        "Python में **colon** और **indentation** क्यों ज़रूरी हैं",
        "**if-else** दो रास्तों में से एक कैसे चुनता है",
        "**if-elif-else** कई रास्तों में से एक कैसे चुनता है, और क्रम क्यों मायने रखता है",
    ],
    "explanation": [
        {
            "heading": "if: कुछ lines तभी चलाओ जब ज़रूरत हो",
            "md": "**if statement** हाँ-या-ना वाला सवाल पूछता है। जवाब `True` हो तो Python उसके नीचे की lines चलाता है। `False` हो तो उन्हें छोड़ देता है।\n\n" + C_IF + "\n\nयह print करता है:\n\n" + O_IF + "\n\nसवाल `temp >= 38.0` को **condition** कहते हैं। ये comparison operators आपने Lesson 1.4 में देखे थे: `==`, `!=`, `<`, `>`, `<=` और `>=`। हर एक `True` या `False` देता है।\n\n`temp = 37.0` करके देखिए। Condition `False` है, इसलिए `Fever` छूट जाता है, और सिर्फ़ `Check done` print होता है।",
            "callout": {"title": "Condition", "md": "ऐसा expression जो True या False हो, जैसे temp >= 38.0। यही तय करता है कि if के नीचे की lines चलेंगी या नहीं।"},
        },
        {
            "heading": "Colon और indentation",
            "md": "दो छोटी चीज़ें Python को बताती हैं कि `if` में क्या-क्या आता है:\n\n1. `if` line के आखिर में **colon** `:`।\n2. **Indentation**: `if` की lines **4 spaces** से शुरू होती हैं।\n\nIndent की हुई lines को **block** कहते हैं। जहाँ indentation खत्म, वहाँ block खत्म। ऊपर के example में `print(\"Fever\")` block के अंदर है, और `print(\"Check done\")` बाहर है, इसलिए वह हमेशा चलता है।\n\nज़्यादातर IDEs colon के बाद Enter दबाने पर 4 spaces अपने-आप डाल देते हैं।",
            "callout": {"title": "Indentation सजावट नहीं है", "md": "Python में line की शुरुआत के spaces program का काम बदल देते हैं। 4 spaces use कीजिए, और block की हर line एक सीध में रखिए।"},
        },
        {
            "heading": "if-else: दो में से एक रास्ता",
            "md": "अक्सर दोनों हालात में कुछ होना चाहिए। **else** दूसरा रास्ता देता है: यह तब चलता है जब condition `False` हो।\n\nजब किसी दवा का stock reorder level से नीचे जाता है, pharmacy उसे फिर से मँगाती है:\n\n" + C_ELSE + "\n\nयह `Reorder now` print करता है, क्योंकि 12, 20 से कम है। `stock = 35` होता तो `Stock OK` print होता।\n\nदोनों में से ठीक एक block चलता है: न दोनों, न कोई नहीं। `else` की अपनी कोई condition नहीं होती; यह भी colon पर खत्म होता है।",
        },
        {
            "heading": "if-elif-else: कई में से एक रास्ता",
            "md": "जब दो से ज़्यादा हालात हों, **elif** use कीजिए, यानी \"else if\"। यह ऊपर वाले number (systolic, mmHg में) से blood pressure की एक आसान जाँच है:\n\n" + C_ELIF + "\n\nयह `High BP, stage 1` print करता है।\n\nPython conditions को **ऊपर से नीचे** जाँचता है और **पहला** block चलाता है जिसकी condition `True` हो। फिर chain का बाकी सब छोड़ देता है। 134 न 120 से कम है, न 130 से, पर 140 से कम है, इसलिए तीसरा block चलता है।\n\nजितने चाहिए उतने `elif` रख सकते हैं। आखिर का `else` ज़रूरी नहीं; यह वो सब पकड़ता है जो ऊपर की conditions ने नहीं पकड़ा।",
            "callout": {"title": "क्रम मायने रखता है", "md": "Python पहली True condition पर रुक जाता है, इसलिए सबसे narrow case पहले जाँचिए। अगर systolic < 140 पहले होता, तो 110 भी stage 1 print करता।"},
        },
        {
            "heading": "and, or, not से conditions जोड़ना",
            "md": "Lesson 1.4 के logical operators कई conditions को एक में जोड़ते हैं:\n\n- **`and`** तभी `True` है जब **दोनों** तरफ़ `True` हो।\n- **`or`** तब `True` है जब **कम से कम एक** तरफ़ `True` हो।\n- **`not`** `True` को `False` और `False` को `True` कर देता है।\n\nबच्चों और बुज़ुर्ग patients के dose में अक्सर ज़्यादा ध्यान चाहिए:\n\n" + C_AND + "\n\nयह `Extra care: check the dose` print करता है, क्योंकि `age >= 65` `True` है, और `or` को सिर्फ़ एक तरफ़ `True` चाहिए।",
        },
    ],
    "walkthrough": {
        "intro": "यह program शरीर का temperature पढ़कर सही message print करता है। तीन में से सिर्फ़ एक message print हो सकता है।",
        "keyTerms": [
            {"meaning": "Block तभी चलाओ जब condition True हो।"},
            {"meaning": "\"Else if\": ऊपर की conditions False हों तो एक और condition जाँचो।"},
            {"meaning": "जब ऊपर की कोई condition True न हो, यह block चलाओ।"},
            {"meaning": "हर if, elif और else line इसी पर खत्म होती है।"},
            {"meaning": "Block में आने वाली lines को दिखाते हैं।"},
        ],
    },
    "errors": {
        "intro": "if की ज़्यादातर errors colon या indentation छूटने से आती हैं।",
        "examples": [
            {"title": "Colon भूल जाना", "md": "हर `if`, `elif` और `else` line colon पर खत्म होनी चाहिए। `if temp >= 38.0:` लिखिए।"},
            {"title": "Block को indent करना भूल जाना", "md": "Colon के बाद Python को कम से कम एक indent की हुई line चाहिए। `print(\"Fever\")` से पहले 4 spaces लगाइए।"},
        ],
    },
    "mistakes": [
        {"mistake": "Condition में `==` की जगह `=` लिखना, जैसे `if dose = 500:`", "see": "SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?", "fix": "`=` value store करता है; `==` तुलना करता है। `if dose == 500:` लिखिए।"},
        {"mistake": "बड़ी condition पहले रखना, जैसे `elif temp >= 39.5` से पहले `if temp >= 38.0`", "see": "कोई error नहीं, पर तेज़ बुखार पर भी सिर्फ़ \"Fever\" print होता है", "fix": "सबसे narrow case पहले: `temp >= 39.5`, फिर `temp >= 38.0`।"},
        {"mistake": "`else` को condition देना, जैसे `else temp < 38.0:`", "see": "SyntaxError: expected ':'", "fix": "`else` कोई condition नहीं लेता। `elif temp < 38.0:` या सिर्फ़ `else:` लिखिए।"},
        {"mistake": "अलग capitals वाला text तुलना करना, जैसे drug \"Aspirin\" हो और `if drug == \"aspirin\"`", "see": "कोई error नहीं, पर condition False आती है", "fix": "एक ही case में तुलना कीजिए: `if drug.lower() == \"aspirin\":`।"},
    ],
    "tasks": [
        {"title": "Reorder करें या नहीं?", "md": "10 strips से कम stock का मतलब है pharmacy को reorder करना होगा। **if-else** use कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["ऐसे शुरू कीजिए: if stock < 10:", "if stock < 10:\n    print(\"Reorder\")\nelse:\n    print(\"In stock\")"]},
        {"title": "Dose की limit जाँचिए", "md": "लिखा गया एक बार का dose limit से ज़्यादा है। Dose के साथ warning print कीजिए, बिल्कुल ऐसे:",
         "hints": ["> से तुलना कीजिए: if dose > max_dose:", "f-string use कीजिए: print(f\"Too high: {dose} mg\")"]},
        {"title": "Result की class", "md": "**if-elif-else** use कीजिए: 75 या ज़्यादा \"Distinction\", 60 या ज़्यादा \"First class\", 50 या ज़्यादा \"Second class\", और उससे कम \"Fail\"। 72 marks के लिए output बिल्कुल यह होना चाहिए:",
         "hints": ["सबसे ऊँची limit पहले जाँचिए: if marks >= 75:", "if marks >= 75:\n    print(\"Distinction\")\nelif marks >= 60:\n    print(\"First class\")\nelif marks >= 50:\n    print(\"Second class\")\nelse:\n    print(\"Fail\")"]},
        {"title": "Bug ढूँढिए", "md": "40.1 temperature पर \"High fever\" print होना चाहिए, पर यह program \"Fever\" print करता है। कोई error message नहीं है। इसे ठीक कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["Python पहला वो block चलाता है जिसकी condition True हो। क्या 40.1 >= 38.0 है?", "पहले temp >= 39.5 जाँचिए, फिर temp >= 38.0।"],
         "solutionNote": "40.1 >= 38.0 True है, इसलिए पहला block चल गया और बाकी छूट गए। Narrow check (39.5) पहले रखने से यह ठीक हो जाता है।"},
    ],
    "quiz": [
        {"q": "x = 5\nif x > 3:\n    print(\"A\")\nelse:\n    print(\"B\")\n\nयह क्या print करता है?", "why": "5 > 3 True है, इसलिए if block चलता है और else छूट जाता है।"},
        {"q": "if line के आखिर में क्या आना चाहिए?", "why": "if, elif और else, तीनों lines colon पर खत्म होती हैं।"},
        {"q": "if-elif-else chain में कितने blocks चलते हैं?", "why": "Python पहला True condition वाला block (या else) चलाता है, फिर बाकी छोड़ देता है।"},
        {"q": "temp = 37.0\nif temp >= 38.0:\n    print(\"Fever\")\nelse:\n    print(\"Normal\")\n\nयह क्या print करता है?", "why": "37.0 >= 38.0 False है, इसलिए else block चलता है।"},
        {"q": "elif का मतलब क्या है?", "why": "elif \"else if\" का छोटा रूप है: एक और condition जाँचो।"},
        {"q": "जब if: के बाद वाली line indent न हो, तो कौन-सी error आती है?", "why": "Colon के बाद Python indent किया हुआ block चाहता है।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 2.1 · if, if-else, if-elif-else",
        "children": [
            {"label": "Condition", "children": [{"label": "True या False"}, {"label": "== != < > <= >="}, {"label": "and / or / not"}]},
            {"label": "if", "children": [{"label": "True हो तो block चलता है"}, {"label": "False हो तो छूटता है"}]},
            {"label": "if-else", "children": [{"label": "दो रास्ते"}, {"label": "ठीक एक चलता है"}]},
            {"label": "if-elif-else", "children": [{"label": "कई रास्ते"}, {"label": "ऊपर से नीचे"}, {"label": "पहला True जीतता है"}]},
            {"label": "Syntax", "children": [{"label": "Colon :"}, {"label": "4-space indent"}, {"label": "Block"}]},
            {"label": "Errors", "children": [{"label": "SyntaxError: expected ':'"}, {"label": "IndentationError"}]},
        ],
    },
    "summary": [
        "**if statement** अपना block तभी चलाता है जब उसकी **condition** `True` हो।",
        "हर `if`, `elif` और `else` line **colon** पर खत्म होती है, और उसके नीचे का block **4 spaces से indent** होता है।",
        "**if-else** दो में से एक रास्ता चुनता है; ठीक एक block चलता है।",
        "**if-elif-else** conditions को **ऊपर से नीचे** जाँचता है और सिर्फ़ **पहली** `True` वाली चलाता है, इसलिए सबसे narrow check पहले रखिए।",
        "**and**, **or** और **not** कई conditions को एक में जोड़ते हैं।",
    ],
}

# ======================================================================= Hinglish
T["hinglish"] = {
    "hook": {
        "title": "Kya yeh bukhaar hai?",
        "md": "Nurse thermometer padhti hai: **38.6 °C**. Kya yeh bukhaar hai? Tez bukhaar? Ya normal?\n\nPharmacist din bhar aise faisle leta hai: stock kam hai kya, dose zyada hai kya, patient bachcha hai kya? Ab tak aapke programs har line upar se neeche chalaate the. Is lesson mein aapka program **tay karega** ki kaun-si lines chalaani hain.",
    },
    "learn": [
        "**if** kuch lines tabhi kaise chalaata hai jab condition **True** ho",
        "Python mein **colon** aur **indentation** kyon zaroori hain",
        "**if-else** do raaston mein se ek kaise chunta hai",
        "**if-elif-else** kai raaston mein se ek kaise chunta hai, aur order kyon matter karta hai",
    ],
    "explanation": [
        {
            "heading": "if: kuch lines tabhi chalao jab zaroorat ho",
            "md": "**if statement** haan-ya-na wala sawaal poochhta hai. Jawaab `True` ho to Python uske neeche ki lines chalaata hai. `False` ho to unhe chhod deta hai.\n\n" + C_IF + "\n\nYeh print karta hai:\n\n" + O_IF + "\n\nSawaal `temp >= 38.0` ko **condition** kehte hain. Yeh comparison operators aapne Lesson 1.4 mein dekhe the: `==`, `!=`, `<`, `>`, `<=` aur `>=`. Har ek `True` ya `False` deta hai.\n\n`temp = 37.0` karke dekhiye. Condition `False` hai, isliye `Fever` chhoot jaata hai, aur sirf `Check done` print hota hai.",
            "callout": {"title": "Condition", "md": "Aisa expression jo True ya False ho, jaise temp >= 38.0. Yahi tay karta hai ki if ke neeche ki lines chalengi ya nahi."},
        },
        {
            "heading": "Colon aur indentation",
            "md": "Do chhoti cheezein Python ko batati hain ki `if` mein kya-kya aata hai:\n\n1. `if` line ke aakhir mein **colon** `:`.\n2. **Indentation**: `if` ki lines **4 spaces** se shuru hoti hain.\n\nIndent ki hui lines ko **block** kehte hain. Jahaan indentation khatam, wahaan block khatam. Upar ke example mein `print(\"Fever\")` block ke andar hai, aur `print(\"Check done\")` bahar hai, isliye woh hamesha chalta hai.\n\nZyadatar IDEs colon ke baad Enter dabaane par 4 spaces apne-aap daal dete hain.",
            "callout": {"title": "Indentation sajaavat nahi hai", "md": "Python mein line ki shuruaat ke spaces program ka kaam badal dete hain. 4 spaces use kijiye, aur block ki har line ek seedh mein rakhiye."},
        },
        {
            "heading": "if-else: do mein se ek raasta",
            "md": "Aksar dono haalaat mein kuch hona chahiye. **else** doosra raasta deta hai: yeh tab chalta hai jab condition `False` ho.\n\nJab kisi dawa ka stock reorder level se neeche jaata hai, pharmacy use phir se mangaati hai:\n\n" + C_ELSE + "\n\nYeh `Reorder now` print karta hai, kyonki 12, 20 se kam hai. `stock = 35` hota to `Stock OK` print hota.\n\nDono mein se theek ek block chalta hai: na dono, na koi nahi. `else` ki apni koi condition nahi hoti; yeh bhi colon par khatam hota hai.",
        },
        {
            "heading": "if-elif-else: kai mein se ek raasta",
            "md": "Jab do se zyada haalaat hon, **elif** use kijiye, yaani \"else if\". Yeh upar wale number (systolic, mmHg mein) se blood pressure ki ek aasaan jaanch hai:\n\n" + C_ELIF + "\n\nYeh `High BP, stage 1` print karta hai.\n\nPython conditions ko **upar se neeche** jaanchta hai aur **pehla** block chalaata hai jiski condition `True` ho. Phir chain ka baaki sab chhod deta hai. 134 na 120 se kam hai, na 130 se, par 140 se kam hai, isliye teesra block chalta hai.\n\nJitne chahiye utne `elif` rakh sakte hain. Aakhir ka `else` zaroori nahi; yeh woh sab pakadta hai jo upar ki conditions ne nahi pakda.",
            "callout": {"title": "Order matter karta hai", "md": "Python pehli True condition par ruk jaata hai, isliye sabse narrow case pehle jaanchiye. Agar systolic < 140 pehle hota, to 110 bhi stage 1 print karta."},
        },
        {
            "heading": "and, or, not se conditions jodna",
            "md": "Lesson 1.4 ke logical operators kai conditions ko ek mein jodte hain:\n\n- **`and`** tabhi `True` hai jab **dono** taraf `True` ho.\n- **`or`** tab `True` hai jab **kam se kam ek** taraf `True` ho.\n- **`not`** `True` ko `False` aur `False` ko `True` kar deta hai.\n\nBachchon aur buzurg patients ke dose mein aksar zyada dhyaan chahiye:\n\n" + C_AND + "\n\nYeh `Extra care: check the dose` print karta hai, kyonki `age >= 65` `True` hai, aur `or` ko sirf ek taraf `True` chahiye.",
        },
    ],
    "walkthrough": {
        "intro": "Yeh program shareer ka temperature padhkar sahi message print karta hai. Teen mein se sirf ek message print ho sakta hai.",
        "keyTerms": [
            {"meaning": "Block tabhi chalao jab condition True ho."},
            {"meaning": "\"Else if\": upar ki conditions False hon to ek aur condition jaancho."},
            {"meaning": "Jab upar ki koi condition True na ho, yeh block chalao."},
            {"meaning": "Har if, elif aur else line isi par khatam hoti hai."},
            {"meaning": "Block mein aane wali lines ko dikhaate hain."},
        ],
    },
    "errors": {
        "intro": "if ki zyadatar errors colon ya indentation chhootne se aati hain.",
        "examples": [
            {"title": "Colon bhool jaana", "md": "Har `if`, `elif` aur `else` line colon par khatam honi chahiye. `if temp >= 38.0:` likhiye."},
            {"title": "Block ko indent karna bhool jaana", "md": "Colon ke baad Python ko kam se kam ek indent ki hui line chahiye. `print(\"Fever\")` se pehle 4 spaces lagaiye."},
        ],
    },
    "mistakes": [
        {"mistake": "Condition mein `==` ki jagah `=` likhna, jaise `if dose = 500:`", "see": "SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?", "fix": "`=` value store karta hai; `==` compare karta hai. `if dose == 500:` likhiye."},
        {"mistake": "Badi condition pehle rakhna, jaise `elif temp >= 39.5` se pehle `if temp >= 38.0`", "see": "Koi error nahi, par tez bukhaar par bhi sirf \"Fever\" print hota hai", "fix": "Sabse narrow case pehle: `temp >= 39.5`, phir `temp >= 38.0`."},
        {"mistake": "`else` ko condition dena, jaise `else temp < 38.0:`", "see": "SyntaxError: expected ':'", "fix": "`else` koi condition nahi leta. `elif temp < 38.0:` ya sirf `else:` likhiye."},
        {"mistake": "Alag capitals wala text compare karna, jaise drug \"Aspirin\" ho aur `if drug == \"aspirin\"`", "see": "Koi error nahi, par condition False aati hai", "fix": "Ek hi case mein compare kijiye: `if drug.lower() == \"aspirin\":`."},
    ],
    "tasks": [
        {"title": "Reorder karein ya nahi?", "md": "10 strips se kam stock ka matlab hai pharmacy ko reorder karna hoga. **if-else** use kijiye taaki output bilkul yeh ho:",
         "hints": ["Aise shuru kijiye: if stock < 10:", "if stock < 10:\n    print(\"Reorder\")\nelse:\n    print(\"In stock\")"]},
        {"title": "Dose ki limit jaanchiye", "md": "Likha gaya ek baar ka dose limit se zyada hai. Dose ke saath warning print kijiye, bilkul aise:",
         "hints": ["> se compare kijiye: if dose > max_dose:", "f-string use kijiye: print(f\"Too high: {dose} mg\")"]},
        {"title": "Result ki class", "md": "**if-elif-else** use kijiye: 75 ya zyada \"Distinction\", 60 ya zyada \"First class\", 50 ya zyada \"Second class\", aur usse kam \"Fail\". 72 marks ke liye output bilkul yeh hona chahiye:",
         "hints": ["Sabse oonchi limit pehle jaanchiye: if marks >= 75:", "if marks >= 75:\n    print(\"Distinction\")\nelif marks >= 60:\n    print(\"First class\")\nelif marks >= 50:\n    print(\"Second class\")\nelse:\n    print(\"Fail\")"]},
        {"title": "Bug dhoondhiye", "md": "40.1 temperature par \"High fever\" print hona chahiye, par yeh program \"Fever\" print karta hai. Koi error message nahi hai. Ise theek kijiye taaki output bilkul yeh ho:",
         "hints": ["Python pehla woh block chalaata hai jiski condition True ho. Kya 40.1 >= 38.0 hai?", "Pehle temp >= 39.5 jaanchiye, phir temp >= 38.0."],
         "solutionNote": "40.1 >= 38.0 True hai, isliye pehla block chal gaya aur baaki chhoot gaye. Narrow check (39.5) pehle rakhne se yeh theek ho jaata hai."},
    ],
    "quiz": [
        {"q": "x = 5\nif x > 3:\n    print(\"A\")\nelse:\n    print(\"B\")\n\nYeh kya print karta hai?", "why": "5 > 3 True hai, isliye if block chalta hai aur else chhoot jaata hai."},
        {"q": "if line ke aakhir mein kya aana chahiye?", "why": "if, elif aur else, teenon lines colon par khatam hoti hain."},
        {"q": "if-elif-else chain mein kitne blocks chalte hain?", "why": "Python pehla True condition wala block (ya else) chalaata hai, phir baaki chhod deta hai."},
        {"q": "temp = 37.0\nif temp >= 38.0:\n    print(\"Fever\")\nelse:\n    print(\"Normal\")\n\nYeh kya print karta hai?", "why": "37.0 >= 38.0 False hai, isliye else block chalta hai."},
        {"q": "elif ka matlab kya hai?", "why": "elif \"else if\" ka chhota roop hai: ek aur condition jaancho."},
        {"q": "Jab if: ke baad wali line indent na ho, to kaun-si error aati hai?", "why": "Colon ke baad Python indent kiya hua block chahta hai."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 2.1 · if, if-else, if-elif-else",
        "children": [
            {"label": "Condition", "children": [{"label": "True ya False"}, {"label": "== != < > <= >="}, {"label": "and / or / not"}]},
            {"label": "if", "children": [{"label": "True ho to block chalta hai"}, {"label": "False ho to chhoot-ta hai"}]},
            {"label": "if-else", "children": [{"label": "Do raaste"}, {"label": "Theek ek chalta hai"}]},
            {"label": "if-elif-else", "children": [{"label": "Kai raaste"}, {"label": "Upar se neeche"}, {"label": "Pehla True jeet-ta hai"}]},
            {"label": "Syntax", "children": [{"label": "Colon :"}, {"label": "4-space indent"}, {"label": "Block"}]},
            {"label": "Errors", "children": [{"label": "SyntaxError: expected ':'"}, {"label": "IndentationError"}]},
        ],
    },
    "summary": [
        "**if statement** apna block tabhi chalaata hai jab uski **condition** `True` ho.",
        "Har `if`, `elif` aur `else` line **colon** par khatam hoti hai, aur uske neeche ka block **4 spaces se indent** hota hai.",
        "**if-else** do mein se ek raasta chunta hai; theek ek block chalta hai.",
        "**if-elif-else** conditions ko **upar se neeche** jaanchta hai aur sirf **pehli** `True` wali chalaata hai, isliye sabse narrow check pehle rakhiye.",
        "**and**, **or** aur **not** kai conditions ko ek mein jodte hain.",
    ],
}

# ======================================================================= Kannada
T["kn"] = {
    "hook": {
        "title": "ಇದು ಜ್ವರನಾ?",
        "md": "Nurse thermometer ಓದುತ್ತಾರೆ: **38.6 °C**. ಇದು ಜ್ವರನಾ? ಜೋರು ಜ್ವರನಾ? ಅಥವಾ normal ಆ?\n\nPharmacist ದಿನವಿಡೀ ಇಂಥ ತೀರ್ಮಾನಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳುತ್ತಾರೆ: stock ಕಡಿಮೆ ಇದೆಯಾ, dose ಜಾಸ್ತಿ ಇದೆಯಾ, patient ಮಗುನಾ? ಇಲ್ಲಿವರೆಗೆ ನಿಮ್ಮ programs ಪ್ರತಿ line ಅನ್ನು ಮೇಲಿಂದ ಕೆಳಗೆ run ಮಾಡುತ್ತಿದ್ದವು. ಈ lesson ನಲ್ಲಿ ಯಾವ lines run ಮಾಡಬೇಕು ಅಂತ ನಿಮ್ಮ program **ತಾನೇ ತೀರ್ಮಾನಿಸುತ್ತೆ**.",
    },
    "learn": [
        "Condition **True** ಆದಾಗ ಮಾತ್ರ **if** ಕೆಲವು lines ಅನ್ನು ಹೇಗೆ run ಮಾಡುತ್ತೆ",
        "Python ನಲ್ಲಿ **colon** ಮತ್ತು **indentation** ಯಾಕೆ ಮುಖ್ಯ",
        "**if-else** ಎರಡು ದಾರಿಗಳಲ್ಲಿ ಒಂದನ್ನು ಹೇಗೆ ಆರಿಸುತ್ತೆ",
        "**if-elif-else** ಹಲವು ದಾರಿಗಳಲ್ಲಿ ಒಂದನ್ನು ಹೇಗೆ ಆರಿಸುತ್ತೆ, ಮತ್ತು ಕ್ರಮ ಯಾಕೆ ಮುಖ್ಯ",
    ],
    "explanation": [
        {
            "heading": "if: ಬೇಕಾದಾಗ ಮಾತ್ರ ಕೆಲವು lines run ಮಾಡಿ",
            "md": "**if statement** ಹೌದು-ಅಥವಾ-ಇಲ್ಲ ಪ್ರಶ್ನೆ ಕೇಳುತ್ತೆ. ಉತ್ತರ `True` ಆದ್ರೆ, Python ಅದರ ಕೆಳಗಿನ lines run ಮಾಡುತ್ತೆ. `False` ಆದ್ರೆ, ಅವನ್ನು ಬಿಟ್ಟುಬಿಡುತ್ತೆ.\n\n" + C_IF + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + O_IF + "\n\n`temp >= 38.0` ಎಂಬ ಪ್ರಶ್ನೆಗೆ **condition** ಅಂತಾರೆ. ಈ comparison operators ಅನ್ನು Lesson 1.4 ನಲ್ಲಿ ನೋಡಿದ್ದೀರಿ: `==`, `!=`, `<`, `>`, `<=` ಮತ್ತು `>=`. ಪ್ರತಿಯೊಂದೂ `True` ಅಥವಾ `False` ಕೊಡುತ್ತೆ.\n\n`temp = 37.0` ಹಾಕಿ ನೋಡಿ. Condition `False`, ಅದಕ್ಕೇ `Fever` ಬಿಟ್ಟುಹೋಗುತ್ತೆ, `Check done` ಮಾತ್ರ print ಆಗುತ್ತೆ.",
            "callout": {"title": "Condition", "md": "True ಅಥವಾ False ಆಗುವ expression, ಉದಾಹರಣೆಗೆ temp >= 38.0. if ಕೆಳಗಿನ lines run ಆಗಬೇಕಾ ಬೇಡವಾ ಅಂತ ಇದೇ ತೀರ್ಮಾನಿಸುತ್ತೆ."},
        },
        {
            "heading": "Colon ಮತ್ತು indentation",
            "md": "`if` ಗೆ ಯಾವುದೆಲ್ಲಾ ಸೇರುತ್ತೆ ಅಂತ ಎರಡು ಚಿಕ್ಕ ವಿಷಯಗಳು Python ಗೆ ಹೇಳುತ್ತವೆ:\n\n1. `if` line ನ ಕೊನೆಯಲ್ಲಿ **colon** `:`.\n2. **Indentation**: `if` ಗೆ ಸೇರಿದ lines **4 spaces** ಇಂದ ಶುರುವಾಗುತ್ತವೆ.\n\nIndent ಮಾಡಿದ lines ಗೆ **block** ಅಂತಾರೆ. Indentation ಎಲ್ಲಿ ಮುಗಿಯುತ್ತೋ, block ಅಲ್ಲೇ ಮುಗಿಯುತ್ತೆ. ಮೇಲಿನ example ನಲ್ಲಿ `print(\"Fever\")` block ಒಳಗಿದೆ, `print(\"Check done\")` ಹೊರಗಿದೆ, ಅದಕ್ಕೇ ಅದು ಯಾವಾಗಲೂ run ಆಗುತ್ತೆ.\n\nColon ಆದಮೇಲೆ Enter ಒತ್ತಿದಾಗ ಹೆಚ್ಚಿನ IDEs 4 spaces ತಾವೇ ಹಾಕುತ್ತವೆ.",
            "callout": {"title": "Indentation ಅಲಂಕಾರ ಅಲ್ಲ", "md": "Python ನಲ್ಲಿ line ಶುರುವಿನ spaces program ಮಾಡುವ ಕೆಲಸವನ್ನೇ ಬದಲಾಯಿಸುತ್ತವೆ. 4 spaces ಬಳಸಿ, block ನ ಪ್ರತಿ line ಒಂದೇ ಸಾಲಿನಲ್ಲಿ ಇರಲಿ."},
        },
        {
            "heading": "if-else: ಎರಡರಲ್ಲಿ ಒಂದು ದಾರಿ",
            "md": "ಹಲವು ಸಲ ಎರಡೂ ಸಂದರ್ಭಗಳಲ್ಲಿ ಏನಾದರೂ ಆಗಬೇಕು. **else** ಎರಡನೇ ದಾರಿ ಕೊಡುತ್ತೆ: condition `False` ಆದಾಗ ಇದು run ಆಗುತ್ತೆ.\n\nಒಂದು ಔಷಧದ stock reorder level ಗಿಂತ ಕೆಳಗೆ ಹೋದಾಗ pharmacy ಅದನ್ನು ಮತ್ತೆ order ಮಾಡುತ್ತೆ:\n\n" + C_ELSE + "\n\nಇದು `Reorder now` print ಮಾಡುತ್ತೆ, ಯಾಕೆಂದರೆ 12, 20 ಕ್ಕಿಂತ ಕಡಿಮೆ. `stock = 35` ಆಗಿದ್ದರೆ `Stock OK` print ಆಗುತ್ತಿತ್ತು.\n\nಎರಡರಲ್ಲಿ ಸರಿಯಾಗಿ ಒಂದು block ಮಾತ್ರ run ಆಗುತ್ತೆ: ಎರಡೂ ಅಲ್ಲ, ಯಾವುದೂ ಇಲ್ಲದೆಯೂ ಅಲ್ಲ. `else` ಗೆ ತನ್ನದೇ condition ಇಲ್ಲ; ಇದೂ colon ಇಂದ ಮುಗಿಯುತ್ತೆ.",
        },
        {
            "heading": "if-elif-else: ಹಲವರಲ್ಲಿ ಒಂದು ದಾರಿ",
            "md": "ಎರಡಕ್ಕಿಂತ ಹೆಚ್ಚು ಸಂದರ್ಭಗಳಿದ್ದಾಗ **elif** ಬಳಸಿ, ಅಂದರೆ \"else if\". ಮೇಲಿನ number (systolic, mmHg ನಲ್ಲಿ) ಬಳಸಿ blood pressure ನ ಒಂದು ಸರಳ check ಇಲ್ಲಿದೆ:\n\n" + C_ELIF + "\n\nಇದು `High BP, stage 1` print ಮಾಡುತ್ತೆ.\n\nPython conditions ಅನ್ನು **ಮೇಲಿಂದ ಕೆಳಗೆ** check ಮಾಡಿ, condition `True` ಆಗಿರುವ **ಮೊದಲ** block ಅನ್ನು run ಮಾಡುತ್ತೆ. ಆಮೇಲೆ chain ನ ಉಳಿದದ್ದೆಲ್ಲಾ ಬಿಟ್ಟುಬಿಡುತ್ತೆ. 134, 120 ಕ್ಕಿಂತ ಕಡಿಮೆ ಇಲ್ಲ, 130 ಕ್ಕಿಂತಲೂ ಇಲ್ಲ, ಆದರೆ 140 ಕ್ಕಿಂತ ಕಡಿಮೆ, ಅದಕ್ಕೇ ಮೂರನೇ block run ಆಗುತ್ತೆ.\n\nಎಷ್ಟು ಬೇಕೋ ಅಷ್ಟು `elif` ಇಡಬಹುದು. ಕೊನೆಯ `else` ಕಡ್ಡಾಯ ಅಲ್ಲ; ಮೇಲಿನ conditions ಹಿಡಿಯದೇ ಇರುವುದನ್ನೆಲ್ಲಾ ಇದು ಹಿಡಿಯುತ್ತೆ.",
            "callout": {"title": "ಕ್ರಮ ಮುಖ್ಯ", "md": "ಮೊದಲ True condition ಸಿಕ್ಕ ತಕ್ಷಣ Python ನಿಲ್ಲುತ್ತೆ, ಅದಕ್ಕೇ ಅತ್ಯಂತ narrow case ಅನ್ನು ಮೊದಲು check ಮಾಡಿ. systolic < 140 ಮೊದಲು ಇದ್ದಿದ್ದರೆ, 110 ಕೂಡ stage 1 ಅಂತ print ಆಗುತ್ತಿತ್ತು."},
        },
        {
            "heading": "and, or, not ಇಂದ conditions ಜೋಡಿಸುವುದು",
            "md": "Lesson 1.4 ನ logical operators ಹಲವು conditions ಅನ್ನು ಒಂದಾಗಿ ಜೋಡಿಸುತ್ತವೆ:\n\n- **`and`** **ಎರಡೂ** ಕಡೆ `True` ಆದಾಗ ಮಾತ್ರ `True`.\n- **`or`** **ಕನಿಷ್ಠ ಒಂದು** ಕಡೆ `True` ಆದರೆ `True`.\n- **`not`** `True` ಅನ್ನು `False` ಮಾಡುತ್ತೆ, `False` ಅನ್ನು `True` ಮಾಡುತ್ತೆ.\n\nಮಕ್ಕಳು ಮತ್ತು ವಯಸ್ಸಾದ patients ನ dose ಗೆ ಹೆಚ್ಚು ಗಮನ ಬೇಕು:\n\n" + C_AND + "\n\nಇದು `Extra care: check the dose` print ಮಾಡುತ್ತೆ, ಯಾಕೆಂದರೆ `age >= 65` `True`, ಮತ್ತು `or` ಗೆ ಒಂದು ಕಡೆ `True` ಆದರೆ ಸಾಕು.",
        },
    ],
    "walkthrough": {
        "intro": "ಈ program ದೇಹದ temperature ಓದಿ ಸರಿಯಾದ message print ಮಾಡುತ್ತೆ. ಮೂರರಲ್ಲಿ ಒಂದೇ message print ಆಗಬಹುದು.",
        "keyTerms": [
            {"meaning": "Condition True ಆದಾಗ ಮಾತ್ರ block run ಮಾಡು."},
            {"meaning": "\"Else if\": ಮೇಲಿನ conditions False ಆದರೆ ಇನ್ನೊಂದು condition check ಮಾಡು."},
            {"meaning": "ಮೇಲಿನ ಯಾವ condition ಕೂಡ True ಆಗದಿದ್ದಾಗ ಈ block run ಮಾಡು."},
            {"meaning": "ಪ್ರತಿ if, elif ಮತ್ತು else line ಇದರಿಂದಲೇ ಮುಗಿಯುತ್ತೆ."},
            {"meaning": "Block ಗೆ ಸೇರಿದ lines ಅನ್ನು ಗುರುತಿಸುತ್ತವೆ."},
        ],
    },
    "errors": {
        "intro": "if ನ ಹೆಚ್ಚಿನ errors colon ಅಥವಾ indentation ಬಿಟ್ಟುಹೋದಾಗ ಬರುತ್ತವೆ.",
        "examples": [
            {"title": "Colon ಮರೆಯುವುದು", "md": "ಪ್ರತಿ `if`, `elif` ಮತ್ತು `else` line colon ಇಂದ ಮುಗಿಯಬೇಕು. `if temp >= 38.0:` ಅಂತ ಬರೆಯಿರಿ."},
            {"title": "Block ಅನ್ನು indent ಮಾಡಲು ಮರೆಯುವುದು", "md": "Colon ಆದಮೇಲೆ Python ಗೆ ಕನಿಷ್ಠ ಒಂದು indent ಮಾಡಿದ line ಬೇಕು. `print(\"Fever\")` ಮುಂಚೆ 4 spaces ಹಾಕಿ."},
        ],
    },
    "mistakes": [
        {"mistake": "Condition ನಲ್ಲಿ `==` ಬದಲು `=` ಬರೆಯುವುದು, ಉದಾ. `if dose = 500:`", "see": "SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?", "fix": "`=` value store ಮಾಡುತ್ತೆ; `==` ಹೋಲಿಸುತ್ತೆ. `if dose == 500:` ಅಂತ ಬರೆಯಿರಿ."},
        {"mistake": "ದೊಡ್ಡ condition ಅನ್ನು ಮೊದಲು ಇಡುವುದು, ಉದಾ. `elif temp >= 39.5` ಗಿಂತ ಮುಂಚೆ `if temp >= 38.0`", "see": "Error ಇಲ್ಲ, ಆದರೆ ಜೋರು ಜ್ವರಕ್ಕೂ \"Fever\" ಮಾತ್ರ print ಆಗುತ್ತೆ", "fix": "ಅತ್ಯಂತ narrow case ಮೊದಲು: `temp >= 39.5`, ಆಮೇಲೆ `temp >= 38.0`."},
        {"mistake": "`else` ಗೆ condition ಕೊಡುವುದು, ಉದಾ. `else temp < 38.0:`", "see": "SyntaxError: expected ':'", "fix": "`else` ಯಾವ condition ಕೂಡ ತೆಗೆದುಕೊಳ್ಳಲ್ಲ. `elif temp < 38.0:` ಅಥವಾ `else:` ಮಾತ್ರ ಬರೆಯಿರಿ."},
        {"mistake": "ಬೇರೆ capitals ಇರುವ text ಹೋಲಿಸುವುದು, ಉದಾ. drug \"Aspirin\" ಇದ್ದು `if drug == \"aspirin\"`", "see": "Error ಇಲ್ಲ, ಆದರೆ condition False ಆಗುತ್ತೆ", "fix": "ಒಂದೇ case ನಲ್ಲಿ ಹೋಲಿಸಿ: `if drug.lower() == \"aspirin\":`."},
    ],
    "tasks": [
        {"title": "Reorder ಮಾಡಬೇಕಾ ಬೇಡವಾ?", "md": "10 strips ಗಿಂತ ಕಡಿಮೆ stock ಅಂದರೆ pharmacy reorder ಮಾಡಬೇಕು. Output ಸರಿಯಾಗಿ ಹೀಗೇ ಬರುವ ಹಾಗೆ **if-else** ಬಳಸಿ:",
         "hints": ["ಹೀಗೆ ಶುರು ಮಾಡಿ: if stock < 10:", "if stock < 10:\n    print(\"Reorder\")\nelse:\n    print(\"In stock\")"]},
        {"title": "Dose limit check ಮಾಡಿ", "md": "ಬರೆದ ಒಂದು ಸಲದ dose limit ಗಿಂತ ಜಾಸ್ತಿ ಇದೆ. Dose ಜೊತೆ warning print ಮಾಡಿ, ಸರಿಯಾಗಿ ಹೀಗೆ:",
         "hints": ["> ಇಂದ ಹೋಲಿಸಿ: if dose > max_dose:", "f-string ಬಳಸಿ: print(f\"Too high: {dose} mg\")"]},
        {"title": "Result ನ class", "md": "**if-elif-else** ಬಳಸಿ: 75 ಅಥವಾ ಹೆಚ್ಚು \"Distinction\", 60 ಅಥವಾ ಹೆಚ್ಚು \"First class\", 50 ಅಥವಾ ಹೆಚ್ಚು \"Second class\", ಅದಕ್ಕಿಂತ ಕಡಿಮೆ \"Fail\". 72 marks ಗೆ output ಸರಿಯಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["ಅತಿ ಎತ್ತರದ limit ಮೊದಲು check ಮಾಡಿ: if marks >= 75:", "if marks >= 75:\n    print(\"Distinction\")\nelif marks >= 60:\n    print(\"First class\")\nelif marks >= 50:\n    print(\"Second class\")\nelse:\n    print(\"Fail\")"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "40.1 temperature ಗೆ \"High fever\" print ಆಗಬೇಕು, ಆದರೆ ಈ program \"Fever\" print ಮಾಡುತ್ತೆ. Error message ಇಲ್ಲ. Output ಸರಿಯಾಗಿ ಹೀಗೇ ಬರುವ ಹಾಗೆ ಸರಿ ಮಾಡಿ:",
         "hints": ["Condition True ಆಗಿರುವ ಮೊದಲ block ಅನ್ನು Python run ಮಾಡುತ್ತೆ. 40.1 >= 38.0 ಆ?", "ಮೊದಲು temp >= 39.5 check ಮಾಡಿ, ಆಮೇಲೆ temp >= 38.0."],
         "solutionNote": "40.1 >= 38.0 True, ಅದಕ್ಕೇ ಮೊದಲ block run ಆಯ್ತು, ಉಳಿದವು ಬಿಟ್ಟುಹೋದವು. Narrow check (39.5) ಮೊದಲು ಇಟ್ಟರೆ ಸರಿಯಾಗುತ್ತೆ."},
    ],
    "quiz": [
        {"q": "x = 5\nif x > 3:\n    print(\"A\")\nelse:\n    print(\"B\")\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "5 > 3 True, ಅದಕ್ಕೇ if block run ಆಗುತ್ತೆ, else ಬಿಟ್ಟುಹೋಗುತ್ತೆ."},
        {"q": "if line ನ ಕೊನೆಯಲ್ಲಿ ಏನು ಬರಬೇಕು?", "why": "if, elif ಮತ್ತು else ಮೂರೂ lines colon ಇಂದ ಮುಗಿಯುತ್ತವೆ."},
        {"q": "if-elif-else chain ನಲ್ಲಿ ಎಷ್ಟು blocks run ಆಗುತ್ತವೆ?", "why": "Python ಮೊದಲ True condition ಇರುವ block (ಅಥವಾ else) run ಮಾಡಿ, ಉಳಿದದ್ದನ್ನು ಬಿಟ್ಟುಬಿಡುತ್ತೆ."},
        {"q": "temp = 37.0\nif temp >= 38.0:\n    print(\"Fever\")\nelse:\n    print(\"Normal\")\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "37.0 >= 38.0 False, ಅದಕ್ಕೇ else block run ಆಗುತ್ತೆ."},
        {"q": "elif ಅಂದರೆ ಏನು?", "why": "elif ಅಂದರೆ \"else if\" ನ ಚಿಕ್ಕ ರೂಪ: ಇನ್ನೊಂದು condition check ಮಾಡು."},
        {"q": "if: ನಂತರದ line indent ಆಗಿಲ್ಲದಿದ್ದರೆ ಯಾವ error ಬರುತ್ತೆ?", "why": "Colon ಆದಮೇಲೆ Python indent ಮಾಡಿದ block ನಿರೀಕ್ಷಿಸುತ್ತೆ."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 2.1 · if, if-else, if-elif-else",
        "children": [
            {"label": "Condition", "children": [{"label": "True ಅಥವಾ False"}, {"label": "== != < > <= >="}, {"label": "and / or / not"}]},
            {"label": "if", "children": [{"label": "True ಆದರೆ block run"}, {"label": "False ಆದರೆ skip"}]},
            {"label": "if-else", "children": [{"label": "ಎರಡು ದಾರಿ"}, {"label": "ಸರಿಯಾಗಿ ಒಂದು run"}]},
            {"label": "if-elif-else", "children": [{"label": "ಹಲವು ದಾರಿ"}, {"label": "ಮೇಲಿಂದ ಕೆಳಗೆ"}, {"label": "ಮೊದಲ True ಗೆಲ್ಲುತ್ತೆ"}]},
            {"label": "Syntax", "children": [{"label": "Colon :"}, {"label": "4-space indent"}, {"label": "Block"}]},
            {"label": "Errors", "children": [{"label": "SyntaxError: expected ':'"}, {"label": "IndentationError"}]},
        ],
    },
    "summary": [
        "**if statement** ತನ್ನ **condition** `True` ಆದಾಗ ಮಾತ್ರ block run ಮಾಡುತ್ತೆ.",
        "ಪ್ರತಿ `if`, `elif` ಮತ್ತು `else` line **colon** ಇಂದ ಮುಗಿಯುತ್ತೆ, ಅದರ ಕೆಳಗಿನ block **4 spaces ಇಂದ indent** ಆಗಿರುತ್ತೆ.",
        "**if-else** ಎರಡರಲ್ಲಿ ಒಂದು ದಾರಿ ಆರಿಸುತ್ತೆ; ಸರಿಯಾಗಿ ಒಂದು block run ಆಗುತ್ತೆ.",
        "**if-elif-else** conditions ಅನ್ನು **ಮೇಲಿಂದ ಕೆಳಗೆ** check ಮಾಡಿ **ಮೊದಲ** `True` ಒಂದನ್ನೇ run ಮಾಡುತ್ತೆ, ಅದಕ್ಕೇ narrow check ಮೊದಲು ಇಡಿ.",
        "**and**, **or** ಮತ್ತು **not** ಹಲವು conditions ಅನ್ನು ಒಂದಾಗಿ ಜೋಡಿಸುತ್ತವೆ.",
    ],
}

# Walkthrough narration
NARR = {
    "hi": [
        "यह program temperature पढ़ता है और तय करता है कि कौन-सा message दिखाना है। तीन में से सिर्फ़ एक message print होगा।",
        "Comment बताता है कि program क्या करता है।",
        "temp में अड़तीस दशमलव छह store होता है।",
        "if पूछता है: क्या temp कम से कम उनतालीस दशमलव पाँच है? अड़तीस दशमलव छह नहीं है, इसलिए condition False है। Python नीचे की indent की हुई line छोड़ देता है।",
        "अब elif अगला सवाल पूछता है: क्या temp कम से कम अड़तीस है? हाँ। यह condition True है।",
        "इसलिए Python elif के नीचे का block चलाता है, और Fever print करता है।",
        "एक block चल चुका है, इसलिए Python else और उसके नीचे की line छोड़ देता है।",
        "आखिरी line indent नहीं है। यह if chain के बाहर है, इसलिए हमेशा चलती है।",
    ],
    "hinglish": [
        "Yeh program temperature padhta hai aur tay karta hai ki kaun-sa message dikhaana hai. Teen mein se sirf ek message print hoga.",
        "Comment batata hai ki program kya karta hai.",
        "temp mein adtees dashamlav chhah store hota hai.",
        "if poochhta hai: kya temp kam se kam untaalis dashamlav paanch hai? Adtees dashamlav chhah nahi hai, isliye condition False hai. Python neeche ki indent ki hui line chhod deta hai.",
        "Ab elif agla sawaal poochhta hai: kya temp kam se kam adtees hai? Haan. Yeh condition True hai.",
        "Isliye Python elif ke neeche ka block chalaata hai, aur Fever print karta hai.",
        "Ek block chal chuka hai, isliye Python else aur uske neeche ki line chhod deta hai.",
        "Aakhri line indent nahi hai. Yeh if chain ke bahar hai, isliye hamesha chalti hai.",
    ],
    "kn": [
        "ಈ program temperature ಓದಿ, ಯಾವ message ತೋರಿಸಬೇಕು ಅಂತ ತೀರ್ಮಾನಿಸುತ್ತೆ. ಮೂರರಲ್ಲಿ ಒಂದೇ message print ಆಗುತ್ತೆ.",
        "Comment ಈ program ಏನು ಮಾಡುತ್ತೆ ಅಂತ ಹೇಳುತ್ತೆ.",
        "temp ನಲ್ಲಿ ಮೂವತ್ತೆಂಟು ಪಾಯಿಂಟ್ ಆರು store ಆಗುತ್ತೆ.",
        "if ಕೇಳುತ್ತೆ: temp ಕನಿಷ್ಠ ಮೂವತ್ತೊಂಬತ್ತು ಪಾಯಿಂಟ್ ಐದು ಇದೆಯಾ? ಮೂವತ್ತೆಂಟು ಪಾಯಿಂಟ್ ಆರು ಇಲ್ಲ, ಅದಕ್ಕೇ condition False. Python ಕೆಳಗಿನ indent ಮಾಡಿದ line ಬಿಟ್ಟುಬಿಡುತ್ತೆ.",
        "ಈಗ elif ಮುಂದಿನ ಪ್ರಶ್ನೆ ಕೇಳುತ್ತೆ: temp ಕನಿಷ್ಠ ಮೂವತ್ತೆಂಟು ಇದೆಯಾ? ಹೌದು. ಈ condition True.",
        "ಅದಕ್ಕೇ Python elif ಕೆಳಗಿನ block run ಮಾಡಿ, Fever print ಮಾಡುತ್ತೆ.",
        "ಒಂದು block ಈಗಾಗಲೇ run ಆಗಿದೆ, ಅದಕ್ಕೇ Python else ಮತ್ತು ಅದರ ಕೆಳಗಿನ line ಬಿಟ್ಟುಬಿಡುತ್ತೆ.",
        "ಕೊನೆಯ line indent ಆಗಿಲ್ಲ. ಇದು if chain ನ ಹೊರಗಿದೆ, ಅದಕ್ಕೇ ಯಾವಾಗಲೂ run ಆಗುತ್ತೆ.",
    ],
}

# Animation narration
ANIM = {
    "hi": [
        "यह temperature है, अड़तीस दशमलव छह, और तीन branches की एक chain।",
        "Python पहला सवाल पूछता है। क्या यह कम से कम उनतालीस दशमलव पाँच है? नहीं, इसलिए यह branch छूट जाती है।",
        "वह elif पर जाता है। क्या यह कम से कम अड़तीस है? हाँ।",
        "इसलिए वह यह block चलाता है, और Fever print करता है।",
        "एक branch चल चुकी है, इसलिए else छूट जाता है। हमेशा सिर्फ़ एक branch चलती है।",
    ],
    "hinglish": [
        "Yeh temperature hai, adtees dashamlav chhah, aur teen branches ki ek chain.",
        "Python pehla sawaal poochhta hai. Kya yeh kam se kam untaalis dashamlav paanch hai? Nahi, isliye yeh branch chhoot jaati hai.",
        "Woh elif par jaata hai. Kya yeh kam se kam adtees hai? Haan.",
        "Isliye woh yeh block chalaata hai, aur Fever print karta hai.",
        "Ek branch chal chuki hai, isliye else chhoot jaata hai. Hamesha sirf ek branch chalti hai.",
    ],
    "kn": [
        "ಇದು temperature, ಮೂವತ್ತೆಂಟು ಪಾಯಿಂಟ್ ಆರು, ಮತ್ತು ಮೂರು branches ಇರುವ ಒಂದು chain.",
        "Python ಮೊದಲ ಪ್ರಶ್ನೆ ಕೇಳುತ್ತೆ. ಇದು ಕನಿಷ್ಠ ಮೂವತ್ತೊಂಬತ್ತು ಪಾಯಿಂಟ್ ಐದು ಇದೆಯಾ? ಇಲ್ಲ, ಅದಕ್ಕೇ ಈ branch ಬಿಟ್ಟುಹೋಗುತ್ತೆ.",
        "ಅದು elif ಗೆ ಹೋಗುತ್ತೆ. ಇದು ಕನಿಷ್ಠ ಮೂವತ್ತೆಂಟು ಇದೆಯಾ? ಹೌದು.",
        "ಅದಕ್ಕೇ ಈ block run ಮಾಡಿ, Fever print ಮಾಡುತ್ತೆ.",
        "ಒಂದು branch run ಆಗಿದೆ, ಅದಕ್ಕೇ else ಬಿಟ್ಟುಹೋಗುತ್ತೆ. ಯಾವಾಗಲೂ ಒಂದೇ branch run ಆಗುತ್ತೆ.",
    ],
}

if __name__ == "__main__":
    build("2-1", "anim-branch", T, NARR, ANIM)

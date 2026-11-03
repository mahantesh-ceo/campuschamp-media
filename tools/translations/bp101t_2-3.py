"""Lesson 2.3 translations (Hindi, Hinglish, Kannada) and voice scripts."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import build  # noqa: E402

_spec = importlib.util.spec_from_file_location("en23", os.path.join(os.path.dirname(__file__), "..", "lessons", "bp101t_2-3_en.py"))
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)

RANGE_TABLE = {
    "hi": "| आप लिखते हैं | आपको मिलता है |\n|---|---|\n| `range(5)` | 0, 1, 2, 3, 4 |\n| `range(1, 6)` | 1, 2, 3, 4, 5 |\n| `range(0, 24, 8)` | 0, 8, 16 |",
    "hinglish": "| Aap likhte hain | Aapko milta hai |\n|---|---|\n| `range(5)` | 0, 1, 2, 3, 4 |\n| `range(1, 6)` | 1, 2, 3, 4, 5 |\n| `range(0, 24, 8)` | 0, 8, 16 |",
    "kn": "| ನೀವು ಬರೆಯುವುದು | ನಿಮಗೆ ಸಿಗುವುದು |\n|---|---|\n| `range(5)` | 0, 1, 2, 3, 4 |\n| `range(1, 6)` | 1, 2, 3, 4, 5 |\n| `range(0, 24, 8)` | 0, 8, 16 |",
}

T = {}

T["hi"] = {
    "hook": {
        "title": "30 दिन का dosing chart",
        "md": "एक patient 30 दिन का course लेकर जाता है, और आप एक chart print करना चाहते हैं: **Day 1, Day 2, ... Day 30**। 30 `print()` lines लिखना धीमा, उबाऊ और गलती वाला होगा।\n\nComputers चीज़ें दोहराने में कमाल के हैं। इस lesson में आप **एक** line लिखेंगे जो जितनी बार चाहिए उतनी बार दोहराती है: **for loop**।",
    },
    "learn": [
        "**for loop** हर item के लिए एक बार block कैसे दोहराता है",
        "**range()** numbers की लड़ी कैसे बनाता है, और stop number क्यों छूट जाता है",
        "**String** के अक्षरों और **list** के items पर loop कैसे चलाएँ",
        "Loop से चीज़ें **जोड़ना** या **गिनना**",
    ],
    "explanation": [
        {
            "heading": "बिना copy किए दोहराना",
            "md": "**for loop** एक ही block को बार-बार चलाता है, मिली हुई हर value के लिए एक बार:\n\n" + E.C_FIRST + "\n\nयह print करता है:\n\n" + E.O_FIRST + "\n\nहर बार **loop variable** `day` अगली value लेता है: पहले 1, फिर 2, फिर 3। Block के एक बार चलने को **iteration** कहते हैं।\n\n`if` वाले नियम यहाँ भी लागू हैं: `for` line **colon** पर खत्म होती है, और block **4 spaces से indent** होता है। `print(\"Course complete\")` indent नहीं है, इसलिए loop खत्म होने के बाद **एक बार** चलता है।",
            "callout": {"title": "Loop", "md": "Code का ऐसा block जो बार-बार चलता है। for loop हर value के लिए उसे एक बार चलाता है; हर बार चलना एक iteration है।"},
        },
        {
            "heading": "range(): numbers की लड़ी",
            "md": "**range()** वो numbers बनाता है जिनसे loop गुज़रता है। इसके तीन रूप हैं:\n\n" + RANGE_TABLE["hi"] + "\n\nतीसरा number **step** है: हर बार कितना जोड़ना है। हर 8 घंटे में ली जाने वाली दवा:\n\n" + E.C_RANGE + "\n\nयह print करता है:\n\n" + E.O_RANGE,
            "callout": {"title": "Stop number कभी शामिल नहीं होता", "md": "range(1, 6) ठीक 6 से पहले रुकता है, slice की तरह। Day 1 से 30 के लिए range(1, 31) लिखिए।"},
        },
        {
            "heading": "Text और lists पर loop",
            "md": "`for` loop सिर्फ़ numbers नहीं, और भी चीज़ों से गुज़र सकता है। यह **string** के हर character पर, या **list** के हर item पर जा सकता है: square brackets के अंदर commas से अलग की गई values।\n\n" + E.C_SEQ + "\n\nयह print करता है:\n\n" + E.O_SEQ + "\n\nLoop variable बारी-बारी हर item लेता है, पहले से आखिरी तक। Lists के बारे में आप Unit III में और सीखेंगे।",
        },
        {
            "heading": "Loop से जोड़ना",
            "md": "Values जोड़ने के लिए loop से **पहले** एक **total** 0 पर शुरू कीजिए, और loop के **अंदर** उसमें जोड़िए। इसे **accumulator** कहते हैं।\n\nएक adult की एक दिन की paracetamol doses:\n\n" + E.C_TOTAL + "\n\nयह `Total today: 2150 mg` print करता है। और कुछ print नहीं होता, क्योंकि 2150, 4000 mg से ज़्यादा नहीं, जो adults की आम daily limit है।\n\n`total += dose` Lesson 1.4 का shortcut है: इसका मतलब `total = total + dose`।",
            "callout": {"title": "Total को loop के बाहर शुरू कीजिए", "md": "अगर total = 0 loop के अंदर है, तो हर बार वह 0 हो जाता है, और आपको सिर्फ़ आखिरी value मिलती है।"},
        },
        {
            "heading": "Loop के अंदर if",
            "md": "Loop और `if` साथ में बढ़िया काम करते हैं: loop हर value पर जाता है, और `if` ज़रूरी values चुनता है। यहाँ nurse की temperature readings में बुखार जाँचा और गिना जाता है:\n\n" + E.C_COUNT + "\n\nयह print करता है:\n\n" + E.O_COUNT + "\n\n`if` block में 8 spaces हैं, क्योंकि वह loop के अंदर है। आखिरी `print` में कोई नहीं, इसलिए सारी readings जाँचने के बाद वह एक बार चलता है।",
        },
    ],
    "walkthrough": {
        "intro": "यह program 3 दिन का tablet chart print करता है और गिनता है कि patient को कितनी tablets चाहिए।",
        "keyTerms": [
            {"meaning": "हर value के लिए block एक बार दोहराओ, value day में रहती है।"},
            {"meaning": "Numbers 1, 2 और 3 (4 छूट जाता है)।"},
            {"meaning": "Loop से पहले running total शुरू करो।"},
            {"meaning": "हर बार total में 2 जोड़ो।"},
        ],
    },
    "errors": {
        "intro": "ये दो errors खुद for line से आती हैं।",
        "examples": [
            {"title": "Colon भूल जाना", "md": "`if` की तरह, `for` line भी colon पर खत्म होनी चाहिए: `for day in range(1, 4):`।"},
            {"title": "range() को number की जगह text देना", "md": "`\"5\"` एक string है, जैसे `input()` से आई। `range()` को integer चाहिए। पहले बदलिए: `range(int(days))`।"},
        ],
    },
    "mistakes": [
        {"mistake": "यह मानना कि `range(1, 30)` में 30 भी है", "see": "कोई error नहीं, पर chart Day 29 पर रुक जाता है", "fix": "Stop छूट जाता है, इसलिए `range(1, 31)` लिखिए।"},
        {"mistake": "`total = 0` को loop के अंदर रखना", "see": "कोई error नहीं, पर total सिर्फ़ आखिरी value होता है", "fix": "Total को एक बार, loop से पहले शुरू कीजिए।"},
        {"mistake": "आखिरी `print` को गलती से indent कर देना", "see": "कोई error नहीं, पर हर iteration के बाद total print होता है", "fix": "जो lines एक बार चलनी हैं, वो loop के बाद, बिना indentation के रखिए।"},
        {"mistake": "`range()` में decimal देना, जैसे `range(1, 7.5)`", "see": "TypeError: 'float' object cannot be interpreted as an integer", "fix": "`range()` सिर्फ़ पूरे numbers लेता है। `int()` या पूरा number use कीजिए।"},
    ],
    "tasks": [
        {"title": "Doses को number दीजिए", "md": "**range()** के साथ **for loop** use करके दिन की तीन doses print कीजिए, बिल्कुल ऐसे:",
         "hints": ["range(1, 4) से 1, 2 और 3 मिलते हैं।", "for n in range(1, 4):\n    print(f\"Dose {n}\")"]},
        {"title": "हर 6 घंटे", "md": "एक antibiotic हर 6 घंटे दी जाती है, आधी रात से शुरू। **step वाला range()** use कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["range() का तीसरा number step है: range(0, 24, 6)।", "for hour in range(0, 24, 6):\n    print(f\"Dose at {hour}:00\")"]},
        {"title": "Doses जोड़िए", "md": "List की doses को loop से जोड़िए, और total बिल्कुल ऐसे print कीजिए:",
         "hints": ["Loop के अंदर: total += dose", "for dose in doses:\n    total += dose\nprint(\"Total:\", total, \"mg\")"]},
        {"title": "Bug ढूँढिए", "md": "एक patient 7 दिन तक रोज़ 3 tablets लेता है, तो उसे 21 tablets चाहिए। यह program 3 बताता है, और कोई error नहीं। इसे ठीक कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["हर iteration की शुरुआत में total के साथ क्या होता है?", "Loop के अंदर वाला total = 0 हटाइए। Loop से पहले वाला काफ़ी है।"],
         "solutionNote": "Loop के अंदर total = 0 हर दिन total को reset कर देता था, इसलिए सिर्फ़ आखिरी 3 बचता था। Loop से पहले एक बार शुरू करने पर यह 21 तक बढ़ता है।"},
    ],
    "quiz": [
        {"q": "range(1, 4) कौन-से numbers देता है?", "why": "range stop number, 4, से ठीक पहले रुकता है।"},
        {"q": "for i in range(3):\n    print(\"Shake well\")\n\n\"Shake well\" कितनी बार print होता है?", "why": "range(3) से 0, 1 और 2 मिलते हैं: तीन values, इसलिए तीन iterations।"},
        {"q": "range(0, 10, 5) क्या देता है?", "why": "0 से शुरू, हर बार 5 जोड़ो, और 10 से पहले रुको।"},
        {"q": "total = 0\nfor n in range(1, 4):\n    total += n\nprint(total)\n\nयह क्या print करता है?", "why": "1 + 2 + 3 = 6।"},
        {"q": "for ch in \"ABC\":\n    print(ch)\n\nक्या print होता है?", "why": "Loop हर character पर जाता है, और हर print नई line से शुरू होता है।"},
        {"q": "Loop खत्म होने के बाद कौन-सी line सिर्फ़ एक बार चलती है?", "why": "जो lines indent नहीं हैं वो loop के बाहर हैं, इसलिए उसके खत्म होने के बाद एक बार चलती हैं।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 2.3 · for loops",
        "children": [
            {"label": "for loop", "children": [{"label": "हर value के लिए दोहराओ"}, {"label": "Loop variable"}, {"label": "Iteration = एक बार चलना"}]},
            {"label": "range()", "children": [{"label": "range(5) → 0-4"}, {"label": "range(1, 6) → 1-5"}, {"label": "range(0, 24, 8) → step"}]},
            {"label": "Sequences", "children": [{"label": "String के characters"}, {"label": "List के items"}]},
            {"label": "Patterns", "children": [{"label": "पहले total = 0"}, {"label": "अंदर total += value"}, {"label": "if से गिनती"}]},
            {"label": "Syntax", "children": [{"label": "Colon :"}, {"label": "4-space block"}, {"label": "Loop के बाद एक बार"}]},
            {"label": "Errors", "children": [{"label": "SyntaxError: expected ':'"}, {"label": "TypeError: range में str/float"}]},
        ],
    },
    "summary": [
        "**for loop** अपना indent किया हुआ block **हर value** के लिए एक बार चलाता है; **loop variable** में मौजूदा value रहती है, और हर बार चलना एक **iteration** है।",
        "**range(stop)**, **range(start, stop)** और **range(start, stop, step)** पूरे numbers की लड़ी बनाते हैं; **stop कभी शामिल नहीं होता**।",
        "for loop **string के हर character** या **list के हर item** पर भी जा सकता है।",
        "जोड़ने के लिए loop से **पहले** `total = 0` शुरू कीजिए और **अंदर** `total += value` use कीजिए।",
        "**Loop के अंदर if** ज़रूरी values चुनता या गिनता है। Loop के बाद, बिना indentation वाली lines एक बार चलती हैं।",
    ],
}

T["hinglish"] = {
    "hook": {
        "title": "30 din ka dosing chart",
        "md": "Ek patient 30 din ka course lekar jaata hai, aur aap ek chart print karna chahte hain: **Day 1, Day 2, ... Day 30**. 30 `print()` lines likhna dheema, boring aur galti wala hoga.\n\nComputers cheezein dohraane mein kamaal ke hain. Is lesson mein aap **ek** line likhenge jo jitni baar chahiye utni baar dohraati hai: **for loop**.",
    },
    "learn": [
        "**for loop** har item ke liye ek baar block kaise dohraata hai",
        "**range()** numbers ki ladi kaise banaata hai, aur stop number kyon chhoot jaata hai",
        "**String** ke aksharon aur **list** ke items par loop kaise chalaayein",
        "Loop se cheezein **jodna** ya **ginna**",
    ],
    "explanation": [
        {
            "heading": "Bina copy kiye dohraana",
            "md": "**for loop** ek hi block ko baar-baar chalaata hai, mili hui har value ke liye ek baar:\n\n" + E.C_FIRST + "\n\nYeh print karta hai:\n\n" + E.O_FIRST + "\n\nHar baar **loop variable** `day` agli value leta hai: pehle 1, phir 2, phir 3. Block ke ek baar chalne ko **iteration** kehte hain.\n\n`if` wale niyam yahaan bhi laagu hain: `for` line **colon** par khatam hoti hai, aur block **4 spaces se indent** hota hai. `print(\"Course complete\")` indent nahi hai, isliye loop khatam hone ke baad **ek baar** chalta hai.",
            "callout": {"title": "Loop", "md": "Code ka aisa block jo baar-baar chalta hai. for loop har value ke liye use ek baar chalaata hai; har baar chalna ek iteration hai."},
        },
        {
            "heading": "range(): numbers ki ladi",
            "md": "**range()** woh numbers banaata hai jinse loop guzarta hai. Iske teen roop hain:\n\n" + RANGE_TABLE["hinglish"] + "\n\nTeesra number **step** hai: har baar kitna jodna hai. Har 8 ghante mein li jaane wali dawa:\n\n" + E.C_RANGE + "\n\nYeh print karta hai:\n\n" + E.O_RANGE,
            "callout": {"title": "Stop number kabhi shaamil nahi hota", "md": "range(1, 6) theek 6 se pehle rukta hai, slice ki tarah. Day 1 se 30 ke liye range(1, 31) likhiye."},
        },
        {
            "heading": "Text aur lists par loop",
            "md": "`for` loop sirf numbers nahi, aur bhi cheezon se guzar sakta hai. Yeh **string** ke har character par, ya **list** ke har item par ja sakta hai: square brackets ke andar commas se alag ki gayi values.\n\n" + E.C_SEQ + "\n\nYeh print karta hai:\n\n" + E.O_SEQ + "\n\nLoop variable baari-baari har item leta hai, pehle se aakhri tak. Lists ke baare mein aap Unit III mein aur seekhenge.",
        },
        {
            "heading": "Loop se jodna",
            "md": "Values jodne ke liye loop se **pehle** ek **total** 0 par shuru kijiye, aur loop ke **andar** usmein jodiye. Ise **accumulator** kehte hain.\n\nEk adult ki ek din ki paracetamol doses:\n\n" + E.C_TOTAL + "\n\nYeh `Total today: 2150 mg` print karta hai. Aur kuch print nahi hota, kyonki 2150, 4000 mg se zyada nahi, jo adults ki aam daily limit hai.\n\n`total += dose` Lesson 1.4 ka shortcut hai: iska matlab `total = total + dose`.",
            "callout": {"title": "Total ko loop ke bahar shuru kijiye", "md": "Agar total = 0 loop ke andar hai, to har baar woh 0 ho jaata hai, aur aapko sirf aakhri value milti hai."},
        },
        {
            "heading": "Loop ke andar if",
            "md": "Loop aur `if` saath mein badhiya kaam karte hain: loop har value par jaata hai, aur `if` zaroori values chunta hai. Yahaan nurse ki temperature readings mein bukhaar jaancha aur gina jaata hai:\n\n" + E.C_COUNT + "\n\nYeh print karta hai:\n\n" + E.O_COUNT + "\n\n`if` block mein 8 spaces hain, kyonki woh loop ke andar hai. Aakhri `print` mein koi nahi, isliye saari readings jaanchne ke baad woh ek baar chalta hai.",
        },
    ],
    "walkthrough": {
        "intro": "Yeh program 3 din ka tablet chart print karta hai aur ginta hai ki patient ko kitni tablets chahiye.",
        "keyTerms": [
            {"meaning": "Har value ke liye block ek baar dohraao, value day mein rehti hai."},
            {"meaning": "Numbers 1, 2 aur 3 (4 chhoot jaata hai)."},
            {"meaning": "Loop se pehle running total shuru karo."},
            {"meaning": "Har baar total mein 2 jodo."},
        ],
    },
    "errors": {
        "intro": "Yeh do errors khud for line se aati hain.",
        "examples": [
            {"title": "Colon bhool jaana", "md": "`if` ki tarah, `for` line bhi colon par khatam honi chahiye: `for day in range(1, 4):`."},
            {"title": "range() ko number ki jagah text dena", "md": "`\"5\"` ek string hai, jaise `input()` se aayi. `range()` ko integer chahiye. Pehle badaliye: `range(int(days))`."},
        ],
    },
    "mistakes": [
        {"mistake": "Yeh maanna ki `range(1, 30)` mein 30 bhi hai", "see": "Koi error nahi, par chart Day 29 par ruk jaata hai", "fix": "Stop chhoot jaata hai, isliye `range(1, 31)` likhiye."},
        {"mistake": "`total = 0` ko loop ke andar rakhna", "see": "Koi error nahi, par total sirf aakhri value hota hai", "fix": "Total ko ek baar, loop se pehle shuru kijiye."},
        {"mistake": "Aakhri `print` ko galti se indent kar dena", "see": "Koi error nahi, par har iteration ke baad total print hota hai", "fix": "Jo lines ek baar chalni hain, woh loop ke baad, bina indentation ke rakhiye."},
        {"mistake": "`range()` mein decimal dena, jaise `range(1, 7.5)`", "see": "TypeError: 'float' object cannot be interpreted as an integer", "fix": "`range()` sirf poore numbers leta hai. `int()` ya poora number use kijiye."},
    ],
    "tasks": [
        {"title": "Doses ko number dijiye", "md": "**range()** ke saath **for loop** use karke din ki teen doses print kijiye, bilkul aise:",
         "hints": ["range(1, 4) se 1, 2 aur 3 milte hain.", "for n in range(1, 4):\n    print(f\"Dose {n}\")"]},
        {"title": "Har 6 ghante", "md": "Ek antibiotic har 6 ghante di jaati hai, aadhi raat se shuru. **Step wala range()** use kijiye taaki output bilkul yeh ho:",
         "hints": ["range() ka teesra number step hai: range(0, 24, 6).", "for hour in range(0, 24, 6):\n    print(f\"Dose at {hour}:00\")"]},
        {"title": "Doses jodiye", "md": "List ki doses ko loop se jodiye, aur total bilkul aise print kijiye:",
         "hints": ["Loop ke andar: total += dose", "for dose in doses:\n    total += dose\nprint(\"Total:\", total, \"mg\")"]},
        {"title": "Bug dhoondhiye", "md": "Ek patient 7 din tak roz 3 tablets leta hai, to use 21 tablets chahiye. Yeh program 3 batata hai, aur koi error nahi. Ise theek kijiye taaki output bilkul yeh ho:",
         "hints": ["Har iteration ki shuruaat mein total ke saath kya hota hai?", "Loop ke andar wala total = 0 hataaiye. Loop se pehle wala kaafi hai."],
         "solutionNote": "Loop ke andar total = 0 har din total ko reset kar deta tha, isliye sirf aakhri 3 bachta tha. Loop se pehle ek baar shuru karne par yeh 21 tak badhta hai."},
    ],
    "quiz": [
        {"q": "range(1, 4) kaun-se numbers deta hai?", "why": "range stop number, 4, se theek pehle rukta hai."},
        {"q": "for i in range(3):\n    print(\"Shake well\")\n\n\"Shake well\" kitni baar print hota hai?", "why": "range(3) se 0, 1 aur 2 milte hain: teen values, isliye teen iterations."},
        {"q": "range(0, 10, 5) kya deta hai?", "why": "0 se shuru, har baar 5 jodo, aur 10 se pehle ruko."},
        {"q": "total = 0\nfor n in range(1, 4):\n    total += n\nprint(total)\n\nYeh kya print karta hai?", "why": "1 + 2 + 3 = 6."},
        {"q": "for ch in \"ABC\":\n    print(ch)\n\nKya print hota hai?", "why": "Loop har character par jaata hai, aur har print nayi line se shuru hota hai."},
        {"q": "Loop khatam hone ke baad kaun-si line sirf ek baar chalti hai?", "why": "Jo lines indent nahi hain woh loop ke bahar hain, isliye uske khatam hone ke baad ek baar chalti hain."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 2.3 · for loops",
        "children": [
            {"label": "for loop", "children": [{"label": "Har value ke liye dohraao"}, {"label": "Loop variable"}, {"label": "Iteration = ek baar chalna"}]},
            {"label": "range()", "children": [{"label": "range(5) → 0-4"}, {"label": "range(1, 6) → 1-5"}, {"label": "range(0, 24, 8) → step"}]},
            {"label": "Sequences", "children": [{"label": "String ke characters"}, {"label": "List ke items"}]},
            {"label": "Patterns", "children": [{"label": "Pehle total = 0"}, {"label": "Andar total += value"}, {"label": "if se ginti"}]},
            {"label": "Syntax", "children": [{"label": "Colon :"}, {"label": "4-space block"}, {"label": "Loop ke baad ek baar"}]},
            {"label": "Errors", "children": [{"label": "SyntaxError: expected ':'"}, {"label": "TypeError: range mein str/float"}]},
        ],
    },
    "summary": [
        "**for loop** apna indent kiya hua block **har value** ke liye ek baar chalaata hai; **loop variable** mein maujooda value rehti hai, aur har baar chalna ek **iteration** hai.",
        "**range(stop)**, **range(start, stop)** aur **range(start, stop, step)** poore numbers ki ladi banaate hain; **stop kabhi shaamil nahi hota**.",
        "for loop **string ke har character** ya **list ke har item** par bhi ja sakta hai.",
        "Jodne ke liye loop se **pehle** `total = 0` shuru kijiye aur **andar** `total += value` use kijiye.",
        "**Loop ke andar if** zaroori values chunta ya ginta hai. Loop ke baad, bina indentation wali lines ek baar chalti hain.",
    ],
}

T["kn"] = {
    "hook": {
        "title": "30 ದಿನದ dosing chart",
        "md": "ಒಬ್ಬ patient 30 ದಿನದ course ತೆಗೆದುಕೊಂಡು ಹೋಗುತ್ತಾರೆ, ನೀವು ಒಂದು chart print ಮಾಡಬೇಕು: **Day 1, Day 2, ... Day 30**. 30 `print()` lines ಬರೆಯುವುದು ನಿಧಾನ, ಬೇಸರ, ಮತ್ತು ತಪ್ಪಾಗುವುದು ಸುಲಭ.\n\nComputers ವಿಷಯಗಳನ್ನು ಪುನರಾವರ್ತಿಸುವುದರಲ್ಲಿ ಅದ್ಭುತ. ಈ lesson ನಲ್ಲಿ ಎಷ್ಟು ಸಲ ಬೇಕೋ ಅಷ್ಟು ಸಲ ಪುನರಾವರ್ತಿಸುವ **ಒಂದು** line ಬರೆಯುತ್ತೀರಿ: **for loop**.",
    },
    "learn": [
        "**for loop** ಪ್ರತಿ item ಗೆ ಒಂದು ಸಲ block ಅನ್ನು ಹೇಗೆ ಪುನರಾವರ್ತಿಸುತ್ತೆ",
        "**range()** numbers ನ ಸರಣಿ ಹೇಗೆ ಮಾಡುತ್ತೆ, ಮತ್ತು stop number ಯಾಕೆ ಬಿಟ್ಟುಹೋಗುತ್ತೆ",
        "**String** ನ ಅಕ್ಷರಗಳು ಮತ್ತು **list** ನ items ಮೇಲೆ loop ಹೇಗೆ ಮಾಡುವುದು",
        "Loop ಇಂದ **ಕೂಡಿಸುವುದು** ಅಥವಾ **ಎಣಿಸುವುದು**",
    ],
    "explanation": [
        {
            "heading": "Copy ಮಾಡದೆ ಪುನರಾವರ್ತನೆ",
            "md": "**for loop** ಒಂದೇ block ಅನ್ನು ಮತ್ತೆ ಮತ್ತೆ run ಮಾಡುತ್ತೆ, ಕೊಟ್ಟ ಪ್ರತಿ value ಗೆ ಒಂದು ಸಲ:\n\n" + E.C_FIRST + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_FIRST + "\n\nಪ್ರತಿ ಸುತ್ತಿನಲ್ಲಿ **loop variable** `day` ಮುಂದಿನ value ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ: ಮೊದಲು 1, ಆಮೇಲೆ 2, ಆಮೇಲೆ 3. Block ಒಂದು ಸಲ run ಆಗುವುದಕ್ಕೆ **iteration** ಅಂತಾರೆ.\n\n`if` ನ ನಿಯಮಗಳು ಇಲ್ಲೂ ಅನ್ವಯ: `for` line **colon** ಇಂದ ಮುಗಿಯುತ್ತೆ, block **4 spaces ಇಂದ indent** ಆಗಿರುತ್ತೆ. `print(\"Course complete\")` indent ಆಗಿಲ್ಲ, ಅದಕ್ಕೇ loop ಮುಗಿದಮೇಲೆ **ಒಂದು ಸಲ** run ಆಗುತ್ತೆ.",
            "callout": {"title": "Loop", "md": "ಮತ್ತೆ ಮತ್ತೆ run ಆಗುವ code block. for loop ಪ್ರತಿ value ಗೆ ಅದನ್ನು ಒಂದು ಸಲ run ಮಾಡುತ್ತೆ; ಪ್ರತಿ run ಒಂದು iteration."},
        },
        {
            "heading": "range(): numbers ನ ಸರಣಿ",
            "md": "Loop ಹಾದುಹೋಗುವ numbers ಅನ್ನು **range()** ಮಾಡುತ್ತೆ. ಇದಕ್ಕೆ ಮೂರು ರೂಪಗಳಿವೆ:\n\n" + RANGE_TABLE["kn"] + "\n\nಮೂರನೇ number **step**: ಪ್ರತಿ ಸಲ ಎಷ್ಟು ಸೇರಿಸಬೇಕು. ಪ್ರತಿ 8 ಗಂಟೆಗೆ ತೆಗೆದುಕೊಳ್ಳುವ ಔಷಧ:\n\n" + E.C_RANGE + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_RANGE,
            "callout": {"title": "Stop number ಯಾವತ್ತೂ ಸೇರಲ್ಲ", "md": "range(1, 6) slice ತರಹ 6 ಕ್ಕೆ ಸ್ವಲ್ಪ ಮುಂಚೆ ನಿಲ್ಲುತ್ತೆ. Day 1 ರಿಂದ 30 ಕ್ಕೆ range(1, 31) ಅಂತ ಬರೆಯಿರಿ."},
        },
        {
            "heading": "Text ಮತ್ತು lists ಮೇಲೆ loop",
            "md": "`for` loop numbers ಮಾತ್ರ ಅಲ್ಲ, ಬೇರೆಯದರ ಮೂಲಕವೂ ಹೋಗಬಹುದು. ಇದು **string** ನ ಪ್ರತಿ character ಗೆ, ಅಥವಾ **list** ನ ಪ್ರತಿ item ಗೆ ಹೋಗಬಹುದು: square brackets ಒಳಗೆ commas ಇಂದ ಬೇರ್ಪಡಿಸಿದ values.\n\n" + E.C_SEQ + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_SEQ + "\n\nLoop variable ಪ್ರತಿ item ಅನ್ನು ಸರದಿಯಲ್ಲಿ, ಮೊದಲಿನಿಂದ ಕೊನೆಯವರೆಗೆ ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ. Lists ಬಗ್ಗೆ Unit III ನಲ್ಲಿ ಇನ್ನೂ ಕಲಿಯುತ್ತೀರಿ.",
        },
        {
            "heading": "Loop ಇಂದ ಕೂಡಿಸುವುದು",
            "md": "Values ಕೂಡಿಸಲು loop ಗೆ **ಮುಂಚೆ** ಒಂದು **total** ಅನ್ನು 0 ಇಂದ ಶುರು ಮಾಡಿ, loop **ಒಳಗೆ** ಅದಕ್ಕೆ ಸೇರಿಸಿ. ಇದಕ್ಕೆ **accumulator** ಅಂತಾರೆ.\n\nಒಬ್ಬ adult ನ ಒಂದು ದಿನದ paracetamol doses:\n\n" + E.C_TOTAL + "\n\nಇದು `Total today: 2150 mg` print ಮಾಡುತ್ತೆ. ಬೇರೇನೂ print ಆಗಲ್ಲ, ಯಾಕೆಂದರೆ 2150, adults ನ ಸಾಮಾನ್ಯ daily limit ಆದ 4000 mg ಗಿಂತ ಜಾಸ್ತಿ ಇಲ್ಲ.\n\n`total += dose` Lesson 1.4 ನ shortcut: ಅಂದರೆ `total = total + dose`.",
            "callout": {"title": "Total ಅನ್ನು loop ಹೊರಗೆ ಶುರು ಮಾಡಿ", "md": "total = 0 loop ಒಳಗೆ ಇದ್ದರೆ, ಪ್ರತಿ ಸುತ್ತಿನಲ್ಲಿ ಅದು 0 ಆಗುತ್ತೆ, ನಿಮಗೆ ಕೊನೆಯ value ಮಾತ್ರ ಸಿಗುತ್ತೆ."},
        },
        {
            "heading": "Loop ಒಳಗೆ if",
            "md": "Loop ಮತ್ತು `if` ಒಟ್ಟಿಗೆ ಚೆನ್ನಾಗಿ ಕೆಲಸ ಮಾಡುತ್ತವೆ: loop ಪ್ರತಿ value ಗೆ ಹೋಗುತ್ತೆ, `if` ಮುಖ್ಯವಾದವನ್ನು ಆರಿಸುತ್ತೆ. ಇಲ್ಲಿ nurse ನ temperature readings ನಲ್ಲಿ ಜ್ವರ check ಮಾಡಿ ಎಣಿಸಲಾಗುತ್ತೆ:\n\n" + E.C_COUNT + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_COUNT + "\n\n`if` block ಗೆ 8 spaces, ಯಾಕೆಂದರೆ ಅದು loop ಒಳಗಿದೆ. ಕೊನೆಯ `print` ಗೆ ಯಾವುದೂ ಇಲ್ಲ, ಅದಕ್ಕೇ ಎಲ್ಲಾ readings check ಆದಮೇಲೆ ಅದು ಒಂದು ಸಲ run ಆಗುತ್ತೆ.",
        },
    ],
    "walkthrough": {
        "intro": "ಈ program 3 ದಿನದ tablet chart print ಮಾಡಿ, patient ಗೆ ಎಷ್ಟು tablets ಬೇಕು ಅಂತ ಎಣಿಸುತ್ತೆ.",
        "keyTerms": [
            {"meaning": "ಪ್ರತಿ value ಗೆ block ಒಂದು ಸಲ ಪುನರಾವರ್ತಿಸು, value day ನಲ್ಲಿ ಇರುತ್ತೆ."},
            {"meaning": "Numbers 1, 2 ಮತ್ತು 3 (4 ಬಿಟ್ಟುಹೋಗುತ್ತೆ)."},
            {"meaning": "Loop ಗೆ ಮುಂಚೆ running total ಶುರು ಮಾಡು."},
            {"meaning": "ಪ್ರತಿ ಸುತ್ತಿನಲ್ಲಿ total ಗೆ 2 ಸೇರಿಸು."},
        ],
    },
    "errors": {
        "intro": "ಈ ಎರಡು errors for line ಇಂದಲೇ ಬರುತ್ತವೆ.",
        "examples": [
            {"title": "Colon ಮರೆಯುವುದು", "md": "`if` ತರಹ, `for` line ಕೂಡ colon ಇಂದ ಮುಗಿಯಬೇಕು: `for day in range(1, 4):`."},
            {"title": "range() ಗೆ number ಬದಲು text ಕೊಡುವುದು", "md": "`\"5\"` ಒಂದು string, ಉದಾ. `input()` ಇಂದ ಬಂದದ್ದು. `range()` ಗೆ integer ಬೇಕು. ಮೊದಲು ಬದಲಾಯಿಸಿ: `range(int(days))`."},
        ],
    },
    "mistakes": [
        {"mistake": "`range(1, 30)` ನಲ್ಲಿ 30 ಕೂಡ ಇದೆ ಅಂದುಕೊಳ್ಳುವುದು", "see": "Error ಇಲ್ಲ, ಆದರೆ chart Day 29 ಕ್ಕೆ ನಿಲ್ಲುತ್ತೆ", "fix": "Stop ಬಿಟ್ಟುಹೋಗುತ್ತೆ, ಅದಕ್ಕೇ `range(1, 31)` ಅಂತ ಬರೆಯಿರಿ."},
        {"mistake": "`total = 0` ಅನ್ನು loop ಒಳಗೆ ಇಡುವುದು", "see": "Error ಇಲ್ಲ, ಆದರೆ total ಕೊನೆಯ value ಮಾತ್ರ", "fix": "Total ಅನ್ನು ಒಂದು ಸಲ, loop ಗೆ ಮುಂಚೆ ಶುರು ಮಾಡಿ."},
        {"mistake": "ಕೊನೆಯ `print` ಅನ್ನು ತಪ್ಪಾಗಿ indent ಮಾಡುವುದು", "see": "Error ಇಲ್ಲ, ಆದರೆ ಪ್ರತಿ iteration ಆದಮೇಲೆ total print ಆಗುತ್ತೆ", "fix": "ಒಂದು ಸಲ run ಆಗಬೇಕಾದ lines ಅನ್ನು loop ಆದಮೇಲೆ, indentation ಇಲ್ಲದೆ ಇಡಿ."},
        {"mistake": "`range()` ಗೆ decimal ಕೊಡುವುದು, ಉದಾ. `range(1, 7.5)`", "see": "TypeError: 'float' object cannot be interpreted as an integer", "fix": "`range()` ಪೂರ್ಣ numbers ಮಾತ್ರ ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ. `int()` ಅಥವಾ ಪೂರ್ಣ number ಬಳಸಿ."},
    ],
    "tasks": [
        {"title": "Doses ಗೆ number ಕೊಡಿ", "md": "**range()** ಜೊತೆ **for loop** ಬಳಸಿ ದಿನದ ಮೂರು doses ಅನ್ನು ಸರಿಯಾಗಿ ಹೀಗೆ print ಮಾಡಿ:",
         "hints": ["range(1, 4) ಇಂದ 1, 2 ಮತ್ತು 3 ಸಿಗುತ್ತವೆ.", "for n in range(1, 4):\n    print(f\"Dose {n}\")"]},
        {"title": "ಪ್ರತಿ 6 ಗಂಟೆಗೆ", "md": "ಒಂದು antibiotic ಅನ್ನು ಪ್ರತಿ 6 ಗಂಟೆಗೆ, ಮಧ್ಯರಾತ್ರಿಯಿಂದ ಶುರು ಮಾಡಿ ಕೊಡಲಾಗುತ್ತೆ. Output ಸರಿಯಾಗಿ ಹೀಗೇ ಬರುವ ಹಾಗೆ **step ಇರುವ range()** ಬಳಸಿ:",
         "hints": ["range() ನ ಮೂರನೇ number step: range(0, 24, 6).", "for hour in range(0, 24, 6):\n    print(f\"Dose at {hour}:00\")"]},
        {"title": "Doses ಕೂಡಿಸಿ", "md": "List ನ doses ಅನ್ನು loop ಇಂದ ಕೂಡಿಸಿ, total ಅನ್ನು ಸರಿಯಾಗಿ ಹೀಗೆ print ಮಾಡಿ:",
         "hints": ["Loop ಒಳಗೆ: total += dose", "for dose in doses:\n    total += dose\nprint(\"Total:\", total, \"mg\")"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "ಒಬ್ಬ patient 7 ದಿನ ದಿನಕ್ಕೆ 3 tablets ತೆಗೆದುಕೊಳ್ಳುತ್ತಾರೆ, ಅದಕ್ಕೇ 21 tablets ಬೇಕು. ಈ program 3 ಅಂತ ಹೇಳುತ್ತೆ, error ಇಲ್ಲ. Output ಸರಿಯಾಗಿ ಹೀಗೇ ಬರುವ ಹಾಗೆ ಸರಿ ಮಾಡಿ:",
         "hints": ["ಪ್ರತಿ iteration ಶುರುವಿನಲ್ಲಿ total ಗೆ ಏನಾಗುತ್ತೆ?", "Loop ಒಳಗಿನ total = 0 ತೆಗೆಯಿರಿ. Loop ಗೆ ಮುಂಚಿನದು ಸಾಕು."],
         "solutionNote": "Loop ಒಳಗಿನ total = 0 ಪ್ರತಿ ದಿನ total ಅನ್ನು reset ಮಾಡುತ್ತಿತ್ತು, ಅದಕ್ಕೇ ಕೊನೆಯ 3 ಮಾತ್ರ ಉಳಿಯುತ್ತಿತ್ತು. Loop ಗೆ ಮುಂಚೆ ಒಂದು ಸಲ ಶುರು ಮಾಡಿದರೆ ಅದು 21 ವರೆಗೆ ಬೆಳೆಯುತ್ತೆ."},
    ],
    "quiz": [
        {"q": "range(1, 4) ಯಾವ numbers ಕೊಡುತ್ತೆ?", "why": "range stop number 4 ಕ್ಕೆ ಸ್ವಲ್ಪ ಮುಂಚೆ ನಿಲ್ಲುತ್ತೆ."},
        {"q": "for i in range(3):\n    print(\"Shake well\")\n\n\"Shake well\" ಎಷ್ಟು ಸಲ print ಆಗುತ್ತೆ?", "why": "range(3) ಇಂದ 0, 1 ಮತ್ತು 2: ಮೂರು values, ಅದಕ್ಕೇ ಮೂರು iterations."},
        {"q": "range(0, 10, 5) ಏನು ಕೊಡುತ್ತೆ?", "why": "0 ಇಂದ ಶುರು, ಪ್ರತಿ ಸಲ 5 ಸೇರಿಸಿ, 10 ಕ್ಕೆ ಮುಂಚೆ ನಿಲ್ಲಿ."},
        {"q": "total = 0\nfor n in range(1, 4):\n    total += n\nprint(total)\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "1 + 2 + 3 = 6."},
        {"q": "for ch in \"ABC\":\n    print(ch)\n\nಏನು print ಆಗುತ್ತೆ?", "why": "Loop ಪ್ರತಿ character ಗೆ ಹೋಗುತ್ತೆ, ಪ್ರತಿ print ಹೊಸ line ಇಂದ ಶುರುವಾಗುತ್ತೆ."},
        {"q": "Loop ಮುಗಿದಮೇಲೆ ಯಾವ line ಒಂದೇ ಸಲ run ಆಗುತ್ತೆ?", "why": "Indent ಆಗದ lines loop ಹೊರಗಿವೆ, ಅದಕ್ಕೇ ಅದು ಮುಗಿದಮೇಲೆ ಒಂದು ಸಲ run ಆಗುತ್ತವೆ."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 2.3 · for loops",
        "children": [
            {"label": "for loop", "children": [{"label": "ಪ್ರತಿ value ಗೆ ಪುನರಾವರ್ತನೆ"}, {"label": "Loop variable"}, {"label": "Iteration = ಒಂದು run"}]},
            {"label": "range()", "children": [{"label": "range(5) → 0-4"}, {"label": "range(1, 6) → 1-5"}, {"label": "range(0, 24, 8) → step"}]},
            {"label": "Sequences", "children": [{"label": "String ನ characters"}, {"label": "List ನ items"}]},
            {"label": "Patterns", "children": [{"label": "ಮುಂಚೆ total = 0"}, {"label": "ಒಳಗೆ total += value"}, {"label": "if ಇಂದ ಎಣಿಕೆ"}]},
            {"label": "Syntax", "children": [{"label": "Colon :"}, {"label": "4-space block"}, {"label": "Loop ಆದಮೇಲೆ ಒಂದು ಸಲ"}]},
            {"label": "Errors", "children": [{"label": "SyntaxError: expected ':'"}, {"label": "TypeError: range ನಲ್ಲಿ str/float"}]},
        ],
    },
    "summary": [
        "**for loop** ತನ್ನ indent ಮಾಡಿದ block ಅನ್ನು **ಪ್ರತಿ value** ಗೆ ಒಂದು ಸಲ run ಮಾಡುತ್ತೆ; **loop variable** ನಲ್ಲಿ ಈಗಿನ value ಇರುತ್ತೆ, ಪ್ರತಿ run ಒಂದು **iteration**.",
        "**range(stop)**, **range(start, stop)** ಮತ್ತು **range(start, stop, step)** ಪೂರ್ಣ numbers ನ ಸರಣಿ ಮಾಡುತ್ತವೆ; **stop ಯಾವತ್ತೂ ಸೇರಲ್ಲ**.",
        "for loop **string ನ ಪ್ರತಿ character** ಅಥವಾ **list ನ ಪ್ರತಿ item** ಗೂ ಹೋಗಬಹುದು.",
        "ಕೂಡಿಸಲು loop ಗೆ **ಮುಂಚೆ** `total = 0` ಶುರು ಮಾಡಿ, **ಒಳಗೆ** `total += value` ಬಳಸಿ.",
        "**Loop ಒಳಗಿನ if** ಮುಖ್ಯ values ಅನ್ನು ಆರಿಸುತ್ತೆ ಅಥವಾ ಎಣಿಸುತ್ತೆ. Loop ಆದಮೇಲಿನ, indentation ಇಲ್ಲದ lines ಒಂದು ಸಲ run ಆಗುತ್ತವೆ.",
    ],
}

NARR = {
    "hi": [
        "यह program दो lines दोहराता है, course के हर दिन के लिए एक बार, और एक running total रखता है।",
        "Comment बताता है कि program क्या करता है।",
        "total loop से पहले zero से शुरू होता है।",
        "range एक से चार, एक, दो और तीन देता है। Loop शुरू होता है, और day एक है।",
        "Total में दो tablets जुड़ती हैं, तो total दो है।",
        "print दिन एक दिखाता है।",
        "Block खत्म हुआ, इसलिए Python loop के ऊपर लौटता है। day दो हो जाता है।",
        "total चार हो जाता है, और print दिन दो दिखाता है।",
        "दिन तीन के लिए एक बार और। total छह हो जाता है।",
        "range में कोई number नहीं बचा, इसलिए loop खत्म। आखिरी line indent नहीं है, इसलिए एक बार चलती है, और total दिखाती है।",
    ],
    "hinglish": [
        "Yeh program do lines dohraata hai, course ke har din ke liye ek baar, aur ek running total rakhta hai.",
        "Comment batata hai ki program kya karta hai.",
        "total loop se pehle zero se shuru hota hai.",
        "range ek se chaar, ek, do aur teen deta hai. Loop shuru hota hai, aur day ek hai.",
        "Total mein do tablets judti hain, to total do hai.",
        "print din ek dikhaata hai.",
        "Block khatam hua, isliye Python loop ke upar lautta hai. day do ho jaata hai.",
        "total chaar ho jaata hai, aur print din do dikhaata hai.",
        "Din teen ke liye ek baar aur. total chhah ho jaata hai.",
        "range mein koi number nahi bacha, isliye loop khatam. Aakhri line indent nahi hai, isliye ek baar chalti hai, aur total dikhaati hai.",
    ],
    "kn": [
        "ಈ program ಎರಡು lines ಅನ್ನು course ನ ಪ್ರತಿ ದಿನಕ್ಕೆ ಒಂದು ಸಲ ಪುನರಾವರ್ತಿಸುತ್ತೆ, ಮತ್ತು ಒಂದು running total ಇಟ್ಟುಕೊಳ್ಳುತ್ತೆ.",
        "Comment ಈ program ಏನು ಮಾಡುತ್ತೆ ಅಂತ ಹೇಳುತ್ತೆ.",
        "total loop ಗೆ ಮುಂಚೆ zero ಇಂದ ಶುರುವಾಗುತ್ತೆ.",
        "range ಒಂದರಿಂದ ನಾಲ್ಕು, ಒಂದು, ಎರಡು ಮತ್ತು ಮೂರು ಕೊಡುತ್ತೆ. Loop ಶುರುವಾಗುತ್ತೆ, day ಒಂದು.",
        "Total ಗೆ ಎರಡು tablets ಸೇರುತ್ತವೆ, ಅದಕ್ಕೇ total ಎರಡು.",
        "print ದಿನ ಒಂದನ್ನು ತೋರಿಸುತ್ತೆ.",
        "Block ಮುಗಿಯಿತು, ಅದಕ್ಕೇ Python loop ನ ಮೇಲಕ್ಕೆ ಹಿಂತಿರುಗುತ್ತೆ. day ಎರಡು ಆಗುತ್ತೆ.",
        "total ನಾಲ್ಕು ಆಗುತ್ತೆ, print ದಿನ ಎರಡನ್ನು ತೋರಿಸುತ್ತೆ.",
        "ದಿನ ಮೂರಕ್ಕೆ ಇನ್ನೊಂದು ಸಲ. total ಆರು ಆಗುತ್ತೆ.",
        "range ನಲ್ಲಿ ಯಾವ number ಕೂಡ ಉಳಿದಿಲ್ಲ, ಅದಕ್ಕೇ loop ಮುಗಿಯುತ್ತೆ. ಕೊನೆಯ line indent ಆಗಿಲ್ಲ, ಅದಕ್ಕೇ ಒಂದು ಸಲ run ಆಗಿ total ತೋರಿಸುತ್ತೆ.",
    ],
}

ANIM = {
    "hi": [
        "total zero से शुरू होता है। Loop तीन बार घूमेगा, दिन एक, दो और तीन के लिए।",
        "पहली बार day एक है। दो tablets जुड़ती हैं, और दिन एक print होता है।",
        "वापस ऊपर। day दो है, और total बढ़कर चार हो जाता है।",
        "एक बार और: दिन तीन, total छह।",
        "कोई number नहीं बचा, इसलिए loop खत्म होता है, और आखिरी line सिर्फ़ एक बार चलती है।",
    ],
    "hinglish": [
        "total zero se shuru hota hai. Loop teen baar ghoomega, din ek, do aur teen ke liye.",
        "Pehli baar day ek hai. Do tablets judti hain, aur din ek print hota hai.",
        "Wapas upar. day do hai, aur total badhkar chaar ho jaata hai.",
        "Ek baar aur: din teen, total chhah.",
        "Koi number nahi bacha, isliye loop khatam hota hai, aur aakhri line sirf ek baar chalti hai.",
    ],
    "kn": [
        "total zero ಇಂದ ಶುರುವಾಗುತ್ತೆ. Loop ಮೂರು ಸಲ ಸುತ್ತುತ್ತೆ, ದಿನ ಒಂದು, ಎರಡು ಮತ್ತು ಮೂರಕ್ಕೆ.",
        "ಮೊದಲ ಸುತ್ತಿನಲ್ಲಿ day ಒಂದು. ಎರಡು tablets ಸೇರುತ್ತವೆ, ದಿನ ಒಂದು print ಆಗುತ್ತೆ.",
        "ಮತ್ತೆ ಮೇಲಕ್ಕೆ. day ಎರಡು, total ನಾಲ್ಕಕ್ಕೆ ಬೆಳೆಯುತ್ತೆ.",
        "ಇನ್ನೊಂದು ಸಲ: ದಿನ ಮೂರು, total ಆರು.",
        "ಯಾವ number ಕೂಡ ಉಳಿದಿಲ್ಲ, ಅದಕ್ಕೇ loop ಮುಗಿಯುತ್ತೆ, ಕೊನೆಯ line ಒಂದೇ ಸಲ run ಆಗುತ್ತೆ.",
    ],
}

if __name__ == "__main__":
    build("2-3", "anim-loop", T, NARR, ANIM)

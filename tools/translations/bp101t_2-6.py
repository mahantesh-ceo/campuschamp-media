"""Lesson 2.6 translations (Hindi, Hinglish, Kannada) and voice scripts."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import build  # noqa: E402

_spec = importlib.util.spec_from_file_location("en26", os.path.join(os.path.dirname(__file__), "..", "lessons", "bp101t_2-6_en.py"))
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)

T = {}

T["hi"] = {
    "hook": {
        "title": "Pharmacy में use होने वाले दो tools बनाइए",
        "md": "अब आप **if**, **loops** और **functions** जानते हैं। इन्हें साथ जोड़िए, और आप असली tools बना सकते हैं।\n\nइस project में आप दो calculators बनाएँगे जो आपको pharmacy subjects में फिर मिलेंगे:\n\n1. एक **BMI calculator**, जो यह भी बताए कि number का मतलब क्या है।\n2. **बच्चों के dose calculators**, **Young's rule** और **Clark's rule** से।\n\n*ये calculators Python सीखने और pharmacology के हिसाब जाँचने के लिए हैं। असली dose हमेशा prescriber, label और official references से आती है।*",
    },
    "learn": [
        "Code लिखने से पहले program को छोटे functions में **plan** करना",
        "**BMI** calculator बनाना जो **if-elif-else** से category return करे",
        "**Young's rule** और **Clark's rule** को functions में बदलना",
        "**Safety checks** जोड़ना और कई patients के लिए **loop** use करना",
    ],
    "explanation": [
        {
            "heading": "Code से पहले plan",
            "md": "Professional programmers problem को छोटे कामों में बाँटते हैं, और **हर काम के लिए एक function** लिखते हैं। BMI tool के लिए:\n\n1. Weight और height से BMI **निकालना**: `bmi(weight_kg, height_m)`।\n2. Number को category में **बाँटना**: `bmi_category(value)`।\n3. नतीजा user को `print()` से **दिखाना**।\n\nहर function छोटा है, उसका नाम साफ़ है, और उसे अलग से test कर सकते हैं। अगर category की limits बदलें, तो आप **एक** function बदलते हैं, और program का हर हिस्सा जो उसे use करता है, अपने-आप update हो जाता है।",
            "callout": {"title": "एक function, एक काम", "md": "अगर किसी function का काम एक छोटे वाक्य में न बता पाएँ, तो उसे दो में बाँट दीजिए।"},
        },
        {
            "heading": "Calculator 1: BMI",
            "md": "**Body Mass Index** है kilograms में weight भाग metres में height का square: BMI = weight ÷ height²। Python में `**` का मतलब \"की power\" है (Lesson 1.4), इसलिए height² है `height_m ** 2`।\n\n" + E.C_BMI + "\n\nयह `BMI: 23.5 (Normal)` print करता है, क्योंकि 68 ÷ 1.70² = 68 ÷ 2.89 ≈ 23.5।\n\nध्यान दीजिए, `bmi_category` text को print करने की जगह **return** करता है। इससे वह दोबारा use हो सकता है: वही function label, report या screen भर सकता है।",
            "callout": {"title": "Indian cut-offs", "md": "ये WHO की categories हैं। Indian guidelines adults के लिए नीची limits use करती हैं: 23 से overweight, 25 से obese। बस एक function बदलना होगा।"},
        },
        {
            "heading": "Calculator 2: बच्चों के doses",
            "md": "Pharmacology के दो पुराने नियम adult dose से बच्चे का dose अंदाज़ा लगाते हैं:\n\n- **Young's rule** (उम्र से, 1 से 12 साल के बच्चों के लिए): child dose = age ÷ (age + 12) × adult dose।\n- **Clark's rule** (वज़न से): child dose = kg में weight ÷ 70 × adult dose। (असली नियम pounds और 150 use करता है; 70 kg आम metric रूप है।)\n\nहर नियम एक line का function बन जाता है:\n\n" + E.C_CHILD + "\n\nयह print करता है:\n\n" + E.O_CHILD + "\n\n6 ÷ 18 × 500 = 166.67, और 20 ÷ 70 × 500 = 142.86। **round()** सबसे पास के पूरे number पर round करता है, जो label पर पढ़ने में आसान है।",
            "callout": {"title": "round()", "md": "round(x) सबसे पास का पूरा number देता है; round(x, 1) एक decimal place रखता है। round(166.67) है 167।"},
        },
        {
            "heading": "Safety checks जोड़ना",
            "md": "Dose वाले calculator को बेतुकी values मना करनी चाहिए और limits माननी चाहिए। Checks को function के **अंदर** रखिए, ताकि हर call करने वाले को वो मुफ़्त मिलें:\n\n" + E.C_SAFE + "\n\nFunction बेमतलब weight पर 0 return करता है, mg-per-kg dose निकालता है, और उसे maximum पर रोक देता है। `if` के अंदर का `return` function को जल्दी खत्म कर देता है, इसलिए नीचे की lines नहीं चलतीं।",
        },
        {
            "heading": "एक loop से कई patients",
            "md": "हिसाब function में है, इसलिए एक **loop** उसे पूरे ward के patients के लिए use कर सकता है:\n\n" + E.C_TABLE + "\n\nयह print करता है:\n\n" + E.O_TABLE + "\n\n40 kg के बच्चे को 15 × 40 = 600 mg मिलता, पर function ने उसे 500 पर रोक दिया। Functions, `if` और loops साथ में: चार lines में पूरा Unit II।",
        },
    ],
    "walkthrough": {
        "intro": "यह program दो functions और एक loop से तीन patients का BMI और category निकालता है, जिनकी height 1.70 m है।",
        "keyTerms": [
            {"meaning": "Height का square (2 की power)।"},
            {"meaning": "Category वापस भेजो और function खत्म करो।"},
            {"meaning": "तभी पहुँचते हैं जब ऊपर की कोई condition True न हो।"},
            {"meaning": "BMI को एक decimal place के साथ दिखाओ।"},
        ],
    },
    "errors": {
        "intro": "Inputs गलत हों तो calculators fail होते हैं। ये दो सबसे आम errors हैं।",
        "examples": [
            {"title": "Zero height", "md": "Zero से भाग देना संभव नहीं। पहले input जाँचिए, जैसे `if height_m <= 0: return 0`, या user से फिर पूछिए।"},
            {"title": "ऐसा number जो अब भी text है", "md": "`input()` हमेशा text देता है। हिसाब से पहले बदलिए: `weight = float(input(\"Weight (kg): \"))`।"},
        ],
    },
    "mistakes": [
        {"mistake": "Height centimetres में डालना, जैसे `bmi(68, 170)`", "see": "कोई error नहीं, पर BMI 0.0024 आता है", "fix": "BMI को metres चाहिए: 170 cm यानी 1.70 m। पहले 100 से भाग दीजिए।"},
        {"mistake": "`height_m ** 2` की जगह `height_m * 2` लिखना", "see": "कोई error नहीं, पर BMI बहुत ज़्यादा आता है", "fix": "`* 2` दोगुना करता है; `** 2` square करता है।"},
        {"mistake": "Clark's rule में units मिलाना, जैसे kg वाले रूप (÷ 70) के साथ pounds", "see": "कोई error नहीं, पर dose दोगुने से भी ज़्यादा आता है", "fix": "एक unit रखिए: kg के साथ 70, या pounds के साथ 150। Unit को parameter के नाम में रखिए: `weight_kg`।"},
        {"mistake": "Calculator function में return की जगह print करना", "see": "पहले कोई error नहीं, पर नतीजा label या loop में use नहीं हो सकता", "fix": "Number return कीजिए; जहाँ चाहिए वहाँ print कीजिए।"},
    ],
    "tasks": [
        {"title": "BMI function पूरा कीजिए", "md": "**bmi()** से weight भाग height का square return करवाइए। Print पहले से लिखा है; output बिल्कुल यह होना चाहिए:",
         "hints": ["Height का square है height_m ** 2।", "    return weight_kg / height_m ** 2"]},
        {"title": "Category return कीजिए", "md": "**bmi_category()** को **if-elif-else** से पूरा कीजिए: 18.5 से कम \"Underweight\", 25 से कम \"Normal\", 30 से कम \"Overweight\", वरना \"Obese\"। 26.1 के लिए output बिल्कुल यह होना चाहिए:",
         "hints": ["हर branch एक शब्द return करती है: return \"Normal\"", "    if value < 18.5:\n        return \"Underweight\"\n    elif value < 25:\n        return \"Normal\"\n    elif value < 30:\n        return \"Overweight\"\n    else:\n        return \"Obese\""]},
        {"title": "Young's rule", "md": "**youngs_rule(age, adult_dose)** लिखिए जो age ÷ (age + 12) × adult dose return करे। 4 साल के बच्चे और 500 mg adult dose के लिए output बिल्कुल यह होना चाहिए:",
         "hints": ["Brackets ज़रूरी हैं: age / (age + 12) * adult_dose", "def youngs_rule(age, adult_dose):\n    return age / (age + 12) * adult_dose"]},
        {"title": "Bug ढूँढिए", "md": "Clark's rule से 35 kg के बच्चे को, 400 mg adult dose पर, 35 ÷ 70 × 400 = 200 mg मिलना चाहिए। यह program 0 mg बताता है, और कोई error नहीं। इसे ठीक कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["देखिए कि brackets की वजह से Python किससे भाग दे रहा है।", "Brackets से यह 28000 से भाग देता है। weight_kg / 70 * adult_dose लिखिए।"],
         "solutionNote": "Brackets के साथ Python ने 35 को 70 × 400 = 28000 से भाग दिया, जिससे 0.00125 मिला, जो round होकर 0 हुआ। Brackets के बिना वह पहले 70 से भाग देता है, फिर 400 से गुणा करता है।"},
    ],
    "quiz": [
        {"q": "एक patient का weight 72 kg और height 1.80 m है। BMI क्या है?", "why": "72 ÷ 1.80² = 72 ÷ 3.24 ≈ 22.2।"},
        {"q": "Young's rule का formula कौन-सा है?", "why": "Young's rule उम्र use करता है: age ÷ (age + 12) × adult dose।"},
        {"q": "इस lesson के bmi_category function से bmi_category(30) क्या return करता है?", "why": "30 < 30 False है, इसलिए कोई condition True नहीं, और else branch Obese return करती है।"},
        {"q": "round(166.67) क्या है?", "why": "round() सबसे पास का पूरा number देता है: 167।"},
        {"q": "यह lesson हर हिसाब को अलग function में क्यों रखता है?", "why": "छोटे नाम वाले functions दोबारा use होते हैं, test करना आसान है, और हर call करने वाले के लिए एक बार में ठीक होते हैं।"},
        {"q": "1.70 ** 2 क्या निकालता है?", "why": "** power operator है: 1.70 का square।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 2.6 · Dosage और BMI calculators",
        "children": [
            {"label": "Plan", "children": [{"label": "एक function, एक काम"}, {"label": "निकालो → बाँटो → दिखाओ"}]},
            {"label": "BMI", "children": [{"label": "weight / height ** 2"}, {"label": "if-elif-else category"}, {"label": "Return करो, print नहीं"}]},
            {"label": "बच्चों का dose", "children": [{"label": "Young's: age/(age+12) × adult"}, {"label": "Clark's: kg/70 × adult"}, {"label": "round()"}]},
            {"label": "Safety", "children": [{"label": "weight <= 0 मना"}, {"label": "Maximum पर रोक"}, {"label": "जल्दी return"}]},
            {"label": "Loop", "children": [{"label": "कई patients"}, {"label": "while True वाला menu"}]},
            {"label": "Errors", "children": [{"label": "ZeroDivisionError"}, {"label": "TypeError: str input"}]},
        ],
    },
    "summary": [
        "Program को **छोटे functions** में plan कीजिए, हर एक का एक काम: निकालना, बाँटना, दिखाना।",
        "**BMI** = weight (kg) ÷ height (m)², लिखा जाता है `weight_kg / height_m ** 2`; एक **if-elif-else** function उसकी category return करता है।",
        "**Young's rule** (age ÷ (age + 12) × adult dose) और **Clark's rule** (kg ÷ 70 × adult dose) एक-एक line के functions बनते हैं; **round()** नतीजा साफ़ करता है।",
        "**Safety checks** function के अंदर रखिए: असंभव inputs मना कीजिए और doses पर limit लगाइए, जल्दी `return` से।",
        "एक **loop** वही functions कई patients के लिए चला सकता है, या `while True` और `break` से **menu** दिखा सकता है।",
    ],
}

T["hinglish"] = {
    "hook": {
        "title": "Pharmacy mein use hone wale do tools banaaiye",
        "md": "Ab aap **if**, **loops** aur **functions** jaante hain. Inhe saath jodiye, aur aap asli tools bana sakte hain.\n\nIs project mein aap do calculators banaayenge jo aapko pharmacy subjects mein phir milenge:\n\n1. Ek **BMI calculator**, jo yeh bhi bataaye ki number ka matlab kya hai.\n2. **Bachchon ke dose calculators**, **Young's rule** aur **Clark's rule** se.\n\n*Yeh calculators Python seekhne aur pharmacology ke hisaab jaanchne ke liye hain. Asli dose hamesha prescriber, label aur official references se aati hai.*",
    },
    "learn": [
        "Code likhne se pehle program ko chhote functions mein **plan** karna",
        "**BMI** calculator banaana jo **if-elif-else** se category return kare",
        "**Young's rule** aur **Clark's rule** ko functions mein badalna",
        "**Safety checks** jodna aur kai patients ke liye **loop** use karna",
    ],
    "explanation": [
        {
            "heading": "Code se pehle plan",
            "md": "Professional programmers problem ko chhote kaamon mein baant-te hain, aur **har kaam ke liye ek function** likhte hain. BMI tool ke liye:\n\n1. Weight aur height se BMI **nikaalna**: `bmi(weight_kg, height_m)`.\n2. Number ko category mein **baantna**: `bmi_category(value)`.\n3. Nateeja user ko `print()` se **dikhaana**.\n\nHar function chhota hai, uska naam saaf hai, aur use alag se test kar sakte hain. Agar category ki limits badlein, to aap **ek** function badalte hain, aur program ka har hissa jo use use karta hai, apne-aap update ho jaata hai.",
            "callout": {"title": "Ek function, ek kaam", "md": "Agar kisi function ka kaam ek chhote vaakya mein na bata paayein, to use do mein baant dijiye."},
        },
        {
            "heading": "Calculator 1: BMI",
            "md": "**Body Mass Index** hai kilograms mein weight bhaag metres mein height ka square: BMI = weight ÷ height². Python mein `**` ka matlab \"ki power\" hai (Lesson 1.4), isliye height² hai `height_m ** 2`.\n\n" + E.C_BMI + "\n\nYeh `BMI: 23.5 (Normal)` print karta hai, kyonki 68 ÷ 1.70² = 68 ÷ 2.89 ≈ 23.5.\n\nDhyaan dijiye, `bmi_category` text ko print karne ki jagah **return** karta hai. Isse woh dobara use ho sakta hai: wahi function label, report ya screen bhar sakta hai.",
            "callout": {"title": "Indian cut-offs", "md": "Yeh WHO ki categories hain. Indian guidelines adults ke liye neechi limits use karti hain: 23 se overweight, 25 se obese. Bas ek function badalna hoga."},
        },
        {
            "heading": "Calculator 2: bachchon ke doses",
            "md": "Pharmacology ke do puraane niyam adult dose se bachche ka dose andaaza lagaate hain:\n\n- **Young's rule** (umar se, 1 se 12 saal ke bachchon ke liye): child dose = age ÷ (age + 12) × adult dose.\n- **Clark's rule** (wazan se): child dose = kg mein weight ÷ 70 × adult dose. (Asli niyam pounds aur 150 use karta hai; 70 kg aam metric roop hai.)\n\nHar niyam ek line ka function ban jaata hai:\n\n" + E.C_CHILD + "\n\nYeh print karta hai:\n\n" + E.O_CHILD + "\n\n6 ÷ 18 × 500 = 166.67, aur 20 ÷ 70 × 500 = 142.86. **round()** sabse paas ke poore number par round karta hai, jo label par padhne mein aasaan hai.",
            "callout": {"title": "round()", "md": "round(x) sabse paas ka poora number deta hai; round(x, 1) ek decimal place rakhta hai. round(166.67) hai 167."},
        },
        {
            "heading": "Safety checks jodna",
            "md": "Dose wale calculator ko betuki values mana karni chahiye aur limits maanni chahiye. Checks ko function ke **andar** rakhiye, taaki har call karne wale ko woh muft milein:\n\n" + E.C_SAFE + "\n\nFunction bematlab weight par 0 return karta hai, mg-per-kg dose nikaalta hai, aur use maximum par rok deta hai. `if` ke andar ka `return` function ko jaldi khatam kar deta hai, isliye neeche ki lines nahi chalti.",
        },
        {
            "heading": "Ek loop se kai patients",
            "md": "Hisaab function mein hai, isliye ek **loop** use poore ward ke patients ke liye use kar sakta hai:\n\n" + E.C_TABLE + "\n\nYeh print karta hai:\n\n" + E.O_TABLE + "\n\n40 kg ke bachche ko 15 × 40 = 600 mg milta, par function ne use 500 par rok diya. Functions, `if` aur loops saath mein: chaar lines mein poora Unit II.",
        },
    ],
    "walkthrough": {
        "intro": "Yeh program do functions aur ek loop se teen patients ka BMI aur category nikaalta hai, jinki height 1.70 m hai.",
        "keyTerms": [
            {"meaning": "Height ka square (2 ki power)."},
            {"meaning": "Category wapas bhejo aur function khatam karo."},
            {"meaning": "Tabhi pahunchte hain jab upar ki koi condition True na ho."},
            {"meaning": "BMI ko ek decimal place ke saath dikhaao."},
        ],
    },
    "errors": {
        "intro": "Inputs galat hon to calculators fail hote hain. Yeh do sabse aam errors hain.",
        "examples": [
            {"title": "Zero height", "md": "Zero se bhaag dena sambhav nahi. Pehle input jaanchiye, jaise `if height_m <= 0: return 0`, ya user se phir poochhiye."},
            {"title": "Aisa number jo ab bhi text hai", "md": "`input()` hamesha text deta hai. Hisaab se pehle badaliye: `weight = float(input(\"Weight (kg): \"))`."},
        ],
    },
    "mistakes": [
        {"mistake": "Height centimetres mein daalna, jaise `bmi(68, 170)`", "see": "Koi error nahi, par BMI 0.0024 aata hai", "fix": "BMI ko metres chahiye: 170 cm yaani 1.70 m. Pehle 100 se bhaag dijiye."},
        {"mistake": "`height_m ** 2` ki jagah `height_m * 2` likhna", "see": "Koi error nahi, par BMI bahut zyada aata hai", "fix": "`* 2` dugna karta hai; `** 2` square karta hai."},
        {"mistake": "Clark's rule mein units milaana, jaise kg wale roop (÷ 70) ke saath pounds", "see": "Koi error nahi, par dose dugne se bhi zyada aata hai", "fix": "Ek unit rakhiye: kg ke saath 70, ya pounds ke saath 150. Unit ko parameter ke naam mein rakhiye: `weight_kg`."},
        {"mistake": "Calculator function mein return ki jagah print karna", "see": "Pehle koi error nahi, par nateeja label ya loop mein use nahi ho sakta", "fix": "Number return kijiye; jahaan chahiye wahaan print kijiye."},
    ],
    "tasks": [
        {"title": "BMI function poora kijiye", "md": "**bmi()** se weight bhaag height ka square return karwaaiye. Print pehle se likha hai; output bilkul yeh hona chahiye:",
         "hints": ["Height ka square hai height_m ** 2.", "    return weight_kg / height_m ** 2"]},
        {"title": "Category return kijiye", "md": "**bmi_category()** ko **if-elif-else** se poora kijiye: 18.5 se kam \"Underweight\", 25 se kam \"Normal\", 30 se kam \"Overweight\", warna \"Obese\". 26.1 ke liye output bilkul yeh hona chahiye:",
         "hints": ["Har branch ek shabd return karti hai: return \"Normal\"", "    if value < 18.5:\n        return \"Underweight\"\n    elif value < 25:\n        return \"Normal\"\n    elif value < 30:\n        return \"Overweight\"\n    else:\n        return \"Obese\""]},
        {"title": "Young's rule", "md": "**youngs_rule(age, adult_dose)** likhiye jo age ÷ (age + 12) × adult dose return kare. 4 saal ke bachche aur 500 mg adult dose ke liye output bilkul yeh hona chahiye:",
         "hints": ["Brackets zaroori hain: age / (age + 12) * adult_dose", "def youngs_rule(age, adult_dose):\n    return age / (age + 12) * adult_dose"]},
        {"title": "Bug dhoondhiye", "md": "Clark's rule se 35 kg ke bachche ko, 400 mg adult dose par, 35 ÷ 70 × 400 = 200 mg milna chahiye. Yeh program 0 mg batata hai, aur koi error nahi. Ise theek kijiye taaki output bilkul yeh ho:",
         "hints": ["Dekhiye ki brackets ki wajah se Python kisse bhaag de raha hai.", "Brackets se yeh 28000 se bhaag deta hai. weight_kg / 70 * adult_dose likhiye."],
         "solutionNote": "Brackets ke saath Python ne 35 ko 70 × 400 = 28000 se bhaag diya, jisse 0.00125 mila, jo round hokar 0 hua. Brackets ke bina woh pehle 70 se bhaag deta hai, phir 400 se guna karta hai."},
    ],
    "quiz": [
        {"q": "Ek patient ka weight 72 kg aur height 1.80 m hai. BMI kya hai?", "why": "72 ÷ 1.80² = 72 ÷ 3.24 ≈ 22.2."},
        {"q": "Young's rule ka formula kaun-sa hai?", "why": "Young's rule umar use karta hai: age ÷ (age + 12) × adult dose."},
        {"q": "Is lesson ke bmi_category function se bmi_category(30) kya return karta hai?", "why": "30 < 30 False hai, isliye koi condition True nahi, aur else branch Obese return karti hai."},
        {"q": "round(166.67) kya hai?", "why": "round() sabse paas ka poora number deta hai: 167."},
        {"q": "Yeh lesson har hisaab ko alag function mein kyon rakhta hai?", "why": "Chhote naam wale functions dobara use hote hain, test karna aasaan hai, aur har call karne wale ke liye ek baar mein theek hote hain."},
        {"q": "1.70 ** 2 kya nikaalta hai?", "why": "** power operator hai: 1.70 ka square."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 2.6 · Dosage aur BMI calculators",
        "children": [
            {"label": "Plan", "children": [{"label": "Ek function, ek kaam"}, {"label": "Nikaalo → baanto → dikhaao"}]},
            {"label": "BMI", "children": [{"label": "weight / height ** 2"}, {"label": "if-elif-else category"}, {"label": "Return karo, print nahi"}]},
            {"label": "Bachchon ka dose", "children": [{"label": "Young's: age/(age+12) × adult"}, {"label": "Clark's: kg/70 × adult"}, {"label": "round()"}]},
            {"label": "Safety", "children": [{"label": "weight <= 0 mana"}, {"label": "Maximum par rok"}, {"label": "Jaldi return"}]},
            {"label": "Loop", "children": [{"label": "Kai patients"}, {"label": "while True wala menu"}]},
            {"label": "Errors", "children": [{"label": "ZeroDivisionError"}, {"label": "TypeError: str input"}]},
        ],
    },
    "summary": [
        "Program ko **chhote functions** mein plan kijiye, har ek ka ek kaam: nikaalna, baantna, dikhaana.",
        "**BMI** = weight (kg) ÷ height (m)², likha jaata hai `weight_kg / height_m ** 2`; ek **if-elif-else** function uski category return karta hai.",
        "**Young's rule** (age ÷ (age + 12) × adult dose) aur **Clark's rule** (kg ÷ 70 × adult dose) ek-ek line ke functions bante hain; **round()** nateeja saaf karta hai.",
        "**Safety checks** function ke andar rakhiye: asambhav inputs mana kijiye aur doses par limit lagaaiye, jaldi `return` se.",
        "Ek **loop** wahi functions kai patients ke liye chala sakta hai, ya `while True` aur `break` se **menu** dikha sakta hai.",
    ],
}

T["kn"] = {
    "hook": {
        "title": "Pharmacy ಬಳಸುವ ಎರಡು tools ಮಾಡಿ",
        "md": "ಈಗ ನಿಮಗೆ **if**, **loops** ಮತ್ತು **functions** ಗೊತ್ತು. ಇವನ್ನು ಒಟ್ಟಿಗೆ ಸೇರಿಸಿದರೆ ನಿಜವಾದ tools ಮಾಡಬಹುದು.\n\nಈ project ನಲ್ಲಿ ನಿಮ್ಮ pharmacy subjects ನಲ್ಲಿ ಮತ್ತೆ ಸಿಗುವ ಎರಡು calculators ಮಾಡುತ್ತೀರಿ:\n\n1. ಒಂದು **BMI calculator**, number ನ ಅರ್ಥವನ್ನೂ ಹೇಳುವಂಥದ್ದು.\n2. **Young's rule** ಮತ್ತು **Clark's rule** ಬಳಸುವ **ಮಕ್ಕಳ dose calculators**.\n\n*ಈ calculators Python ಕಲಿಯಲು ಮತ್ತು pharmacology ಲೆಕ್ಕ check ಮಾಡಲು ಮಾತ್ರ. ನಿಜವಾದ dose ಯಾವಾಗಲೂ prescriber, label ಮತ್ತು official references ಇಂದ ಬರುತ್ತೆ.*",
    },
    "learn": [
        "Code ಬರೆಯುವ ಮುಂಚೆ program ಅನ್ನು ಚಿಕ್ಕ functions ಆಗಿ **plan** ಮಾಡುವುದು",
        "**if-elif-else** ಇಂದ category return ಮಾಡುವ **BMI** calculator ಮಾಡುವುದು",
        "**Young's rule** ಮತ್ತು **Clark's rule** ಅನ್ನು functions ಆಗಿ ಬದಲಾಯಿಸುವುದು",
        "**Safety checks** ಸೇರಿಸಿ, ಹಲವು patients ಗೆ **loop** ಬಳಸುವುದು",
    ],
    "explanation": [
        {
            "heading": "Code ಗಿಂತ ಮುಂಚೆ plan",
            "md": "Professional programmers ಒಂದು problem ಅನ್ನು ಚಿಕ್ಕ ಕೆಲಸಗಳಾಗಿ ವಿಭಾಗಿಸಿ, **ಪ್ರತಿ ಕೆಲಸಕ್ಕೆ ಒಂದು function** ಬರೆಯುತ್ತಾರೆ. BMI tool ಗೆ:\n\n1. Weight ಮತ್ತು height ಇಂದ BMI **ಲೆಕ್ಕ ಹಾಕುವುದು**: `bmi(weight_kg, height_m)`.\n2. Number ಅನ್ನು category ಗೆ **ವರ್ಗೀಕರಿಸುವುದು**: `bmi_category(value)`.\n3. ಫಲಿತಾಂಶವನ್ನು user ಗೆ `print()` ಇಂದ **ತೋರಿಸುವುದು**.\n\nಪ್ರತಿ function ಚಿಕ್ಕದು, ಸ್ಪಷ್ಟ ಹೆಸರು ಇದೆ, ಬೇರೆಯಾಗಿ test ಮಾಡಬಹುದು. Category limits ಬದಲಾದರೆ **ಒಂದೇ** function ಬದಲಾಯಿಸುತ್ತೀರಿ, ಅದನ್ನು ಬಳಸುವ program ನ ಪ್ರತಿ ಭಾಗ ತಾನಾಗಿ update ಆಗುತ್ತೆ.",
            "callout": {"title": "ಒಂದು function, ಒಂದು ಕೆಲಸ", "md": "ಒಂದು function ಏನು ಮಾಡುತ್ತೆ ಅಂತ ಒಂದು ಚಿಕ್ಕ ವಾಕ್ಯದಲ್ಲಿ ಹೇಳಲಾಗದಿದ್ದರೆ, ಅದನ್ನು ಎರಡಾಗಿ ಒಡೆಯಿರಿ."},
        },
        {
            "heading": "Calculator 1: BMI",
            "md": "**Body Mass Index** ಅಂದರೆ kilograms ನ weight ಭಾಗಿಸು metres ನ height ನ square: BMI = weight ÷ height². Python ನಲ್ಲಿ `**` ಅಂದರೆ \"ಘಾತ\" (Lesson 1.4), ಅದಕ್ಕೇ height² ಅಂದರೆ `height_m ** 2`.\n\n" + E.C_BMI + "\n\nಇದು `BMI: 23.5 (Normal)` print ಮಾಡುತ್ತೆ, ಯಾಕೆಂದರೆ 68 ÷ 1.70² = 68 ÷ 2.89 ≈ 23.5.\n\nಗಮನಿಸಿ, `bmi_category` text ಅನ್ನು print ಮಾಡುವ ಬದಲು **return** ಮಾಡುತ್ತೆ. ಅದರಿಂದ ಅದನ್ನು ಮತ್ತೆ ಬಳಸಬಹುದು: ಅದೇ function label, report ಅಥವಾ screen ತುಂಬಬಹುದು.",
            "callout": {"title": "Indian cut-offs", "md": "ಇವು WHO categories. Indian guidelines adults ಗೆ ಕಡಿಮೆ limits ಬಳಸುತ್ತವೆ: 23 ಇಂದ overweight, 25 ಇಂದ obese. ಒಂದು function ಬದಲಾಯಿಸಿದರೆ ಸಾಕು."},
        },
        {
            "heading": "Calculator 2: ಮಕ್ಕಳ doses",
            "md": "Pharmacology ನ ಎರಡು ಹಳೆಯ ನಿಯಮಗಳು adult dose ಇಂದ ಮಗುವಿನ dose ಅಂದಾಜು ಮಾಡುತ್ತವೆ:\n\n- **Young's rule** (ವಯಸ್ಸಿನಿಂದ, 1 ರಿಂದ 12 ವರ್ಷದ ಮಕ್ಕಳಿಗೆ): child dose = age ÷ (age + 12) × adult dose.\n- **Clark's rule** (ತೂಕದಿಂದ): child dose = kg ನಲ್ಲಿ weight ÷ 70 × adult dose. (ಮೂಲ ನಿಯಮ pounds ಮತ್ತು 150 ಬಳಸುತ್ತೆ; 70 kg ಸಾಮಾನ್ಯ metric ರೂಪ.)\n\nಪ್ರತಿ ನಿಯಮ ಒಂದು line ನ function ಆಗುತ್ತೆ:\n\n" + E.C_CHILD + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_CHILD + "\n\n6 ÷ 18 × 500 = 166.67, ಮತ್ತು 20 ÷ 70 × 500 = 142.86. **round()** ಹತ್ತಿರದ ಪೂರ್ಣ number ಗೆ round ಮಾಡುತ್ತೆ, label ಮೇಲೆ ಓದಲು ಸುಲಭ.",
            "callout": {"title": "round()", "md": "round(x) ಹತ್ತಿರದ ಪೂರ್ಣ number ಕೊಡುತ್ತೆ; round(x, 1) ಒಂದು decimal place ಇಡುತ್ತೆ. round(166.67) ಅಂದರೆ 167."},
        },
        {
            "heading": "Safety checks ಸೇರಿಸುವುದು",
            "md": "Doses ಗೆ ಬಳಸುವ calculator ಅರ್ಥವಿಲ್ಲದ values ಅನ್ನು ತಿರಸ್ಕರಿಸಬೇಕು, limits ಪಾಲಿಸಬೇಕು. Checks ಅನ್ನು function **ಒಳಗೆ** ಇಡಿ, ಆಗ call ಮಾಡುವ ಎಲ್ಲರಿಗೂ ಅವು ಸಿಗುತ್ತವೆ:\n\n" + E.C_SAFE + "\n\nFunction ಅರ್ಥವಿಲ್ಲದ weight ಗೆ 0 return ಮಾಡುತ್ತೆ, mg-per-kg dose ಲೆಕ್ಕ ಹಾಕುತ್ತೆ, ಮತ್ತು maximum ನಲ್ಲಿ ನಿಲ್ಲಿಸುತ್ತೆ. `if` ಒಳಗಿನ `return` function ಅನ್ನು ಬೇಗ ಮುಗಿಸುತ್ತೆ, ಅದಕ್ಕೇ ಕೆಳಗಿನ lines run ಆಗಲ್ಲ.",
        },
        {
            "heading": "ಒಂದು loop ಇಂದ ಹಲವು patients",
            "md": "ಲೆಕ್ಕ function ನಲ್ಲಿದೆ, ಅದಕ್ಕೇ ಒಂದು **loop** ಇಡೀ ward ನ patients ಗೆ ಅದನ್ನು ಬಳಸಬಹುದು:\n\n" + E.C_TABLE + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_TABLE + "\n\n40 kg ಮಗುವಿಗೆ 15 × 40 = 600 mg ಸಿಗುತ್ತಿತ್ತು, ಆದರೆ function ಅದನ್ನು 500 ಕ್ಕೆ ನಿಲ್ಲಿಸಿತು. Functions, `if` ಮತ್ತು loops ಒಟ್ಟಿಗೆ: ನಾಲ್ಕು lines ನಲ್ಲಿ ಇಡೀ Unit II.",
        },
    ],
    "walkthrough": {
        "intro": "ಈ program ಎರಡು functions ಮತ್ತು ಒಂದು loop ಬಳಸಿ, 1.70 m height ಇರುವ ಮೂರು patients ನ BMI ಮತ್ತು category ಲೆಕ್ಕ ಹಾಕುತ್ತೆ.",
        "keyTerms": [
            {"meaning": "Height ನ square (2 ರ ಘಾತ)."},
            {"meaning": "Category ಹಿಂದೆ ಕಳಿಸಿ function ಮುಗಿಸು."},
            {"meaning": "ಮೇಲಿನ ಯಾವ condition ಕೂಡ True ಆಗದಿದ್ದಾಗ ಮಾತ್ರ ಇಲ್ಲಿಗೆ ಬರುತ್ತೆ."},
            {"meaning": "BMI ಅನ್ನು ಒಂದು decimal place ಜೊತೆ ತೋರಿಸು."},
        ],
    },
    "errors": {
        "intro": "Inputs ತಪ್ಪಾಗಿದ್ದರೆ calculators fail ಆಗುತ್ತವೆ. ಇವು ಅತ್ಯಂತ ಸಾಮಾನ್ಯ ಎರಡು errors.",
        "examples": [
            {"title": "Zero height", "md": "Zero ಇಂದ ಭಾಗಿಸುವುದು ಅಸಾಧ್ಯ. ಮೊದಲು input check ಮಾಡಿ, ಉದಾ. `if height_m <= 0: return 0`, ಅಥವಾ user ಗೆ ಮತ್ತೆ ಕೇಳಿ."},
            {"title": "ಇನ್ನೂ text ಆಗಿರುವ number", "md": "`input()` ಯಾವಾಗಲೂ text ಕೊಡುತ್ತೆ. ಲೆಕ್ಕಕ್ಕೆ ಮುಂಚೆ ಬದಲಾಯಿಸಿ: `weight = float(input(\"Weight (kg): \"))`."},
        ],
    },
    "mistakes": [
        {"mistake": "Height ಅನ್ನು centimetres ನಲ್ಲಿ ಹಾಕುವುದು, ಉದಾ. `bmi(68, 170)`", "see": "Error ಇಲ್ಲ, ಆದರೆ BMI 0.0024 ಬರುತ್ತೆ", "fix": "BMI ಗೆ metres ಬೇಕು: 170 cm ಅಂದರೆ 1.70 m. ಮೊದಲು 100 ಇಂದ ಭಾಗಿಸಿ."},
        {"mistake": "`height_m ** 2` ಬದಲು `height_m * 2` ಬರೆಯುವುದು", "see": "Error ಇಲ್ಲ, ಆದರೆ BMI ತುಂಬಾ ಜಾಸ್ತಿ ಬರುತ್ತೆ", "fix": "`* 2` ದ್ವಿಗುಣ ಮಾಡುತ್ತೆ; `** 2` square ಮಾಡುತ್ತೆ."},
        {"mistake": "Clark's rule ನಲ್ಲಿ units ಬೆರೆಸುವುದು, ಉದಾ. kg ರೂಪದ (÷ 70) ಜೊತೆ pounds", "see": "Error ಇಲ್ಲ, ಆದರೆ dose ಎರಡು ಪಟ್ಟಿಗಿಂತ ಜಾಸ್ತಿ ಬರುತ್ತೆ", "fix": "ಒಂದೇ unit ಇಡಿ: kg ಜೊತೆ 70, ಅಥವಾ pounds ಜೊತೆ 150. Unit ಅನ್ನು parameter ಹೆಸರಿನಲ್ಲಿ ಇಡಿ: `weight_kg`."},
        {"mistake": "Calculator function ನಲ್ಲಿ return ಬದಲು print ಮಾಡುವುದು", "see": "ಮೊದಲು error ಇಲ್ಲ, ಆದರೆ ಫಲಿತಾಂಶವನ್ನು label ಅಥವಾ loop ನಲ್ಲಿ ಬಳಸಲಾಗಲ್ಲ", "fix": "Number return ಮಾಡಿ; ಬೇಕಾದ ಕಡೆ print ಮಾಡಿ."},
    ],
    "tasks": [
        {"title": "BMI function ಪೂರ್ಣಗೊಳಿಸಿ", "md": "**bmi()** weight ಭಾಗಿಸು height ನ square ಅನ್ನು return ಮಾಡಲಿ. Print ಮೊದಲೇ ಬರೆದಿದೆ; output ಸರಿಯಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["Height ನ square ಅಂದರೆ height_m ** 2.", "    return weight_kg / height_m ** 2"]},
        {"title": "Category return ಮಾಡಿ", "md": "**bmi_category()** ಅನ್ನು **if-elif-else** ಇಂದ ಪೂರ್ಣಗೊಳಿಸಿ: 18.5 ಕ್ಕಿಂತ ಕಡಿಮೆ \"Underweight\", 25 ಕ್ಕಿಂತ ಕಡಿಮೆ \"Normal\", 30 ಕ್ಕಿಂತ ಕಡಿಮೆ \"Overweight\", ಇಲ್ಲದಿದ್ದರೆ \"Obese\". 26.1 ಕ್ಕೆ output ಸರಿಯಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["ಪ್ರತಿ branch ಒಂದು ಪದ return ಮಾಡುತ್ತೆ: return \"Normal\"", "    if value < 18.5:\n        return \"Underweight\"\n    elif value < 25:\n        return \"Normal\"\n    elif value < 30:\n        return \"Overweight\"\n    else:\n        return \"Obese\""]},
        {"title": "Young's rule", "md": "age ÷ (age + 12) × adult dose ಅನ್ನು return ಮಾಡುವ **youngs_rule(age, adult_dose)** ಬರೆಯಿರಿ. 4 ವರ್ಷದ ಮಗು ಮತ್ತು 500 mg adult dose ಗೆ output ಸರಿಯಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["Brackets ಮುಖ್ಯ: age / (age + 12) * adult_dose", "def youngs_rule(age, adult_dose):\n    return age / (age + 12) * adult_dose"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "Clark's rule ಪ್ರಕಾರ, 400 mg adult dose ಇರುವ 35 kg ಮಗುವಿಗೆ 35 ÷ 70 × 400 = 200 mg ಸಿಗಬೇಕು. ಈ program 0 mg ಅಂತ ಹೇಳುತ್ತೆ, error ಇಲ್ಲ. Output ಸರಿಯಾಗಿ ಹೀಗೇ ಬರುವ ಹಾಗೆ ಸರಿ ಮಾಡಿ:",
         "hints": ["Brackets ಇಂದ Python ಯಾವುದರಿಂದ ಭಾಗಿಸುತ್ತಿದೆ ಅಂತ ಲೆಕ್ಕ ಹಾಕಿ.", "Brackets ಇಂದ ಅದು 28000 ಇಂದ ಭಾಗಿಸುತ್ತೆ. weight_kg / 70 * adult_dose ಅಂತ ಬರೆಯಿರಿ."],
         "solutionNote": "Brackets ಜೊತೆ Python 35 ಅನ್ನು 70 × 400 = 28000 ಇಂದ ಭಾಗಿಸಿ 0.00125 ಕೊಟ್ಟಿತು, ಅದು round ಆಗಿ 0. Brackets ಇಲ್ಲದೆ ಅದು ಮೊದಲು 70 ಇಂದ ಭಾಗಿಸಿ, ಆಮೇಲೆ 400 ಇಂದ ಗುಣಿಸುತ್ತೆ."},
    ],
    "quiz": [
        {"q": "ಒಬ್ಬ patient ನ weight 72 kg, height 1.80 m. BMI ಎಷ್ಟು?", "why": "72 ÷ 1.80² = 72 ÷ 3.24 ≈ 22.2."},
        {"q": "Young's rule ನ formula ಯಾವುದು?", "why": "Young's rule ವಯಸ್ಸು ಬಳಸುತ್ತೆ: age ÷ (age + 12) × adult dose."},
        {"q": "ಈ lesson ನ bmi_category function ಇಂದ bmi_category(30) ಏನು return ಮಾಡುತ್ತೆ?", "why": "30 < 30 False, ಅದಕ್ಕೇ ಯಾವ condition ಕೂಡ True ಇಲ್ಲ, else branch Obese return ಮಾಡುತ್ತೆ."},
        {"q": "round(166.67) ಎಷ್ಟು?", "why": "round() ಹತ್ತಿರದ ಪೂರ್ಣ number ಕೊಡುತ್ತೆ: 167."},
        {"q": "ಈ lesson ಪ್ರತಿ ಲೆಕ್ಕವನ್ನು ಬೇರೆ function ನಲ್ಲಿ ಯಾಕೆ ಇಡುತ್ತೆ?", "why": "ಚಿಕ್ಕ ಹೆಸರಿನ functions ಮತ್ತೆ ಬಳಸಬಹುದು, test ಮಾಡುವುದು ಸುಲಭ, ಮತ್ತು ಎಲ್ಲಾ callers ಗೆ ಒಮ್ಮೆಲೇ ಸರಿಯಾಗುತ್ತವೆ."},
        {"q": "1.70 ** 2 ಏನು ಲೆಕ್ಕ ಹಾಕುತ್ತೆ?", "why": "** ಘಾತ operator: 1.70 ನ square."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 2.6 · Dosage ಮತ್ತು BMI calculators",
        "children": [
            {"label": "Plan", "children": [{"label": "ಒಂದು function, ಒಂದು ಕೆಲಸ"}, {"label": "ಲೆಕ್ಕ → ವರ್ಗೀಕರಣ → ತೋರಿಸು"}]},
            {"label": "BMI", "children": [{"label": "weight / height ** 2"}, {"label": "if-elif-else category"}, {"label": "Return ಮಾಡಿ, print ಅಲ್ಲ"}]},
            {"label": "ಮಕ್ಕಳ dose", "children": [{"label": "Young's: age/(age+12) × adult"}, {"label": "Clark's: kg/70 × adult"}, {"label": "round()"}]},
            {"label": "Safety", "children": [{"label": "weight <= 0 ತಿರಸ್ಕರಿಸಿ"}, {"label": "Maximum ನಲ್ಲಿ ನಿಲ್ಲಿಸಿ"}, {"label": "ಬೇಗ return"}]},
            {"label": "Loop", "children": [{"label": "ಹಲವು patients"}, {"label": "while True menu"}]},
            {"label": "Errors", "children": [{"label": "ZeroDivisionError"}, {"label": "TypeError: str input"}]},
        ],
    },
    "summary": [
        "Program ಅನ್ನು **ಚಿಕ್ಕ functions** ಆಗಿ plan ಮಾಡಿ, ಪ್ರತಿಯೊಂದಕ್ಕೂ ಒಂದು ಕೆಲಸ: ಲೆಕ್ಕ, ವರ್ಗೀಕರಣ, ತೋರಿಸುವುದು.",
        "**BMI** = weight (kg) ÷ height (m)², `weight_kg / height_m ** 2` ಅಂತ ಬರೆಯುತ್ತೇವೆ; ಒಂದು **if-elif-else** function ಅದರ category return ಮಾಡುತ್ತೆ.",
        "**Young's rule** (age ÷ (age + 12) × adult dose) ಮತ್ತು **Clark's rule** (kg ÷ 70 × adult dose) ಒಂದೊಂದು line ನ functions ಆಗುತ್ತವೆ; **round()** ಫಲಿತಾಂಶ ಅಚ್ಚುಕಟ್ಟು ಮಾಡುತ್ತೆ.",
        "**Safety checks** ಅನ್ನು function ಒಳಗೆ ಇಡಿ: ಅಸಾಧ್ಯ inputs ತಿರಸ್ಕರಿಸಿ, doses ಗೆ limit ಹಾಕಿ, ಬೇಗ `return` ಇಂದ.",
        "ಒಂದು **loop** ಅದೇ functions ಅನ್ನು ಹಲವು patients ಗೆ run ಮಾಡಬಹುದು, ಅಥವಾ `while True` ಮತ್ತು `break` ಇಂದ **menu** ತೋರಿಸಬಹುದು.",
    ],
}

NARR = {
    "hi": [
        "यह एक छोटा, पूरा program है: दो functions काम करते हैं, और एक loop उन्हें तीन patients के लिए चलाता है।",
        "Comment program का नाम बताता है।",
        "def, bmi function बनाता है: weight भाग height का square। Python उसे बाद के लिए याद रखता है।",
        "def, category function बनाता है, जो number के लिए एक शब्द return करता है। अभी कुछ नहीं चलता।",
        "Loop पहले weight से शुरू होता है, पचास kilogram।",
        "bmi को पचास और एक दशमलव सात के साथ call किया जाता है। यह लगभग सत्रह दशमलव तीन return करता है।",
        "Category function में सत्रह दशमलव तीन, अठारह दशमलव पाँच से कम है, इसलिए यह Underweight return करता है, और function वहीं खत्म।",
        "print सब कुछ एक decimal place के साथ जोड़कर दिखाता है।",
        "अगला, अड़सठ kilogram: BMI तेईस दशमलव पाँच। यह अठारह दशमलव पाँच से कम नहीं, पर पच्चीस से कम है, इसलिए: Normal।",
        "आखिर में, नब्बे kilogram: BMI इकतीस दशमलव एक। तीनों में से कोई condition True नहीं, इसलिए आखिरी return Obese देता है।",
    ],
    "hinglish": [
        "Yeh ek chhota, poora program hai: do functions kaam karte hain, aur ek loop unhe teen patients ke liye chalaata hai.",
        "Comment program ka naam batata hai.",
        "def, bmi function banaata hai: weight bhaag height ka square. Python use baad ke liye yaad rakhta hai.",
        "def, category function banaata hai, jo number ke liye ek shabd return karta hai. Abhi kuch nahi chalta.",
        "Loop pehle weight se shuru hota hai, pachaas kilogram.",
        "bmi ko pachaas aur ek dashamlav saat ke saath call kiya jaata hai. Yeh lagbhag satrah dashamlav teen return karta hai.",
        "Category function mein satrah dashamlav teen, athaarah dashamlav paanch se kam hai, isliye yeh Underweight return karta hai, aur function wahin khatam.",
        "print sab kuch ek decimal place ke saath jodkar dikhaata hai.",
        "Agla, adsath kilogram: BMI teis dashamlav paanch. Yeh athaarah dashamlav paanch se kam nahi, par pachchees se kam hai, isliye: Normal.",
        "Aakhir mein, nabbe kilogram: BMI iktees dashamlav ek. Teenon mein se koi condition True nahi, isliye aakhri return Obese deta hai.",
    ],
    "kn": [
        "ಇದು ಒಂದು ಚಿಕ್ಕ, ಪೂರ್ಣ program: ಎರಡು functions ಕೆಲಸ ಮಾಡುತ್ತವೆ, ಒಂದು loop ಅವನ್ನು ಮೂರು patients ಗೆ run ಮಾಡುತ್ತೆ.",
        "Comment program ನ ಹೆಸರು ಹೇಳುತ್ತೆ.",
        "def, bmi function ಮಾಡುತ್ತೆ: weight ಭಾಗಿಸು height ನ square. Python ಅದನ್ನು ಆಮೇಲೆಗಾಗಿ ನೆನಪಿಟ್ಟುಕೊಳ್ಳುತ್ತೆ.",
        "def, category function ಮಾಡುತ್ತೆ, ಅದು number ಗೆ ಒಂದು ಪದ return ಮಾಡುತ್ತೆ. ಇನ್ನೂ ಏನೂ run ಆಗಲ್ಲ.",
        "Loop ಮೊದಲ weight ಇಂದ ಶುರುವಾಗುತ್ತೆ, ಐವತ್ತು kilogram.",
        "bmi ಅನ್ನು ಐವತ್ತು ಮತ್ತು ಒಂದು ಪಾಯಿಂಟ್ ಏಳು ಜೊತೆ call ಮಾಡಲಾಗುತ್ತೆ. ಅದು ಸುಮಾರು ಹದಿನೇಳು ಪಾಯಿಂಟ್ ಮೂರು return ಮಾಡುತ್ತೆ.",
        "Category function ನಲ್ಲಿ ಹದಿನೇಳು ಪಾಯಿಂಟ್ ಮೂರು, ಹದಿನೆಂಟು ಪಾಯಿಂಟ್ ಐದಕ್ಕಿಂತ ಕಡಿಮೆ, ಅದಕ್ಕೇ ಅದು Underweight return ಮಾಡುತ್ತೆ, function ಅಲ್ಲೇ ಮುಗಿಯುತ್ತೆ.",
        "print ಎಲ್ಲವನ್ನೂ ಒಂದು decimal place ಜೊತೆ ಸೇರಿಸಿ ತೋರಿಸುತ್ತೆ.",
        "ಮುಂದೆ, ಅರವತ್ತೆಂಟು kilogram: BMI ಇಪ್ಪತ್ಮೂರು ಪಾಯಿಂಟ್ ಐದು. ಇದು ಹದಿನೆಂಟು ಪಾಯಿಂಟ್ ಐದಕ್ಕಿಂತ ಕಡಿಮೆ ಇಲ್ಲ, ಆದರೆ ಇಪ್ಪತ್ತೈದಕ್ಕಿಂತ ಕಡಿಮೆ, ಅದಕ್ಕೇ: Normal.",
        "ಕೊನೆಗೆ, ತೊಂಬತ್ತು kilogram: BMI ಮೂವತ್ತೊಂದು ಪಾಯಿಂಟ್ ಒಂದು. ಮೂರರಲ್ಲಿ ಯಾವ condition ಕೂಡ True ಇಲ್ಲ, ಅದಕ್ಕೇ ಕೊನೆಯ return Obese ಕೊಡುತ್ತೆ.",
    ],
}

ANIM = {
    "hi": [
        "दो inputs: अड़सठ kilogram, और एक दशमलव सात metre।",
        "ये bmi function में जाते हैं, जो weight को height के square से भाग देता है।",
        "यह तेईस दशमलव पाँच return करता है।",
        "वह number category function में जाता है। यह अठारह दशमलव पाँच से कम नहीं, पर पच्चीस से कम है।",
        "इसलिए यह Normal return करता है, और program जवाब print करता है। दो छोटे functions, एक साफ़ नतीजा।",
    ],
    "hinglish": [
        "Do inputs: adsath kilogram, aur ek dashamlav saat metre.",
        "Yeh bmi function mein jaate hain, jo weight ko height ke square se bhaag deta hai.",
        "Yeh teis dashamlav paanch return karta hai.",
        "Woh number category function mein jaata hai. Yeh athaarah dashamlav paanch se kam nahi, par pachchees se kam hai.",
        "Isliye yeh Normal return karta hai, aur program jawaab print karta hai. Do chhote functions, ek saaf nateeja.",
    ],
    "kn": [
        "ಎರಡು inputs: ಅರವತ್ತೆಂಟು kilogram, ಮತ್ತು ಒಂದು ಪಾಯಿಂಟ್ ಏಳು metre.",
        "ಇವು bmi function ಗೆ ಹೋಗುತ್ತವೆ, ಅದು weight ಅನ್ನು height ನ square ಇಂದ ಭಾಗಿಸುತ್ತೆ.",
        "ಅದು ಇಪ್ಪತ್ಮೂರು ಪಾಯಿಂಟ್ ಐದು return ಮಾಡುತ್ತೆ.",
        "ಆ number category function ಗೆ ಹೋಗುತ್ತೆ. ಅದು ಹದಿನೆಂಟು ಪಾಯಿಂಟ್ ಐದಕ್ಕಿಂತ ಕಡಿಮೆ ಇಲ್ಲ, ಆದರೆ ಇಪ್ಪತ್ತೈದಕ್ಕಿಂತ ಕಡಿಮೆ.",
        "ಅದಕ್ಕೇ ಅದು Normal return ಮಾಡುತ್ತೆ, program ಉತ್ತರ print ಮಾಡುತ್ತೆ. ಎರಡು ಚಿಕ್ಕ functions, ಒಂದು ಸ್ಪಷ್ಟ ಫಲಿತಾಂಶ.",
    ],
}

if __name__ == "__main__":
    build("2-6", "anim-pipeline", T, NARR, ANIM)

"""Lesson 2.5 translations (Hindi, Hinglish, Kannada) and voice scripts."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import build  # noqa: E402

_spec = importlib.util.spec_from_file_location("en25", os.path.join(os.path.dirname(__file__), "..", "lessons", "bp101t_2-5_en.py"))
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)


def say_en(t):
    return t


T = {}

T["hi"] = {
    "hook": {
        "title": "एक बार लिखो, हर जगह use करो",
        "md": "Hospital pharmacy का एक app कई जगह शरीर के वज़न से dose निकालता है: prescription screen पर, label पर, stock report में। अगर formula दस जगह copy हो और किसी एक copy में गलती हो, तो patient को गलत dose मिल सकता है।\n\nइलाज है formula को **एक बार** लिखना, उसे एक **नाम** देना, और हर जगह वही नाम use करना। Code का यह नाम वाला, दोबारा use होने वाला हिस्सा **function** है। Lesson 1.1 से आप functions use कर रहे हैं: `print()`, `len()` और `input()`। आज आप अपना function लिखेंगे।",
    },
    "learn": [
        "**def** से function **define** करना, और उसे **call** करना",
        "**Parameters** से function अलग-अलग values के साथ कैसे काम करता है",
        "**return** नतीजा वापस कैसे भेजता है, और यह print जैसा क्यों नहीं",
        "**Default values** और **local variables** कैसे काम करते हैं",
    ],
    "explanation": [
        {
            "heading": "आपका पहला function",
            "md": "Function को keyword **def**, एक नाम, brackets और colon से **define** करते हैं। नीचे की indent की हुई lines उसकी **body** हैं:\n\n" + E.C_DEF + "\n\nयह print करता है:\n\n" + E.O_DEF + "\n\nFunction define करने से वह **चलता नहीं**। Python बस उसे याद रख लेता है। Body तब चलती है जब आप function का नाम brackets के साथ लिखकर उसे **call** करते हैं: `label()`।",
            "callout": {"title": "Function", "md": "Code का नाम वाला block जो एक काम करता है। def से उसे एक बार define करते हैं, और जब चाहें उसका नाम brackets के साथ लिखकर चलाते हैं।"},
        },
        {
            "heading": "Parameters: function को जानकारी देना",
            "md": "जब आप function को values दे सकें, तो वह कहीं ज़्यादा काम का हो जाता है। `def` के brackets के अंदर के नाम **parameters** हैं:\n\n" + E.C_PARAM + "\n\nयह print करता है:\n\n" + E.O_PARAM + "\n\nCall में आप जो values देते हैं, जैसे `\"Paracetamol\"` और `500`, वो **arguments** हैं। ये parameters से **क्रम में** मिलते हैं: पहला argument `drug` में, दूसरा `mg` में।",
        },
        {
            "heading": "return: नतीजा वापस भेजना",
            "md": "`print()` value को सिर्फ़ screen पर दिखाता है। Function के नतीजे को program में आगे **use** करने के लिए function को उसे **return** करना होगा:\n\n" + E.C_RET + "\n\nयह print करता है:\n\n" + E.O_RET + "\n\n`return` value को उस जगह वापस देता है जहाँ function call हुआ था, ताकि आप उसे store करें, print करें, या उससे हिसाब लगाएँ। यह function को खत्म भी करता है: `return` के बाद की lines कभी नहीं चलतीं।",
            "callout": {"title": "return नहीं, तो None", "md": "बिना return का function None देता है, जो Python में \"कुछ नहीं\" का शब्द है। अगर function में return की जगह print करें, तो dose = child_dose(20, 15) में None store होता है।"},
        },
        {
            "heading": "Default values और नाम वाले arguments",
            "md": "Parameter की एक **default value** हो सकती है, जो call में न दी जाए तो use होती है। Call में arguments को नाम से भी दे सकते हैं, तब उनका क्रम मायने नहीं रखता:\n\n" + E.C_DEFAULT + "\n\nयह print करता है:\n\n" + E.O_DEFAULT + "\n\nDefault वाले parameters, बिना default वालों के **बाद** आने चाहिए।",
        },
        {
            "heading": "Function के अंदर के variables अंदर ही रहते हैं",
            "md": "Function के अंदर बना variable **local** होता है: वह सिर्फ़ function चलने तक रहता है।\n\n" + E.C_LOCAL + "\n\nयह `10` print करता है। पर function के बाद `print(total)` लिखें तो `NameError: name 'total' is not defined` आएगा, क्योंकि function खत्म होते ही `total` गायब हो गया। बाहर value use करनी हो तो उसे **return** कीजिए।\n\nयह अच्छी बात है: हर function के अपने variables होते हैं, इसलिए functions गलती से एक-दूसरे की values नहीं बदल सकते।",
            "callout": {"title": "Functions क्यों लिखें?", "md": "एक बार लिखो, कई बार use करो। गलती एक जगह ठीक करो। किसी step को साफ़ नाम दो, जैसे mg_to_g। और हर हिस्से को अलग से test करो।"},
        },
    ],
    "walkthrough": {
        "intro": "यह program milligrams को grams में बदलने वाला function define करता है, फिर उसे दो बार call करता है।",
        "keyTerms": [
            {"meaning": "mg_to_g नाम का function define करो, एक parameter के साथ।"},
            {"meaning": "एक parameter: हर call में दी गई value लेता है।"},
            {"meaning": "नतीजा call करने वाले को वापस भेजो।"},
            {"meaning": "Function को argument 500 के साथ call करो।"},
        ],
    },
    "errors": {
        "intro": "ये दो errors function को call करने के तरीके से आती हैं।",
        "examples": [
            {"title": "Define करने से पहले function call करना", "md": "Python ऊपर से नीचे चलता है, इसलिए line 1 पर उसने अभी `def` देखा ही नहीं। Function definitions ऊपर रखिए, call करने से पहले।"},
            {"title": "एक argument छोड़ देना", "md": "Function के दो parameters हैं, पर call सिर्फ़ एक value देता है। दोनों दीजिए: `child_dose(20, 15)`, या parameter को default value दीजिए।"},
        ],
    },
    "mistakes": [
        {"mistake": "Call करते समय brackets भूल जाना, जैसे `label()` की जगह `label`", "see": "कोई error नहीं, पर कुछ नहीं होता", "fix": "Call में हमेशा brackets चाहिए: `label()`।"},
        {"mistake": "Function में return की जगह print करना, फिर नतीजे से हिसाब लगाना", "see": "TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'", "fix": "Value वापस भेजने के लिए `return` use कीजिए; ज़रूरत हो तो बाहर print कीजिए।"},
        {"mistake": "`return` के बाद lines लिखना और उम्मीद करना कि वो चलेंगी", "see": "कोई error नहीं, पर वो lines कभी नहीं चलतीं", "fix": "Function को जो कुछ करना है, वो सब `return` से पहले रखिए।"},
        {"mistake": "Arguments गलत क्रम में देना, जैसे `dose_label(500, \"Paracetamol\")`", "see": "कोई error नहीं, पर label पर \"500: Paracetamol mg\" आता है", "fix": "Parameters का क्रम मिलाइए, या नाम दीजिए: `dose_label(drug=\"Paracetamol\", mg=500)`।"},
    ],
    "tasks": [
        {"title": "Label वाला function", "md": "**warning** नाम का function define कीजिए जो `Shake well before use` print करे। फिर उसे **दो बार call** कीजिए, ताकि output बिल्कुल यह हो:",
         "hints": ["def warning():\n    print(\"Shake well before use\")", "उसे warning() से दो अलग lines पर call कीजिए, बिना indentation के।"]},
        {"title": "Parameters वाला function", "md": "**dose_label(drug, mg)** को पूरा कीजिए ताकि वह drug और dose print करे। Call पहले से लिखा है; output बिल्कुल यह होना चाहिए:",
         "hints": ["Function के अंदर दोनों parameters एक print में use कीजिए।", "    print(f\"{drug} {mg} mg\")"]},
        {"title": "Daily dose return कीजिए", "md": "**daily_dose(dose, times)** को dose गुणा दिन में कितनी बार का नतीजा **return** करवाइए। अभी यह `None` print करता है। Output बिल्कुल यह होना चाहिए:",
         "hints": ["return value को call पर वापस भेजता है।", "    return dose * times"]},
        {"title": "Bug ढूँढिए", "md": "एक syrup में हर ml में 50 mg है। 250 mg dose के लिए patient को 5 ml चाहिए, पर यह program number को अलग line पर print करता है और फिर `Give None ml` कहता है। इसे ठीक कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["जब function में return न हो, तो वह क्या वापस देता है?", "Function के अंदर print(...) को return ... में बदलिए।"],
         "solutionNote": "print ने 5.0 सिर्फ़ screen पर दिखाया; function ने खुद None वापस दिया, इसलिए volume None था। return, 5.0 को volume में वापस भेजता है।"},
    ],
    "quiz": [
        {"q": "Python में कौन-सा keyword function define करता है?", "why": "Functions def, नाम, brackets और colon से define होते हैं।"},
        {"q": "def double(x):\n    return x * 2\n\nprint(double(4))\n\nयह क्या print करता है?", "why": "double(4), 4 * 2 यानी 8 return करता है।"},
        {"q": "return statement न हो तो function क्या वापस देता है?", "why": "return के बिना Python None वापस देता है।"},
        {"q": "def child_dose(weight, mg_per_kg): में weight क्या है?", "why": "def के brackets के नाम parameters हैं; call में दी गई values arguments हैं।"},
        {"q": "def greet(name=\"Patient\"):\n    print(\"Hello\", name)\n\ngreet()\n\nयह क्या print करता है?", "why": "कोई argument नहीं दिया गया, इसलिए default value \"Patient\" use होती है।"},
        {"q": "Function के अंदर return के बाद लिखी lines का क्या होता है?", "why": "return function को तुरंत खत्म कर देता है।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 2.5 · Functions",
        "children": [
            {"label": "Define", "children": [{"label": "def name():"}, {"label": "Indent की हुई body"}, {"label": "अभी नहीं चलता"}]},
            {"label": "Call", "children": [{"label": "name()"}, {"label": "Body चलाता है"}, {"label": "कई बार call"}]},
            {"label": "Parameters", "children": [{"label": "def में नाम"}, {"label": "Arguments = call की values"}, {"label": "क्रम से मिलते हैं"}]},
            {"label": "return", "children": [{"label": "नतीजा वापस भेजता है"}, {"label": "Function खत्म करता है"}, {"label": "return नहीं → None"}]},
            {"label": "Extras", "children": [{"label": "Default values"}, {"label": "नाम वाले arguments"}, {"label": "Local variables"}]},
            {"label": "Errors", "children": [{"label": "NameError: अभी define नहीं"}, {"label": "TypeError: argument छूटा"}]},
        ],
    },
    "summary": [
        "**Function** code का नाम वाला block है। **def** उसे define करता है; वह तभी चलता है जब आप उसे brackets के साथ **call** करें, जैसे `label()`।",
        "**Parameters** `def` line के नाम हैं; **arguments** call में दी गई values हैं, जो क्रम से या नाम से मिलती हैं।",
        "**return** नतीजा call करने वाले को वापस भेजता है और function खत्म करता है; बिना `return` का function **None** देता है।",
        "Parameter की **default value** हो सकती है, जो call में न दी जाए तो use होती है।",
        "Function के अंदर बने variables **local** होते हैं: function खत्म होते ही गायब, इसलिए जो चाहिए उसे return कीजिए।",
    ],
}

T["hinglish"] = {
    "hook": {
        "title": "Ek baar likho, har jagah use karo",
        "md": "Hospital pharmacy ka ek app kai jagah shareer ke wazan se dose nikaalta hai: prescription screen par, label par, stock report mein. Agar formula das jagah copy ho aur kisi ek copy mein galti ho, to patient ko galat dose mil sakta hai.\n\nIlaaj hai formula ko **ek baar** likhna, use ek **naam** dena, aur har jagah wahi naam use karna. Code ka yeh naam wala, dobara use hone wala hissa **function** hai. Lesson 1.1 se aap functions use kar rahe hain: `print()`, `len()` aur `input()`. Aaj aap apna function likhenge.",
    },
    "learn": [
        "**def** se function **define** karna, aur use **call** karna",
        "**Parameters** se function alag-alag values ke saath kaise kaam karta hai",
        "**return** nateeja wapas kaise bhejta hai, aur yeh print jaisa kyon nahi",
        "**Default values** aur **local variables** kaise kaam karte hain",
    ],
    "explanation": [
        {
            "heading": "Aapka pehla function",
            "md": "Function ko keyword **def**, ek naam, brackets aur colon se **define** karte hain. Neeche ki indent ki hui lines uski **body** hain:\n\n" + E.C_DEF + "\n\nYeh print karta hai:\n\n" + E.O_DEF + "\n\nFunction define karne se woh **chalta nahi**. Python bas use yaad rakh leta hai. Body tab chalti hai jab aap function ka naam brackets ke saath likhkar use **call** karte hain: `label()`.",
            "callout": {"title": "Function", "md": "Code ka naam wala block jo ek kaam karta hai. def se use ek baar define karte hain, aur jab chahein uska naam brackets ke saath likhkar chalaate hain."},
        },
        {
            "heading": "Parameters: function ko jaankaari dena",
            "md": "Jab aap function ko values de sakein, to woh kahin zyada kaam ka ho jaata hai. `def` ke brackets ke andar ke naam **parameters** hain:\n\n" + E.C_PARAM + "\n\nYeh print karta hai:\n\n" + E.O_PARAM + "\n\nCall mein aap jo values dete hain, jaise `\"Paracetamol\"` aur `500`, woh **arguments** hain. Yeh parameters se **kram mein** milte hain: pehla argument `drug` mein, doosra `mg` mein.",
        },
        {
            "heading": "return: nateeja wapas bhejna",
            "md": "`print()` value ko sirf screen par dikhaata hai. Function ke nateeje ko program mein aage **use** karne ke liye function ko use **return** karna hoga:\n\n" + E.C_RET + "\n\nYeh print karta hai:\n\n" + E.O_RET + "\n\n`return` value ko us jagah wapas deta hai jahaan function call hua tha, taaki aap use store karein, print karein, ya usse hisaab lagaayein. Yeh function ko khatam bhi karta hai: `return` ke baad ki lines kabhi nahi chalti.",
            "callout": {"title": "return nahi, to None", "md": "Bina return ka function None deta hai, jo Python mein \"kuch nahi\" ka shabd hai. Agar function mein return ki jagah print karein, to dose = child_dose(20, 15) mein None store hota hai."},
        },
        {
            "heading": "Default values aur naam wale arguments",
            "md": "Parameter ki ek **default value** ho sakti hai, jo call mein na di jaaye to use hoti hai. Call mein arguments ko naam se bhi de sakte hain, tab unka kram matter nahi karta:\n\n" + E.C_DEFAULT + "\n\nYeh print karta hai:\n\n" + E.O_DEFAULT + "\n\nDefault wale parameters, bina default walon ke **baad** aane chahiye.",
        },
        {
            "heading": "Function ke andar ke variables andar hi rehte hain",
            "md": "Function ke andar bana variable **local** hota hai: woh sirf function chalne tak rehta hai.\n\n" + E.C_LOCAL + "\n\nYeh `10` print karta hai. Par function ke baad `print(total)` likhein to `NameError: name 'total' is not defined` aayega, kyonki function khatam hote hi `total` gaayab ho gaya. Bahar value use karni ho to use **return** kijiye.\n\nYeh achchhi baat hai: har function ke apne variables hote hain, isliye functions galti se ek-doosre ki values nahi badal sakte.",
            "callout": {"title": "Functions kyon likhein?", "md": "Ek baar likho, kai baar use karo. Galti ek jagah theek karo. Kisi step ko saaf naam do, jaise mg_to_g. Aur har hisse ko alag se test karo."},
        },
    ],
    "walkthrough": {
        "intro": "Yeh program milligrams ko grams mein badalne wala function define karta hai, phir use do baar call karta hai.",
        "keyTerms": [
            {"meaning": "mg_to_g naam ka function define karo, ek parameter ke saath."},
            {"meaning": "Ek parameter: har call mein di gayi value leta hai."},
            {"meaning": "Nateeja call karne wale ko wapas bhejo."},
            {"meaning": "Function ko argument 500 ke saath call karo."},
        ],
    },
    "errors": {
        "intro": "Yeh do errors function ko call karne ke tareeke se aati hain.",
        "examples": [
            {"title": "Define karne se pehle function call karna", "md": "Python upar se neeche chalta hai, isliye line 1 par usne abhi `def` dekha hi nahi. Function definitions upar rakhiye, call karne se pehle."},
            {"title": "Ek argument chhod dena", "md": "Function ke do parameters hain, par call sirf ek value deta hai. Dono dijiye: `child_dose(20, 15)`, ya parameter ko default value dijiye."},
        ],
    },
    "mistakes": [
        {"mistake": "Call karte samay brackets bhool jaana, jaise `label()` ki jagah `label`", "see": "Koi error nahi, par kuch nahi hota", "fix": "Call mein hamesha brackets chahiye: `label()`."},
        {"mistake": "Function mein return ki jagah print karna, phir nateeje se hisaab lagaana", "see": "TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'", "fix": "Value wapas bhejne ke liye `return` use kijiye; zaroorat ho to bahar print kijiye."},
        {"mistake": "`return` ke baad lines likhna aur ummeed karna ki woh chalengi", "see": "Koi error nahi, par woh lines kabhi nahi chalti", "fix": "Function ko jo kuch karna hai, woh sab `return` se pehle rakhiye."},
        {"mistake": "Arguments galat kram mein dena, jaise `dose_label(500, \"Paracetamol\")`", "see": "Koi error nahi, par label par \"500: Paracetamol mg\" aata hai", "fix": "Parameters ka kram milaaiye, ya naam dijiye: `dose_label(drug=\"Paracetamol\", mg=500)`."},
    ],
    "tasks": [
        {"title": "Label wala function", "md": "**warning** naam ka function define kijiye jo `Shake well before use` print kare. Phir use **do baar call** kijiye, taaki output bilkul yeh ho:",
         "hints": ["def warning():\n    print(\"Shake well before use\")", "Use warning() se do alag lines par call kijiye, bina indentation ke."]},
        {"title": "Parameters wala function", "md": "**dose_label(drug, mg)** ko poora kijiye taaki woh drug aur dose print kare. Call pehle se likha hai; output bilkul yeh hona chahiye:",
         "hints": ["Function ke andar dono parameters ek print mein use kijiye.", "    print(f\"{drug} {mg} mg\")"]},
        {"title": "Daily dose return kijiye", "md": "**daily_dose(dose, times)** ko dose guna din mein kitni baar ka nateeja **return** karwaaiye. Abhi yeh `None` print karta hai. Output bilkul yeh hona chahiye:",
         "hints": ["return value ko call par wapas bhejta hai.", "    return dose * times"]},
        {"title": "Bug dhoondhiye", "md": "Ek syrup mein har ml mein 50 mg hai. 250 mg dose ke liye patient ko 5 ml chahiye, par yeh program number ko alag line par print karta hai aur phir `Give None ml` kehta hai. Ise theek kijiye taaki output bilkul yeh ho:",
         "hints": ["Jab function mein return na ho, to woh kya wapas deta hai?", "Function ke andar print(...) ko return ... mein badaliye."],
         "solutionNote": "print ne 5.0 sirf screen par dikhaaya; function ne khud None wapas diya, isliye volume None tha. return, 5.0 ko volume mein wapas bhejta hai."},
    ],
    "quiz": [
        {"q": "Python mein kaun-sa keyword function define karta hai?", "why": "Functions def, naam, brackets aur colon se define hote hain."},
        {"q": "def double(x):\n    return x * 2\n\nprint(double(4))\n\nYeh kya print karta hai?", "why": "double(4), 4 * 2 yaani 8 return karta hai."},
        {"q": "return statement na ho to function kya wapas deta hai?", "why": "return ke bina Python None wapas deta hai."},
        {"q": "def child_dose(weight, mg_per_kg): mein weight kya hai?", "why": "def ke brackets ke naam parameters hain; call mein di gayi values arguments hain."},
        {"q": "def greet(name=\"Patient\"):\n    print(\"Hello\", name)\n\ngreet()\n\nYeh kya print karta hai?", "why": "Koi argument nahi diya gaya, isliye default value \"Patient\" use hoti hai."},
        {"q": "Function ke andar return ke baad likhi lines ka kya hota hai?", "why": "return function ko turant khatam kar deta hai."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 2.5 · Functions",
        "children": [
            {"label": "Define", "children": [{"label": "def name():"}, {"label": "Indent ki hui body"}, {"label": "Abhi nahi chalta"}]},
            {"label": "Call", "children": [{"label": "name()"}, {"label": "Body chalaata hai"}, {"label": "Kai baar call"}]},
            {"label": "Parameters", "children": [{"label": "def mein naam"}, {"label": "Arguments = call ki values"}, {"label": "Kram se milte hain"}]},
            {"label": "return", "children": [{"label": "Nateeja wapas bhejta hai"}, {"label": "Function khatam karta hai"}, {"label": "return nahi → None"}]},
            {"label": "Extras", "children": [{"label": "Default values"}, {"label": "Naam wale arguments"}, {"label": "Local variables"}]},
            {"label": "Errors", "children": [{"label": "NameError: abhi define nahi"}, {"label": "TypeError: argument chhoota"}]},
        ],
    },
    "summary": [
        "**Function** code ka naam wala block hai. **def** use define karta hai; woh tabhi chalta hai jab aap use brackets ke saath **call** karein, jaise `label()`.",
        "**Parameters** `def` line ke naam hain; **arguments** call mein di gayi values hain, jo kram se ya naam se milti hain.",
        "**return** nateeja call karne wale ko wapas bhejta hai aur function khatam karta hai; bina `return` ka function **None** deta hai.",
        "Parameter ki **default value** ho sakti hai, jo call mein na di jaaye to use hoti hai.",
        "Function ke andar bane variables **local** hote hain: function khatam hote hi gaayab, isliye jo chahiye use return kijiye.",
    ],
}

T["kn"] = {
    "hook": {
        "title": "ಒಮ್ಮೆ ಬರೆಯಿರಿ, ಎಲ್ಲೆಡೆ ಬಳಸಿ",
        "md": "Hospital pharmacy ನ ಒಂದು app ಹಲವು ಕಡೆ ದೇಹದ ತೂಕದಿಂದ dose ಲೆಕ್ಕ ಹಾಕುತ್ತೆ: prescription screen ನಲ್ಲಿ, label ನಲ್ಲಿ, stock report ನಲ್ಲಿ. Formula ಹತ್ತು ಕಡೆ copy ಆಗಿದ್ದು ಒಂದು copy ಯಲ್ಲಿ ತಪ್ಪಿದ್ದರೆ, patient ಗೆ ತಪ್ಪು dose ಸಿಗಬಹುದು.\n\nಪರಿಹಾರ: formula ಅನ್ನು **ಒಮ್ಮೆ** ಬರೆದು, ಅದಕ್ಕೆ ಒಂದು **ಹೆಸರು** ಕೊಟ್ಟು, ಎಲ್ಲೆಡೆ ಆ ಹೆಸರನ್ನೇ ಬಳಸುವುದು. Code ನ ಈ ಹೆಸರಿರುವ, ಮತ್ತೆ ಬಳಸಬಹುದಾದ ಭಾಗವೇ **function**. Lesson 1.1 ಇಂದ ನೀವು functions ಬಳಸುತ್ತಿದ್ದೀರಿ: `print()`, `len()` ಮತ್ತು `input()`. ಇವತ್ತು ನಿಮ್ಮದೇ function ಬರೆಯುತ್ತೀರಿ.",
    },
    "learn": [
        "**def** ಇಂದ function **define** ಮಾಡುವುದು, ಮತ್ತು ಅದನ್ನು **call** ಮಾಡುವುದು",
        "**Parameters** ಇಂದ function ಬೇರೆ ಬೇರೆ values ಜೊತೆ ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತೆ",
        "**return** ಫಲಿತಾಂಶವನ್ನು ಹೇಗೆ ಹಿಂದೆ ಕಳಿಸುತ್ತೆ, ಮತ್ತು ಅದು print ತರಹ ಯಾಕಲ್ಲ",
        "**Default values** ಮತ್ತು **local variables** ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತವೆ",
    ],
    "explanation": [
        {
            "heading": "ನಿಮ್ಮ ಮೊದಲ function",
            "md": "Function ಅನ್ನು keyword **def**, ಒಂದು ಹೆಸರು, brackets ಮತ್ತು colon ಇಂದ **define** ಮಾಡುತ್ತೀರಿ. ಕೆಳಗಿನ indent ಮಾಡಿದ lines ಅದರ **body**:\n\n" + E.C_DEF + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_DEF + "\n\nFunction define ಮಾಡಿದರೆ ಅದು **run ಆಗಲ್ಲ**. Python ಅದನ್ನು ನೆನಪಿಟ್ಟುಕೊಳ್ಳುತ್ತೆ ಅಷ್ಟೇ. Function ನ ಹೆಸರನ್ನು brackets ಜೊತೆ ಬರೆದು **call** ಮಾಡಿದಾಗ ಪ್ರತಿ ಸಲ body run ಆಗುತ್ತೆ: `label()`.",
            "callout": {"title": "Function", "md": "ಒಂದು ಕೆಲಸ ಮಾಡುವ ಹೆಸರಿರುವ code block. def ಇಂದ ಒಮ್ಮೆ define ಮಾಡಿ, ಬೇಕಾದಾಗ ಅದರ ಹೆಸರನ್ನು brackets ಜೊತೆ ಬರೆದು run ಮಾಡುತ್ತೀರಿ."},
        },
        {
            "heading": "Parameters: function ಗೆ ಮಾಹಿತಿ ಕೊಡುವುದು",
            "md": "Function ಗೆ values ಕೊಡಲು ಸಾಧ್ಯವಾದಾಗ ಅದು ಇನ್ನೂ ಹೆಚ್ಚು ಉಪಯುಕ್ತ. `def` ನ brackets ಒಳಗಿನ ಹೆಸರುಗಳು **parameters**:\n\n" + E.C_PARAM + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_PARAM + "\n\nCall ನಲ್ಲಿ ಕೊಡುವ values, ಉದಾ. `\"Paracetamol\"` ಮತ್ತು `500`, **arguments**. ಇವು parameters ಜೊತೆ **ಕ್ರಮವಾಗಿ** ಹೊಂದುತ್ತವೆ: ಮೊದಲ argument `drug` ಗೆ, ಎರಡನೆಯದು `mg` ಗೆ.",
        },
        {
            "heading": "return: ಫಲಿತಾಂಶ ಹಿಂದೆ ಕಳಿಸುವುದು",
            "md": "`print()` value ಅನ್ನು screen ಮೇಲೆ ತೋರಿಸುತ್ತೆ ಅಷ್ಟೇ. Function ನ ಫಲಿತಾಂಶವನ್ನು program ನಲ್ಲಿ ಮುಂದೆ **ಬಳಸಲು**, function ಅದನ್ನು **return** ಮಾಡಬೇಕು:\n\n" + E.C_RET + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_RET + "\n\n`return` value ಅನ್ನು function call ಆದ ಜಾಗಕ್ಕೆ ಹಿಂದೆ ಕೊಡುತ್ತೆ, ಆಗ ನೀವು ಅದನ್ನು store ಮಾಡಬಹುದು, print ಮಾಡಬಹುದು, ಅಥವಾ ಲೆಕ್ಕ ಹಾಕಬಹುದು. ಇದು function ಅನ್ನು ಮುಗಿಸುತ್ತೆ ಕೂಡ: `return` ನಂತರದ lines ಯಾವತ್ತೂ run ಆಗಲ್ಲ.",
            "callout": {"title": "return ಇಲ್ಲದಿದ್ದರೆ None", "md": "return ಇಲ್ಲದ function None ಕೊಡುತ್ತೆ, Python ನಲ್ಲಿ \"ಏನೂ ಇಲ್ಲ\" ಅನ್ನುವ ಪದ. Function ಒಳಗೆ return ಬದಲು print ಮಾಡಿದರೆ, dose = child_dose(20, 15) ನಲ್ಲಿ None store ಆಗುತ್ತೆ."},
        },
        {
            "heading": "Default values ಮತ್ತು ಹೆಸರಿನ arguments",
            "md": "Parameter ಗೆ ಒಂದು **default value** ಇರಬಹುದು, call ನಲ್ಲಿ ಕೊಡದಿದ್ದಾಗ ಅದು ಬಳಕೆಯಾಗುತ್ತೆ. Call ನಲ್ಲಿ arguments ಅನ್ನು ಹೆಸರಿನಿಂದಲೂ ಕೊಡಬಹುದು, ಆಗ ಅವುಗಳ ಕ್ರಮ ಮುಖ್ಯ ಅಲ್ಲ:\n\n" + E.C_DEFAULT + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_DEFAULT + "\n\nDefault ಇರುವ parameters, default ಇಲ್ಲದವುಗಳ **ನಂತರ** ಬರಬೇಕು.",
        },
        {
            "heading": "Function ಒಳಗಿನ variables ಒಳಗೇ ಇರುತ್ತವೆ",
            "md": "Function ಒಳಗೆ ಮಾಡಿದ variable **local**: function run ಆಗುವವರೆಗೆ ಮಾತ್ರ ಇರುತ್ತೆ.\n\n" + E.C_LOCAL + "\n\nಇದು `10` print ಮಾಡುತ್ತೆ. ಆದರೆ function ನಂತರ `print(total)` ಬರೆದರೆ `NameError: name 'total' is not defined` ಬರುತ್ತೆ, ಯಾಕೆಂದರೆ function ಮುಗಿದಾಗ `total` ಮಾಯವಾಯಿತು. Value ಹೊರಗೆ ಬಳಸಬೇಕಾದರೆ ಅದನ್ನು **return** ಮಾಡಿ.\n\nಇದು ಒಳ್ಳೆಯದು: ಪ್ರತಿ function ಗೆ ತನ್ನದೇ variables, ಅದಕ್ಕೇ functions ಆಕಸ್ಮಿಕವಾಗಿ ಒಂದರ values ಇನ್ನೊಂದು ಬದಲಾಯಿಸಲ್ಲ.",
            "callout": {"title": "Functions ಯಾಕೆ ಬರೆಯಬೇಕು?", "md": "ಒಮ್ಮೆ ಬರೆಯಿರಿ, ಹಲವು ಸಲ ಬಳಸಿ. ತಪ್ಪನ್ನು ಒಂದೇ ಕಡೆ ಸರಿ ಮಾಡಿ. ಒಂದು step ಗೆ ಸ್ಪಷ್ಟ ಹೆಸರು ಕೊಡಿ, ಉದಾ. mg_to_g. ಮತ್ತು ಪ್ರತಿ ಭಾಗವನ್ನು ಬೇರೆಯಾಗಿ test ಮಾಡಿ."},
        },
    ],
    "walkthrough": {
        "intro": "ಈ program milligrams ಅನ್ನು grams ಗೆ ಬದಲಾಯಿಸುವ function define ಮಾಡಿ, ಅದನ್ನು ಎರಡು ಸಲ call ಮಾಡುತ್ತೆ.",
        "keyTerms": [
            {"meaning": "ಒಂದು parameter ಇರುವ mg_to_g ಎಂಬ function define ಮಾಡು."},
            {"meaning": "ಒಂದು parameter: ಪ್ರತಿ call ನಲ್ಲಿ ಕೊಟ್ಟ value ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ."},
            {"meaning": "ಫಲಿತಾಂಶವನ್ನು call ಮಾಡಿದವರಿಗೆ ಹಿಂದೆ ಕಳಿಸು."},
            {"meaning": "Function ಅನ್ನು argument 500 ಜೊತೆ call ಮಾಡು."},
        ],
    },
    "errors": {
        "intro": "ಈ ಎರಡು errors function ಅನ್ನು call ಮಾಡುವ ರೀತಿಯಿಂದ ಬರುತ್ತವೆ.",
        "examples": [
            {"title": "Define ಮಾಡುವ ಮುಂಚೆ function call ಮಾಡುವುದು", "md": "Python ಮೇಲಿಂದ ಕೆಳಗೆ run ಆಗುತ್ತೆ, ಅದಕ್ಕೇ line 1 ನಲ್ಲಿ ಅದು ಇನ್ನೂ `def` ನೋಡಿಲ್ಲ. Function definitions ಅನ್ನು ಮೇಲೆ, call ಮಾಡುವ ಮುಂಚೆ ಇಡಿ."},
            {"title": "ಒಂದು argument ಬಿಡುವುದು", "md": "Function ಗೆ ಎರಡು parameters ಇವೆ, ಆದರೆ call ಒಂದೇ value ಕೊಡುತ್ತೆ. ಎರಡೂ ಕೊಡಿ: `child_dose(20, 15)`, ಅಥವಾ parameter ಗೆ default value ಕೊಡಿ."},
        ],
    },
    "mistakes": [
        {"mistake": "Call ಮಾಡುವಾಗ brackets ಮರೆಯುವುದು, ಉದಾ. `label()` ಬದಲು `label`", "see": "Error ಇಲ್ಲ, ಆದರೆ ಏನೂ ಆಗಲ್ಲ", "fix": "Call ಗೆ ಯಾವಾಗಲೂ brackets ಬೇಕು: `label()`."},
        {"mistake": "Function ಒಳಗೆ return ಬದಲು print ಮಾಡಿ, ಆಮೇಲೆ ಫಲಿತಾಂಶದಿಂದ ಲೆಕ್ಕ ಹಾಕುವುದು", "see": "TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'", "fix": "Value ಹಿಂದೆ ಕಳಿಸಲು `return` ಬಳಸಿ; ಬೇಕಾದರೆ ಹೊರಗೆ print ಮಾಡಿ."},
        {"mistake": "`return` ನಂತರ lines ಬರೆದು ಅವು run ಆಗುತ್ತವೆ ಅಂತ ನಿರೀಕ್ಷಿಸುವುದು", "see": "Error ಇಲ್ಲ, ಆದರೆ ಆ lines ಯಾವತ್ತೂ run ಆಗಲ್ಲ", "fix": "Function ಮಾಡಬೇಕಾದ ಎಲ್ಲವನ್ನೂ `return` ಗಿಂತ ಮುಂಚೆ ಇಡಿ."},
        {"mistake": "Arguments ಅನ್ನು ತಪ್ಪು ಕ್ರಮದಲ್ಲಿ ಕೊಡುವುದು, ಉದಾ. `dose_label(500, \"Paracetamol\")`", "see": "Error ಇಲ್ಲ, ಆದರೆ label \"500: Paracetamol mg\" ಅಂತ ಬರುತ್ತೆ", "fix": "Parameters ನ ಕ್ರಮ ಹೊಂದಿಸಿ, ಅಥವಾ ಹೆಸರು ಕೊಡಿ: `dose_label(drug=\"Paracetamol\", mg=500)`."},
    ],
    "tasks": [
        {"title": "Label function", "md": "`Shake well before use` print ಮಾಡುವ **warning** ಎಂಬ function define ಮಾಡಿ. ಆಮೇಲೆ ಅದನ್ನು **ಎರಡು ಸಲ call** ಮಾಡಿ, output ಸರಿಯಾಗಿ ಹೀಗಿರಲಿ:",
         "hints": ["def warning():\n    print(\"Shake well before use\")", "ಅದನ್ನು warning() ಇಂದ ಎರಡು ಬೇರೆ lines ನಲ್ಲಿ, indentation ಇಲ್ಲದೆ call ಮಾಡಿ."]},
        {"title": "Parameters ಇರುವ function", "md": "**dose_label(drug, mg)** ಅನ್ನು ಪೂರ್ಣಗೊಳಿಸಿ, ಅದು drug ಮತ್ತು dose print ಮಾಡಲಿ. Call ಮೊದಲೇ ಬರೆದಿದೆ; output ಸರಿಯಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["Function ಒಳಗೆ ಎರಡೂ parameters ಅನ್ನು ಒಂದು print ನಲ್ಲಿ ಬಳಸಿ.", "    print(f\"{drug} {mg} mg\")"]},
        {"title": "Daily dose return ಮಾಡಿ", "md": "**daily_dose(dose, times)** dose ಅನ್ನು ದಿನಕ್ಕೆ ಎಷ್ಟು ಸಲ ಅನ್ನುವುದರಿಂದ ಗುಣಿಸಿ **return** ಮಾಡಲಿ. ಈಗ ಅದು `None` print ಮಾಡುತ್ತೆ. Output ಸರಿಯಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["return value ಅನ್ನು call ಗೆ ಹಿಂದೆ ಕಳಿಸುತ್ತೆ.", "    return dose * times"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "ಒಂದು syrup ನ ಪ್ರತಿ ml ನಲ್ಲಿ 50 mg ಇದೆ. 250 mg dose ಗೆ patient ಗೆ 5 ml ಬೇಕು, ಆದರೆ ಈ program number ಅನ್ನು ಬೇರೆ line ನಲ್ಲಿ print ಮಾಡಿ, ಆಮೇಲೆ `Give None ml` ಅಂತ ಹೇಳುತ್ತೆ. Output ಸರಿಯಾಗಿ ಹೀಗೇ ಬರುವ ಹಾಗೆ ಸರಿ ಮಾಡಿ:",
         "hints": ["Function ಗೆ return ಇಲ್ಲದಿದ್ದಾಗ ಅದು ಏನು ಹಿಂದೆ ಕೊಡುತ್ತೆ?", "Function ಒಳಗಿನ print(...) ಅನ್ನು return ... ಗೆ ಬದಲಾಯಿಸಿ."],
         "solutionNote": "print 5.0 ಅನ್ನು screen ಮೇಲೆ ತೋರಿಸಿತು ಅಷ್ಟೇ; function ತಾನು None ಕೊಟ್ಟಿತು, ಅದಕ್ಕೇ volume None ಆಯ್ತು. return, 5.0 ಅನ್ನು volume ಗೆ ಹಿಂದೆ ಕಳಿಸುತ್ತೆ."},
    ],
    "quiz": [
        {"q": "Python ನಲ್ಲಿ ಯಾವ keyword function define ಮಾಡುತ್ತೆ?", "why": "Functions def, ಹೆಸರು, brackets ಮತ್ತು colon ಇಂದ define ಆಗುತ್ತವೆ."},
        {"q": "def double(x):\n    return x * 2\n\nprint(double(4))\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "double(4), 4 * 2 ಅಂದರೆ 8 return ಮಾಡುತ್ತೆ."},
        {"q": "return statement ಇಲ್ಲದಿದ್ದರೆ function ಏನು ಹಿಂದೆ ಕೊಡುತ್ತೆ?", "why": "return ಇಲ್ಲದೆ Python None ಕೊಡುತ್ತೆ."},
        {"q": "def child_dose(weight, mg_per_kg): ನಲ್ಲಿ weight ಏನು?", "why": "def ನ brackets ಒಳಗಿನ ಹೆಸರುಗಳು parameters; call ನಲ್ಲಿ ಕೊಡುವ values arguments."},
        {"q": "def greet(name=\"Patient\"):\n    print(\"Hello\", name)\n\ngreet()\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "ಯಾವ argument ಕೂಡ ಕೊಟ್ಟಿಲ್ಲ, ಅದಕ್ಕೇ default value \"Patient\" ಬಳಕೆಯಾಗುತ್ತೆ."},
        {"q": "Function ಒಳಗೆ return ನಂತರ ಬರೆದ lines ಗೆ ಏನಾಗುತ್ತೆ?", "why": "return function ಅನ್ನು ತಕ್ಷಣ ಮುಗಿಸುತ್ತೆ."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 2.5 · Functions",
        "children": [
            {"label": "Define", "children": [{"label": "def name():"}, {"label": "Indent ಮಾಡಿದ body"}, {"label": "ಇನ್ನೂ run ಆಗಲ್ಲ"}]},
            {"label": "Call", "children": [{"label": "name()"}, {"label": "Body run ಮಾಡುತ್ತೆ"}, {"label": "ಹಲವು ಸಲ call"}]},
            {"label": "Parameters", "children": [{"label": "def ನಲ್ಲಿ ಹೆಸರು"}, {"label": "Arguments = call ನ values"}, {"label": "ಕ್ರಮವಾಗಿ ಹೊಂದುತ್ತವೆ"}]},
            {"label": "return", "children": [{"label": "ಫಲಿತಾಂಶ ಹಿಂದೆ ಕಳಿಸುತ್ತೆ"}, {"label": "Function ಮುಗಿಸುತ್ತೆ"}, {"label": "return ಇಲ್ಲ → None"}]},
            {"label": "Extras", "children": [{"label": "Default values"}, {"label": "ಹೆಸರಿನ arguments"}, {"label": "Local variables"}]},
            {"label": "Errors", "children": [{"label": "NameError: ಇನ್ನೂ define ಆಗಿಲ್ಲ"}, {"label": "TypeError: argument ಬಿಟ್ಟಿದೆ"}]},
        ],
    },
    "summary": [
        "**Function** ಹೆಸರಿರುವ code block. **def** ಅದನ್ನು define ಮಾಡುತ್ತೆ; brackets ಜೊತೆ **call** ಮಾಡಿದಾಗ ಮಾತ್ರ run ಆಗುತ್ತೆ, ಉದಾ. `label()`.",
        "**Parameters** `def` line ನ ಹೆಸರುಗಳು; **arguments** call ನಲ್ಲಿ ಕೊಡುವ values, ಕ್ರಮವಾಗಿ ಅಥವಾ ಹೆಸರಿನಿಂದ ಹೊಂದುತ್ತವೆ.",
        "**return** ಫಲಿತಾಂಶವನ್ನು call ಮಾಡಿದವರಿಗೆ ಹಿಂದೆ ಕಳಿಸಿ function ಮುಗಿಸುತ್ತೆ; `return` ಇಲ್ಲದ function **None** ಕೊಡುತ್ತೆ.",
        "Parameter ಗೆ **default value** ಇರಬಹುದು, call ನಲ್ಲಿ ಕೊಡದಿದ್ದಾಗ ಅದು ಬಳಕೆಯಾಗುತ್ತೆ.",
        "Function ಒಳಗೆ ಮಾಡಿದ variables **local**: ಅದು ಮುಗಿದಾಗ ಮಾಯವಾಗುತ್ತವೆ, ಅದಕ್ಕೇ ಬೇಕಾದ್ದನ್ನು return ಮಾಡಿ.",
    ],
}

NARR = {
    "hi": [
        "यह program conversion को एक बार, function के रूप में लिखता है, और उसे दो बार use करता है।",
        "Comment बताता है कि function क्या करता है।",
        "def, m g to g नाम का function बनाता है, जिसका एक parameter है, m g। Python उसे याद रखता है, पर body अभी नहीं चलाता।",
        "यहाँ function को पाँच सौ के साथ call किया गया। Python function में कूदता है, और parameter m g को पाँच सौ मिलता है।",
        "अंदर, grams है पाँच सौ भाग एक हज़ार: zero दशमलव पाँच।",
        "return, zero दशमलव पाँच को उस line पर वापस भेजता है जिसने function call किया।",
        "Line छह पर वापस, call की जगह उसका नतीजा आ जाता है, और print उसे दिखाता है।",
        "वही function फिर call होता है, दो हज़ार पाँच सौ के साथ। इस बार वह दो दशमलव पाँच return करता है।",
    ],
    "hinglish": [
        "Yeh program conversion ko ek baar, function ke roop mein likhta hai, aur use do baar use karta hai.",
        "Comment batata hai ki function kya karta hai.",
        "def, m g to g naam ka function banaata hai, jiska ek parameter hai, m g. Python use yaad rakhta hai, par body abhi nahi chalaata.",
        "Yahaan function ko paanch sau ke saath call kiya gaya. Python function mein koodta hai, aur parameter m g ko paanch sau milta hai.",
        "Andar, grams hai paanch sau bhaag ek hazaar: zero dashamlav paanch.",
        "return, zero dashamlav paanch ko us line par wapas bhejta hai jisne function call kiya.",
        "Line chhah par wapas, call ki jagah uska nateeja aa jaata hai, aur print use dikhaata hai.",
        "Wahi function phir call hota hai, do hazaar paanch sau ke saath. Is baar woh do dashamlav paanch return karta hai.",
    ],
    "kn": [
        "ಈ program conversion ಅನ್ನು ಒಮ್ಮೆ, function ಆಗಿ ಬರೆದು, ಎರಡು ಸಲ ಬಳಸುತ್ತೆ.",
        "Comment function ಏನು ಮಾಡುತ್ತೆ ಅಂತ ಹೇಳುತ್ತೆ.",
        "def, m g to g ಎಂಬ function ಮಾಡುತ್ತೆ, ಅದಕ್ಕೆ ಒಂದು parameter, m g. Python ಅದನ್ನು ನೆನಪಿಟ್ಟುಕೊಳ್ಳುತ್ತೆ, ಆದರೆ body ಈಗ run ಮಾಡಲ್ಲ.",
        "ಇಲ್ಲಿ function ಅನ್ನು ಐನೂರು ಜೊತೆ call ಮಾಡಲಾಗಿದೆ. Python function ಒಳಗೆ ಜಿಗಿಯುತ್ತೆ, parameter m g ಗೆ ಐನೂರು ಸಿಗುತ್ತೆ.",
        "ಒಳಗೆ, grams ಅಂದರೆ ಐನೂರು ಭಾಗಿಸು ಸಾವಿರ: zero ಪಾಯಿಂಟ್ ಐದು.",
        "return, zero ಪಾಯಿಂಟ್ ಐದನ್ನು function call ಮಾಡಿದ line ಗೆ ಹಿಂದೆ ಕಳಿಸುತ್ತೆ.",
        "Line ಆರಕ್ಕೆ ಹಿಂತಿರುಗಿ, call ಜಾಗದಲ್ಲಿ ಅದರ ಫಲಿತಾಂಶ ಬರುತ್ತೆ, print ಅದನ್ನು ತೋರಿಸುತ್ತೆ.",
        "ಅದೇ function ಮತ್ತೆ call ಆಗುತ್ತೆ, ಎರಡು ಸಾವಿರದ ಐನೂರು ಜೊತೆ. ಈ ಸಲ ಅದು ಎರಡು ಪಾಯಿಂಟ್ ಐದು return ಮಾಡುತ್ತೆ.",
    ],
}

ANIM = {
    "hi": [
        "def lines बस Python को एक नया शब्द सिखाती हैं, m g to g। अभी कुछ नहीं चलता।",
        "आखिरी line function को पाँच सौ के साथ call करती है। Python function में कूदता है, और parameter m g को पाँच सौ मिलता है।",
        "Body grams निकालती है: zero दशमलव पाँच।",
        "return, zero दशमलव पाँच को वहाँ वापस ले जाता है जहाँ function call हुआ था।",
        "Call, zero दशमलव पाँच बन जाता है, और print उसे दिखाता है।",
    ],
    "hinglish": [
        "def lines bas Python ko ek naya shabd sikhaati hain, m g to g. Abhi kuch nahi chalta.",
        "Aakhri line function ko paanch sau ke saath call karti hai. Python function mein koodta hai, aur parameter m g ko paanch sau milta hai.",
        "Body grams nikaalti hai: zero dashamlav paanch.",
        "return, zero dashamlav paanch ko wahaan wapas le jaata hai jahaan function call hua tha.",
        "Call, zero dashamlav paanch ban jaata hai, aur print use dikhaata hai.",
    ],
    "kn": [
        "def lines Python ಗೆ ಒಂದು ಹೊಸ ಪದ ಕಲಿಸುತ್ತವೆ ಅಷ್ಟೇ, m g to g. ಇನ್ನೂ ಏನೂ run ಆಗಲ್ಲ.",
        "ಕೊನೆಯ line function ಅನ್ನು ಐನೂರು ಜೊತೆ call ಮಾಡುತ್ತೆ. Python function ಒಳಗೆ ಜಿಗಿಯುತ್ತೆ, parameter m g ಗೆ ಐನೂರು ಸಿಗುತ್ತೆ.",
        "Body grams ಲೆಕ್ಕ ಹಾಕುತ್ತೆ: zero ಪಾಯಿಂಟ್ ಐದು.",
        "return, zero ಪಾಯಿಂಟ್ ಐದನ್ನು function call ಆದ ಜಾಗಕ್ಕೆ ಹಿಂದೆ ಕೊಂಡೊಯ್ಯುತ್ತೆ.",
        "Call zero ಪಾಯಿಂಟ್ ಐದು ಆಗುತ್ತೆ, print ಅದನ್ನು ತೋರಿಸುತ್ತೆ.",
    ],
}

if __name__ == "__main__":
    build("2-5", "anim-call", T, NARR, ANIM, say_en=lambda t: t.replace("m g to g", "M G to G"))

"""Lesson 3.6 translations (Hindi, Hinglish, Kannada) and voice scripts."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import build  # noqa: E402

_spec = importlib.util.spec_from_file_location("en36", os.path.join(os.path.dirname(__file__), "..", "lessons", "bp101t_3-6_en.py"))
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)

T = {}

T["hi"] = {
    "hook": {
        "title": "हर patient visit एक row है",
        "md": "जब patient OPD आता है, hospital हर बार वही चीज़ें दर्ज करता है: एक ID, age, sex, diagnosis, लिखी गई drugs। Pharmacovigilance centre हर adverse reaction report के लिए वही fields दर्ज करता है। हज़ारों visits, सबके **एक जैसे fields**, मिलकर एक **structured dataset** बनाते हैं।\n\nClinical research, drug safety और hospital planning इसी तरह के data पर चलते हैं। आज आप lists और dictionaries से, जो आप पहले से जानते हैं, ऐसा dataset रखेंगे, patients चुनेंगे, groups की तुलना करेंगे, खराब data पकड़ेंगे, और patient की privacy बचाएँगे।",
    },
    "learn": [
        "**Records**, **fields** और **structured data** क्या हैं",
        "Dataset को **list of dictionaries** के रूप में रखना, और condition से records चुनना",
        "**Group** के हिसाब से सार निकालना, जैसे पुरुषों और महिलाओं की average sugar",
        "**Missing** और असंभव values पकड़ना, और privacy के लिए **identifiers** हटाना",
    ],
    "explanation": [
        {
            "heading": "Records और fields",
            "md": "Structured data एक **table** है। हर **row** एक **record** है (एक patient, एक visit, एक report) और हर **column** एक **field** है (age, sex, sugar):\n\n" + E.T_TABLE + "\n\nPython में इसे रखने का स्वाभाविक तरीका है **list of dictionaries**: हर record की एक dictionary, field के नाम keys के रूप में:\n\n" + E.C_RECORDS + "\n\nयह print करता है:\n\n" + E.O_RECORDS + "\n\n`patients[0]` पहला record है; `patients[0][\"sugar\"]` उसका एक field। `for` loop हर record पर जाता है।",
            "callout": {"title": "Structured data", "md": "Records में व्यवस्थित data जिनके fields एक जैसे हों, table की तरह। Spreadsheets, CSV files और hospital registers structured हैं; doctors के free-text notes नहीं।"},
        },
        {
            "heading": "Records चुनना",
            "md": "Condition से मेल खाने वाले records चुनने के लिए dataset पर loop चलाइए और जो चाहिए उन्हें रखिए। 126 mg/dL या उससे ज़्यादा fasting blood sugar diabetes की ओर इशारा करती है:\n\n" + E.C_SELECT + "\n\nयह print करता है:\n\n" + E.O_SELECT + "\n\nExcel का filter ठीक यही करता है, और Unit IV में Pandas इसे एक line में करेगा।",
        },
        {
            "heading": "Group के हिसाब से सार",
            "md": "अक्सर आप groups की तुलना करना चाहते हैं: पुरुष और महिलाएँ, wards, age groups। Lesson 3.3 का गिनती वाला pattern दो बार use कीजिए, एक बार totals के लिए और एक बार counts के लिए:\n\n" + E.C_GROUP + "\n\nयह print करता है:\n\n" + E.O_GROUP + "\n\nदोनों महिलाओं की readings का average (118 + 165) / 2 = 141.5 है। तीन patients के साथ यह हाथ से आसान है; तीन हज़ार के साथ भी यही सात lines काम करती हैं।",
        },
        {
            "heading": "Missing और असंभव values",
            "md": "असली datasets कभी perfect नहीं होते। कोई field **missing** हो सकता है (Python `None` use करता है, Excel खाली दिखाता है) या **असंभव**, जैसे 540 की age जो 54 होनी थी। हिसाब से पहले check कीजिए:\n\n" + E.C_CLEAN + "\n\nयह print करता है:\n\n" + E.O_CLEAN + "\n\n`is None` missing value की जाँच करता है। `0 < age < 120` एक बार में range check करता है। इन problems को ढूँढना **data cleaning** कहलाता है, और ज़्यादातर असली projects में इसमें analysis से भी ज़्यादा समय लगता है।",
            "callout": {"title": "Missing value का कभी अंदाज़ा मत लगाइए", "md": "Missing age या dose की जगह चुपचाप 0 मत डालिए: average गलत होगा। उसे flag कीजिए, source से पूछिए, या record छोड़कर report में बताइए।"},
        },
        {
            "heading": "Privacy: patient की पहचान हटाइए",
            "md": "नाम, phone numbers, पते और Aadhaar numbers patient की **पहचान** कराते हैं। भारत के **Digital Personal Data Protection Act, 2023** के तहत health data सुरक्षित रखना ज़रूरी है। Analysis से पहले सिर्फ़ ज़रूरी fields रखिए और नाम की जगह `P01` जैसा code use कीजिए:\n\n" + E.C_ANON + "\n\nयह print करता है:\n\n" + E.O_ANON + "\n\nAnalysis फिर भी चलता है, और file पढ़ने वाला कोई नहीं बता सकता कि patient कौन है। इसे **de-identification** (या anonymisation) कहते हैं।",
            "callout": {"title": "Data dictionary रखिए", "md": "Data dictionary हर field की list है: उसका नाम, type, unit और allowed values (age: int, years, 0 से 120)। जब कई लोग data भरते हैं तो यह dataset को एक जैसा रखती है।"},
        },
    ],
    "walkthrough": {
        "intro": "यह program तीन adverse drug reaction (ADR) reports पढ़ता है, हर drug की reports गिनता है और serious वाली गिनता है।",
        "keyTerms": [
            {"meaning": "एक dataset: हर record की एक dictionary वाली list।"},
            {"meaning": "मौजूदा record का एक field।"},
            {"meaning": "हर drug के records गिनो।"},
            {"meaning": "सिर्फ़ उन records के लिए चलता है जहाँ serious True है।"},
        ],
    },
    "errors": {
        "intro": "दोनों errors ऐसे records से आती हैं जो program की उम्मीद जैसे नहीं दिखते।",
        "examples": [
            {"title": "Field का नाम अलग spelling में", "md": "Field `\"sugar\"` है, छोटे s के साथ। Field के नाम बिल्कुल मिलने चाहिए। हर field की spelling तय करने वाली data dictionary, कई लोगों के data भरने पर इससे बचाती है।"},
            {"title": "Missing value की तुलना", "md": "P05 की age नहीं है, इसलिए Python से पूछा जाता है कि क्या None 40 से कम है, जिसका कोई मतलब नहीं। पहले missing values check कीजिए: `if r[\"age\"] is not None and r[\"age\"] < 40:`।"},
        ],
    },
    "mistakes": [
        {"mistake": "कुछ records में field की spelling अलग: `\"Age\"` और `\"age\"`", "see": "कुछ records के लिए KeyError", "fix": "Data dictionary में field के नाम तय कीजिए और हर जगह वही use कीजिए।"},
        {"mistake": "Units मिलाना: कुछ doses mg में, कुछ g में", "see": "कोई error नहीं, पर averages और totals गलत", "fix": "हर value एक unit में रखिए; data भरते समय convert कीजिए।"},
        {"mistake": "खाली या \"NA\" value को convert करना: `int(\"NA\")`", "see": "ValueError: invalid literal for int() with base 10: 'NA'", "fix": "Convert करने से पहले missing values check कीजिए।"},
        {"mistake": "Analysis वाली files में नाम और phone numbers रखना", "see": "कोई error नहीं, पर file share होने पर privacy का उल्लंघन", "fix": "Identifiers हटाइए और P01 जैसे patient codes use कीजिए।"},
    ],
    "tasks": [
        {"title": "हर record दिखाइए", "md": "**patients** पर loop चलाइए और हर patient की id और sugar reading print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["for p in patients: हर record पर जाता है।", "for p in patients:\n    print(p[\"id\"], p[\"sugar\"])"]},
        {"title": "महिलाओं को गिनिए", "md": "गिनिए कि कितने records में sex **\"F\"** है। Output बिल्कुल यह होना चाहिए:",
         "hints": ["Records पर loop चलाइए और p[\"sex\"] == \"F\" test कीजिए।", "for p in patients:\n    if p[\"sex\"] == \"F\":\n        count += 1"]},
        {"title": "Average age", "md": "हर record का **age** field जोड़िए और average age print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["Loop के अंदर total += p[\"age\"]।", "print(\"Average age:\", total / len(patients))"]},
        {"title": "Bug ढूँढिए", "md": "इस program को 60 से ऊपर के patients दिखाने हैं, पर यह P05 पर crash होता है, जिसकी age missing है। Condition ठीक कीजिए ताकि missing ages छूट जाएँ और output बिल्कुल यह हो:",
         "hints": ["None की number से तुलना नहीं हो सकती। पहले उसे check कीजिए।", "if r[\"age\"] is not None and r[\"age\"] > 60:"],
         "solutionNote": "and पहले बाईं तरफ़ check करता है: P05 के लिए r[\"age\"] is not None False है, इसलिए Python None > 60 कभी नहीं आज़माता।"},
    ],
    "quiz": [
        {"q": "Dataset की table में एक row क्या है?", "why": "हर row एक record है: एक patient, visit या report।"},
        {"q": "Dataset की table में एक column क्या है?", "why": "हर column एक field है, जैसे age या sugar।"},
        {"q": "Patient records का dataset रखने के लिए सबसे अच्छी Python structure कौन-सी है?", "why": "हर record की एक dictionary, सब एक list के अंदर।"},
        {"q": "कैसे check करें कि कोई field missing (None) है?", "why": "is None, Python की missing value check करता है।"},
        {"q": "इनमें से कौन-सी चीज़ सीधे patient की पहचान कराती है?", "why": "Phone number एक व्यक्ति की ओर इशारा करता है; analysis से पहले उसे हटाइए।"},
        {"q": "Data dictionary किसलिए है?", "why": "यह data भरने वाले सबको एक जैसा रखती है।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 3.6 · Healthcare datasets",
        "children": [
            {"label": "Dataset", "children": [{"label": "Records की table"}, {"label": "Row = record"}, {"label": "Column = field"}]},
            {"label": "Python में", "children": [{"label": "List of dicts"}, {"label": "records[0][\"age\"]"}, {"label": "for r in records"}]},
            {"label": "चुनना और group", "children": [{"label": "if condition → append"}, {"label": "get() से गिनती"}, {"label": "हर group का average"}]},
            {"label": "Data quality", "children": [{"label": "Missing: None"}, {"label": "Range से बाहर values"}, {"label": "एक जैसी units और नाम"}]},
            {"label": "Privacy", "children": [{"label": "नाम, phone हटाओ"}, {"label": "Patient IDs use करो"}, {"label": "DPDP Act 2023"}]},
            {"label": "Errors", "children": [{"label": "KeyError: field name"}, {"label": "TypeError: None compare"}]},
        ],
    },
    "summary": [
        "**Structured data** एक table है: हर **row** एक **record**, हर **column** एक **field**।",
        "Python में dataset एक **list of dictionaries** है: `patients[0][\"sugar\"]` एक record का एक field है।",
        "Loop और `if` से records चुनिए; `get()` से totals और counts बनाकर **group** के हिसाब से सार निकालिए।",
        "हिसाब से पहले **missing** (`is None`) और **असंभव** values check कीजिए; missing value का कभी अंदाज़ा मत लगाइए।",
        "Privacy बचाइए: **identifiers** (नाम, phone, Aadhaar) हटाइए और `P01` जैसे codes use कीजिए, जैसा DPDP Act 2023 कहता है।",
    ],
}

T["hinglish"] = {
    "hook": {
        "title": "Har patient visit ek row hai",
        "md": "Jab patient OPD aata hai, hospital har baar wahi cheezein darj karta hai: ek ID, age, sex, diagnosis, likhi gayi drugs. Pharmacovigilance centre har adverse reaction report ke liye wahi fields darj karta hai. Hazaaron visits, sabke **ek jaise fields**, milkar ek **structured dataset** banaate hain.\n\nClinical research, drug safety aur hospital planning isi tarah ke data par chalte hain. Aaj aap lists aur dictionaries se, jo aap pehle se jaante hain, aisa dataset rakhenge, patients chunenge, groups ki tulna karenge, kharaab data pakdenge, aur patient ki privacy bachaayenge.",
    },
    "learn": [
        "**Records**, **fields** aur **structured data** kya hain",
        "Dataset ko **list of dictionaries** ke roop mein rakhna, aur condition se records chunna",
        "**Group** ke hisaab se saar nikaalna, jaise purushon aur mahilaon ki average sugar",
        "**Missing** aur asambhav values pakadna, aur privacy ke liye **identifiers** hataana",
    ],
    "explanation": [
        {
            "heading": "Records aur fields",
            "md": "Structured data ek **table** hai. Har **row** ek **record** hai (ek patient, ek visit, ek report) aur har **column** ek **field** hai (age, sex, sugar):\n\n" + E.T_TABLE + "\n\nPython mein ise rakhne ka swaabhaavik tareeka hai **list of dictionaries**: har record ki ek dictionary, field ke naam keys ke roop mein:\n\n" + E.C_RECORDS + "\n\nYeh print karta hai:\n\n" + E.O_RECORDS + "\n\n`patients[0]` pehla record hai; `patients[0][\"sugar\"]` uska ek field. `for` loop har record par jaata hai.",
            "callout": {"title": "Structured data", "md": "Records mein vyavasthit data jinke fields ek jaise hon, table ki tarah. Spreadsheets, CSV files aur hospital registers structured hain; doctors ke free-text notes nahi."},
        },
        {
            "heading": "Records chunna",
            "md": "Condition se mel khaane wale records chunne ke liye dataset par loop chalaaiye aur jo chahiye unhe rakhiye. 126 mg/dL ya usse zyada fasting blood sugar diabetes ki or ishaara karti hai:\n\n" + E.C_SELECT + "\n\nYeh print karta hai:\n\n" + E.O_SELECT + "\n\nExcel ka filter theek yahi karta hai, aur Unit IV mein Pandas ise ek line mein karega.",
        },
        {
            "heading": "Group ke hisaab se saar",
            "md": "Aksar aap groups ki tulna karna chahte hain: purush aur mahilaayein, wards, age groups. Lesson 3.3 ka ginti wala pattern do baar use kijiye, ek baar totals ke liye aur ek baar counts ke liye:\n\n" + E.C_GROUP + "\n\nYeh print karta hai:\n\n" + E.O_GROUP + "\n\nDono mahilaon ki readings ka average (118 + 165) / 2 = 141.5 hai. Teen patients ke saath yeh haath se aasaan hai; teen hazaar ke saath bhi yahi saat lines kaam karti hain.",
        },
        {
            "heading": "Missing aur asambhav values",
            "md": "Asli datasets kabhi perfect nahi hote. Koi field **missing** ho sakta hai (Python `None` use karta hai, Excel khaali dikhaata hai) ya **asambhav**, jaise 540 ki age jo 54 honi thi. Hisaab se pehle check kijiye:\n\n" + E.C_CLEAN + "\n\nYeh print karta hai:\n\n" + E.O_CLEAN + "\n\n`is None` missing value ki jaanch karta hai. `0 < age < 120` ek baar mein range check karta hai. In problems ko dhoondhna **data cleaning** kehlaata hai, aur zyaadatar asli projects mein ismein analysis se bhi zyada samay lagta hai.",
            "callout": {"title": "Missing value ka kabhi andaaza mat lagaaiye", "md": "Missing age ya dose ki jagah chupchaap 0 mat daaliye: average galat hoga. Use flag kijiye, source se poochhiye, ya record chhodkar report mein bataaiye."},
        },
        {
            "heading": "Privacy: patient ki pehchaan hataaiye",
            "md": "Naam, phone numbers, pate aur Aadhaar numbers patient ki **pehchaan** karaate hain. Bharat ke **Digital Personal Data Protection Act, 2023** ke tahat health data surakshit rakhna zaroori hai. Analysis se pehle sirf zaroori fields rakhiye aur naam ki jagah `P01` jaisa code use kijiye:\n\n" + E.C_ANON + "\n\nYeh print karta hai:\n\n" + E.O_ANON + "\n\nAnalysis phir bhi chalta hai, aur file padhne wala koi nahi bata sakta ki patient kaun hai. Ise **de-identification** (ya anonymisation) kehte hain.",
            "callout": {"title": "Data dictionary rakhiye", "md": "Data dictionary har field ki list hai: uska naam, type, unit aur allowed values (age: int, years, 0 se 120). Jab kai log data bharte hain to yeh dataset ko ek jaisa rakhti hai."},
        },
    ],
    "walkthrough": {
        "intro": "Yeh program teen adverse drug reaction (ADR) reports padhta hai, har drug ki reports ginta hai aur serious wali ginta hai.",
        "keyTerms": [
            {"meaning": "Ek dataset: har record ki ek dictionary wali list."},
            {"meaning": "Maujooda record ka ek field."},
            {"meaning": "Har drug ke records gino."},
            {"meaning": "Sirf un records ke liye chalta hai jahaan serious True hai."},
        ],
    },
    "errors": {
        "intro": "Dono errors aise records se aati hain jo program ki ummeed jaise nahi dikhte.",
        "examples": [
            {"title": "Field ka naam alag spelling mein", "md": "Field `\"sugar\"` hai, chhote s ke saath. Field ke naam bilkul milne chahiye. Har field ki spelling tay karne wali data dictionary, kai logon ke data bharne par isse bachaati hai."},
            {"title": "Missing value ki tulna", "md": "P05 ki age nahi hai, isliye Python se poochha jaata hai ki kya None 40 se kam hai, jiska koi matlab nahi. Pehle missing values check kijiye: `if r[\"age\"] is not None and r[\"age\"] < 40:`."},
        ],
    },
    "mistakes": [
        {"mistake": "Kuch records mein field ki spelling alag: `\"Age\"` aur `\"age\"`", "see": "Kuch records ke liye KeyError", "fix": "Data dictionary mein field ke naam tay kijiye aur har jagah wahi use kijiye."},
        {"mistake": "Units milaana: kuch doses mg mein, kuch g mein", "see": "Koi error nahi, par averages aur totals galat", "fix": "Har value ek unit mein rakhiye; data bharte samay convert kijiye."},
        {"mistake": "Khaali ya \"NA\" value ko convert karna: `int(\"NA\")`", "see": "ValueError: invalid literal for int() with base 10: 'NA'", "fix": "Convert karne se pehle missing values check kijiye."},
        {"mistake": "Analysis wali files mein naam aur phone numbers rakhna", "see": "Koi error nahi, par file share hone par privacy ka ullanghan", "fix": "Identifiers hataaiye aur P01 jaise patient codes use kijiye."},
    ],
    "tasks": [
        {"title": "Har record dikhaaiye", "md": "**patients** par loop chalaaiye aur har patient ki id aur sugar reading print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["for p in patients: har record par jaata hai.", "for p in patients:\n    print(p[\"id\"], p[\"sugar\"])"]},
        {"title": "Mahilaon ko giniye", "md": "Giniye ki kitne records mein sex **\"F\"** hai. Output bilkul yeh hona chahiye:",
         "hints": ["Records par loop chalaaiye aur p[\"sex\"] == \"F\" test kijiye.", "for p in patients:\n    if p[\"sex\"] == \"F\":\n        count += 1"]},
        {"title": "Average age", "md": "Har record ka **age** field jodiye aur average age print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["Loop ke andar total += p[\"age\"].", "print(\"Average age:\", total / len(patients))"]},
        {"title": "Bug dhoondhiye", "md": "Is program ko 60 se upar ke patients dikhaane hain, par yeh P05 par crash hota hai, jiski age missing hai. Condition theek kijiye taaki missing ages chhoot jaayein aur output bilkul yeh ho:",
         "hints": ["None ki number se tulna nahi ho sakti. Pehle use check kijiye.", "if r[\"age\"] is not None and r[\"age\"] > 60:"],
         "solutionNote": "and pehle baayin taraf check karta hai: P05 ke liye r[\"age\"] is not None False hai, isliye Python None > 60 kabhi nahi aazmaata."},
    ],
    "quiz": [
        {"q": "Dataset ki table mein ek row kya hai?", "why": "Har row ek record hai: ek patient, visit ya report."},
        {"q": "Dataset ki table mein ek column kya hai?", "why": "Har column ek field hai, jaise age ya sugar."},
        {"q": "Patient records ka dataset rakhne ke liye sabse achhi Python structure kaun-si hai?", "why": "Har record ki ek dictionary, sab ek list ke andar."},
        {"q": "Kaise check karein ki koi field missing (None) hai?", "why": "is None, Python ki missing value check karta hai."},
        {"q": "Inmein se kaun-si cheez seedhe patient ki pehchaan karaati hai?", "why": "Phone number ek vyakti ki or ishaara karta hai; analysis se pehle use hataaiye."},
        {"q": "Data dictionary kis liye hai?", "why": "Yeh data bharne wale sabko ek jaisa rakhti hai."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 3.6 · Healthcare datasets",
        "children": [
            {"label": "Dataset", "children": [{"label": "Records ki table"}, {"label": "Row = record"}, {"label": "Column = field"}]},
            {"label": "Python mein", "children": [{"label": "List of dicts"}, {"label": "records[0][\"age\"]"}, {"label": "for r in records"}]},
            {"label": "Chunna aur group", "children": [{"label": "if condition → append"}, {"label": "get() se ginti"}, {"label": "Har group ka average"}]},
            {"label": "Data quality", "children": [{"label": "Missing: None"}, {"label": "Range se bahar values"}, {"label": "Ek jaisi units aur naam"}]},
            {"label": "Privacy", "children": [{"label": "Naam, phone hataao"}, {"label": "Patient IDs use karo"}, {"label": "DPDP Act 2023"}]},
            {"label": "Errors", "children": [{"label": "KeyError: field name"}, {"label": "TypeError: None compare"}]},
        ],
    },
    "summary": [
        "**Structured data** ek table hai: har **row** ek **record**, har **column** ek **field**.",
        "Python mein dataset ek **list of dictionaries** hai: `patients[0][\"sugar\"]` ek record ka ek field hai.",
        "Loop aur `if` se records chuniye; `get()` se totals aur counts banaakar **group** ke hisaab se saar nikaaliye.",
        "Hisaab se pehle **missing** (`is None`) aur **asambhav** values check kijiye; missing value ka kabhi andaaza mat lagaaiye.",
        "Privacy bachaaiye: **identifiers** (naam, phone, Aadhaar) hataaiye aur `P01` jaise codes use kijiye, jaisa DPDP Act 2023 kehta hai.",
    ],
}

T["kn"] = {
    "hook": {
        "title": "ಪ್ರತಿ patient visit ಒಂದು row",
        "md": "Patient OPD ಗೆ ಬಂದಾಗ hospital ಪ್ರತಿ ಸಲ ಅದೇ ವಿಷಯಗಳನ್ನು ದಾಖಲಿಸುತ್ತೆ: ಒಂದು ID, age, sex, diagnosis, ಬರೆದ drugs. Pharmacovigilance centre ಪ್ರತಿ adverse reaction report ಗೆ ಅದೇ fields ದಾಖಲಿಸುತ್ತೆ. ಸಾವಿರಾರು visits, ಎಲ್ಲಕ್ಕೂ **ಒಂದೇ fields**, ಸೇರಿ ಒಂದು **structured dataset** ಆಗುತ್ತೆ.\n\nClinical research, drug safety ಮತ್ತು hospital planning ಇಂತಹ data ಮೇಲೆ ನಡೆಯುತ್ತವೆ. ಇವತ್ತು ನಿಮಗೆ ಈಗಾಗಲೇ ಗೊತ್ತಿರುವ lists ಮತ್ತು dictionaries ಬಳಸಿ ಅಂತಹ dataset ಇಡುತ್ತೀರಿ, patients ಆರಿಸುತ್ತೀರಿ, groups ಹೋಲಿಸುತ್ತೀರಿ, ಕೆಟ್ಟ data ಹಿಡಿಯುತ್ತೀರಿ, patient privacy ಕಾಪಾಡುತ್ತೀರಿ.",
    },
    "learn": [
        "**Records**, **fields** ಮತ್ತು **structured data** ಅಂದ್ರೆ ಏನು",
        "Dataset ಅನ್ನು **list of dictionaries** ಆಗಿ ಇಡುವುದು, condition ಇಂದ records ಆರಿಸುವುದು",
        "**Group** ಪ್ರಕಾರ ಸಾರಾಂಶ, ಗಂಡಸರು ಮತ್ತು ಹೆಂಗಸರ average sugar ತರಹ",
        "**Missing** ಮತ್ತು ಅಸಾಧ್ಯ values ಹಿಡಿಯುವುದು, privacy ಗಾಗಿ **identifiers** ತೆಗೆಯುವುದು",
    ],
    "explanation": [
        {
            "heading": "Records ಮತ್ತು fields",
            "md": "Structured data ಒಂದು **table**. ಪ್ರತಿ **row** ಒಂದು **record** (ಒಬ್ಬ patient, ಒಂದು visit, ಒಂದು report), ಪ್ರತಿ **column** ಒಂದು **field** (age, sex, sugar):\n\n" + E.T_TABLE + "\n\nPython ನಲ್ಲಿ ಇದನ್ನು ಇಡಲು ಸಹಜ ದಾರಿ **list of dictionaries**: ಪ್ರತಿ record ಗೆ ಒಂದು dictionary, field ಹೆಸರುಗಳು keys ಆಗಿ:\n\n" + E.C_RECORDS + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_RECORDS + "\n\n`patients[0]` ಮೊದಲ record; `patients[0][\"sugar\"]` ಅದರ ಒಂದು field. `for` loop ಪ್ರತಿ record ಗೆ ಹೋಗುತ್ತೆ.",
            "callout": {"title": "Structured data", "md": "ಒಂದೇ fields ಇರುವ records ಆಗಿ ಜೋಡಿಸಿದ data, table ತರಹ. Spreadsheets, CSV files ಮತ್ತು hospital registers structured; doctors ನ free-text notes ಅಲ್ಲ."},
        },
        {
            "heading": "Records ಆರಿಸುವುದು",
            "md": "Condition ಗೆ ಹೊಂದುವ records ಆರಿಸಲು dataset ಮೇಲೆ loop ಓಡಿಸಿ, ಬೇಕಾದವನ್ನು ಉಳಿಸಿ. 126 mg/dL ಅಥವಾ ಅದಕ್ಕಿಂತ ಹೆಚ್ಚಿನ fasting blood sugar diabetes ಸೂಚಿಸುತ್ತೆ:\n\n" + E.C_SELECT + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_SELECT + "\n\nExcel ನ filter ಇದನ್ನೇ ಮಾಡುತ್ತೆ, Unit IV ನಲ್ಲಿ Pandas ಇದನ್ನು ಒಂದೇ line ನಲ್ಲಿ ಮಾಡುತ್ತೆ.",
        },
        {
            "heading": "Group ಪ್ರಕಾರ ಸಾರಾಂಶ",
            "md": "ಸಾಮಾನ್ಯವಾಗಿ groups ಹೋಲಿಸಬೇಕಾಗುತ್ತೆ: ಗಂಡಸರು ಮತ್ತು ಹೆಂಗಸರು, wards, age groups. Lesson 3.3 ನ ಎಣಿಕೆಯ pattern ಅನ್ನು ಎರಡು ಸಲ ಬಳಸಿ, ಒಮ್ಮೆ totals ಗೆ, ಒಮ್ಮೆ counts ಗೆ:\n\n" + E.C_GROUP + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_GROUP + "\n\nಇಬ್ಬರು ಹೆಂಗಸರ readings average (118 + 165) / 2 = 141.5. ಮೂರು patients ಇದ್ದಾಗ ಕೈಯಲ್ಲೇ ಸುಲಭ; ಮೂರು ಸಾವಿರ ಇದ್ದರೂ ಇದೇ ಏಳು lines ಕೆಲಸ ಮಾಡುತ್ತವೆ.",
        },
        {
            "heading": "Missing ಮತ್ತು ಅಸಾಧ್ಯ values",
            "md": "ನಿಜವಾದ datasets ಯಾವತ್ತೂ perfect ಅಲ್ಲ. ಒಂದು field **missing** ಇರಬಹುದು (Python `None` ಬಳಸುತ್ತೆ, Excel ಖಾಲಿ ತೋರಿಸುತ್ತೆ) ಅಥವಾ **ಅಸಾಧ್ಯ**, 54 ಆಗಬೇಕಿದ್ದ 540 age ತರಹ. ಲೆಕ್ಕ ಹಾಕುವ ಮುಂಚೆ check ಮಾಡಿ:\n\n" + E.C_CLEAN + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_CLEAN + "\n\n`is None` missing value ಪರೀಕ್ಷಿಸುತ್ತೆ. `0 < age < 120` ಒಂದೇ ಸಲ range check ಮಾಡುತ್ತೆ. ಈ ಸಮಸ್ಯೆಗಳನ್ನು ಹುಡುಕುವುದನ್ನು **data cleaning** ಅಂತಾರೆ, ಹೆಚ್ಚಿನ ನಿಜ projects ನಲ್ಲಿ ಇದಕ್ಕೆ analysis ಗಿಂತ ಹೆಚ್ಚು ಸಮಯ ಬೇಕಾಗುತ್ತೆ.",
            "callout": {"title": "Missing value ಅನ್ನು ಯಾವತ್ತೂ ಊಹಿಸಬೇಡಿ", "md": "Missing age ಅಥವಾ dose ಬದಲು ಸುಮ್ಮನೆ 0 ಹಾಕಬೇಡಿ: average ತಪ್ಪಾಗುತ್ತೆ. Flag ಮಾಡಿ, source ಕೇಳಿ, ಅಥವಾ record ಬಿಟ್ಟು report ನಲ್ಲಿ ತಿಳಿಸಿ."},
        },
        {
            "heading": "Privacy: patient ಗುರುತು ತೆಗೆಯಿರಿ",
            "md": "ಹೆಸರು, phone numbers, ವಿಳಾಸ ಮತ್ತು Aadhaar numbers patient ಅನ್ನು **ಗುರುತಿಸುತ್ತವೆ**. ಭಾರತದ **Digital Personal Data Protection Act, 2023** ಪ್ರಕಾರ health data ಸುರಕ್ಷಿತವಾಗಿಡಬೇಕು. Analysis ಮುಂಚೆ ಬೇಕಾದ fields ಮಾತ್ರ ಇಡಿ, ಹೆಸರಿನ ಬದಲು `P01` ತರಹದ code ಬಳಸಿ:\n\n" + E.C_ANON + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_ANON + "\n\nAnalysis ಇನ್ನೂ ಕೆಲಸ ಮಾಡುತ್ತೆ, file ಓದುವ ಯಾರಿಗೂ patient ಯಾರು ಅಂತ ಗೊತ್ತಾಗಲ್ಲ. ಇದನ್ನು **de-identification** (ಅಥವಾ anonymisation) ಅಂತಾರೆ.",
            "callout": {"title": "Data dictionary ಇಡಿ", "md": "Data dictionary ಪ್ರತಿ field ನ list: ಅದರ ಹೆಸರು, type, unit ಮತ್ತು allowed values (age: int, years, 0 ಇಂದ 120). ಹಲವರು data ತುಂಬುವಾಗ ಇದು dataset ಅನ್ನು ಏಕರೂಪವಾಗಿಡುತ್ತೆ."},
        },
    ],
    "walkthrough": {
        "intro": "ಈ program ಮೂರು adverse drug reaction (ADR) reports ಓದಿ, ಪ್ರತಿ drug ನ reports ಎಣಿಸಿ, serious ಆದವನ್ನು ಎಣಿಸುತ್ತೆ.",
        "keyTerms": [
            {"meaning": "ಒಂದು dataset: ಪ್ರತಿ record ಗೆ ಒಂದು dictionary ಇರುವ list."},
            {"meaning": "ಈಗಿನ record ನ ಒಂದು field."},
            {"meaning": "ಪ್ರತಿ drug ನ records ಎಣಿಸು."},
            {"meaning": "serious True ಇರುವ records ಗೆ ಮಾತ್ರ ಓಡುತ್ತೆ."},
        ],
    },
    "errors": {
        "intro": "ಎರಡೂ errors program ನಿರೀಕ್ಷಿಸಿದಂತೆ ಕಾಣದ records ಇಂದ ಬರುತ್ತವೆ.",
        "examples": [
            {"title": "Field ಹೆಸರು ಬೇರೆ spelling ನಲ್ಲಿ", "md": "Field `\"sugar\"`, ಸಣ್ಣ s ಜೊತೆ. Field ಹೆಸರುಗಳು ನಿಖರವಾಗಿ ಹೊಂದಬೇಕು. ಪ್ರತಿ field ನ spelling ನಿಗದಿ ಮಾಡುವ data dictionary, ಹಲವರು data ತುಂಬುವಾಗ ಇದನ್ನು ತಡೆಯುತ್ತೆ."},
            {"title": "Missing value ಹೋಲಿಸುವುದು", "md": "P05 ಗೆ age ಇಲ್ಲ, ಹಾಗಾಗಿ None 40 ಕ್ಕಿಂತ ಕಡಿಮೆಯಾ ಅಂತ Python ಕೇಳುತ್ತೆ, ಅದಕ್ಕೆ ಅರ್ಥ ಇಲ್ಲ. ಮೊದಲು missing values check ಮಾಡಿ: `if r[\"age\"] is not None and r[\"age\"] < 40:`."},
        ],
    },
    "mistakes": [
        {"mistake": "ಕೆಲವು records ನಲ್ಲಿ field ಬೇರೆ spelling: `\"Age\"` ಮತ್ತು `\"age\"`", "see": "ಕೆಲವು records ಗೆ KeyError", "fix": "Data dictionary ನಲ್ಲಿ field ಹೆಸರುಗಳನ್ನು ನಿಗದಿ ಮಾಡಿ, ಎಲ್ಲೆಡೆ ಅವನ್ನೇ ಬಳಸಿ."},
        {"mistake": "Units ಬೆರೆಸುವುದು: ಕೆಲವು doses mg ನಲ್ಲಿ, ಕೆಲವು g ನಲ್ಲಿ", "see": "Error ಇಲ್ಲ, ಆದರೆ averages ಮತ್ತು totals ತಪ್ಪು", "fix": "ಪ್ರತಿ value ಒಂದೇ unit ನಲ್ಲಿ ಇಡಿ; data ತುಂಬುವಾಗ convert ಮಾಡಿ."},
        {"mistake": "ಖಾಲಿ ಅಥವಾ \"NA\" value convert ಮಾಡುವುದು: `int(\"NA\")`", "see": "ValueError: invalid literal for int() with base 10: 'NA'", "fix": "Convert ಮಾಡುವ ಮುಂಚೆ missing values check ಮಾಡಿ."},
        {"mistake": "Analysis files ನಲ್ಲಿ ಹೆಸರು ಮತ್ತು phone numbers ಇಡುವುದು", "see": "Error ಇಲ್ಲ, ಆದರೆ file share ಆದರೆ privacy ಉಲ್ಲಂಘನೆ", "fix": "Identifiers ತೆಗೆದು P01 ತರಹದ patient codes ಬಳಸಿ."},
    ],
    "tasks": [
        {"title": "ಪ್ರತಿ record ತೋರಿಸಿ", "md": "**patients** ಮೇಲೆ loop ಓಡಿಸಿ, ಪ್ರತಿ patient ನ id ಮತ್ತು sugar reading print ಮಾಡಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["for p in patients: ಪ್ರತಿ record ಗೆ ಹೋಗುತ್ತೆ.", "for p in patients:\n    print(p[\"id\"], p[\"sugar\"])"]},
        {"title": "ಹೆಂಗಸರನ್ನು ಎಣಿಸಿ", "md": "ಎಷ್ಟು records ನಲ್ಲಿ sex **\"F\"** ಇದೆ ಅಂತ ಎಣಿಸಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["Records ಮೇಲೆ loop ಓಡಿಸಿ p[\"sex\"] == \"F\" test ಮಾಡಿ.", "for p in patients:\n    if p[\"sex\"] == \"F\":\n        count += 1"]},
        {"title": "Average age", "md": "ಪ್ರತಿ record ನ **age** field ಕೂಡಿಸಿ average age print ಮಾಡಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["Loop ಒಳಗೆ total += p[\"age\"].", "print(\"Average age:\", total / len(patients))"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "ಈ program 60 ಕ್ಕಿಂತ ಹೆಚ್ಚಿನ patients ತೋರಿಸಬೇಕು, ಆದರೆ age missing ಇರುವ P05 ಹತ್ತಿರ crash ಆಗುತ್ತೆ. Missing ages ಬಿಟ್ಟುಹೋಗುವಂತೆ condition ಸರಿ ಮಾಡಿ, output ನಿಖರವಾಗಿ ಹೀಗಿರಲಿ:",
         "hints": ["None ಅನ್ನು number ಜೊತೆ ಹೋಲಿಸಲು ಆಗಲ್ಲ. ಮೊದಲು ಅದನ್ನು check ಮಾಡಿ.", "if r[\"age\"] is not None and r[\"age\"] > 60:"],
         "solutionNote": "and ಮೊದಲು ಎಡಭಾಗ check ಮಾಡುತ್ತೆ: P05 ಗೆ r[\"age\"] is not None False, ಹಾಗಾಗಿ Python None > 60 ಪ್ರಯತ್ನಿಸುವುದೇ ಇಲ್ಲ."},
    ],
    "quiz": [
        {"q": "Dataset table ನಲ್ಲಿ ಒಂದು row ಏನು?", "why": "ಪ್ರತಿ row ಒಂದು record: ಒಬ್ಬ patient, visit ಅಥವಾ report."},
        {"q": "Dataset table ನಲ್ಲಿ ಒಂದು column ಏನು?", "why": "ಪ್ರತಿ column ಒಂದು field, age ಅಥವಾ sugar ತರಹ."},
        {"q": "Patient records dataset ಇಡಲು ಉತ್ತಮ Python structure ಯಾವುದು?", "why": "ಪ್ರತಿ record ಗೆ ಒಂದು dictionary, ಎಲ್ಲವೂ ಒಂದು list ಒಳಗೆ."},
        {"q": "ಒಂದು field missing (None) ಇದೆಯಾ ಅಂತ ಹೇಗೆ check ಮಾಡುತ್ತೀರಿ?", "why": "is None Python ನ missing value check ಮಾಡುತ್ತೆ."},
        {"q": "ಇವುಗಳಲ್ಲಿ ಯಾವುದು patient ಅನ್ನು ನೇರವಾಗಿ ಗುರುತಿಸುತ್ತೆ?", "why": "Phone number ಒಬ್ಬ ವ್ಯಕ್ತಿಯನ್ನು ಸೂಚಿಸುತ್ತೆ; analysis ಮುಂಚೆ ತೆಗೆಯಿರಿ."},
        {"q": "Data dictionary ಯಾಕೆ?", "why": "Data ತುಂಬುವ ಎಲ್ಲರನ್ನೂ ಏಕರೂಪವಾಗಿಡುತ್ತೆ."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 3.6 · Healthcare datasets",
        "children": [
            {"label": "Dataset", "children": [{"label": "Records ನ table"}, {"label": "Row = record"}, {"label": "Column = field"}]},
            {"label": "Python ನಲ್ಲಿ", "children": [{"label": "List of dicts"}, {"label": "records[0][\"age\"]"}, {"label": "for r in records"}]},
            {"label": "ಆರಿಸು ಮತ್ತು group", "children": [{"label": "if condition → append"}, {"label": "get() ಇಂದ ಎಣಿಕೆ"}, {"label": "ಪ್ರತಿ group average"}]},
            {"label": "Data quality", "children": [{"label": "Missing: None"}, {"label": "Range ಹೊರಗಿನ values"}, {"label": "ಒಂದೇ units ಮತ್ತು ಹೆಸರು"}]},
            {"label": "Privacy", "children": [{"label": "ಹೆಸರು, phone ತೆಗೆ"}, {"label": "Patient IDs ಬಳಸು"}, {"label": "DPDP Act 2023"}]},
            {"label": "Errors", "children": [{"label": "KeyError: field name"}, {"label": "TypeError: None compare"}]},
        ],
    },
    "summary": [
        "**Structured data** ಒಂದು table: ಪ್ರತಿ **row** ಒಂದು **record**, ಪ್ರತಿ **column** ಒಂದು **field**.",
        "Python ನಲ್ಲಿ dataset ಒಂದು **list of dictionaries**: `patients[0][\"sugar\"]` ಒಂದು record ನ ಒಂದು field.",
        "Loop ಮತ್ತು `if` ಇಂದ records ಆರಿಸಿ; `get()` ಇಂದ totals ಮತ್ತು counts ಮಾಡಿ **group** ಪ್ರಕಾರ ಸಾರಾಂಶ ತೆಗೆಯಿರಿ.",
        "ಲೆಕ್ಕದ ಮುಂಚೆ **missing** (`is None`) ಮತ್ತು **ಅಸಾಧ್ಯ** values check ಮಾಡಿ; missing value ಅನ್ನು ಯಾವತ್ತೂ ಊಹಿಸಬೇಡಿ.",
        "Privacy ಕಾಪಾಡಿ: **identifiers** (ಹೆಸರು, phone, Aadhaar) ತೆಗೆದು `P01` ತರಹದ codes ಬಳಸಿ, DPDP Act 2023 ಹೇಳುವಂತೆ.",
    ],
}

NARR = {
    "hi": [
        "यह program adverse drug reaction reports का सार निकालता है, वैसी reports जो pharmacists राष्ट्रीय pharmacovigilance programme को भेजते हैं।",
        "Comment बताता है कि data क्या है: A D R reports।",
        "reports dictionaries की list है। हर dictionary एक record है, वही तीन fields के साथ: drug, reaction और serious।",
        "by_drug हर drug की reports गिनेगा। यह खाली शुरू होता है।",
        "serious, serious reactions गिनेगा। यह zero से शुरू होता है।",
        "Loop एक बार में एक record लेता है। पहला है Amoxicillin, rash के साथ।",
        "यह गिनती का pattern है। Amoxicillin नया है, इसलिए get zero देता है, और उसकी गिनती एक हो जाती है।",
        "Rash serious नहीं है, इसलिए serious गिनती zero पर रहती है।",
        "दूसरा record Ibuprofen है। उसकी गिनती एक होती है।",
        "तीसरा फिर Amoxicillin है, अब दो। और anaphylaxis serious है, इसलिए serious एक हो जाता है।",
        "print हर drug की reports की संख्या दिखाता है।",
        "और एक serious reaction, जिसे असली practice में जल्दी report करना ज़रूरी है।",
    ],
    "hinglish": [
        "Yeh program adverse drug reaction reports ka saar nikaalta hai, waisi reports jo pharmacists rashtriya pharmacovigilance programme ko bhejte hain.",
        "Comment batata hai ki data kya hai: A D R reports.",
        "reports dictionaries ki list hai. Har dictionary ek record hai, wahi teen fields ke saath: drug, reaction aur serious.",
        "by_drug har drug ki reports ginega. Yeh khaali shuru hota hai.",
        "serious, serious reactions ginega. Yeh zero se shuru hota hai.",
        "Loop ek baar mein ek record leta hai. Pehla hai Amoxicillin, rash ke saath.",
        "Yeh ginti ka pattern hai. Amoxicillin naya hai, isliye get zero deta hai, aur uski ginti ek ho jaati hai.",
        "Rash serious nahi hai, isliye serious ginti zero par rehti hai.",
        "Doosra record Ibuprofen hai. Uski ginti ek hoti hai.",
        "Teesra phir Amoxicillin hai, ab do. Aur anaphylaxis serious hai, isliye serious ek ho jaata hai.",
        "print har drug ki reports ki sankhya dikhaata hai.",
        "Aur ek serious reaction, jise asli practice mein jaldi report karna zaroori hai.",
    ],
    "kn": [
        "ಈ program adverse drug reaction reports ನ ಸಾರಾಂಶ ಮಾಡುತ್ತೆ, pharmacists ರಾಷ್ಟ್ರೀಯ pharmacovigilance programme ಗೆ ಕಳಿಸುವ ತರಹದ reports.",
        "Comment data ಏನು ಅಂತ ಹೇಳುತ್ತೆ: A D R reports.",
        "reports dictionaries ನ list. ಪ್ರತಿ dictionary ಒಂದು record, ಅದೇ ಮೂರು fields ಜೊತೆ: drug, reaction ಮತ್ತು serious.",
        "by_drug ಪ್ರತಿ drug ನ reports ಎಣಿಸುತ್ತೆ. ಇದು ಖಾಲಿಯಾಗಿ ಶುರು.",
        "serious, serious reactions ಎಣಿಸುತ್ತೆ. ಇದು zero ಇಂದ ಶುರು.",
        "Loop ಒಂದು ಸಲಕ್ಕೆ ಒಂದು record ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ. ಮೊದಲದು Amoxicillin, rash ಜೊತೆ.",
        "ಇದು ಎಣಿಕೆಯ pattern. Amoxicillin ಹೊಸದು, ಹಾಗಾಗಿ get zero ಕೊಡುತ್ತೆ, ಅದರ ಎಣಿಕೆ ಒಂದು ಆಗುತ್ತೆ.",
        "Rash serious ಅಲ್ಲ, ಹಾಗಾಗಿ serious ಎಣಿಕೆ zero ನಲ್ಲೇ ಇರುತ್ತೆ.",
        "ಎರಡನೇ record Ibuprofen. ಅದರ ಎಣಿಕೆ ಒಂದು ಆಗುತ್ತೆ.",
        "ಮೂರನೇದು ಮತ್ತೆ Amoxicillin, ಈಗ ಎರಡು. Anaphylaxis serious, ಹಾಗಾಗಿ serious ಒಂದು ಆಗುತ್ತೆ.",
        "print ಪ್ರತಿ drug ನ reports ಸಂಖ್ಯೆ ತೋರಿಸುತ್ತೆ.",
        "ಮತ್ತು ಒಂದು serious reaction, ನಿಜ practice ನಲ್ಲಿ ಇದನ್ನು ಬೇಗ report ಮಾಡಬೇಕು.",
    ],
}

ANIM = {
    "hi": [
        "Structured dataset एक table है। हर row एक report है, और हर column एक field।",
        "पहली report Amoxicillin की है। उसकी गिनती एक हो जाती है।",
        "दूसरी Ibuprofen की है, इसलिए Ibuprofen की गिनती एक हो जाती है।",
        "तीसरी फिर Amoxicillin की है, और serious है: anaphylaxis। Amoxicillin दो पर जाता है, और serious एक पर।",
        "तीन rows, एक बार में। यही loop तीस हज़ार reports का सार निकाल देगा।",
    ],
    "hinglish": [
        "Structured dataset ek table hai. Har row ek report hai, aur har column ek field.",
        "Pehli report Amoxicillin ki hai. Uski ginti ek ho jaati hai.",
        "Doosri Ibuprofen ki hai, isliye Ibuprofen ki ginti ek ho jaati hai.",
        "Teesri phir Amoxicillin ki hai, aur serious hai: anaphylaxis. Amoxicillin do par jaata hai, aur serious ek par.",
        "Teen rows, ek baar mein. Yahi loop tees hazaar reports ka saar nikaal dega.",
    ],
    "kn": [
        "Structured dataset ಒಂದು table. ಪ್ರತಿ row ಒಂದು report, ಪ್ರತಿ column ಒಂದು field.",
        "ಮೊದಲ report Amoxicillin ದು. ಅದರ ಎಣಿಕೆ ಒಂದು ಆಗುತ್ತೆ.",
        "ಎರಡನೇದು Ibuprofen ದು, ಹಾಗಾಗಿ Ibuprofen ಎಣಿಕೆ ಒಂದು ಆಗುತ್ತೆ.",
        "ಮೂರನೇದು ಮತ್ತೆ Amoxicillin, ಮತ್ತು serious: anaphylaxis. Amoxicillin ಎರಡಕ್ಕೆ, serious ಒಂದಕ್ಕೆ ಹೋಗುತ್ತೆ.",
        "ಮೂರು rows, ಒಂದೇ ಸುತ್ತು. ಇದೇ loop ಮೂವತ್ತು ಸಾವಿರ reports ನ ಸಾರಾಂಶ ಮಾಡುತ್ತೆ.",
    ],
}

if __name__ == "__main__":
    build("3-6", "anim-table", T, NARR, ANIM, say_en=lambda t: t.replace("by_drug", "by drug"))

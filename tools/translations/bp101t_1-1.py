"""Full translations of Lesson 1.1 (everything except code, error output and exam answers).

Run `python3 tools/translations/bp101t_1-1.py` to merge these into
content/bp101t/1-1/{hi,hinglish,kn}.json, keeping the existing narrator and animation captions.
Arrays merge by position on the website, so every list keeps the English order.
"""
import json
import os

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")

T = {}

# ---------------------------------------------------------------- Hindi (Devanagari)
T["hi"] = {
    "hook": {
        "title": "आपका पहला program, सिर्फ 10 मिनट में",
        "md": "इस lesson के अंत तक आप अपना **पहला Python program** लिखेंगे और चलाएँगे: एक छोटा सा medicine label, जो दवा का नाम, उसकी strength और पूरे दिन की dose print करता है।\n\nकोई installation नहीं। Coding का कोई background नहीं चाहिए। बस आपका phone।",
    },
    "learn": [
        "**Program** और **programming language** क्या होते हैं",
        "Pharmacy students **Python** ही क्यों सीख रहे हैं",
        "Python एक **program कैसे चलाता है**, line by line, ऊपर से नीचे तक",
    ],
    "explanation": [
        {
            "heading": "Program क्या है?",
            "md": "एक **prescription** के बारे में सोचिए। यह साफ़ निर्देशों की एक list है, जो क्रम से लिखी होती है:",
            "quote": "Paracetamol 500 mg की 1 tablet, दिन में तीन बार, खाने के बाद लें।",
            "mdAfter": "Patient इन निर्देशों को step by step follow करता है।\n\nएक **program** भी बिल्कुल यही है, बस computer के लिए। यह निर्देशों की एक list है, जो क्रम से लिखी होती है, और computer इन्हें बिल्कुल वैसे ही follow करता है।",
        },
        {
            "heading": "Programming language क्या है?",
            "md": "Computer English नहीं समझता। **Programming language** एक खास भाषा है, जिसे इंसान और computer दोनों समझ सकते हैं। हम इसमें निर्देश लिखते हैं, और computer उन्हें पूरा करता है।\n\nकई programming languages हैं: C, Java, JavaScript, और **Python**।",
        },
        {
            "heading": "Python ही क्यों?",
            "md": "Python को **Guido van Rossum** ने बनाया था और यह पहली बार **1991** में release हुई। आज यह दुनिया की सबसे popular languages में से एक है, और आपके syllabus के लिए इसे इसलिए चुना गया क्योंकि:\n\n- **यह लगभग English जैसी पढ़ी जाती है**, इसलिए beginners के लिए आसान है।\n- **यह सबके लिए free है।**\n- **इसमें data, graphs और science के लिए ready-made toolkits (libraries) हैं।**\n- **Pharmacy और healthcare में इसका बहुत use होता है**: clinical trial data analyse करना, drug concentration curves बनाना, adverse drug reaction (ADR) reports study करना, और computer पर नई दवाएँ design करना।",
        },
        {
            "heading": "Python एक program कैसे चलाता है?",
            "md": "सोचिए, एक pharmacist prescription पढ़ रहा है। वह **पहली line, फिर अगली, फिर अगली** पढ़ता है, क्रम से, और हर line पर काम करता है।\n\nPython भी ऐसे ही काम करता है। **Interpreter** नाम का एक खास program आपका code पढ़ता है और उसे **एक बार में एक line, ऊपर से नीचे तक** चलाता है।",
            "callout": {
                "title": "Interpreter",
                "md": "Python का वह हिस्सा जो आपका code पढ़ता है और हर instruction को पूरा करता है।",
            },
        },
    ],
    "walkthrough": {
        "intro": "यह रहा आपका पहला program। Python इसे line by line चलाएगा।",
        "keyTerms": [
            {"meaning": "इंसानों के लिए एक note; Python इसे ignore करता है।"},
            {"meaning": "Text या numbers को screen पर दिखाता है।"},
            {"meaning": "Quotes के अंदर का text, बिल्कुल वैसा ही दिखाया जाता है जैसा लिखा है।"},
            {"meaning": "गुणा (multiply)।"},
        ],
    },
    "errors": {
        "intro": "गलतियाँ होना normal है। Python आपको साफ़ बताता है कि वह कहाँ अटका।",
        "examples": [
            {
                "title": "Python उस line पर रुक जाता है जो उसे समझ नहीं आती",
                "md": "Python ने line 1 सही से चला दी। Line 2 पर उसे `weight` शब्द मिला, लेकिन किसी ने Python को नहीं बताया था कि `weight` का मतलब क्या है। इसलिए वह रुक गया, बिल्कुल उस pharmacist की तरह जो prescription की किसी अस्पष्ट line पर रुक जाता है। Line 3 कभी चली ही नहीं।",
            },
            {
                "title": "एक missing bracket सब कुछ रोक देता है",
                "md": "यहाँ **कुछ भी** print नहीं होता, Line 1 भी नहीं। कुछ भी चलाने से पहले Python जल्दी से check करता है कि पूरा program सही लिखा है या नहीं। Missing bracket एक लिखने की गलती है (**syntax error**), इसलिए Python शुरू ही नहीं करता।",
                "callout": {"title": "Syntax", "md": "किसी programming language के grammar के नियम।"},
            },
        ],
    },
    "mistakes": [
        {"mistake": "`Print` को capital P से लिखना", "fix": "Python case-sensitive है। `print` हमेशा small letters में लिखें।"},
        {"mistake": "WhatsApp या Word से code copy करना, जिसमें टेढ़े quotes “ ” होते हैं", "fix": "सीधे quotes \" \" use करें। Editor में quotes खुद type करें।"},
        {"mistake": "Line की शुरुआत में spaces डाल देना", "fix": "अभी के लिए, हर line बिल्कुल बाईं तरफ से शुरू करें।"},
        {"mistake": "Text के चारों ओर quotes भूल जाना, जैसे `print(Paracetamol)`", "fix": "Text को quotes के अंदर रखें: `print(\"Paracetamol\")`।"},
    ],
    "tasks": [
        {"title": "Hello बोलिए", "md": "एक program लिखिए जो बिल्कुल यही print करे:", "hints": ["print() use करें, और sentence को quotes के अंदर रखें।"]},
        {
            "title": "एक medicine label बनाइए",
            "md": "एक program लिखिए जो यह label print करे। Daily dose (250 × 4) Python से **calculate** करवाइए; 1000 खुद type मत कीजिए।",
            "hints": ["हर line के लिए एक print() use करें।", "Strength वाली line के लिए try करें: print(\"Strength  :\", 250, \"mg\")।"],
        },
        {
            "title": "Bug ढूँढिए",
            "md": "इस program में एक गलती है। इसे ठीक कीजिए ताकि यह `Drug: Amoxicillin` print करे।",
            "hints": ["Python case-sensitive है।"],
            "solutionNote": "`print` small letters में होना चाहिए।",
        },
    ],
    "quiz": [
        {"q": "Python किसने बनाया?", "why": "Python को Guido van Rossum ने बनाया; यह पहली बार 1991 में release हुई।"},
        {
            "q": "Python किसी program की lines को किस क्रम में चलाता है?",
            "options": ["Randomly", "नीचे से ऊपर", "ऊपर से नीचे, एक बार में एक line", "सिर्फ आखिरी line"],
            "why": "Interpreter code को ऊपर से नीचे, एक बार में एक line चलाता है।",
        },
        {"q": "कौन सी line screen पर Hello सही से दिखाती है?", "why": "print small letters में होना चाहिए, और text quotes के अंदर होना चाहिए।"},
        {"q": "जो line # से शुरू होती है, वह है:", "options": ["Error", "Comment, जिसे Python ignore करता है", "Heading", "Library"], "why": "Comments इंसानों के लिए notes हैं; Python इन्हें छोड़ देता है।"},
        {
            "q": "print(\"Dose:\", 2 * 250, \"mg\") का output क्या है?",
            "options": ["Dose: 2 * 250 mg", "Dose: 500 mg", "Dose:500mg", "Error आएगा"],
            "why": "Python पहले 2 × 250 = 500 calculate करता है, और print हर item के बीच space लगाता है।",
        },
    ],
    "exam": {"note": "University exam English में लिखा जाता है, इसलिए model answers English में ही रखे गए हैं। ये practice के लिए important questions हैं; असली university questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 1.1 · Python basics",
        "children": [
            {"label": "Program", "children": [{"label": "निर्देशों की list"}, {"label": "क्रम से follow होती है"}, {"label": "Prescription जैसा"}]},
            {"label": "Programming language", "children": [{"label": "इंसान और computer दोनों समझें"}, {"label": "जैसे: C, Java, Python"}]},
            {"label": "Python क्यों", "children": [{"label": "English जैसी पढ़ी जाती है"}, {"label": "Free"}, {"label": "Data और graphs के लिए libraries"}, {"label": "Pharmacy में use", "children": [{"label": "Clinical trial data"}, {"label": "PK curves"}, {"label": "ADR reports"}, {"label": "Drug design"}]}]},
            {"label": "कैसे चलता है", "children": [{"label": "Interpreter"}, {"label": "एक बार में एक line"}, {"label": "ऊपर से नीचे"}]},
            {"label": "पहला code", "children": [{"label": "print() output दिखाता है"}, {"label": "# से comment शुरू"}, {"label": "Quotes में text = string"}, {"label": "* मतलब गुणा"}]},
            {"label": "Errors", "children": [{"label": "NameError: अनजान शब्द", "children": [{"label": "उसी line पर रुकता है"}]}, {"label": "SyntaxError: लिखने की गलती", "children": [{"label": "कुछ भी नहीं चलता"}]}]},
        ],
    },
    "summary": [
        "**Program** निर्देशों की एक list है, जिसे computer क्रम से follow करता है, बिल्कुल prescription की तरह।",
        "**Python** एक free और पढ़ने में आसान programming language है, जिसका pharmacy और healthcare में बहुत use होता है।",
        "**Interpreter** Python code को **एक बार में एक line, ऊपर से नीचे तक** चलाता है।",
        "**print()** text और numbers को screen पर दिखाता है; **#** से comment शुरू होता है।",
        "**Errors** साफ़ बताते हैं कि Python कहाँ अटका। Syntax error हो तो program शुरू ही नहीं होता।",
    ],
}

# ---------------------------------------------------------------- Hinglish (Roman)
T["hinglish"] = {
    "hook": {
        "title": "Aapka pehla program, sirf 10 minute mein",
        "md": "Is lesson ke end tak aap apna **pehla Python program** likhenge aur chalayenge: ek chhota sa medicine label, jo dawa ka naam, uski strength aur poore din ki dose print karta hai.\n\nKoi installation nahi. Coding ka koi background nahi chahiye. Bas aapka phone.",
    },
    "learn": [
        "**Program** aur **programming language** kya hote hain",
        "Pharmacy students **Python** hi kyun seekh rahe hain",
        "Python ek **program kaise chalata hai**, line by line, upar se neeche tak",
    ],
    "explanation": [
        {
            "heading": "Program kya hai?",
            "md": "Ek **prescription** ke baare mein sochiye. Yeh saaf nirdeshon ki ek list hai, jo kram se likhi hoti hai:",
            "quote": "Paracetamol 500 mg ki 1 tablet, din mein teen baar, khaane ke baad lein.",
            "mdAfter": "Patient in nirdeshon ko step by step follow karta hai.\n\nEk **program** bhi bilkul yahi hai, bas computer ke liye. Yeh nirdeshon ki ek list hai, jo kram se likhi hoti hai, aur computer inhe bilkul waise hi follow karta hai.",
        },
        {
            "heading": "Programming language kya hai?",
            "md": "Computer English nahi samajhta. **Programming language** ek khaas bhasha hai, jise insaan aur computer dono samajh sakte hain. Hum isme nirdesh likhte hain, aur computer unhe poora karta hai.\n\nKai programming languages hain: C, Java, JavaScript, aur **Python**.",
        },
        {
            "heading": "Python hi kyun?",
            "md": "Python ko **Guido van Rossum** ne banaya tha aur yeh pehli baar **1991** mein release hui. Aaj yeh duniya ki sabse popular languages mein se ek hai, aur aapke syllabus ke liye ise isliye chuna gaya kyunki:\n\n- **Yeh lagbhag English jaisi padhi jaati hai**, isliye beginners ke liye aasaan hai.\n- **Yeh sabke liye free hai.**\n- **Isme data, graphs aur science ke liye ready-made toolkits (libraries) hain.**\n- **Pharmacy aur healthcare mein iska bahut use hota hai**: clinical trial data analyse karna, drug concentration curves banana, adverse drug reaction (ADR) reports study karna, aur computer par nayi dawaiyan design karna.",
        },
        {
            "heading": "Python ek program kaise chalata hai?",
            "md": "Sochiye, ek pharmacist prescription padh raha hai. Woh **pehli line, phir agli, phir agli** padhta hai, kram se, aur har line par kaam karta hai.\n\nPython bhi aise hi kaam karta hai. **Interpreter** naam ka ek khaas program aapka code padhta hai aur use **ek baar mein ek line, upar se neeche tak** chalata hai.",
            "callout": {"title": "Interpreter", "md": "Python ka woh hissa jo aapka code padhta hai aur har instruction ko poora karta hai."},
        },
    ],
    "walkthrough": {
        "intro": "Yeh raha aapka pehla program. Python ise line by line chalayega.",
        "keyTerms": [
            {"meaning": "Insaanon ke liye ek note; Python ise ignore karta hai."},
            {"meaning": "Text ya numbers ko screen par dikhata hai."},
            {"meaning": "Quotes ke andar ka text, bilkul waisa hi dikhaya jaata hai jaisa likha hai."},
            {"meaning": "Guna (multiply)."},
        ],
    },
    "errors": {
        "intro": "Galtiyan hona normal hai. Python aapko saaf batata hai ki woh kahan atka.",
        "examples": [
            {
                "title": "Python us line par ruk jaata hai jo use samajh nahi aati",
                "md": "Python ne line 1 sahi se chala di. Line 2 par use `weight` shabd mila, lekin kisi ne Python ko nahi bataya tha ki `weight` ka matlab kya hai. Isliye woh ruk gaya, bilkul us pharmacist ki tarah jo prescription ki kisi unclear line par ruk jaata hai. Line 3 kabhi chali hi nahi.",
            },
            {
                "title": "Ek missing bracket sab kuch rok deta hai",
                "md": "Yahan **kuch bhi** print nahi hota, Line 1 bhi nahi. Kuch bhi chalane se pehle Python jaldi se check karta hai ki poora program sahi likha hai ya nahi. Missing bracket ek likhne ki galti hai (**syntax error**), isliye Python shuru hi nahi karta.",
                "callout": {"title": "Syntax", "md": "Kisi programming language ke grammar ke niyam."},
            },
        ],
    },
    "mistakes": [
        {"mistake": "`Print` ko capital P se likhna", "fix": "Python case-sensitive hai. `print` hamesha small letters mein likhein."},
        {"mistake": "WhatsApp ya Word se code copy karna, jisme tedhe quotes “ ” hote hain", "fix": "Seedhe quotes \" \" use karein. Editor mein quotes khud type karein."},
        {"mistake": "Line ki shuruaat mein spaces daal dena", "fix": "Abhi ke liye, har line bilkul left side se shuru karein."},
        {"mistake": "Text ke chaaron taraf quotes bhool jaana, jaise `print(Paracetamol)`", "fix": "Text ko quotes ke andar rakhein: `print(\"Paracetamol\")`."},
    ],
    "tasks": [
        {"title": "Hello boliye", "md": "Ek program likhiye jo bilkul yahi print kare:", "hints": ["print() use karein, aur sentence ko quotes ke andar rakhein."]},
        {
            "title": "Ek medicine label banaiye",
            "md": "Ek program likhiye jo yeh label print kare. Daily dose (250 × 4) Python se **calculate** karwaiye; 1000 khud type mat kijiye.",
            "hints": ["Har line ke liye ek print() use karein.", "Strength wali line ke liye try karein: print(\"Strength  :\", 250, \"mg\")."],
        },
        {
            "title": "Bug dhoondhiye",
            "md": "Is program mein ek galti hai. Ise theek kijiye taaki yeh `Drug: Amoxicillin` print kare.",
            "hints": ["Python case-sensitive hai."],
            "solutionNote": "`print` small letters mein hona chahiye.",
        },
    ],
    "quiz": [
        {"q": "Python kisne banaya?", "why": "Python ko Guido van Rossum ne banaya; yeh pehli baar 1991 mein release hui."},
        {
            "q": "Python kisi program ki lines ko kis kram mein chalata hai?",
            "options": ["Randomly", "Neeche se upar", "Upar se neeche, ek baar mein ek line", "Sirf aakhri line"],
            "why": "Interpreter code ko upar se neeche, ek baar mein ek line chalata hai.",
        },
        {"q": "Kaunsi line screen par Hello sahi se dikhati hai?", "why": "print small letters mein hona chahiye, aur text quotes ke andar hona chahiye."},
        {"q": "Jo line # se shuru hoti hai, woh hai:", "options": ["Error", "Comment, jise Python ignore karta hai", "Heading", "Library"], "why": "Comments insaanon ke liye notes hain; Python inhe chhod deta hai."},
        {
            "q": "print(\"Dose:\", 2 * 250, \"mg\") ka output kya hai?",
            "options": ["Dose: 2 * 250 mg", "Dose: 500 mg", "Dose:500mg", "Error aayega"],
            "why": "Python pehle 2 × 250 = 500 calculate karta hai, aur print har item ke beech space lagata hai.",
        },
    ],
    "exam": {"note": "University exam English mein likha jaata hai, isliye model answers English mein hi rakhe gaye hain. Yeh practice ke liye important questions hain; asli university questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 1.1 · Python basics",
        "children": [
            {"label": "Program", "children": [{"label": "Nirdeshon ki list"}, {"label": "Kram se follow hoti hai"}, {"label": "Prescription jaisa"}]},
            {"label": "Programming language", "children": [{"label": "Insaan aur computer dono samjhein"}, {"label": "Jaise: C, Java, Python"}]},
            {"label": "Python kyun", "children": [{"label": "English jaisi padhi jaati hai"}, {"label": "Free"}, {"label": "Data aur graphs ke liye libraries"}, {"label": "Pharmacy mein use", "children": [{"label": "Clinical trial data"}, {"label": "PK curves"}, {"label": "ADR reports"}, {"label": "Drug design"}]}]},
            {"label": "Kaise chalta hai", "children": [{"label": "Interpreter"}, {"label": "Ek baar mein ek line"}, {"label": "Upar se neeche"}]},
            {"label": "Pehla code", "children": [{"label": "print() output dikhata hai"}, {"label": "# se comment shuru"}, {"label": "Quotes mein text = string"}, {"label": "* matlab guna"}]},
            {"label": "Errors", "children": [{"label": "NameError: anjaan shabd", "children": [{"label": "Usi line par rukta hai"}]}, {"label": "SyntaxError: likhne ki galti", "children": [{"label": "Kuch bhi nahi chalta"}]}]},
        ],
    },
    "summary": [
        "**Program** nirdeshon ki ek list hai, jise computer kram se follow karta hai, bilkul prescription ki tarah.",
        "**Python** ek free aur padhne mein aasaan programming language hai, jiska pharmacy aur healthcare mein bahut use hota hai.",
        "**Interpreter** Python code ko **ek baar mein ek line, upar se neeche tak** chalata hai.",
        "**print()** text aur numbers ko screen par dikhata hai; **#** se comment shuru hota hai.",
        "**Errors** saaf batate hain ki Python kahan atka. Syntax error ho to program shuru hi nahi hota.",
    ],
}

# ---------------------------------------------------------------- Kannada
T["kn"] = {
    "hook": {
        "title": "ನಿಮ್ಮ ಮೊದಲ program, ಕೇವಲ 10 ನಿಮಿಷದಲ್ಲಿ",
        "md": "ಈ lesson ಮುಗಿಯುವಷ್ಟರಲ್ಲಿ ನೀವು ನಿಮ್ಮ **ಮೊದಲ Python program** ಬರೆದು run ಮಾಡ್ತೀರಿ: ಔಷಧಿಯ ಹೆಸರು, ಅದರ strength ಮತ್ತು ದಿನದ ಒಟ್ಟು dose ಅನ್ನು print ಮಾಡುವ ಒಂದು ಚಿಕ್ಕ medicine label.\n\nಯಾವುದೇ installation ಬೇಡ. Coding background ಬೇಡ. ನಿಮ್ಮ phone ಸಾಕು.",
    },
    "learn": [
        "**Program** ಮತ್ತು **programming language** ಅಂದ್ರೆ ಏನು",
        "Pharmacy students ಯಾಕೆ **Python** ಕಲಿಯುತ್ತಿದ್ದಾರೆ",
        "Python ಒಂದು **program ಅನ್ನು ಹೇಗೆ run ಮಾಡುತ್ತೆ**, line by line, ಮೇಲಿಂದ ಕೆಳಗೆ",
    ],
    "explanation": [
        {
            "heading": "Program ಅಂದ್ರೆ ಏನು?",
            "md": "ಒಂದು **prescription** ಬಗ್ಗೆ ಯೋಚಿಸಿ. ಅದು ಕ್ರಮವಾಗಿ ಬರೆದ ಸ್ಪಷ್ಟ ಸೂಚನೆಗಳ ಒಂದು list:",
            "quote": "Paracetamol 500 mg ನ 1 tablet ಅನ್ನು, ದಿನಕ್ಕೆ ಮೂರು ಸಲ, ಊಟದ ನಂತರ ತೆಗೆದುಕೊಳ್ಳಿ.",
            "mdAfter": "Patient ಈ ಸೂಚನೆಗಳನ್ನು step by step ಪಾಲಿಸುತ್ತಾರೆ.\n\nಒಂದು **program** ಕೂಡ ಇದೇ idea, ಆದರೆ computer ಗಾಗಿ. ಅದು ಕ್ರಮವಾಗಿ ಬರೆದ ಸೂಚನೆಗಳ list, ಮತ್ತು computer ಅವನ್ನು ಬರೆದ ಹಾಗೆಯೇ ಪಾಲಿಸುತ್ತೆ.",
        },
        {
            "heading": "Programming language ಅಂದ್ರೆ ಏನು?",
            "md": "Computer ಗೆ English ಅರ್ಥ ಆಗಲ್ಲ. **Programming language** ಅಂದ್ರೆ ಮನುಷ್ಯರು ಮತ್ತು computer ಇಬ್ಬರಿಗೂ ಅರ್ಥ ಆಗುವ ಒಂದು ವಿಶೇಷ ಭಾಷೆ. ನಾವು ಅದರಲ್ಲಿ ಸೂಚನೆಗಳನ್ನು ಬರೆಯುತ್ತೇವೆ, computer ಅವನ್ನು ಮಾಡಿ ಮುಗಿಸುತ್ತೆ.\n\nತುಂಬಾ programming languages ಇವೆ: C, Java, JavaScript, ಮತ್ತು **Python**.",
        },
        {
            "heading": "Python ಯಾಕೆ?",
            "md": "Python ಅನ್ನು **Guido van Rossum** ತಯಾರಿಸಿದರು, ಮತ್ತು ಅದು ಮೊದಲ ಸಲ **1991** ರಲ್ಲಿ release ಆಯಿತು. ಇವತ್ತು ಇದು ಪ್ರಪಂಚದ ಅತ್ಯಂತ popular languages ಗಳಲ್ಲಿ ಒಂದು, ಮತ್ತು ನಿಮ್ಮ syllabus ಗೆ ಇದನ್ನೇ ಆಯ್ಕೆ ಮಾಡಿರುವುದಕ್ಕೆ ಕಾರಣ:\n\n- **ಇದು ಹೆಚ್ಚು ಕಡಿಮೆ English ತರಹ ಓದೋಕೆ ಆಗುತ್ತೆ**, ಹಾಗಾಗಿ beginners ಗೆ ಸುಲಭ.\n- **ಇದು ಎಲ್ಲರಿಗೂ free.**\n- **Data, graphs ಮತ್ತು science ಗಾಗಿ ready-made toolkits (libraries) ಇವೆ.**\n- **Pharmacy ಮತ್ತು healthcare ನಲ್ಲಿ ಇದನ್ನು ತುಂಬಾ use ಮಾಡ್ತಾರೆ**: clinical trial data analyse ಮಾಡೋಕೆ, drug concentration curves ಬರೆಯೋಕೆ, adverse drug reaction (ADR) reports study ಮಾಡೋಕೆ, ಮತ್ತು computer ನಲ್ಲಿ ಹೊಸ ಔಷಧಿಗಳನ್ನು design ಮಾಡೋಕೆ.",
        },
        {
            "heading": "Python ಒಂದು program ಅನ್ನು ಹೇಗೆ run ಮಾಡುತ್ತೆ?",
            "md": "ಒಬ್ಬ pharmacist prescription ಓದುತ್ತಿದ್ದಾರೆ ಅಂತ ಕಲ್ಪಿಸಿಕೊಳ್ಳಿ. ಅವರು **ಮೊದಲ line, ಆಮೇಲೆ ಮುಂದಿನದು, ಆಮೇಲೆ ಮುಂದಿನದು** ಕ್ರಮವಾಗಿ ಓದಿ, ಪ್ರತಿ line ಪ್ರಕಾರ ಕೆಲಸ ಮಾಡ್ತಾರೆ.\n\nPython ಕೂಡ ಹೀಗೇ ಕೆಲಸ ಮಾಡುತ್ತೆ. **Interpreter** ಅನ್ನುವ ಒಂದು ವಿಶೇಷ program ನಿಮ್ಮ code ಓದಿ, ಅದನ್ನು **ಒಂದು ಸಲಕ್ಕೆ ಒಂದು line, ಮೇಲಿಂದ ಕೆಳಗೆ** run ಮಾಡುತ್ತೆ.",
            "callout": {"title": "Interpreter", "md": "ನಿಮ್ಮ code ಓದಿ, ಪ್ರತಿ instruction ಅನ್ನು ಮಾಡಿ ಮುಗಿಸುವ Python ನ ಭಾಗ."},
        },
    ],
    "walkthrough": {
        "intro": "ಇಲ್ಲಿದೆ ನಿಮ್ಮ ಮೊದಲ program. Python ಇದನ್ನು line by line run ಮಾಡುತ್ತೆ.",
        "keyTerms": [
            {"meaning": "ಮನುಷ್ಯರಿಗಾಗಿ ಬರೆದ note; Python ಇದನ್ನು ignore ಮಾಡುತ್ತೆ."},
            {"meaning": "Text ಅಥವಾ numbers ಅನ್ನು screen ಮೇಲೆ ತೋರಿಸುತ್ತೆ."},
            {"meaning": "Quotes ಒಳಗಿನ text, ಬರೆದ ಹಾಗೆಯೇ ತೋರಿಸಲಾಗುತ್ತೆ."},
            {"meaning": "ಗುಣಾಕಾರ (multiply)."},
        ],
    },
    "errors": {
        "intro": "ತಪ್ಪುಗಳು ಆಗೋದು normal. Python ಎಲ್ಲಿ ಸಿಕ್ಕಿಹಾಕಿಕೊಂಡಿತು ಅಂತ ಸ್ಪಷ್ಟವಾಗಿ ಹೇಳುತ್ತೆ.",
        "examples": [
            {
                "title": "Python ಗೆ ಅರ್ಥ ಆಗದ line ನಲ್ಲಿ ಅದು ನಿಲ್ಲುತ್ತೆ",
                "md": "Python line 1 ಅನ್ನು ಸರಿಯಾಗಿ run ಮಾಡಿತು. Line 2 ನಲ್ಲಿ ಅದಕ್ಕೆ `weight` ಅನ್ನುವ ಪದ ಸಿಕ್ಕಿತು, ಆದರೆ `weight` ಅಂದ್ರೆ ಏನು ಅಂತ ಯಾರೂ Python ಗೆ ಹೇಳಿರಲಿಲ್ಲ. ಹಾಗಾಗಿ ಅದು ನಿಂತುಬಿಟ್ಟಿತು, prescription ನ ಅಸ್ಪಷ್ಟ line ನಲ್ಲಿ ನಿಲ್ಲುವ pharmacist ತರಹ. Line 3 run ಆಗಲೇ ಇಲ್ಲ.",
            },
            {
                "title": "ಒಂದು missing bracket ಎಲ್ಲವನ್ನೂ ನಿಲ್ಲಿಸುತ್ತೆ",
                "md": "ಇಲ್ಲಿ **ಏನೂ** print ಆಗಲ್ಲ, Line 1 ಕೂಡ ಇಲ್ಲ. ಏನನ್ನಾದರೂ run ಮಾಡುವ ಮೊದಲು, ಇಡೀ program ಸರಿಯಾಗಿ ಬರೆದಿದೆಯಾ ಅಂತ Python ಬೇಗ check ಮಾಡುತ್ತೆ. Missing bracket ಒಂದು ಬರವಣಿಗೆಯ ತಪ್ಪು (**syntax error**), ಹಾಗಾಗಿ Python ಶುರುವೇ ಮಾಡಲ್ಲ.",
                "callout": {"title": "Syntax", "md": "ಒಂದು programming language ನ grammar ನಿಯಮಗಳು."},
            },
        ],
    },
    "mistakes": [
        {"mistake": "`Print` ಅನ್ನು capital P ಇಂದ ಬರೆಯುವುದು", "fix": "Python case-sensitive. `print` ಅನ್ನು ಯಾವಾಗಲೂ small letters ನಲ್ಲಿ ಬರೆಯಿರಿ."},
        {"mistake": "WhatsApp ಅಥವಾ Word ಇಂದ curly quotes “ ” ಇರುವ code copy ಮಾಡುವುದು", "fix": "ನೇರ quotes \" \" use ಮಾಡಿ. Editor ನಲ್ಲಿ quotes ಅನ್ನು ನೀವೇ type ಮಾಡಿ."},
        {"mistake": "Line ನ ಶುರುವಿನಲ್ಲಿ spaces ಹಾಕುವುದು", "fix": "ಸದ್ಯಕ್ಕೆ, ಪ್ರತಿ line ಅನ್ನು ಎಡಭಾಗದ ಅಂಚಿನಿಂದಲೇ ಶುರು ಮಾಡಿ."},
        {"mistake": "Text ಸುತ್ತ quotes ಹಾಕಲು ಮರೆಯುವುದು, ಉದಾ: `print(Paracetamol)`", "fix": "Text ಅನ್ನು quotes ಒಳಗೆ ಹಾಕಿ: `print(\"Paracetamol\")`."},
    ],
    "tasks": [
        {"title": "Hello ಹೇಳಿ", "md": "ಇದನ್ನೇ ನಿಖರವಾಗಿ print ಮಾಡುವ ಒಂದು program ಬರೆಯಿರಿ:", "hints": ["print() use ಮಾಡಿ, sentence ಅನ್ನು quotes ಒಳಗೆ ಹಾಕಿ."]},
        {
            "title": "ಒಂದು medicine label ಮಾಡಿ",
            "md": "ಈ label ಅನ್ನು print ಮಾಡುವ program ಬರೆಯಿರಿ. Daily dose (250 × 4) ಅನ್ನು Python ಇಂದಲೇ **calculate** ಮಾಡಿಸಿ; 1000 ಅನ್ನು ನೀವೇ type ಮಾಡಬೇಡಿ.",
            "hints": ["ಪ್ರತಿ line ಗೆ ಒಂದು print() use ಮಾಡಿ.", "Strength line ಗೆ ಇದನ್ನು try ಮಾಡಿ: print(\"Strength  :\", 250, \"mg\")."],
        },
        {
            "title": "Bug ಹುಡುಕಿ",
            "md": "ಈ program ನಲ್ಲಿ ಒಂದು ತಪ್ಪಿದೆ. ಅದು `Drug: Amoxicillin` ಅಂತ print ಮಾಡುವ ಹಾಗೆ ಸರಿ ಮಾಡಿ.",
            "hints": ["Python case-sensitive."],
            "solutionNote": "`print` small letters ನಲ್ಲಿ ಇರಬೇಕು.",
        },
    ],
    "quiz": [
        {"q": "Python ಅನ್ನು ಯಾರು ತಯಾರಿಸಿದರು?", "why": "Python ಅನ್ನು Guido van Rossum ತಯಾರಿಸಿದರು; ಅದು ಮೊದಲ ಸಲ 1991 ರಲ್ಲಿ release ಆಯಿತು."},
        {
            "q": "Python ಒಂದು program ನ lines ಅನ್ನು ಯಾವ ಕ್ರಮದಲ್ಲಿ run ಮಾಡುತ್ತೆ?",
            "options": ["Random ಆಗಿ", "ಕೆಳಗಿನಿಂದ ಮೇಲೆ", "ಮೇಲಿಂದ ಕೆಳಗೆ, ಒಂದು ಸಲಕ್ಕೆ ಒಂದು line", "ಕೊನೆಯ line ಮಾತ್ರ"],
            "why": "Interpreter code ಅನ್ನು ಮೇಲಿಂದ ಕೆಳಗೆ, ಒಂದು ಸಲಕ್ಕೆ ಒಂದು line run ಮಾಡುತ್ತೆ.",
        },
        {"q": "ಯಾವ line screen ಮೇಲೆ Hello ಅನ್ನು ಸರಿಯಾಗಿ ತೋರಿಸುತ್ತೆ?", "why": "print small letters ನಲ್ಲಿ ಇರಬೇಕು, ಮತ್ತು text quotes ಒಳಗೆ ಇರಬೇಕು."},
        {"q": "# ಇಂದ ಶುರುವಾಗುವ line ಅಂದ್ರೆ:", "options": ["Error", "Comment, ಇದನ್ನು Python ignore ಮಾಡುತ್ತೆ", "Heading", "Library"], "why": "Comments ಮನುಷ್ಯರಿಗಾಗಿ notes; Python ಅವನ್ನು skip ಮಾಡುತ್ತೆ."},
        {
            "q": "print(\"Dose:\", 2 * 250, \"mg\") ನ output ಏನು?",
            "options": ["Dose: 2 * 250 mg", "Dose: 500 mg", "Dose:500mg", "Error ಬರುತ್ತೆ"],
            "why": "Python ಮೊದಲು 2 × 250 = 500 calculate ಮಾಡುತ್ತೆ, ಮತ್ತು print ಪ್ರತಿ item ನಡುವೆ space ಹಾಕುತ್ತೆ.",
        },
    ],
    "exam": {"note": "University exam ಅನ್ನು English ನಲ್ಲಿ ಬರೆಯುತ್ತೀರಿ, ಹಾಗಾಗಿ model answers English ನಲ್ಲೇ ಇವೆ. ಇವು practice ಗಾಗಿ important questions; ನಿಜವಾದ university questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 1.1 · Python basics",
        "children": [
            {"label": "Program", "children": [{"label": "ಸೂಚನೆಗಳ list"}, {"label": "ಕ್ರಮವಾಗಿ ಪಾಲಿಸಲಾಗುತ್ತೆ"}, {"label": "Prescription ತರಹ"}]},
            {"label": "Programming language", "children": [{"label": "ಮನುಷ್ಯರು, computer ಇಬ್ಬರಿಗೂ ಅರ್ಥ"}, {"label": "ಉದಾ: C, Java, Python"}]},
            {"label": "Python ಯಾಕೆ", "children": [{"label": "English ತರಹ ಓದಬಹುದು"}, {"label": "Free"}, {"label": "Data, graphs ಗೆ libraries"}, {"label": "Pharmacy ಯಲ್ಲಿ use", "children": [{"label": "Clinical trial data"}, {"label": "PK curves"}, {"label": "ADR reports"}, {"label": "Drug design"}]}]},
            {"label": "ಹೇಗೆ run ಆಗುತ್ತೆ", "children": [{"label": "Interpreter"}, {"label": "ಒಂದು ಸಲಕ್ಕೆ ಒಂದು line"}, {"label": "ಮೇಲಿಂದ ಕೆಳಗೆ"}]},
            {"label": "ಮೊದಲ code", "children": [{"label": "print() output ತೋರಿಸುತ್ತೆ"}, {"label": "# ಇಂದ comment ಶುರು"}, {"label": "Quotes ಒಳಗಿನ text = string"}, {"label": "* ಅಂದ್ರೆ ಗುಣಾಕಾರ"}]},
            {"label": "Errors", "children": [{"label": "NameError: ಗೊತ್ತಿಲ್ಲದ ಪದ", "children": [{"label": "ಅದೇ line ನಲ್ಲಿ ನಿಲ್ಲುತ್ತೆ"}]}, {"label": "SyntaxError: ಬರವಣಿಗೆಯ ತಪ್ಪು", "children": [{"label": "ಏನೂ run ಆಗಲ್ಲ"}]}]},
        ],
    },
    "summary": [
        "**Program** ಅಂದ್ರೆ computer ಕ್ರಮವಾಗಿ ಪಾಲಿಸುವ ಸೂಚನೆಗಳ list, prescription ತರಹ.",
        "**Python** ಒಂದು free, ಓದೋಕೆ ಸುಲಭವಾದ programming language; pharmacy ಮತ್ತು healthcare ನಲ್ಲಿ ತುಂಬಾ use ಆಗುತ್ತೆ.",
        "**Interpreter** Python code ಅನ್ನು **ಒಂದು ಸಲಕ್ಕೆ ಒಂದು line, ಮೇಲಿಂದ ಕೆಳಗೆ** run ಮಾಡುತ್ತೆ.",
        "**print()** text ಮತ್ತು numbers ಅನ್ನು screen ಮೇಲೆ ತೋರಿಸುತ್ತೆ; **#** ಇಂದ comment ಶುರುವಾಗುತ್ತೆ.",
        "**Errors** Python ಎಲ್ಲಿ ಸಿಕ್ಕಿಹಾಕಿಕೊಂಡಿತು ಅಂತ ಸ್ಪಷ್ಟವಾಗಿ ಹೇಳುತ್ತವೆ. Syntax error ಇದ್ದರೆ program ಶುರುವೇ ಆಗಲ್ಲ.",
    ],
}

SECTIONS = ["hook", "learn", "explanation", "walkthrough", "errors", "mistakes", "tasks",
            "quiz", "exam", "mindmap", "summary", "video", "animations"]


def merge(base, extra):
    """Merge extra into base the same way the website does (objects by key, lists by index)."""
    if isinstance(base, dict) and isinstance(extra, dict):
        out = dict(base)
        for k, v in extra.items():
            out[k] = merge(base[k], v) if k in base else v
        return out
    if isinstance(base, list) and isinstance(extra, list):
        out = list(base)
        for i, v in enumerate(extra):
            if i < len(out):
                out[i] = merge(out[i], v)
            else:
                out.append(v)
        return out
    return extra


if __name__ == "__main__":
    folder = os.path.join(ROOT, "content", "bp101t", "1-1")
    for lang, data in T.items():
        path = os.path.join(folder, f"{lang}.json")
        current = json.load(open(path, encoding="utf-8"))  # keeps narrator + animation captions
        updated = merge(current, data)
        updated["translatedSections"] = SECTIONS
        json.dump(updated, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("updated", path)

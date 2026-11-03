"""Lesson 2.2 translations (Hindi, Hinglish, Kannada) and voice scripts."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import build  # noqa: E402

_spec = importlib.util.spec_from_file_location("en22", os.path.join(os.path.dirname(__file__), "..", "lessons", "bp101t_2-2_en.py"))
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)
C_STORE, C_AND, C_CHILD, C_GUARD = E.C_STORE, E.C_AND, E.C_CHILD, E.C_GUARD

T = {}

T["hi"] = {
    "hook": {
        "title": "एक सवाल से अगला सवाल",
        "md": "एक parent अपने बच्चे के लिए बुखार की दवा माँगते हैं। Pharmacist का पहला सवाल: **बच्चा है या बड़ा?** बच्चा हो, तभी अगला सवाल मायने रखता है: **बच्चे का वज़न कितना है?**\n\nकुछ फ़ैसले किसी दूसरे फ़ैसले के **अंदर** ही समझ आते हैं। इस lesson में आप `if` के अंदर `if` लिखेंगे।\n\n*इस lesson की doses सिर्फ़ Python सीखने के लिए हैं। असली dose हमेशा prescriber और label से आती है।*",
    },
    "learn": [
        "एक **if** को दूसरे **if** के अंदर कैसे रखें (**nested** condition)",
        "**Indentation** कैसे बताता है कि कौन-सा `else` किस `if` का है",
        "Nested `if` कब use करें, और कब **and** या **elif** आसान है",
        "किसी value को use करने से पहले **उसे जाँचना**",
    ],
    "explanation": [
        {
            "heading": "फ़ैसले के अंदर फ़ैसला",
            "md": "**Nested if** एक `if` statement है जो किसी दूसरे `if` (या `else`) के block के अंदर हो। अंदर वाला सवाल तभी पूछा जाता है जब बाहर वाला जवाब वहाँ तक ले जाए।\n\nInsulin और कई vaccines 2 से 8 °C के बीच रखने होते हैं। Storage check पहले पूछता है कि दवा को fridge चाहिए या नहीं, और उसके बाद ही temperature जाँचता है:\n\n" + C_STORE + "\n\nयह `Too warm: move to the fridge` print करता है। बाहर वाला `if` `True` है, इसलिए Python उसके block में जाता है। वहाँ `temp <= 8` `False` है, इसलिए अंदर वाला `else` चलता है।\n\nअगर `needs_fridge` `False` होता, तो Python temperature देखता ही नहीं: सीधा बाहर वाले `else` पर जाता।",
            "callout": {"title": "Nested if", "md": "किसी दूसरे if या else के block के अंदर लिखा if statement। अंदर की condition तभी जाँची जाती है जब Python उस block तक पहुँचे।"},
        },
        {
            "heading": "Indentation levels दिखाता है",
            "md": "Nesting का हर level **4 और spaces** जोड़ता है:\n\n- बाहर वाला `if` और उसका `else` left edge से शुरू होते हैं।\n- अंदर वाला `if` और उसका `else` **4 spaces** के बाद शुरू होते हैं।\n- अंदर के blocks की lines **8 spaces** के बाद शुरू होती हैं।\n\n`else` उस `if` का होता है जो **उसी indentation** पर हो। Storage example में 4 spaces वाला `else`, `if temp <= 8` के साथ जुड़ता है, और left edge वाला `else`, `if needs_fridge` के साथ।",
            "callout": {"title": "हर else को उसके if की सीध में रखिए", "md": "else को 4 spaces खिसकाइए और वह किसी दूसरे if से जुड़ जाएगा। Python शायद error न दे, पर program गलत फ़ैसला लेगा।"},
        },
        {
            "heading": "Nested if, या and?",
            "md": "जब अंदर वाले `if` का कोई `else` न हो, तो nested `if` का मतलब **and** वाले एक `if` जैसा ही है:\n\n" + C_AND + "\n\n`and` वाला रूप छोटा और पढ़ने में आसान है। Nesting तब use कीजिए जब अंदर वाले फ़ैसले का **अपना** `else` हो, या बाहर वाला block पहले कोई और काम करे, जैसे अगले example में।",
            "callout": {"title": "Nesting कम रखिए", "md": "आमतौर पर nesting के दो levels काफ़ी हैं। ज़्यादा गहरे जाएँ तो and, or या elif chain आज़माइए।"},
        },
        {
            "heading": "दो सवालों के बीच काम करना",
            "md": "बच्चों का dose अक्सर शरीर के वज़न से निकाला जाता है, जैसे हर kg के लिए 15 mg, एक ऊपरी limit के साथ। Limit dose निकालने के **बाद** ही मायने रखती है, इसलिए check child block के अंदर है:\n\n" + C_CHILD + "\n\nयह `Child dose: 360 mg` print करता है, क्योंकि 15 × 24 = 360 और 360, 500 से ज़्यादा नहीं है। 40 kg के बच्चे के लिए 15 × 40 = 600, तो अंदर वाला `if` उसे 500 पर रोक देगा।\n\nध्यान दीजिए, `print(\"Child dose:\", ...)` में 4 spaces हैं, 8 नहीं: यह हर बच्चे के लिए चलता है, dose रुका हो या नहीं।",
        },
        {
            "heading": "पहले value जाँचिए",
            "md": "Program को ऐसी value से हिसाब नहीं लगाना चाहिए जिसका कोई मतलब न हो, जैसे 0 या negative वज़न। Check को **बाहर वाले** `if` में रखिए, और असली काम उसके अंदर कीजिए:\n\n" + C_GUARD + "\n\nयह `Check the weight` print करता है। ऐसे checks गलती से type हुए number से patient को बचाते हैं। असली programs user की type की हुई हर value जाँचते हैं।",
        },
    ],
    "walkthrough": {
        "intro": "यह program पहले वज़न जाँचता है, फिर child dose और adult dose में से एक चुनता है। यह सिर्फ़ Python सीखने के लिए है, असली dosing के लिए नहीं।",
        "keyTerms": [
            {"meaning": "पहला सवाल: क्या वज़न 0 से ज़्यादा है?"},
            {"meaning": "सिर्फ़ बाहर वाले block के अंदर पूछा जाता है: क्या patient बच्चा है?"},
            {"meaning": "Nesting का एक level, फिर दो।"},
            {"meaning": "else उसी indentation वाले if का होता है।"},
        ],
    },
    "errors": {
        "intro": "Nested blocks में indentation ध्यान से चाहिए। ये दो errors गलत जगह spaces से आती हैं।",
        "examples": [
            {"title": "ऐसा else जो किसी की सीध में नहीं", "md": "`else` में 6 spaces हैं, पर ऊपर किसी `if` में 6 नहीं हैं। इसे उस `if` की सीध में रखिए जिसका यह है: `if age < 2:` के साथ जुड़ने के लिए 4 spaces।"},
            {"title": "अंदर वाला block indent नहीं है", "md": "अंदर वाले `if` को भी अपना indent किया हुआ block चाहिए। `print(\"Infant\")` को 8 spaces दीजिए: 4 बाहर वाले level के, और 4 अंदर वाले के।"},
        ],
    },
    "mistakes": [
        {"mistake": "`else` को गलत level पर रखना, जिससे वह बाहर वाले `if` से जुड़ जाए", "see": "कोई error नहीं, पर गलत message print होता है, या कुछ भी नहीं", "fix": "`else` को ठीक उस `if` के नीचे रखिए जिसका वह है।"},
        {"mistake": "Variable सिर्फ़ एक branch में बनाना, फिर `if` के बाद use करना", "see": "NameError: name 'dose' is not defined", "fix": "हर branch में variable को value दीजिए, या `if` से पहले।"},
        {"mistake": "तीन-चार levels गहरी nesting करना", "see": "कोई error नहीं, पर program पढ़ना मुश्किल और बिगड़ना आसान", "fix": "Conditions को `and` से जोड़िए, या `elif` chain use कीजिए।"},
        {"mistake": "Value जाँचने से पहले उससे हिसाब लगाना, जैसे 0 वज़न", "see": "कोई error नहीं, पर dose 0 mg या negative आता है", "fix": "पहले बाहर वाले `if` में value जाँचिए।"},
    ],
    "tasks": [
        {"title": "क्या vaccine सही रखा है?", "md": "Vaccine को fridge चाहिए, और fridge 5 °C दिखा रहा है। **Nested if** use कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["if needs_fridge: से शुरू कीजिए और उसके अंदर, 4 spaces पर, if temp <= 8: रखिए।", "if needs_fridge:\n    if temp <= 8:\n        print(\"Stored correctly\")\n    else:\n        print(\"Too warm\")\nelse:\n    print(\"Room temperature\")"]},
        {"title": "वज़न से child dose", "md": "बच्चे (12 से कम) के लिए dose हर kg पर 15 mg है। बाकी सबके लिए \"Adult dose: 500 mg\" print कीजिए। 20 kg के इस 6 साल के बच्चे के लिए output बिल्कुल यह होना चाहिए:",
         "hints": ["if age < 12: के अंदर dose = 15 * weight निकालिए।", "if age < 12:\n    dose = 15 * weight\n    print(\"Child dose:\", dose, \"mg\")\nelse:\n    print(\"Adult dose: 500 mg\")"]},
        {"title": "Safety check जोड़िए", "md": "किसी ने negative वज़न type कर दिया, और program आराम से negative dose print कर रहा है। Dose वाले code को एक बाहरी `if weight > 0:` में रखिए, और वरना \"Check the weight\" print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["ऊपर if weight > 0: रखिए, और पूरे age check को 4 spaces और अंदर कीजिए।", "if weight > 0:\n    if age < 12:\n        print(\"Child dose:\", 15 * weight, \"mg\")\n    else:\n        print(\"Adult dose: 500 mg\")\nelse:\n    print(\"Check the weight\")"]},
        {"title": "Bug ढूँढिए", "md": "यह 30 साल की patient pregnant नहीं है, तो program को \"Standard adult dose\" print करना चाहिए। पर यह कुछ भी print नहीं करता, और कोई error भी नहीं। इसे ठीक कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["else किस if का है? उसका indentation देखिए।", "else को if pregnant: से जुड़ना चाहिए, इसलिए उसे 4 spaces दीजिए, और उसके print को 8।"],
         "solutionNote": "Left edge पर else, if age >= 18 से जुड़ा था, जो True था, इसलिए वह कभी नहीं चला। 4 spaces पर वह if pregnant: से जुड़ता है, जो False है, इसलिए चलता है।"},
    ],
    "quiz": [
        {"q": "a = 5\nb = 2\nif a > 3:\n    if b > 3:\n        print(\"X\")\n    else:\n        print(\"Y\")\nelse:\n    print(\"Z\")\n\nयह क्या print करता है?", "why": "a > 3 True है, इसलिए Python बाहर वाले block में जाता है; b > 3 False है, इसलिए अंदर वाला else Y print करता है।"},
        {"q": "Nested code में Python कैसे जानता है कि else किस if का है?", "why": "else उसी indentation वाले if से जुड़ता है।"},
        {"q": "कौन-सी एक line इस nested code (बिना else) जैसी ही है?\n\nif a:\n    if b:\n        print(\"OK\")", "why": "print तक पहुँचने के लिए दोनों conditions True होनी चाहिए, यही and का मतलब है।"},
        {"q": "अंदर वाले if (दो level गहरे) के अंदर की line कितने spaces से शुरू होती है?", "why": "हर level 4 spaces जोड़ता है: 4 + 4 = 8।"},
        {"q": "age = 15\nif age >= 18:\n    if age >= 65:\n        print(\"Senior\")\n    else:\n        print(\"Adult\")\nelse:\n    print(\"Minor\")\n\nयह क्या print करता है?", "why": "15 >= 18 False है, इसलिए Python पूरा बाहर वाला block छोड़कर बाहर वाला else चलाता है।"},
        {"q": "dose सिर्फ़ एक ऐसे if block में बना जिसकी condition False थी, फिर if के बाद print हुआ। क्या होगा?", "why": "dose बनाने वाली line कभी चली ही नहीं, इसलिए यह नाम अभी है ही नहीं।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 2.2 · Nested conditions",
        "children": [
            {"label": "Nested if", "children": [{"label": "if के अंदर if"}, {"label": "पहुँचने पर ही अंदर वाला सवाल"}]},
            {"label": "Indentation", "children": [{"label": "हर level पर 4 spaces"}, {"label": "else उसी level से जुड़ता है"}]},
            {"label": "या and use करें", "children": [{"label": "अंदर else नहीं → and"}, {"label": "ज़्यादा से ज़्यादा 2 levels"}]},
            {"label": "बीच में काम", "children": [{"label": "पहले हिसाब, फिर check"}, {"label": "Dose पर limit"}]},
            {"label": "पहले जाँचिए", "children": [{"label": "बाहर वाला if जाँचता है"}, {"label": "weight > 0"}]},
            {"label": "Errors", "children": [{"label": "IndentationError"}, {"label": "NameError"}]},
        ],
    },
    "summary": [
        "**Nested if** किसी दूसरे `if` या `else` के block के अंदर का `if` है; अंदर की condition तभी जाँची जाती है जब Python वहाँ पहुँचे।",
        "Nesting का हर level **4 spaces** जोड़ता है, और `else` **उसी indentation** वाले `if` का होता है।",
        "बिना अंदर वाले `else` का nested `if`, **and** वाले एक `if` से लिखा जा सकता है; nesting लगभग दो levels तक रखिए।",
        "बाहर वाले block में **पहले हिसाब** लगाइए, फिर अंदर वाला `if` नतीजा जाँचे।",
        "**Value use करने से पहले उसे जाँचिए**, जैसे `if weight > 0:`, ताकि type की गलती से गलत dose न बने।",
    ],
}

T["hinglish"] = {
    "hook": {
        "title": "Ek sawaal se agla sawaal",
        "md": "Ek parent apne bachche ke liye bukhaar ki dawa maangte hain. Pharmacist ka pehla sawaal: **bachcha hai ya bada?** Bachcha ho, tabhi agla sawaal matter karta hai: **bachche ka wazan kitna hai?**\n\nKuch faisle kisi doosre faisle ke **andar** hi samajh aate hain. Is lesson mein aap `if` ke andar `if` likhenge.\n\n*Is lesson ki doses sirf Python seekhne ke liye hain. Asli dose hamesha prescriber aur label se aati hai.*",
    },
    "learn": [
        "Ek **if** ko doosre **if** ke andar kaise rakhein (**nested** condition)",
        "**Indentation** kaise batata hai ki kaun-sa `else` kis `if` ka hai",
        "Nested `if` kab use karein, aur kab **and** ya **elif** aasaan hai",
        "Kisi value ko use karne se pehle **use jaanchna**",
    ],
    "explanation": [
        {
            "heading": "Faisle ke andar faisla",
            "md": "**Nested if** ek `if` statement hai jo kisi doosre `if` (ya `else`) ke block ke andar ho. Andar wala sawaal tabhi poochha jaata hai jab bahar wala jawaab wahaan tak le jaaye.\n\nInsulin aur kai vaccines 2 se 8 °C ke beech rakhne hote hain. Storage check pehle poochhta hai ki dawa ko fridge chahiye ya nahi, aur uske baad hi temperature jaanchta hai:\n\n" + C_STORE + "\n\nYeh `Too warm: move to the fridge` print karta hai. Bahar wala `if` `True` hai, isliye Python uske block mein jaata hai. Wahaan `temp <= 8` `False` hai, isliye andar wala `else` chalta hai.\n\nAgar `needs_fridge` `False` hota, to Python temperature dekhta hi nahi: seedha bahar wale `else` par jaata.",
            "callout": {"title": "Nested if", "md": "Kisi doosre if ya else ke block ke andar likha if statement. Andar ki condition tabhi jaanchi jaati hai jab Python us block tak pahunche."},
        },
        {
            "heading": "Indentation levels dikhaata hai",
            "md": "Nesting ka har level **4 aur spaces** jodta hai:\n\n- Bahar wala `if` aur uska `else` left edge se shuru hote hain.\n- Andar wala `if` aur uska `else` **4 spaces** ke baad shuru hote hain.\n- Andar ke blocks ki lines **8 spaces** ke baad shuru hoti hain.\n\n`else` us `if` ka hota hai jo **usi indentation** par ho. Storage example mein 4 spaces wala `else`, `if temp <= 8` ke saath judta hai, aur left edge wala `else`, `if needs_fridge` ke saath.",
            "callout": {"title": "Har else ko uske if ki seedh mein rakhiye", "md": "else ko 4 spaces khiskaaiye aur woh kisi doosre if se jud jaayega. Python shaayad error na de, par program galat faisla lega."},
        },
        {
            "heading": "Nested if, ya and?",
            "md": "Jab andar wale `if` ka koi `else` na ho, to nested `if` ka matlab **and** wale ek `if` jaisa hi hai:\n\n" + C_AND + "\n\n`and` wala roop chhota aur padhne mein aasaan hai. Nesting tab use kijiye jab andar wale faisle ka **apna** `else` ho, ya bahar wala block pehle koi aur kaam kare, jaise agle example mein.",
            "callout": {"title": "Nesting kam rakhiye", "md": "Aam taur par nesting ke do levels kaafi hain. Zyada gehre jaayein to and, or ya elif chain aazmaaiye."},
        },
        {
            "heading": "Do sawaalon ke beech kaam karna",
            "md": "Bachchon ka dose aksar shareer ke wazan se nikaala jaata hai, jaise har kg ke liye 15 mg, ek oopari limit ke saath. Limit dose nikaalne ke **baad** hi matter karti hai, isliye check child block ke andar hai:\n\n" + C_CHILD + "\n\nYeh `Child dose: 360 mg` print karta hai, kyonki 15 × 24 = 360 aur 360, 500 se zyada nahi hai. 40 kg ke bachche ke liye 15 × 40 = 600, to andar wala `if` use 500 par rok dega.\n\nDhyaan dijiye, `print(\"Child dose:\", ...)` mein 4 spaces hain, 8 nahi: yeh har bachche ke liye chalta hai, dose ruka ho ya nahi.",
        },
        {
            "heading": "Pehle value jaanchiye",
            "md": "Program ko aisi value se hisaab nahi lagaana chahiye jiska koi matlab na ho, jaise 0 ya negative wazan. Check ko **bahar wale** `if` mein rakhiye, aur asli kaam uske andar kijiye:\n\n" + C_GUARD + "\n\nYeh `Check the weight` print karta hai. Aise checks galti se type hue number se patient ko bachaate hain. Asli programs user ki type ki hui har value jaanchte hain.",
        },
    ],
    "walkthrough": {
        "intro": "Yeh program pehle wazan jaanchta hai, phir child dose aur adult dose mein se ek chunta hai. Yeh sirf Python seekhne ke liye hai, asli dosing ke liye nahi.",
        "keyTerms": [
            {"meaning": "Pehla sawaal: kya wazan 0 se zyada hai?"},
            {"meaning": "Sirf bahar wale block ke andar poochha jaata hai: kya patient bachcha hai?"},
            {"meaning": "Nesting ka ek level, phir do."},
            {"meaning": "else usi indentation wale if ka hota hai."},
        ],
    },
    "errors": {
        "intro": "Nested blocks mein indentation dhyaan se chahiye. Yeh do errors galat jagah spaces se aati hain.",
        "examples": [
            {"title": "Aisa else jo kisi ki seedh mein nahi", "md": "`else` mein 6 spaces hain, par upar kisi `if` mein 6 nahi hain. Ise us `if` ki seedh mein rakhiye jiska yeh hai: `if age < 2:` ke saath judne ke liye 4 spaces."},
            {"title": "Andar wala block indent nahi hai", "md": "Andar wale `if` ko bhi apna indent kiya hua block chahiye. `print(\"Infant\")` ko 8 spaces dijiye: 4 bahar wale level ke, aur 4 andar wale ke."},
        ],
    },
    "mistakes": [
        {"mistake": "`else` ko galat level par rakhna, jisse woh bahar wale `if` se jud jaaye", "see": "Koi error nahi, par galat message print hota hai, ya kuch bhi nahi", "fix": "`else` ko theek us `if` ke neeche rakhiye jiska woh hai."},
        {"mistake": "Variable sirf ek branch mein banaana, phir `if` ke baad use karna", "see": "NameError: name 'dose' is not defined", "fix": "Har branch mein variable ko value dijiye, ya `if` se pehle."},
        {"mistake": "Teen-chaar levels gehri nesting karna", "see": "Koi error nahi, par program padhna mushkil aur bigadna aasaan", "fix": "Conditions ko `and` se jodiye, ya `elif` chain use kijiye."},
        {"mistake": "Value jaanchne se pehle usse hisaab lagaana, jaise 0 wazan", "see": "Koi error nahi, par dose 0 mg ya negative aata hai", "fix": "Pehle bahar wale `if` mein value jaanchiye."},
    ],
    "tasks": [
        {"title": "Kya vaccine sahi rakha hai?", "md": "Vaccine ko fridge chahiye, aur fridge 5 °C dikha raha hai. **Nested if** use kijiye taaki output bilkul yeh ho:",
         "hints": ["if needs_fridge: se shuru kijiye aur uske andar, 4 spaces par, if temp <= 8: rakhiye.", "if needs_fridge:\n    if temp <= 8:\n        print(\"Stored correctly\")\n    else:\n        print(\"Too warm\")\nelse:\n    print(\"Room temperature\")"]},
        {"title": "Wazan se child dose", "md": "Bachche (12 se kam) ke liye dose har kg par 15 mg hai. Baaki sabke liye \"Adult dose: 500 mg\" print kijiye. 20 kg ke is 6 saal ke bachche ke liye output bilkul yeh hona chahiye:",
         "hints": ["if age < 12: ke andar dose = 15 * weight nikaaliye.", "if age < 12:\n    dose = 15 * weight\n    print(\"Child dose:\", dose, \"mg\")\nelse:\n    print(\"Adult dose: 500 mg\")"]},
        {"title": "Safety check jodiye", "md": "Kisi ne negative wazan type kar diya, aur program aaraam se negative dose print kar raha hai. Dose wale code ko ek bahari `if weight > 0:` mein rakhiye, aur warna \"Check the weight\" print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["Upar if weight > 0: rakhiye, aur poore age check ko 4 spaces aur andar kijiye.", "if weight > 0:\n    if age < 12:\n        print(\"Child dose:\", 15 * weight, \"mg\")\n    else:\n        print(\"Adult dose: 500 mg\")\nelse:\n    print(\"Check the weight\")"]},
        {"title": "Bug dhoondhiye", "md": "Yeh 30 saal ki patient pregnant nahi hai, to program ko \"Standard adult dose\" print karna chahiye. Par yeh kuch bhi print nahi karta, aur koi error bhi nahi. Ise theek kijiye taaki output bilkul yeh ho:",
         "hints": ["else kis if ka hai? Uska indentation dekhiye.", "else ko if pregnant: se judna chahiye, isliye use 4 spaces dijiye, aur uske print ko 8."],
         "solutionNote": "Left edge par else, if age >= 18 se juda tha, jo True tha, isliye woh kabhi nahi chala. 4 spaces par woh if pregnant: se judta hai, jo False hai, isliye chalta hai."},
    ],
    "quiz": [
        {"q": "a = 5\nb = 2\nif a > 3:\n    if b > 3:\n        print(\"X\")\n    else:\n        print(\"Y\")\nelse:\n    print(\"Z\")\n\nYeh kya print karta hai?", "why": "a > 3 True hai, isliye Python bahar wale block mein jaata hai; b > 3 False hai, isliye andar wala else Y print karta hai."},
        {"q": "Nested code mein Python kaise jaanta hai ki else kis if ka hai?", "why": "else usi indentation wale if se judta hai."},
        {"q": "Kaun-si ek line is nested code (bina else) jaisi hi hai?\n\nif a:\n    if b:\n        print(\"OK\")", "why": "print tak pahunchne ke liye dono conditions True honi chahiye, yahi and ka matlab hai."},
        {"q": "Andar wale if (do level gehre) ke andar ki line kitne spaces se shuru hoti hai?", "why": "Har level 4 spaces jodta hai: 4 + 4 = 8."},
        {"q": "age = 15\nif age >= 18:\n    if age >= 65:\n        print(\"Senior\")\n    else:\n        print(\"Adult\")\nelse:\n    print(\"Minor\")\n\nYeh kya print karta hai?", "why": "15 >= 18 False hai, isliye Python poora bahar wala block chhodkar bahar wala else chalaata hai."},
        {"q": "dose sirf ek aise if block mein bana jiski condition False thi, phir if ke baad print hua. Kya hoga?", "why": "dose banaane wali line kabhi chali hi nahi, isliye yeh naam abhi hai hi nahi."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 2.2 · Nested conditions",
        "children": [
            {"label": "Nested if", "children": [{"label": "if ke andar if"}, {"label": "Pahunchne par hi andar wala sawaal"}]},
            {"label": "Indentation", "children": [{"label": "Har level par 4 spaces"}, {"label": "else usi level se judta hai"}]},
            {"label": "Ya and use karein", "children": [{"label": "Andar else nahi → and"}, {"label": "Zyada se zyada 2 levels"}]},
            {"label": "Beech mein kaam", "children": [{"label": "Pehle hisaab, phir check"}, {"label": "Dose par limit"}]},
            {"label": "Pehle jaanchiye", "children": [{"label": "Bahar wala if jaanchta hai"}, {"label": "weight > 0"}]},
            {"label": "Errors", "children": [{"label": "IndentationError"}, {"label": "NameError"}]},
        ],
    },
    "summary": [
        "**Nested if** kisi doosre `if` ya `else` ke block ke andar ka `if` hai; andar ki condition tabhi jaanchi jaati hai jab Python wahaan pahunche.",
        "Nesting ka har level **4 spaces** jodta hai, aur `else` **usi indentation** wale `if` ka hota hai.",
        "Bina andar wale `else` ka nested `if`, **and** wale ek `if` se likha ja sakta hai; nesting lagbhag do levels tak rakhiye.",
        "Bahar wale block mein **pehle hisaab** lagaaiye, phir andar wala `if` nateeja jaanche.",
        "**Value use karne se pehle use jaanchiye**, jaise `if weight > 0:`, taaki type ki galti se galat dose na bane.",
    ],
}

T["kn"] = {
    "hook": {
        "title": "ಒಂದು ಪ್ರಶ್ನೆಯಿಂದ ಮುಂದಿನ ಪ್ರಶ್ನೆ",
        "md": "ಒಬ್ಬ parent ತಮ್ಮ ಮಗುವಿಗೆ ಜ್ವರದ ಔಷಧ ಕೇಳುತ್ತಾರೆ. Pharmacist ನ ಮೊದಲ ಪ್ರಶ್ನೆ: **ಮಗುವಾ ಅಥವಾ ದೊಡ್ಡವರಾ?** ಮಗು ಆದರೆ ಮಾತ್ರ ಮುಂದಿನ ಪ್ರಶ್ನೆ ಮುಖ್ಯ: **ಮಗುವಿನ ತೂಕ ಎಷ್ಟು?**\n\nಕೆಲವು ತೀರ್ಮಾನಗಳು ಇನ್ನೊಂದು ತೀರ್ಮಾನದ **ಒಳಗೆ** ಮಾತ್ರ ಅರ್ಥ ಆಗುತ್ತವೆ. ಈ lesson ನಲ್ಲಿ ನೀವು `if` ಒಳಗೆ `if` ಬರೆಯುತ್ತೀರಿ.\n\n*ಈ lesson ನ doses Python ಕಲಿಯಲು ಮಾತ್ರ. ನಿಜವಾದ dose ಯಾವಾಗಲೂ prescriber ಮತ್ತು label ಇಂದ ಬರುತ್ತೆ.*",
    },
    "learn": [
        "ಒಂದು **if** ಅನ್ನು ಇನ್ನೊಂದು **if** ಒಳಗೆ ಹೇಗೆ ಇಡುವುದು (**nested** condition)",
        "ಯಾವ `else` ಯಾವ `if` ಗೆ ಸೇರಿದ್ದು ಅಂತ **indentation** ಹೇಗೆ ತೋರಿಸುತ್ತೆ",
        "Nested `if` ಯಾವಾಗ ಬಳಸಬೇಕು, ಮತ್ತು ಯಾವಾಗ **and** ಅಥವಾ **elif** ಸುಲಭ",
        "ಒಂದು value ಬಳಸುವ ಮುಂಚೆ **ಅದನ್ನು check ಮಾಡುವುದು**",
    ],
    "explanation": [
        {
            "heading": "ತೀರ್ಮಾನದ ಒಳಗೆ ತೀರ್ಮಾನ",
            "md": "**Nested if** ಅಂದರೆ ಇನ್ನೊಂದು `if` (ಅಥವಾ `else`) ನ block ಒಳಗಿರುವ `if` statement. ಹೊರಗಿನ ಉತ್ತರ ಅಲ್ಲಿಗೆ ಕರೆದೊಯ್ದಾಗ ಮಾತ್ರ ಒಳಗಿನ ಪ್ರಶ್ನೆ ಕೇಳಲಾಗುತ್ತೆ.\n\nInsulin ಮತ್ತು ಹಲವು vaccines ಅನ್ನು 2 ರಿಂದ 8 °C ನಡುವೆ ಇಡಬೇಕು. Storage check ಮೊದಲು ಔಷಧಕ್ಕೆ fridge ಬೇಕಾ ಅಂತ ಕೇಳುತ್ತೆ, ಆಮೇಲೆಯೇ temperature check ಮಾಡುತ್ತೆ:\n\n" + C_STORE + "\n\nಇದು `Too warm: move to the fridge` print ಮಾಡುತ್ತೆ. ಹೊರಗಿನ `if` `True`, ಅದಕ್ಕೇ Python ಅದರ block ಒಳಗೆ ಹೋಗುತ್ತೆ. ಅಲ್ಲಿ `temp <= 8` `False`, ಅದಕ್ಕೇ ಒಳಗಿನ `else` run ಆಗುತ್ತೆ.\n\n`needs_fridge` `False` ಆಗಿದ್ದರೆ, Python temperature ನೋಡುತ್ತಲೇ ಇರಲಿಲ್ಲ: ನೇರವಾಗಿ ಹೊರಗಿನ `else` ಗೆ ಹೋಗುತ್ತಿತ್ತು.",
            "callout": {"title": "Nested if", "md": "ಇನ್ನೊಂದು if ಅಥವಾ else ನ block ಒಳಗೆ ಬರೆದ if statement. Python ಆ block ತಲುಪಿದಾಗ ಮಾತ್ರ ಒಳಗಿನ condition check ಆಗುತ್ತೆ."},
        },
        {
            "heading": "Indentation levels ತೋರಿಸುತ್ತೆ",
            "md": "Nesting ನ ಪ್ರತಿ level **ಇನ್ನೂ 4 spaces** ಸೇರಿಸುತ್ತೆ:\n\n- ಹೊರಗಿನ `if` ಮತ್ತು ಅದರ `else` left edge ಇಂದ ಶುರುವಾಗುತ್ತವೆ.\n- ಒಳಗಿನ `if` ಮತ್ತು ಅದರ `else` **4 spaces** ಆದಮೇಲೆ ಶುರುವಾಗುತ್ತವೆ.\n- ಒಳಗಿನ blocks ನ lines **8 spaces** ಆದಮೇಲೆ ಶುರುವಾಗುತ್ತವೆ.\n\n`else` **ಅದೇ indentation** ನಲ್ಲಿರುವ `if` ಗೆ ಸೇರುತ್ತೆ. Storage example ನಲ್ಲಿ 4 spaces ಇರುವ `else`, `if temp <= 8` ಜೊತೆ ಸೇರುತ್ತೆ, left edge ನ `else`, `if needs_fridge` ಜೊತೆ.",
            "callout": {"title": "ಪ್ರತಿ else ಅನ್ನು ಅದರ if ನ ಸಾಲಿನಲ್ಲೇ ಇಡಿ", "md": "else ಅನ್ನು 4 spaces ಸರಿಸಿದರೆ ಅದು ಬೇರೆ if ಜೊತೆ ಸೇರುತ್ತೆ. Python error ಕೊಡದೇ ಇರಬಹುದು, ಆದರೆ program ತಪ್ಪು ತೀರ್ಮಾನ ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ."},
        },
        {
            "heading": "Nested if, ಅಥವಾ and?",
            "md": "ಒಳಗಿನ `if` ಗೆ `else` ಇಲ್ಲದಿದ್ದಾಗ, nested `if` ಅಂದರೆ **and** ಇರುವ ಒಂದೇ `if` ಗೆ ಸಮ:\n\n" + C_AND + "\n\n`and` ಇರುವ ರೂಪ ಚಿಕ್ಕದು, ಓದಲು ಸುಲಭ. ಒಳಗಿನ ತೀರ್ಮಾನಕ್ಕೆ **ತನ್ನದೇ** `else` ಇದ್ದಾಗ, ಅಥವಾ ಹೊರಗಿನ block ಮೊದಲು ಬೇರೆ ಕೆಲಸ ಮಾಡುವಾಗ nesting ಬಳಸಿ, ಮುಂದಿನ example ತರಹ.",
            "callout": {"title": "Nesting ಕಡಿಮೆ ಇರಲಿ", "md": "ಸಾಮಾನ್ಯವಾಗಿ ಎರಡು levels nesting ಸಾಕು. ಇನ್ನೂ ಆಳಕ್ಕೆ ಹೋದರೆ and, or ಅಥವಾ elif chain ಪ್ರಯತ್ನಿಸಿ."},
        },
        {
            "heading": "ಎರಡು ಪ್ರಶ್ನೆಗಳ ನಡುವೆ ಕೆಲಸ",
            "md": "ಮಕ್ಕಳ dose ಹಲವು ಸಲ ದೇಹದ ತೂಕದಿಂದ ಲೆಕ್ಕ ಹಾಕುತ್ತಾರೆ, ಉದಾ. ಪ್ರತಿ kg ಗೆ 15 mg, ಒಂದು ಮೇಲಿನ limit ಜೊತೆ. Dose ಲೆಕ್ಕ ಹಾಕಿದ **ನಂತರ** ಮಾತ್ರ limit ಮುಖ್ಯ, ಅದಕ್ಕೇ check child block ಒಳಗಿದೆ:\n\n" + C_CHILD + "\n\nಇದು `Child dose: 360 mg` print ಮಾಡುತ್ತೆ, ಯಾಕೆಂದರೆ 15 × 24 = 360, ಮತ್ತು 360, 500 ಕ್ಕಿಂತ ಜಾಸ್ತಿ ಇಲ್ಲ. 40 kg ಮಗುವಿಗೆ 15 × 40 = 600, ಆಗ ಒಳಗಿನ `if` ಅದನ್ನು 500 ಕ್ಕೆ ನಿಲ್ಲಿಸುತ್ತೆ.\n\nಗಮನಿಸಿ, `print(\"Child dose:\", ...)` ಗೆ 4 spaces, 8 ಅಲ್ಲ: dose ನಿಲ್ಲಿಸಿರಲಿ ಇಲ್ಲದಿರಲಿ, ಇದು ಪ್ರತಿ ಮಗುವಿಗೂ run ಆಗುತ್ತೆ.",
        },
        {
            "heading": "ಮೊದಲು value check ಮಾಡಿ",
            "md": "ಅರ್ಥವಿಲ್ಲದ value ಇಂದ, ಉದಾ. 0 ಅಥವಾ negative ತೂಕದಿಂದ, program ಲೆಕ್ಕ ಹಾಕಬಾರದು. Check ಅನ್ನು **ಹೊರಗಿನ** `if` ನಲ್ಲಿ ಇಡಿ, ನಿಜವಾದ ಕೆಲಸ ಅದರ ಒಳಗೆ ಮಾಡಿ:\n\n" + C_GUARD + "\n\nಇದು `Check the weight` print ಮಾಡುತ್ತೆ. ತಪ್ಪಾಗಿ type ಮಾಡಿದ number ಇಂದ ಇಂಥ checks patient ಅನ್ನು ಕಾಪಾಡುತ್ತವೆ. ನಿಜವಾದ programs user type ಮಾಡುವ ಪ್ರತಿ value ಅನ್ನು check ಮಾಡುತ್ತವೆ.",
        },
    ],
    "walkthrough": {
        "intro": "ಈ program ಮೊದಲು ತೂಕ check ಮಾಡುತ್ತೆ, ಆಮೇಲೆ child dose ಮತ್ತು adult dose ನಲ್ಲಿ ಒಂದನ್ನು ಆರಿಸುತ್ತೆ. ಇದು Python ಕಲಿಯಲು ಮಾತ್ರ, ನಿಜವಾದ dosing ಗೆ ಅಲ್ಲ.",
        "keyTerms": [
            {"meaning": "ಮೊದಲ ಪ್ರಶ್ನೆ: ತೂಕ 0 ಕ್ಕಿಂತ ಜಾಸ್ತಿ ಇದೆಯಾ?"},
            {"meaning": "ಹೊರಗಿನ block ಒಳಗೆ ಮಾತ್ರ ಕೇಳಲಾಗುತ್ತೆ: patient ಮಗುವಾ?"},
            {"meaning": "Nesting ನ ಒಂದು level, ಆಮೇಲೆ ಎರಡು."},
            {"meaning": "else ಅದೇ indentation ನ if ಗೆ ಸೇರುತ್ತೆ."},
        ],
    },
    "errors": {
        "intro": "Nested blocks ಗೆ indentation ಎಚ್ಚರಿಕೆಯಿಂದ ಬೇಕು. ಈ ಎರಡು errors ತಪ್ಪು ಜಾಗದ spaces ಇಂದ ಬರುತ್ತವೆ.",
        "examples": [
            {"title": "ಯಾವುದರ ಸಾಲಿಗೂ ಸೇರದ else", "md": "`else` ಗೆ 6 spaces ಇವೆ, ಆದರೆ ಮೇಲಿನ ಯಾವ `if` ಗೂ 6 ಇಲ್ಲ. ಅದು ಸೇರಬೇಕಾದ `if` ನ ಸಾಲಿನಲ್ಲಿ ಇಡಿ: `if age < 2:` ಜೊತೆ ಸೇರಲು 4 spaces."},
            {"title": "ಒಳಗಿನ block indent ಆಗಿಲ್ಲ", "md": "ಒಳಗಿನ `if` ಗೂ ತನ್ನದೇ indent ಮಾಡಿದ block ಬೇಕು. `print(\"Infant\")` ಗೆ 8 spaces ಕೊಡಿ: 4 ಹೊರಗಿನ level ಗೆ, ಇನ್ನೂ 4 ಒಳಗಿನದಕ್ಕೆ."},
        ],
    },
    "mistakes": [
        {"mistake": "`else` ಅನ್ನು ತಪ್ಪು level ನಲ್ಲಿ ಇಡುವುದು, ಆಗ ಅದು ಹೊರಗಿನ `if` ಜೊತೆ ಸೇರುತ್ತೆ", "see": "Error ಇಲ್ಲ, ಆದರೆ ತಪ್ಪು message print ಆಗುತ್ತೆ, ಅಥವಾ ಏನೂ ಆಗಲ್ಲ", "fix": "`else` ಅನ್ನು ಅದು ಸೇರಬೇಕಾದ `if` ನ ಕೆಳಗೇ ಸರಿಯಾಗಿ ಇಡಿ."},
        {"mistake": "ಒಂದೇ branch ನಲ್ಲಿ variable ಮಾಡಿ, `if` ಆದಮೇಲೆ ಬಳಸುವುದು", "see": "NameError: name 'dose' is not defined", "fix": "ಪ್ರತಿ branch ನಲ್ಲೂ, ಅಥವಾ `if` ಮುಂಚೆ, variable ಗೆ value ಕೊಡಿ."},
        {"mistake": "ಮೂರು-ನಾಲ್ಕು levels ಆಳದ nesting", "see": "Error ಇಲ್ಲ, ಆದರೆ program ಓದಲು ಕಷ್ಟ, ಕೆಡುವುದು ಸುಲಭ", "fix": "Conditions ಅನ್ನು `and` ಇಂದ ಜೋಡಿಸಿ, ಅಥವಾ `elif` chain ಬಳಸಿ."},
        {"mistake": "Value check ಮಾಡುವ ಮುಂಚೆ ಅದರಿಂದ ಲೆಕ್ಕ ಹಾಕುವುದು, ಉದಾ. 0 ತೂಕ", "see": "Error ಇಲ್ಲ, ಆದರೆ dose 0 mg ಅಥವಾ negative ಬರುತ್ತೆ", "fix": "ಮೊದಲು ಹೊರಗಿನ `if` ನಲ್ಲಿ value check ಮಾಡಿ."},
    ],
    "tasks": [
        {"title": "Vaccine ಸರಿಯಾಗಿ ಇಟ್ಟಿದೆಯಾ?", "md": "Vaccine ಗೆ fridge ಬೇಕು, fridge 5 °C ತೋರಿಸುತ್ತಿದೆ. Output ಸರಿಯಾಗಿ ಹೀಗೇ ಬರುವ ಹಾಗೆ **nested if** ಬಳಸಿ:",
         "hints": ["if needs_fridge: ಇಂದ ಶುರು ಮಾಡಿ, ಅದರ ಒಳಗೆ 4 spaces ನಲ್ಲಿ if temp <= 8: ಇಡಿ.", "if needs_fridge:\n    if temp <= 8:\n        print(\"Stored correctly\")\n    else:\n        print(\"Too warm\")\nelse:\n    print(\"Room temperature\")"]},
        {"title": "ತೂಕದಿಂದ child dose", "md": "ಮಗುವಿಗೆ (12 ಕ್ಕಿಂತ ಕಡಿಮೆ) dose ಪ್ರತಿ kg ಗೆ 15 mg. ಬೇರೆ ಎಲ್ಲರಿಗೂ \"Adult dose: 500 mg\" print ಮಾಡಿ. 20 kg ಇರುವ ಈ 6 ವರ್ಷದ ಮಗುವಿಗೆ output ಸರಿಯಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["if age < 12: ಒಳಗೆ dose = 15 * weight ಲೆಕ್ಕ ಹಾಕಿ.", "if age < 12:\n    dose = 15 * weight\n    print(\"Child dose:\", dose, \"mg\")\nelse:\n    print(\"Adult dose: 500 mg\")"]},
        {"title": "Safety check ಸೇರಿಸಿ", "md": "ಯಾರೋ negative ತೂಕ type ಮಾಡಿದ್ದಾರೆ, program ಆರಾಮವಾಗಿ negative dose print ಮಾಡುತ್ತಿದೆ. Dose code ಅನ್ನು ಒಂದು ಹೊರಗಿನ `if weight > 0:` ಒಳಗೆ ಇಡಿ, ಇಲ್ಲದಿದ್ದರೆ \"Check the weight\" print ಮಾಡಿ. Output ಸರಿಯಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["ಮೇಲೆ if weight > 0: ಇಡಿ, ಇಡೀ age check ಅನ್ನು ಇನ್ನೂ 4 spaces ಒಳಗೆ ಸರಿಸಿ.", "if weight > 0:\n    if age < 12:\n        print(\"Child dose:\", 15 * weight, \"mg\")\n    else:\n        print(\"Adult dose: 500 mg\")\nelse:\n    print(\"Check the weight\")"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "ಈ 30 ವರ್ಷದ patient pregnant ಅಲ್ಲ, ಅದಕ್ಕೇ program \"Standard adult dose\" print ಮಾಡಬೇಕು. ಆದರೆ ಅದು ಏನನ್ನೂ print ಮಾಡಲ್ಲ, error ಕೂಡ ಇಲ್ಲ. Output ಸರಿಯಾಗಿ ಹೀಗೇ ಬರುವ ಹಾಗೆ ಸರಿ ಮಾಡಿ:",
         "hints": ["else ಯಾವ if ಗೆ ಸೇರಿದ್ದು? ಅದರ indentation ನೋಡಿ.", "else, if pregnant: ಜೊತೆ ಸೇರಬೇಕು, ಅದಕ್ಕೇ ಅದಕ್ಕೆ 4 spaces ಕೊಡಿ, ಅದರ print ಗೆ 8."],
         "solutionNote": "Left edge ನಲ್ಲಿ else, if age >= 18 ಜೊತೆ ಸೇರಿತ್ತು, ಅದು True, ಅದಕ್ಕೇ else ಯಾವತ್ತೂ run ಆಗಲಿಲ್ಲ. 4 spaces ನಲ್ಲಿ ಅದು if pregnant: ಜೊತೆ ಸೇರುತ್ತೆ, ಅದು False, ಅದಕ್ಕೇ run ಆಗುತ್ತೆ."},
    ],
    "quiz": [
        {"q": "a = 5\nb = 2\nif a > 3:\n    if b > 3:\n        print(\"X\")\n    else:\n        print(\"Y\")\nelse:\n    print(\"Z\")\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "a > 3 True, ಅದಕ್ಕೇ Python ಹೊರಗಿನ block ಒಳಗೆ ಹೋಗುತ್ತೆ; b > 3 False, ಅದಕ್ಕೇ ಒಳಗಿನ else Y print ಮಾಡುತ್ತೆ."},
        {"q": "Nested code ನಲ್ಲಿ else ಯಾವ if ಗೆ ಸೇರಿದ್ದು ಅಂತ Python ಗೆ ಹೇಗೆ ಗೊತ್ತಾಗುತ್ತೆ?", "why": "else ಅದೇ indentation ನ if ಜೊತೆ ಸೇರುತ್ತೆ."},
        {"q": "ಈ nested code (else ಇಲ್ಲದ) ಗೆ ಸಮವಾದ ಒಂದು line ಯಾವುದು?\n\nif a:\n    if b:\n        print(\"OK\")", "why": "print ತಲುಪಲು ಎರಡೂ conditions True ಆಗಬೇಕು, and ಅಂದರೆ ಅದೇ."},
        {"q": "ಒಳಗಿನ if (ಎರಡು level ಆಳ) ನ ಒಳಗಿನ line ಎಷ್ಟು spaces ಇಂದ ಶುರುವಾಗುತ್ತೆ?", "why": "ಪ್ರತಿ level 4 spaces ಸೇರಿಸುತ್ತೆ: 4 + 4 = 8."},
        {"q": "age = 15\nif age >= 18:\n    if age >= 65:\n        print(\"Senior\")\n    else:\n        print(\"Adult\")\nelse:\n    print(\"Minor\")\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "15 >= 18 False, ಅದಕ್ಕೇ Python ಇಡೀ ಹೊರಗಿನ block ಬಿಟ್ಟು ಹೊರಗಿನ else run ಮಾಡುತ್ತೆ."},
        {"q": "Condition False ಆಗಿದ್ದ if block ಒಳಗೆ ಮಾತ್ರ dose ಮಾಡಲಾಯಿತು, ಆಮೇಲೆ if ನಂತರ print ಮಾಡಲಾಯಿತು. ಏನಾಗುತ್ತೆ?", "why": "dose ಮಾಡುವ line run ಆಗಲೇ ಇಲ್ಲ, ಅದಕ್ಕೇ ಆ ಹೆಸರು ಇನ್ನೂ ಇಲ್ಲ."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 2.2 · Nested conditions",
        "children": [
            {"label": "Nested if", "children": [{"label": "if ಒಳಗೆ if"}, {"label": "ತಲುಪಿದಾಗ ಮಾತ್ರ ಒಳಗಿನ ಪ್ರಶ್ನೆ"}]},
            {"label": "Indentation", "children": [{"label": "ಪ್ರತಿ level ಗೆ 4 spaces"}, {"label": "else ಅದೇ level ಗೆ ಸೇರುತ್ತೆ"}]},
            {"label": "ಅಥವಾ and ಬಳಸಿ", "children": [{"label": "ಒಳಗೆ else ಇಲ್ಲ → and"}, {"label": "ಗರಿಷ್ಠ 2 levels"}]},
            {"label": "ನಡುವೆ ಕೆಲಸ", "children": [{"label": "ಮೊದಲು ಲೆಕ್ಕ, ಆಮೇಲೆ check"}, {"label": "Dose ಗೆ limit"}]},
            {"label": "ಮೊದಲು check", "children": [{"label": "ಹೊರಗಿನ if check ಮಾಡುತ್ತೆ"}, {"label": "weight > 0"}]},
            {"label": "Errors", "children": [{"label": "IndentationError"}, {"label": "NameError"}]},
        ],
    },
    "summary": [
        "**Nested if** ಅಂದರೆ ಇನ್ನೊಂದು `if` ಅಥವಾ `else` ನ block ಒಳಗಿನ `if`; Python ಅಲ್ಲಿಗೆ ತಲುಪಿದಾಗ ಮಾತ್ರ ಒಳಗಿನ condition check ಆಗುತ್ತೆ.",
        "Nesting ನ ಪ್ರತಿ level **4 spaces** ಸೇರಿಸುತ್ತೆ, ಮತ್ತು `else` **ಅದೇ indentation** ನ `if` ಗೆ ಸೇರುತ್ತೆ.",
        "ಒಳಗೆ `else` ಇಲ್ಲದ nested `if` ಅನ್ನು **and** ಇರುವ ಒಂದೇ `if` ಆಗಿ ಬರೆಯಬಹುದು; nesting ಸುಮಾರು ಎರಡು levels ಒಳಗಿರಲಿ.",
        "ಹೊರಗಿನ block ನಲ್ಲಿ **ಮೊದಲು ಲೆಕ್ಕ** ಹಾಕಿ, ಆಮೇಲೆ ಒಳಗಿನ `if` ಫಲಿತಾಂಶ check ಮಾಡಲಿ.",
        "**Value ಬಳಸುವ ಮುಂಚೆ check ಮಾಡಿ**, ಉದಾ. `if weight > 0:`, type ತಪ್ಪಿನಿಂದ ತಪ್ಪು dose ಬರದಿರಲಿ.",
    ],
}

NARR = {
    "hi": [
        "यह program दो सवाल पूछता है, एक दूसरे के अंदर। पहला: क्या वज़न ठीक है? फिर: क्या patient बच्चा है?",
        "Comment बताता है कि program क्या करता है, और यह कि यह सिर्फ़ सीखने के लिए है।",
        "age में आठ store होता है।",
        "weight में चौबीस store होता है, kilogram में।",
        "बाहर वाला if जाँचता है कि वज़न zero से ज़्यादा है। चौबीस है, इसलिए Python बाहर वाले block में जाता है।",
        "उसके अंदर, अंदर वाला if पूछता है: क्या age बारह से कम है? आठ है, इसलिए Python अंदर वाले block में जाता है।",
        "dose है पंद्रह गुणा चौबीस, यानी तीन सौ साठ।",
        "print child dose दिखाता है।",
        "इस else में चार spaces हैं, इसलिए यह अंदर वाले if का है। अंदर वाला if True था, इसलिए यह छूट जाता है।",
        "यह else left edge पर है, इसलिए यह बाहर वाले if का है। वह भी True था, इसलिए यह भी छूट जाता है, और program खत्म होता है।",
    ],
    "hinglish": [
        "Yeh program do sawaal poochhta hai, ek doosre ke andar. Pehla: kya wazan theek hai? Phir: kya patient bachcha hai?",
        "Comment batata hai ki program kya karta hai, aur yeh ki yeh sirf seekhne ke liye hai.",
        "age mein aath store hota hai.",
        "weight mein chaubees store hota hai, kilogram mein.",
        "Bahar wala if jaanchta hai ki wazan zero se zyada hai. Chaubees hai, isliye Python bahar wale block mein jaata hai.",
        "Uske andar, andar wala if poochhta hai: kya age baarah se kam hai? Aath hai, isliye Python andar wale block mein jaata hai.",
        "dose hai pandrah guna chaubees, yaani teen sau saath.",
        "print child dose dikhaata hai.",
        "Is else mein chaar spaces hain, isliye yeh andar wale if ka hai. Andar wala if True tha, isliye yeh chhoot jaata hai.",
        "Yeh else left edge par hai, isliye yeh bahar wale if ka hai. Woh bhi True tha, isliye yeh bhi chhoot jaata hai, aur program khatam hota hai.",
    ],
    "kn": [
        "ಈ program ಎರಡು ಪ್ರಶ್ನೆಗಳನ್ನು ಕೇಳುತ್ತೆ, ಒಂದರ ಒಳಗೆ ಇನ್ನೊಂದು. ಮೊದಲು: ತೂಕ ಸರಿಯಾಗಿದೆಯಾ? ಆಮೇಲೆ: patient ಮಗುವಾ?",
        "Comment ಈ program ಏನು ಮಾಡುತ್ತೆ ಅಂತ, ಮತ್ತು ಇದು ಕಲಿಯಲು ಮಾತ್ರ ಅಂತ ಹೇಳುತ್ತೆ.",
        "age ನಲ್ಲಿ ಎಂಟು store ಆಗುತ್ತೆ.",
        "weight ನಲ್ಲಿ ಇಪ್ಪತ್ನಾಲ್ಕು store ಆಗುತ್ತೆ, kilogram ನಲ್ಲಿ.",
        "ಹೊರಗಿನ if ತೂಕ zero ಗಿಂತ ಜಾಸ್ತಿ ಇದೆಯಾ ಅಂತ check ಮಾಡುತ್ತೆ. ಇಪ್ಪತ್ನಾಲ್ಕು ಇದೆ, ಅದಕ್ಕೇ Python ಹೊರಗಿನ block ಒಳಗೆ ಹೋಗುತ್ತೆ.",
        "ಅದರ ಒಳಗೆ, ಒಳಗಿನ if ಕೇಳುತ್ತೆ: age ಹನ್ನೆರಡಕ್ಕಿಂತ ಕಡಿಮೆ ಇದೆಯಾ? ಎಂಟು ಇದೆ, ಅದಕ್ಕೇ Python ಒಳಗಿನ block ಒಳಗೆ ಹೋಗುತ್ತೆ.",
        "dose ಅಂದರೆ ಹದಿನೈದು ಗುಣಿಸು ಇಪ್ಪತ್ನಾಲ್ಕು, ಅಂದರೆ ಮುನ್ನೂರ ಅರವತ್ತು.",
        "print child dose ತೋರಿಸುತ್ತೆ.",
        "ಈ else ಗೆ ನಾಲ್ಕು spaces ಇವೆ, ಅದಕ್ಕೇ ಇದು ಒಳಗಿನ if ಗೆ ಸೇರಿದ್ದು. ಒಳಗಿನ if True ಆಗಿತ್ತು, ಅದಕ್ಕೇ ಇದು ಬಿಟ್ಟುಹೋಗುತ್ತೆ.",
        "ಈ else left edge ನಲ್ಲಿದೆ, ಅದಕ್ಕೇ ಇದು ಹೊರಗಿನ if ಗೆ ಸೇರಿದ್ದು. ಅದೂ True ಆಗಿತ್ತು, ಅದಕ್ಕೇ ಇದೂ ಬಿಟ್ಟುಹೋಗುತ್ತೆ, program ಮುಗಿಯುತ್ತೆ.",
    ],
}

ANIM = {
    "hi": [
        "इस दवा को fridge चाहिए, और thermometer बारह degree दिखा रहा है।",
        "पहले बाहर वाला सवाल: क्या इसे fridge चाहिए? हाँ, इसलिए Python अंदर जाता है।",
        "अब जाकर अंदर वाला सवाल पूछा जाता है: क्या यह आठ degree या उससे ठंडा है? बारह नहीं है।",
        "इसलिए अंदर वाला else चलता है। यह अंदर वाले if की सीध में है।",
        "बाहर वाला else बाहर वाले if का है, जो True था, इसलिए वह छूट जाता है।",
    ],
    "hinglish": [
        "Is dawa ko fridge chahiye, aur thermometer baarah degree dikha raha hai.",
        "Pehle bahar wala sawaal: kya ise fridge chahiye? Haan, isliye Python andar jaata hai.",
        "Ab jaakar andar wala sawaal poochha jaata hai: kya yeh aath degree ya usse thanda hai? Baarah nahi hai.",
        "Isliye andar wala else chalta hai. Yeh andar wale if ki seedh mein hai.",
        "Bahar wala else bahar wale if ka hai, jo True tha, isliye woh chhoot jaata hai.",
    ],
    "kn": [
        "ಈ ಔಷಧಕ್ಕೆ fridge ಬೇಕು, thermometer ಹನ್ನೆರಡು degree ತೋರಿಸುತ್ತಿದೆ.",
        "ಮೊದಲು ಹೊರಗಿನ ಪ್ರಶ್ನೆ: ಇದಕ್ಕೆ fridge ಬೇಕಾ? ಹೌದು, ಅದಕ್ಕೇ Python ಒಳಗೆ ಹೋಗುತ್ತೆ.",
        "ಈಗ ಮಾತ್ರ ಒಳಗಿನ ಪ್ರಶ್ನೆ ಕೇಳಲಾಗುತ್ತೆ: ಇದು ಎಂಟು degree ಅಥವಾ ಅದಕ್ಕಿಂತ ತಣ್ಣಗಿದೆಯಾ? ಹನ್ನೆರಡು ಇಲ್ಲ.",
        "ಅದಕ್ಕೇ ಒಳಗಿನ else run ಆಗುತ್ತೆ. ಇದು ಒಳಗಿನ if ನ ಸಾಲಿನಲ್ಲಿದೆ.",
        "ಹೊರಗಿನ else ಹೊರಗಿನ if ಗೆ ಸೇರಿದ್ದು, ಅದು True ಆಗಿತ್ತು, ಅದಕ್ಕೇ ಅದು ಬಿಟ್ಟುಹೋಗುತ್ತೆ.",
    ],
}

if __name__ == "__main__":
    build("2-2", "anim-nest", T, NARR, ANIM)

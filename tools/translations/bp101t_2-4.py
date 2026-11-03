"""Lesson 2.4 translations (Hindi, Hinglish, Kannada) and voice scripts."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import build  # noqa: E402

_spec = importlib.util.spec_from_file_location("en24", os.path.join(os.path.dirname(__file__), "..", "lessons", "bp101t_2-4_en.py"))
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)

FW = {
    "hi": "| Use | कब | Example |\n|---|---|---|\n| `for` | Values पता हैं, या कितनी बार | Day 1 से 30, list की हर दवा |\n| `while` | **कुछ होने तक** दोहराना है | जब तक amount 10 mg से कम न हो, जब तक सही number type न हो |",
    "hinglish": "| Use | Kab | Example |\n|---|---|---|\n| `for` | Values pata hain, ya kitni baar | Day 1 se 30, list ki har dawa |\n| `while` | **Kuch hone tak** dohraana hai | Jab tak amount 10 mg se kam na ho, jab tak sahi number type na ho |",
    "kn": "| Use | ಯಾವಾಗ | Example |\n|---|---|---|\n| `for` | Values ಗೊತ್ತು, ಅಥವಾ ಎಷ್ಟು ಸಲ ಅಂತ ಗೊತ್ತು | Day 1 ರಿಂದ 30, list ನ ಪ್ರತಿ ಔಷಧ |\n| `while` | **ಏನಾದರೂ ಆಗುವವರೆಗೆ** ಪುನರಾವರ್ತನೆ | Amount 10 mg ಗಿಂತ ಕಡಿಮೆ ಆಗುವವರೆಗೆ, ಸರಿಯಾದ number type ಆಗುವವರೆಗೆ |",
}

T = {}

T["hi"] = {
    "hook": {
        "title": "दवा कब तक खत्म होगी?",
        "md": "एक patient के शरीर में किसी दवा की **100 mg** है। हर **4 घंटे** में उसका आधा हिस्सा निकल जाता है। यह समय दवा की **half-life** है। कितने घंटे बाद **10 mg** से कम बचेगा?\n\nआपको पहले से नहीं पता कि कितनी बार आधा करना पड़ेगा, इसलिए fixed `range()` वाला `for` loop ठीक नहीं बैठता। आपको ऐसा loop चाहिए जो **तब तक** चले **जब तक** कुछ सच है। यही आज का lesson है।\n\n*इस lesson के numbers Python सीखने के लिए बनाए गए हैं। असली half-life हर दवा की अलग होती है।*",
    },
    "learn": [
        "**while loop** तब तक कैसे दोहराता है जब तक उसकी condition **True** है",
        "कब **while** और कब **for** use करें",
        "Loop **खत्म** हो, यह कैसे पक्का करें, और **infinite loop** क्या है",
        "**break** loop को जल्दी कैसे रोकता है, और **continue** एक round कैसे छोड़ता है",
    ],
    "explanation": [
        {
            "heading": "जब तक condition True है, दोहराओ",
            "md": "**while loop** अपनी condition जाँचता है, `True` हो तो block चलाता है, फिर वापस जाकर फिर जाँचता है। जैसे ही condition पहली बार `False` हो, यह रुक जाता है।\n\n" + E.C_WHILE + "\n\nयह `Below 10 mg after 16 hours` print करता है। Amount ऐसे घटता है: 100 → 50 → 25 → 12.5 → 6.25। चौथी बार आधा करने के बाद `6.25 > 10` `False` है, इसलिए loop खत्म।\n\nSyntax `if` जैसा ही है: condition, colon, और indent किया block। फ़र्क यह है कि `if` अपना block **ज़्यादा से ज़्यादा एक बार** चलाता है, और `while` **बार-बार**।",
            "callout": {"title": "while loop", "md": "ऐसा loop जो तब तक अपना block दोहराता है जब तक condition True है। हर round से पहले condition जाँची जाती है।"},
        },
        {
            "heading": "for या while?",
            "md": FW["hi"] + "\n\nकई problems दोनों तरह लिखी जा सकती हैं, पर सही चुनाव program को छोटा और साफ़ बनाता है।",
        },
        {
            "heading": "पक्का कीजिए कि loop खत्म हो",
            "md": "`while` block के अंदर कुछ ऐसा होना चाहिए जो condition बदले, वरना loop कभी नहीं रुकेगा:\n\n" + E.C_STOCK + "\n\nयह print करता है:\n\n" + E.O_STOCK + "\n\n`stock -= 1` हर round में stock एक कम करता है। इसके बिना `stock > 0` हमेशा `True` रहता, और program बिना रुके `Dispense one strip` print करता रहता। इसे **infinite loop** कहते हैं।",
            "callout": {"title": "Infinite loop में फँस गए?", "md": "IDE में Stop button दबाइए, या terminal में Ctrl + C। फिर देखिए कि loop condition वाले variable को बदलता है या नहीं।"},
        },
        {
            "heading": "break: loop अभी रोको",
            "md": "**break** loop को तुरंत खत्म कर देता है, भले values बची हों। यह `for` और `while` दोनों में काम करता है। यहाँ pharmacist पहला expired batch मिलने तक batches जाँचता है:\n\n" + E.C_BREAK + "\n\nयह print करता है:\n\n" + E.O_BREAK + "\n\n2028 कभी जाँचा ही नहीं गया: `break` सीधा loop से बाहर कूद गया।\n\nएक आम pattern है `while True` के साथ `break`: सही जवाब मिलने तक पूछते रहो।\n\n" + E.C_ASK + "\n\n`while True` अकेले हमेशा चलता; `break` ही बाहर निकलने का अकेला रास्ता है।",
        },
        {
            "heading": "continue: अगले round पर जाओ",
            "md": "**continue** block का बाकी हिस्सा **सिर्फ़ इस round के लिए** छोड़ देता है, और सीधा अगली value पर जाता है। Reading fail होने पर thermometer कभी-कभी 0 save कर देता है:\n\n" + E.C_CONT + "\n\nयह print करता है:\n\n" + E.O_CONT + "\n\n`break` loop को हमेशा के लिए छोड़ देता है; `continue` बस अगले round पर चला जाता है।",
            "callout": {"title": "while loop में continue", "md": "while loop में variable को continue से पहले update कीजिए। वरना update भी छूट जाएगा, और loop कभी खत्म नहीं होगा।"},
        },
    ],
    "walkthrough": {
        "intro": "यह program 100 mg dose को हर 4 घंटे में आधा करता है, जब तक 10 mg से कम न बचे, और बताता है कि इसमें कितना समय लगा।",
        "keyTerms": [
            {"meaning": "जब तक यह True है, block दोहराओ।"},
            {"meaning": "हर half-life पर amount आधा करो।"},
            {"meaning": "समय गिनो, हर round में 4 घंटे।"},
            {"meaning": "Loop खत्म होता है, और अगली line चलती है।"},
        ],
    },
    "errors": {
        "intro": "while, break और continue के साथ ये दो errors आम हैं।",
        "examples": [
            {"title": "Value देने से पहले variable use करना", "md": "`while` line `doses_given` को तब जाँचती है जब उसमें कुछ store ही नहीं हुआ। पहले शुरुआती value दीजिए: `doses_given = 0`।"},
            {"title": "Loop के बाहर break", "md": "`break` और `continue` सिर्फ़ `for` या `while` loop के अंदर काम करते हैं। Loop के बाहर रुकना हो तो `if-else` use कीजिए।"},
        ],
    },
    "mistakes": [
        {"mistake": "Condition वाला variable बदलना भूल जाना, जैसे `stock -= 1` न लिखना", "see": "कोई error नहीं, पर program कभी नहीं रुकता (infinite loop)", "fix": "Stop दबाइए, फिर loop के अंदर ऐसी line जोड़िए जो condition को False की ओर ले जाए।"},
        {"mistake": "Condition उल्टी लिखना, जैसे amount 100 से शुरू हो और `while amount < 10:`", "see": "कोई error नहीं, पर loop कभी चलता ही नहीं", "fix": "ज़ोर से पढ़िए: \"जब तक amount 10 से ज़्यादा है, दोहराओ\" यानी `while amount > 10:`।"},
        {"mistake": "while loop में `continue` को update से पहले रखना, जैसे `i += 1` उसके नीचे", "see": "कोई error नहीं, पर loop एक ही value पर हमेशा अटका रहता है", "fix": "`continue` से पहले variable update कीजिए, या for loop use कीजिए।"},
        {"mistake": "गिनती पता हो फिर भी counter के साथ while use करना", "see": "कोई error नहीं, पर program लंबा और बिगड़ने में आसान", "fix": "कितनी बार, यह पता हो तो `for ... in range(...)` use कीजिए।"},
    ],
    "tasks": [
        {"title": "Stock की उल्टी गिनती", "md": "**while loop** से strips को 3 से नीचे गिनिए, बिल्कुल ऐसे print करते हुए:",
         "hints": ["Loop के अंदर stock -= 1 याद रखिए, वरना यह कभी खत्म नहीं होगा।", "while stock > 0:\n    print(f\"Strips left: {stock}\")\n    stock -= 1"]},
        {"title": "6 घंटे की half-life", "md": "एक दवा 80 mg से शुरू होती है और हर 6 घंटे में आधी होती है। **जब तक amount 10 mg या ज़्यादा है**, आधा करते रहिए, और बिल्कुल ऐसे print कीजिए:",
         "hints": ["Condition है amount >= 10। अंदर: amount = amount / 2 और hours += 6।", "while amount >= 10:\n    amount = amount / 2\n    hours += 6\nprint(\"Below 10 mg after\", hours, \"hours\")"]},
        {"title": "पहले expired batch पर रुकिए", "md": "Expiry years जाँचिए। 2025 से पहले का साल मिले तो उसे print कीजिए और `break` से **रुक जाइए**। Output बिल्कुल यह होना चाहिए:",
         "hints": ["for loop के अंदर: if year < 2025: print कीजिए, फिर break।", "for year in years:\n    if year < 2025:\n        print(\"Expired:\", year)\n        break"]},
        {"title": "Bug ढूँढिए", "md": "इन readings में सिर्फ़ 3 असली हैं; zeros failed readings हैं। Program 5 बताता है, और कोई error नहीं। इसे ठीक कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["क्या zero reading, continue के छोड़ने से पहले ही गिन ली जाती है?", "valid += 1 को if block के नीचे ले जाइए, ताकि zeros उसे छोड़ दें।"],
         "solutionNote": "continue सिर्फ़ अपने बाद वाली lines छोड़ता है। गिनती उससे पहले थी, इसलिए हर reading गिनी गई। गिनती if के बाद रखने से zeros छूट जाते हैं।"},
    ],
    "quiz": [
        {"q": "n = 1\nwhile n < 4:\n    print(n)\n    n += 1\n\nयह क्या print करता है?", "why": "Loop n = 1, 2 और 3 के लिए चलता है। n 4 होने पर n < 4 False है।"},
        {"q": "अगर while loop के अंदर कुछ भी उसकी condition न बदले तो क्या होगा?", "why": "Condition True रहे तो loop घूमता ही रहता है।"},
        {"q": "break क्या करता है?", "why": "break सीधा loop से बाहर कूदता है; loop के बाद वाली line आगे चलती है।"},
        {"q": "continue क्या करता है?", "why": "continue सिर्फ़ इस round के लिए block की बाकी lines छोड़ता है।"},
        {"q": "सही dose type होने तक पूछते रहना है। कौन-सा loop सबसे ठीक है?", "why": "कितनी कोशिशें लगेंगी पता नहीं, इसलिए while (अक्सर while True और break) ठीक है।"},
        {"q": "count = 10\nwhile count > 10:\n    print(\"A\")\n\nA कितनी बार print होता है?", "why": "पहली ही जाँच में 10 > 10 False है, इसलिए block कभी नहीं चलता।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 2.4 · while, break, continue",
        "children": [
            {"label": "while loop", "children": [{"label": "True रहने तक दोहराओ"}, {"label": "हर round से पहले जाँच"}]},
            {"label": "for बनाम while", "children": [{"label": "for: values पता हैं"}, {"label": "while: कुछ होने तक"}]},
            {"label": "Loop खत्म करना", "children": [{"label": "Variable बदलो"}, {"label": "Infinite loop"}, {"label": "Stop / Ctrl + C"}]},
            {"label": "break", "children": [{"label": "अभी loop छोड़ो"}, {"label": "while True + break"}]},
            {"label": "continue", "children": [{"label": "यह round छोड़ो"}, {"label": "continue से पहले update"}]},
            {"label": "Errors", "children": [{"label": "NameError"}, {"label": "'break' outside loop"}]},
        ],
    },
    "summary": [
        "**while loop** अपना block **तब तक** दोहराता है जब तक condition `True` है, हर round से पहले जाँचते हुए।",
        "Values या गिनती पता हो तो **for**; **कुछ होने तक** दोहराना हो तो **while**।",
        "`while` loop के अंदर कुछ condition बदलना चाहिए; वरना **infinite loop** बनता है।",
        "**break** loop तुरंत छोड़ देता है; `while True` और `break` सही जवाब मिलने तक पूछते रहते हैं।",
        "**continue** एक round का बाकी हिस्सा छोड़कर अगले पर जाता है; while loop में उससे पहले variable update कीजिए।",
    ],
}

T["hinglish"] = {
    "hook": {
        "title": "Dawa kab tak khatam hogi?",
        "md": "Ek patient ke shareer mein kisi dawa ki **100 mg** hai. Har **4 ghante** mein uska aadha hissa nikal jaata hai. Yeh samay dawa ki **half-life** hai. Kitne ghante baad **10 mg** se kam bachega?\n\nAapko pehle se nahi pata ki kitni baar aadha karna padega, isliye fixed `range()` wala `for` loop theek nahi baithta. Aapko aisa loop chahiye jo **tab tak** chale **jab tak** kuch sach hai. Yahi aaj ka lesson hai.\n\n*Is lesson ke numbers Python seekhne ke liye banaaye gaye hain. Asli half-life har dawa ki alag hoti hai.*",
    },
    "learn": [
        "**while loop** tab tak kaise dohraata hai jab tak uski condition **True** hai",
        "Kab **while** aur kab **for** use karein",
        "Loop **khatam** ho, yeh kaise pakka karein, aur **infinite loop** kya hai",
        "**break** loop ko jaldi kaise rokta hai, aur **continue** ek round kaise chhodta hai",
    ],
    "explanation": [
        {
            "heading": "Jab tak condition True hai, dohraao",
            "md": "**while loop** apni condition jaanchta hai, `True` ho to block chalaata hai, phir wapas jaakar phir jaanchta hai. Jaise hi condition pehli baar `False` ho, yeh ruk jaata hai.\n\n" + E.C_WHILE + "\n\nYeh `Below 10 mg after 16 hours` print karta hai. Amount aise ghatta hai: 100 → 50 → 25 → 12.5 → 6.25. Chauthi baar aadha karne ke baad `6.25 > 10` `False` hai, isliye loop khatam.\n\nSyntax `if` jaisa hi hai: condition, colon, aur indent kiya block. Fark yeh hai ki `if` apna block **zyada se zyada ek baar** chalaata hai, aur `while` **baar-baar**.",
            "callout": {"title": "while loop", "md": "Aisa loop jo tab tak apna block dohraata hai jab tak condition True hai. Har round se pehle condition jaanchi jaati hai."},
        },
        {
            "heading": "for ya while?",
            "md": FW["hinglish"] + "\n\nKai problems dono tarah likhi ja sakti hain, par sahi chunaav program ko chhota aur saaf banaata hai.",
        },
        {
            "heading": "Pakka kijiye ki loop khatam ho",
            "md": "`while` block ke andar kuch aisa hona chahiye jo condition badle, warna loop kabhi nahi rukega:\n\n" + E.C_STOCK + "\n\nYeh print karta hai:\n\n" + E.O_STOCK + "\n\n`stock -= 1` har round mein stock ek kam karta hai. Iske bina `stock > 0` hamesha `True` rehta, aur program bina ruke `Dispense one strip` print karta rehta. Ise **infinite loop** kehte hain.",
            "callout": {"title": "Infinite loop mein phans gaye?", "md": "IDE mein Stop button dabaaiye, ya terminal mein Ctrl + C. Phir dekhiye ki loop condition wale variable ko badalta hai ya nahi."},
        },
        {
            "heading": "break: loop abhi roko",
            "md": "**break** loop ko turant khatam kar deta hai, bhale values bachi hon. Yeh `for` aur `while` dono mein kaam karta hai. Yahaan pharmacist pehla expired batch milne tak batches jaanchta hai:\n\n" + E.C_BREAK + "\n\nYeh print karta hai:\n\n" + E.O_BREAK + "\n\n2028 kabhi jaancha hi nahi gaya: `break` seedha loop se bahar kood gaya.\n\nEk aam pattern hai `while True` ke saath `break`: sahi jawaab milne tak poochhte raho.\n\n" + E.C_ASK + "\n\n`while True` akele hamesha chalta; `break` hi bahar nikalne ka akela raasta hai.",
        },
        {
            "heading": "continue: agle round par jaao",
            "md": "**continue** block ka baaki hissa **sirf is round ke liye** chhod deta hai, aur seedha agli value par jaata hai. Reading fail hone par thermometer kabhi-kabhi 0 save kar deta hai:\n\n" + E.C_CONT + "\n\nYeh print karta hai:\n\n" + E.O_CONT + "\n\n`break` loop ko hamesha ke liye chhod deta hai; `continue` bas agle round par chala jaata hai.",
            "callout": {"title": "while loop mein continue", "md": "while loop mein variable ko continue se pehle update kijiye. Warna update bhi chhoot jaayega, aur loop kabhi khatam nahi hoga."},
        },
    ],
    "walkthrough": {
        "intro": "Yeh program 100 mg dose ko har 4 ghante mein aadha karta hai, jab tak 10 mg se kam na bache, aur batata hai ki ismein kitna samay laga.",
        "keyTerms": [
            {"meaning": "Jab tak yeh True hai, block dohraao."},
            {"meaning": "Har half-life par amount aadha karo."},
            {"meaning": "Samay gino, har round mein 4 ghante."},
            {"meaning": "Loop khatam hota hai, aur agli line chalti hai."},
        ],
    },
    "errors": {
        "intro": "while, break aur continue ke saath yeh do errors aam hain.",
        "examples": [
            {"title": "Value dene se pehle variable use karna", "md": "`while` line `doses_given` ko tab jaanchti hai jab usmein kuch store hi nahi hua. Pehle shuruaati value dijiye: `doses_given = 0`."},
            {"title": "Loop ke bahar break", "md": "`break` aur `continue` sirf `for` ya `while` loop ke andar kaam karte hain. Loop ke bahar rukna ho to `if-else` use kijiye."},
        ],
    },
    "mistakes": [
        {"mistake": "Condition wala variable badalna bhool jaana, jaise `stock -= 1` na likhna", "see": "Koi error nahi, par program kabhi nahi rukta (infinite loop)", "fix": "Stop dabaaiye, phir loop ke andar aisi line jodiye jo condition ko False ki or le jaaye."},
        {"mistake": "Condition ulti likhna, jaise amount 100 se shuru ho aur `while amount < 10:`", "see": "Koi error nahi, par loop kabhi chalta hi nahi", "fix": "Zor se padhiye: \"jab tak amount 10 se zyada hai, dohraao\" yaani `while amount > 10:`."},
        {"mistake": "while loop mein `continue` ko update se pehle rakhna, jaise `i += 1` uske neeche", "see": "Koi error nahi, par loop ek hi value par hamesha atka rehta hai", "fix": "`continue` se pehle variable update kijiye, ya for loop use kijiye."},
        {"mistake": "Ginti pata ho phir bhi counter ke saath while use karna", "see": "Koi error nahi, par program lamba aur bigadne mein aasaan", "fix": "Kitni baar, yeh pata ho to `for ... in range(...)` use kijiye."},
    ],
    "tasks": [
        {"title": "Stock ki ulti ginti", "md": "**while loop** se strips ko 3 se neeche giniye, bilkul aise print karte hue:",
         "hints": ["Loop ke andar stock -= 1 yaad rakhiye, warna yeh kabhi khatam nahi hoga.", "while stock > 0:\n    print(f\"Strips left: {stock}\")\n    stock -= 1"]},
        {"title": "6 ghante ki half-life", "md": "Ek dawa 80 mg se shuru hoti hai aur har 6 ghante mein aadhi hoti hai. **Jab tak amount 10 mg ya zyada hai**, aadha karte rahiye, aur bilkul aise print kijiye:",
         "hints": ["Condition hai amount >= 10. Andar: amount = amount / 2 aur hours += 6.", "while amount >= 10:\n    amount = amount / 2\n    hours += 6\nprint(\"Below 10 mg after\", hours, \"hours\")"]},
        {"title": "Pehle expired batch par rukiye", "md": "Expiry years jaanchiye. 2025 se pehle ka saal mile to use print kijiye aur `break` se **ruk jaaiye**. Output bilkul yeh hona chahiye:",
         "hints": ["for loop ke andar: if year < 2025: print kijiye, phir break.", "for year in years:\n    if year < 2025:\n        print(\"Expired:\", year)\n        break"]},
        {"title": "Bug dhoondhiye", "md": "In readings mein sirf 3 asli hain; zeros failed readings hain. Program 5 batata hai, aur koi error nahi. Ise theek kijiye taaki output bilkul yeh ho:",
         "hints": ["Kya zero reading, continue ke chhodne se pehle hi gin li jaati hai?", "valid += 1 ko if block ke neeche le jaaiye, taaki zeros use chhod dein."],
         "solutionNote": "continue sirf apne baad wali lines chhodta hai. Ginti usse pehle thi, isliye har reading gini gayi. Ginti if ke baad rakhne se zeros chhoot jaate hain."},
    ],
    "quiz": [
        {"q": "n = 1\nwhile n < 4:\n    print(n)\n    n += 1\n\nYeh kya print karta hai?", "why": "Loop n = 1, 2 aur 3 ke liye chalta hai. n 4 hone par n < 4 False hai."},
        {"q": "Agar while loop ke andar kuch bhi uski condition na badle to kya hoga?", "why": "Condition True rahe to loop ghoomta hi rehta hai."},
        {"q": "break kya karta hai?", "why": "break seedha loop se bahar koodta hai; loop ke baad wali line aage chalti hai."},
        {"q": "continue kya karta hai?", "why": "continue sirf is round ke liye block ki baaki lines chhodta hai."},
        {"q": "Sahi dose type hone tak poochhte rehna hai. Kaun-sa loop sabse theek hai?", "why": "Kitni koshishein lagengi pata nahi, isliye while (aksar while True aur break) theek hai."},
        {"q": "count = 10\nwhile count > 10:\n    print(\"A\")\n\nA kitni baar print hota hai?", "why": "Pehli hi jaanch mein 10 > 10 False hai, isliye block kabhi nahi chalta."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 2.4 · while, break, continue",
        "children": [
            {"label": "while loop", "children": [{"label": "True rehne tak dohraao"}, {"label": "Har round se pehle jaanch"}]},
            {"label": "for vs while", "children": [{"label": "for: values pata hain"}, {"label": "while: kuch hone tak"}]},
            {"label": "Loop khatam karna", "children": [{"label": "Variable badlo"}, {"label": "Infinite loop"}, {"label": "Stop / Ctrl + C"}]},
            {"label": "break", "children": [{"label": "Abhi loop chhodo"}, {"label": "while True + break"}]},
            {"label": "continue", "children": [{"label": "Yeh round chhodo"}, {"label": "continue se pehle update"}]},
            {"label": "Errors", "children": [{"label": "NameError"}, {"label": "'break' outside loop"}]},
        ],
    },
    "summary": [
        "**while loop** apna block **tab tak** dohraata hai jab tak condition `True` hai, har round se pehle jaanchte hue.",
        "Values ya ginti pata ho to **for**; **kuch hone tak** dohraana ho to **while**.",
        "`while` loop ke andar kuch condition badalna chahiye; warna **infinite loop** banta hai.",
        "**break** loop turant chhod deta hai; `while True` aur `break` sahi jawaab milne tak poochhte rehte hain.",
        "**continue** ek round ka baaki hissa chhodkar agle par jaata hai; while loop mein usse pehle variable update kijiye.",
    ],
}

T["kn"] = {
    "hook": {
        "title": "ಔಷಧ ಯಾವಾಗ ಖಾಲಿ ಆಗುತ್ತೆ?",
        "md": "ಒಬ್ಬ patient ನ ದೇಹದಲ್ಲಿ ಒಂದು ಔಷಧದ **100 mg** ಇದೆ. ಪ್ರತಿ **4 ಗಂಟೆಗೆ** ಅದರ ಅರ್ಧ ಹೊರಹೋಗುತ್ತೆ. ಆ ಸಮಯವೇ ಔಷಧದ **half-life**. ಎಷ್ಟು ಗಂಟೆ ಆದಮೇಲೆ **10 mg** ಗಿಂತ ಕಡಿಮೆ ಉಳಿಯುತ್ತೆ?\n\nಎಷ್ಟು ಸಲ ಅರ್ಧ ಮಾಡಬೇಕು ಅಂತ ಮುಂಚೆಯೇ ಗೊತ್ತಿಲ್ಲ, ಅದಕ್ಕೇ fixed `range()` ಇರುವ `for` loop ಸರಿಹೊಂದಲ್ಲ. ಏನೋ ನಿಜ **ಆಗಿರುವವರೆಗೆ** ಮುಂದುವರಿಯುವ loop ಬೇಕು. ಇದೇ ಇವತ್ತಿನ lesson.\n\n*ಈ lesson ನ numbers Python ಕಲಿಯಲು ಮಾಡಿದವು. ನಿಜವಾದ half-life ಔಷಧದಿಂದ ಔಷಧಕ್ಕೆ ಬೇರೆ.*",
    },
    "learn": [
        "Condition **True** ಆಗಿರುವವರೆಗೆ **while loop** ಹೇಗೆ ಪುನರಾವರ್ತಿಸುತ್ತೆ",
        "ಯಾವಾಗ **while** ಮತ್ತು ಯಾವಾಗ **for** ಬಳಸಬೇಕು",
        "Loop **ಮುಗಿಯುವುದನ್ನು** ಹೇಗೆ ಖಚಿತಪಡಿಸುವುದು, ಮತ್ತು **infinite loop** ಅಂದರೆ ಏನು",
        "**break** loop ಅನ್ನು ಬೇಗ ಹೇಗೆ ನಿಲ್ಲಿಸುತ್ತೆ, **continue** ಒಂದು ಸುತ್ತು ಹೇಗೆ ಬಿಡುತ್ತೆ",
    ],
    "explanation": [
        {
            "heading": "Condition True ಆಗಿರುವವರೆಗೆ ಪುನರಾವರ್ತಿಸಿ",
            "md": "**while loop** ತನ್ನ condition check ಮಾಡುತ್ತೆ, `True` ಆದರೆ block run ಮಾಡುತ್ತೆ, ಆಮೇಲೆ ಹಿಂತಿರುಗಿ ಮತ್ತೆ check ಮಾಡುತ್ತೆ. Condition ಮೊದಲ ಸಲ `False` ಆದ ತಕ್ಷಣ ನಿಲ್ಲುತ್ತೆ.\n\n" + E.C_WHILE + "\n\nಇದು `Below 10 mg after 16 hours` print ಮಾಡುತ್ತೆ. Amount ಹೀಗೆ ಕಡಿಮೆ ಆಗುತ್ತೆ: 100 → 50 → 25 → 12.5 → 6.25. ನಾಲ್ಕನೇ ಸಲ ಅರ್ಧ ಮಾಡಿದಮೇಲೆ `6.25 > 10` `False`, ಅದಕ್ಕೇ loop ಮುಗಿಯುತ್ತೆ.\n\nSyntax `if` ತರಹವೇ: condition, colon, ಮತ್ತು indent ಮಾಡಿದ block. ವ್ಯತ್ಯಾಸ ಅಂದರೆ `if` ತನ್ನ block ಅನ್ನು **ಹೆಚ್ಚೆಂದರೆ ಒಂದು ಸಲ** run ಮಾಡುತ್ತೆ, `while` **ಮತ್ತೆ ಮತ್ತೆ**.",
            "callout": {"title": "while loop", "md": "Condition True ಆಗಿರುವವರೆಗೆ ತನ್ನ block ಪುನರಾವರ್ತಿಸುವ loop. ಪ್ರತಿ ಸುತ್ತಿಗೆ ಮುಂಚೆ condition check ಆಗುತ್ತೆ."},
        },
        {
            "heading": "for ಅಥವಾ while?",
            "md": FW["kn"] + "\n\nಹಲವು problems ಎರಡೂ ರೀತಿ ಬರೆಯಬಹುದು, ಆದರೆ ಸರಿಯಾದ ಆಯ್ಕೆ program ಅನ್ನು ಚಿಕ್ಕದಾಗಿ, ಸ್ಪಷ್ಟವಾಗಿ ಮಾಡುತ್ತೆ.",
        },
        {
            "heading": "Loop ಮುಗಿಯುವುದನ್ನು ಖಚಿತಪಡಿಸಿ",
            "md": "`while` block ಒಳಗೆ condition ಬದಲಾಯಿಸುವ ಏನಾದರೂ ಇರಬೇಕು, ಇಲ್ಲದಿದ್ದರೆ loop ಯಾವತ್ತೂ ನಿಲ್ಲಲ್ಲ:\n\n" + E.C_STOCK + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_STOCK + "\n\n`stock -= 1` ಪ್ರತಿ ಸುತ್ತಿನಲ್ಲಿ stock ಅನ್ನು ಒಂದು ಕಡಿಮೆ ಮಾಡುತ್ತೆ. ಇದು ಇಲ್ಲದಿದ್ದರೆ `stock > 0` ಯಾವಾಗಲೂ `True`, program ನಿಲ್ಲದೆ `Dispense one strip` print ಮಾಡುತ್ತಲೇ ಇರುತ್ತೆ. ಇದಕ್ಕೆ **infinite loop** ಅಂತಾರೆ.",
            "callout": {"title": "Infinite loop ನಲ್ಲಿ ಸಿಕ್ಕಿಕೊಂಡಿರಾ?", "md": "IDE ನಲ್ಲಿ Stop button ಒತ್ತಿ, ಅಥವಾ terminal ನಲ್ಲಿ Ctrl + C. ಆಮೇಲೆ loop condition ನ variable ಅನ್ನು ಬದಲಾಯಿಸುತ್ತಾ ಅಂತ check ಮಾಡಿ."},
        },
        {
            "heading": "break: loop ಈಗಲೇ ನಿಲ್ಲಿಸಿ",
            "md": "**break** values ಉಳಿದಿದ್ದರೂ loop ಅನ್ನು ತಕ್ಷಣ ಮುಗಿಸುತ್ತೆ. ಇದು `for` ಮತ್ತು `while` ಎರಡರಲ್ಲೂ ಕೆಲಸ ಮಾಡುತ್ತೆ. ಇಲ್ಲಿ pharmacist ಮೊದಲ expired batch ಸಿಗುವವರೆಗೆ batches check ಮಾಡುತ್ತಾರೆ:\n\n" + E.C_BREAK + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_BREAK + "\n\n2028 check ಆಗಲೇ ಇಲ್ಲ: `break` ನೇರವಾಗಿ loop ಇಂದ ಹೊರಗೆ ಜಿಗಿಯಿತು.\n\nಒಂದು ಸಾಮಾನ್ಯ pattern `while True` ಜೊತೆ `break`: ಸರಿಯಾದ ಉತ್ತರ ಬರುವವರೆಗೆ ಕೇಳುತ್ತಲೇ ಇರಿ.\n\n" + E.C_ASK + "\n\n`while True` ತಾನಾಗಿ ಯಾವಾಗಲೂ run ಆಗುತ್ತೆ; `break` ಒಂದೇ ಹೊರಗೆ ಬರುವ ದಾರಿ.",
        },
        {
            "heading": "continue: ಮುಂದಿನ ಸುತ್ತಿಗೆ ಹೋಗಿ",
            "md": "**continue** block ನ ಉಳಿದ ಭಾಗವನ್ನು **ಈ ಸುತ್ತಿಗೆ ಮಾತ್ರ** ಬಿಟ್ಟು, ನೇರವಾಗಿ ಮುಂದಿನ value ಗೆ ಹೋಗುತ್ತೆ. Reading fail ಆದಾಗ thermometer ಕೆಲವೊಮ್ಮೆ 0 save ಮಾಡುತ್ತೆ:\n\n" + E.C_CONT + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_CONT + "\n\n`break` loop ಅನ್ನು ಶಾಶ್ವತವಾಗಿ ಬಿಡುತ್ತೆ; `continue` ಮುಂದಿನ ಸುತ್ತಿಗೆ ಮಾತ್ರ ಹೋಗುತ್ತೆ.",
            "callout": {"title": "while loop ನಲ್ಲಿ continue", "md": "while loop ನಲ್ಲಿ continue ಗಿಂತ ಮುಂಚೆ variable update ಮಾಡಿ. ಇಲ್ಲದಿದ್ದರೆ update ಕೂಡ ಬಿಟ್ಟುಹೋಗುತ್ತೆ, loop ಯಾವತ್ತೂ ಮುಗಿಯಲ್ಲ."},
        },
    ],
    "walkthrough": {
        "intro": "ಈ program 100 mg dose ಅನ್ನು 10 mg ಗಿಂತ ಕಡಿಮೆ ಉಳಿಯುವವರೆಗೆ ಪ್ರತಿ 4 ಗಂಟೆಗೆ ಅರ್ಧ ಮಾಡಿ, ಅದಕ್ಕೆ ಎಷ್ಟು ಸಮಯ ಆಯ್ತು ಅಂತ ಹೇಳುತ್ತೆ.",
        "keyTerms": [
            {"meaning": "ಇದು True ಆಗಿರುವವರೆಗೆ block ಪುನರಾವರ್ತಿಸು."},
            {"meaning": "ಪ್ರತಿ half-life ಗೆ amount ಅರ್ಧ ಮಾಡು."},
            {"meaning": "ಸಮಯ ಎಣಿಸು, ಪ್ರತಿ ಸುತ್ತಿಗೆ 4 ಗಂಟೆ."},
            {"meaning": "Loop ಮುಗಿಯುತ್ತೆ, ಮುಂದಿನ line run ಆಗುತ್ತೆ."},
        ],
    },
    "errors": {
        "intro": "while, break ಮತ್ತು continue ಜೊತೆ ಈ ಎರಡು errors ಸಾಮಾನ್ಯ.",
        "examples": [
            {"title": "Value ಕೊಡುವ ಮುಂಚೆ variable ಬಳಸುವುದು", "md": "ಏನೂ store ಆಗುವ ಮುಂಚೆಯೇ `while` line `doses_given` ಅನ್ನು check ಮಾಡುತ್ತೆ. ಮೊದಲು ಶುರುವಿನ value ಕೊಡಿ: `doses_given = 0`."},
            {"title": "Loop ಹೊರಗೆ break", "md": "`break` ಮತ್ತು `continue` `for` ಅಥವಾ `while` loop ಒಳಗೆ ಮಾತ್ರ ಕೆಲಸ ಮಾಡುತ್ತವೆ. Loop ಹೊರಗೆ ನಿಲ್ಲಿಸಲು `if-else` ಬಳಸಿ."},
        ],
    },
    "mistakes": [
        {"mistake": "Condition ನ variable ಬದಲಾಯಿಸಲು ಮರೆಯುವುದು, ಉದಾ. `stock -= 1` ಇಲ್ಲದಿರುವುದು", "see": "Error ಇಲ್ಲ, ಆದರೆ program ಯಾವತ್ತೂ ನಿಲ್ಲಲ್ಲ (infinite loop)", "fix": "Stop ಒತ್ತಿ, ಆಮೇಲೆ condition ಅನ್ನು False ಕಡೆಗೆ ಸರಿಸುವ line ಅನ್ನು loop ಒಳಗೆ ಸೇರಿಸಿ."},
        {"mistake": "Condition ಅನ್ನು ತಿರುಗುಮುರುಗು ಬರೆಯುವುದು, ಉದಾ. amount 100 ಇಂದ ಶುರುವಾದಾಗ `while amount < 10:`", "see": "Error ಇಲ್ಲ, ಆದರೆ loop ಒಮ್ಮೆಯೂ run ಆಗಲ್ಲ", "fix": "ಜೋರಾಗಿ ಓದಿ: \"amount 10 ಕ್ಕಿಂತ ಜಾಸ್ತಿ ಇರುವವರೆಗೆ ಪುನರಾವರ್ತಿಸು\" ಅಂದರೆ `while amount > 10:`."},
        {"mistake": "while loop ನಲ್ಲಿ `continue` ಅನ್ನು update ಗಿಂತ ಮುಂಚೆ ಇಡುವುದು, ಉದಾ. `i += 1` ಅದರ ಕೆಳಗೆ", "see": "Error ಇಲ್ಲ, ಆದರೆ loop ಒಂದೇ value ನಲ್ಲಿ ಶಾಶ್ವತವಾಗಿ ಸಿಕ್ಕಿಕೊಳ್ಳುತ್ತೆ", "fix": "`continue` ಗಿಂತ ಮುಂಚೆ variable update ಮಾಡಿ, ಅಥವಾ for loop ಬಳಸಿ."},
        {"mistake": "ಎಣಿಕೆ ಗೊತ್ತಿದ್ದರೂ counter ಜೊತೆ while ಬಳಸುವುದು", "see": "Error ಇಲ್ಲ, ಆದರೆ program ಉದ್ದ, ಕೆಡುವುದು ಸುಲಭ", "fix": "ಎಷ್ಟು ಸಲ ಅಂತ ಗೊತ್ತಿದ್ದರೆ `for ... in range(...)` ಬಳಸಿ."},
    ],
    "tasks": [
        {"title": "Stock ಅನ್ನು ಕೆಳಗೆ ಎಣಿಸಿ", "md": "**while loop** ಬಳಸಿ strips ಅನ್ನು 3 ರಿಂದ ಕೆಳಗೆ ಎಣಿಸಿ, ಸರಿಯಾಗಿ ಹೀಗೆ print ಮಾಡಿ:",
         "hints": ["Loop ಒಳಗೆ stock -= 1 ನೆನಪಿಡಿ, ಇಲ್ಲದಿದ್ದರೆ ಅದು ಮುಗಿಯಲ್ಲ.", "while stock > 0:\n    print(f\"Strips left: {stock}\")\n    stock -= 1"]},
        {"title": "6 ಗಂಟೆಯ half-life", "md": "ಒಂದು ಔಷಧ 80 mg ಇಂದ ಶುರುವಾಗಿ ಪ್ರತಿ 6 ಗಂಟೆಗೆ ಅರ್ಧ ಆಗುತ್ತೆ. **Amount 10 mg ಅಥವಾ ಹೆಚ್ಚು ಇರುವವರೆಗೆ** ಅರ್ಧ ಮಾಡುತ್ತಾ ಇರಿ, ಮತ್ತು ಸರಿಯಾಗಿ ಹೀಗೆ print ಮಾಡಿ:",
         "hints": ["Condition amount >= 10. ಒಳಗೆ: amount = amount / 2 ಮತ್ತು hours += 6.", "while amount >= 10:\n    amount = amount / 2\n    hours += 6\nprint(\"Below 10 mg after\", hours, \"hours\")"]},
        {"title": "ಮೊದಲ expired batch ನಲ್ಲಿ ನಿಲ್ಲಿ", "md": "Expiry years check ಮಾಡಿ. 2025 ಕ್ಕಿಂತ ಮುಂಚಿನ ವರ್ಷ ಸಿಕ್ಕಾಗ ಅದನ್ನು print ಮಾಡಿ `break` ಇಂದ **ನಿಲ್ಲಿ**. Output ಸರಿಯಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["for loop ಒಳಗೆ: if year < 2025: print ಮಾಡಿ, ಆಮೇಲೆ break.", "for year in years:\n    if year < 2025:\n        print(\"Expired:\", year)\n        break"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "ಈ readings ನಲ್ಲಿ 3 ಮಾತ್ರ ನಿಜವಾದವು; zeros fail ಆದ readings. Program 5 ಅಂತ ಹೇಳುತ್ತೆ, error ಇಲ್ಲ. Output ಸರಿಯಾಗಿ ಹೀಗೇ ಬರುವ ಹಾಗೆ ಸರಿ ಮಾಡಿ:",
         "hints": ["continue ಬಿಡುವ ಮುಂಚೆಯೇ zero reading ಎಣಿಕೆ ಆಗುತ್ತಾ?", "valid += 1 ಅನ್ನು if block ಕೆಳಗೆ ಸರಿಸಿ, ಆಗ zeros ಅದನ್ನು ಬಿಡುತ್ತವೆ."],
         "solutionNote": "continue ತನ್ನ ನಂತರದ lines ಮಾತ್ರ ಬಿಡುತ್ತೆ. ಎಣಿಕೆ ಅದಕ್ಕಿಂತ ಮುಂಚೆ ಇತ್ತು, ಅದಕ್ಕೇ ಪ್ರತಿ reading ಎಣಿಕೆ ಆಯ್ತು. ಎಣಿಕೆಯನ್ನು if ನಂತರ ಇಟ್ಟರೆ zeros ಬಿಟ್ಟುಹೋಗುತ್ತವೆ."},
    ],
    "quiz": [
        {"q": "n = 1\nwhile n < 4:\n    print(n)\n    n += 1\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "Loop n = 1, 2 ಮತ್ತು 3 ಕ್ಕೆ run ಆಗುತ್ತೆ. n 4 ಆದಾಗ n < 4 False."},
        {"q": "while loop ಒಳಗೆ ಯಾವುದೂ ಅದರ condition ಬದಲಾಯಿಸದಿದ್ದರೆ ಏನಾಗುತ್ತೆ?", "why": "Condition True ಆಗಿಯೇ ಉಳಿದರೆ loop ಸುತ್ತುತ್ತಲೇ ಇರುತ್ತೆ."},
        {"q": "break ಏನು ಮಾಡುತ್ತೆ?", "why": "break ನೇರವಾಗಿ loop ಇಂದ ಹೊರಗೆ ಜಿಗಿಯುತ್ತೆ; loop ನಂತರದ line ಮುಂದೆ run ಆಗುತ್ತೆ."},
        {"q": "continue ಏನು ಮಾಡುತ್ತೆ?", "why": "continue ಈ ಸುತ್ತಿಗೆ ಮಾತ್ರ block ನ ಉಳಿದ lines ಬಿಡುತ್ತೆ."},
        {"q": "ಸರಿಯಾದ dose type ಆಗುವವರೆಗೆ ಕೇಳುತ್ತಾ ಇರಬೇಕು. ಯಾವ loop ಹೆಚ್ಚು ಸೂಕ್ತ?", "why": "ಎಷ್ಟು ಪ್ರಯತ್ನ ಬೇಕು ಅಂತ ಗೊತ್ತಿಲ್ಲ, ಅದಕ್ಕೇ while (ಹೆಚ್ಚಾಗಿ while True ಮತ್ತು break) ಸೂಕ್ತ."},
        {"q": "count = 10\nwhile count > 10:\n    print(\"A\")\n\nA ಎಷ್ಟು ಸಲ print ಆಗುತ್ತೆ?", "why": "ಮೊದಲ check ನಲ್ಲೇ 10 > 10 False, ಅದಕ್ಕೇ block ಒಮ್ಮೆಯೂ run ಆಗಲ್ಲ."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 2.4 · while, break, continue",
        "children": [
            {"label": "while loop", "children": [{"label": "True ಇರುವವರೆಗೆ ಪುನರಾವರ್ತನೆ"}, {"label": "ಪ್ರತಿ ಸುತ್ತಿಗೆ ಮುಂಚೆ check"}]},
            {"label": "for ಮತ್ತು while", "children": [{"label": "for: values ಗೊತ್ತು"}, {"label": "while: ಏನಾದರೂ ಆಗುವವರೆಗೆ"}]},
            {"label": "Loop ಮುಗಿಸುವುದು", "children": [{"label": "Variable ಬದಲಾಯಿಸಿ"}, {"label": "Infinite loop"}, {"label": "Stop / Ctrl + C"}]},
            {"label": "break", "children": [{"label": "ಈಗಲೇ loop ಬಿಡಿ"}, {"label": "while True + break"}]},
            {"label": "continue", "children": [{"label": "ಈ ಸುತ್ತು ಬಿಡಿ"}, {"label": "continue ಗೆ ಮುಂಚೆ update"}]},
            {"label": "Errors", "children": [{"label": "NameError"}, {"label": "'break' outside loop"}]},
        ],
    },
    "summary": [
        "**while loop** condition `True` ಆಗಿರುವ **ವರೆಗೆ** ತನ್ನ block ಪುನರಾವರ್ತಿಸುತ್ತೆ, ಪ್ರತಿ ಸುತ್ತಿಗೆ ಮುಂಚೆ check ಮಾಡುತ್ತಾ.",
        "Values ಅಥವಾ ಎಣಿಕೆ ಗೊತ್ತಿದ್ದರೆ **for**; **ಏನಾದರೂ ಆಗುವವರೆಗೆ** ಪುನರಾವರ್ತಿಸಬೇಕಾದರೆ **while**.",
        "`while` loop ಒಳಗೆ ಏನಾದರೂ condition ಬದಲಾಯಿಸಬೇಕು; ಇಲ್ಲದಿದ್ದರೆ **infinite loop** ಆಗುತ್ತೆ.",
        "**break** loop ಅನ್ನು ತಕ್ಷಣ ಬಿಡುತ್ತೆ; `while True` ಮತ್ತು `break` ಸರಿಯಾದ ಉತ್ತರ ಬರುವವರೆಗೆ ಕೇಳುತ್ತಲೇ ಇರುತ್ತವೆ.",
        "**continue** ಒಂದು ಸುತ್ತಿನ ಉಳಿದ ಭಾಗ ಬಿಟ್ಟು ಮುಂದಿನದಕ್ಕೆ ಹೋಗುತ್ತೆ; while loop ನಲ್ಲಿ ಅದಕ್ಕಿಂತ ಮುಂಚೆ variable update ಮಾಡಿ.",
    ],
}

NARR = {
    "hi": [
        "यह program तब तक दोहराता है जब तक कोई condition False न हो जाए। हमें पहले से नहीं पता कि कितने rounds लगेंगे।",
        "Comment सवाल बताता है।",
        "amount सौ milligram से शुरू होता है।",
        "hours zero से शुरू होता है।",
        "while जाँचता है: क्या amount दस से ज़्यादा है? सौ है, इसलिए Python block में जाता है।",
        "Amount आधा होकर पचास हो जाता है।",
        "चार घंटे बीत गए।",
        "वापस while line पर। पचास अब भी दस से ज़्यादा है, इसलिए फिर घूमता है: पच्चीस, फिर बारह दशमलव पाँच। Hours बढ़कर बारह।",
        "बारह दशमलव पाँच अब भी दस से ज़्यादा है, इसलिए एक round और: छह दशमलव दो पाँच milligram, सोलह घंटे पर।",
        "अब: क्या छह दशमलव दो पाँच, दस से ज़्यादा है? नहीं। Condition False है, इसलिए loop खत्म।",
        "print घंटे दिखाता है।",
        "और जितना amount बचा है।",
    ],
    "hinglish": [
        "Yeh program tab tak dohraata hai jab tak koi condition False na ho jaaye. Humein pehle se nahi pata ki kitne rounds lagenge.",
        "Comment sawaal batata hai.",
        "amount sau milligram se shuru hota hai.",
        "hours zero se shuru hota hai.",
        "while jaanchta hai: kya amount das se zyada hai? Sau hai, isliye Python block mein jaata hai.",
        "Amount aadha hokar pachaas ho jaata hai.",
        "Chaar ghante beet gaye.",
        "Wapas while line par. Pachaas ab bhi das se zyada hai, isliye phir ghoomta hai: pachchees, phir baarah dashamlav paanch. Hours badhkar baarah.",
        "Baarah dashamlav paanch ab bhi das se zyada hai, isliye ek round aur: chhah dashamlav do paanch milligram, solah ghante par.",
        "Ab: kya chhah dashamlav do paanch, das se zyada hai? Nahi. Condition False hai, isliye loop khatam.",
        "print ghante dikhaata hai.",
        "Aur jitna amount bacha hai.",
    ],
    "kn": [
        "ಈ program ಒಂದು condition False ಆಗುವವರೆಗೆ ಪುನರಾವರ್ತಿಸುತ್ತೆ. ಎಷ್ಟು ಸುತ್ತು ಬೇಕು ಅಂತ ಮುಂಚೆಯೇ ಗೊತ್ತಿಲ್ಲ.",
        "Comment ಪ್ರಶ್ನೆಯನ್ನು ಹೇಳುತ್ತೆ.",
        "amount ನೂರು milligram ಇಂದ ಶುರುವಾಗುತ್ತೆ.",
        "hours zero ಇಂದ ಶುರುವಾಗುತ್ತೆ.",
        "while check ಮಾಡುತ್ತೆ: amount ಹತ್ತಕ್ಕಿಂತ ಜಾಸ್ತಿ ಇದೆಯಾ? ನೂರು ಇದೆ, ಅದಕ್ಕೇ Python block ಒಳಗೆ ಹೋಗುತ್ತೆ.",
        "Amount ಅರ್ಧ ಆಗಿ ಐವತ್ತು ಆಗುತ್ತೆ.",
        "ನಾಲ್ಕು ಗಂಟೆ ಕಳೆಯಿತು.",
        "ಮತ್ತೆ while line ಗೆ. ಐವತ್ತು ಇನ್ನೂ ಹತ್ತಕ್ಕಿಂತ ಜಾಸ್ತಿ, ಅದಕ್ಕೇ ಮತ್ತೆ ಸುತ್ತುತ್ತೆ: ಇಪ್ಪತ್ತೈದು, ಆಮೇಲೆ ಹನ್ನೆರಡು ಪಾಯಿಂಟ್ ಐದು. Hours ಹನ್ನೆರಡಕ್ಕೆ ಬೆಳೆಯುತ್ತೆ.",
        "ಹನ್ನೆರಡು ಪಾಯಿಂಟ್ ಐದು ಇನ್ನೂ ಹತ್ತಕ್ಕಿಂತ ಜಾಸ್ತಿ, ಅದಕ್ಕೇ ಇನ್ನೊಂದು ಸುತ್ತು: ಆರು ಪಾಯಿಂಟ್ ಎರಡು ಐದು milligram, ಹದಿನಾರು ಗಂಟೆಗೆ.",
        "ಈಗ: ಆರು ಪಾಯಿಂಟ್ ಎರಡು ಐದು, ಹತ್ತಕ್ಕಿಂತ ಜಾಸ್ತಿ ಇದೆಯಾ? ಇಲ್ಲ. Condition False, ಅದಕ್ಕೇ loop ಮುಗಿಯುತ್ತೆ.",
        "print ಗಂಟೆಗಳನ್ನು ತೋರಿಸುತ್ತೆ.",
        "ಮತ್ತು ಉಳಿದ amount ಅನ್ನು.",
    ],
}

ANIM = {
    "hi": [
        "सौ milligram, zero घंटे पर। while line पूछती है: क्या यह दस से ज़्यादा है? हाँ।",
        "आधा हिस्सा निकल जाता है, और चार घंटे बीतते हैं। पचास milligram।",
        "अब भी दस से ज़्यादा, इसलिए यह घूमता रहता है: पच्चीस, फिर बारह दशमलव पाँच।",
        "एक बार और आधा: छह दशमलव दो पाँच, सोलह घंटे पर। अब condition False है।",
        "Loop अपने-आप रुकता है, और जवाब print होता है: सोलह घंटे।",
    ],
    "hinglish": [
        "Sau milligram, zero ghante par. while line poochhti hai: kya yeh das se zyada hai? Haan.",
        "Aadha hissa nikal jaata hai, aur chaar ghante beette hain. Pachaas milligram.",
        "Ab bhi das se zyada, isliye yeh ghoomta rehta hai: pachchees, phir baarah dashamlav paanch.",
        "Ek baar aur aadha: chhah dashamlav do paanch, solah ghante par. Ab condition False hai.",
        "Loop apne-aap rukta hai, aur jawaab print hota hai: solah ghante.",
    ],
    "kn": [
        "ನೂರು milligram, zero ಗಂಟೆಗೆ. while line ಕೇಳುತ್ತೆ: ಇದು ಹತ್ತಕ್ಕಿಂತ ಜಾಸ್ತಿ ಇದೆಯಾ? ಹೌದು.",
        "ಅರ್ಧ ಹೊರಹೋಗುತ್ತೆ, ನಾಲ್ಕು ಗಂಟೆ ಕಳೆಯುತ್ತೆ. ಐವತ್ತು milligram.",
        "ಇನ್ನೂ ಹತ್ತಕ್ಕಿಂತ ಜಾಸ್ತಿ, ಅದಕ್ಕೇ ಸುತ್ತುತ್ತಲೇ ಇರುತ್ತೆ: ಇಪ್ಪತ್ತೈದು, ಆಮೇಲೆ ಹನ್ನೆರಡು ಪಾಯಿಂಟ್ ಐದು.",
        "ಇನ್ನೊಂದು ಸಲ ಅರ್ಧ: ಆರು ಪಾಯಿಂಟ್ ಎರಡು ಐದು, ಹದಿನಾರು ಗಂಟೆಗೆ. ಈಗ condition False.",
        "Loop ತಾನಾಗಿ ನಿಲ್ಲುತ್ತೆ, ಉತ್ತರ print ಆಗುತ್ತೆ: ಹದಿನಾರು ಗಂಟೆ.",
    ],
}

if __name__ == "__main__":
    build("2-4", "anim-halflife", T, NARR, ANIM)

"""Lesson 3.5 translations (Hindi, Hinglish, Kannada) and voice scripts."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import build  # noqa: E402

_spec = importlib.util.spec_from_file_location("en35", os.path.join(os.path.dirname(__file__), "..", "lessons", "bp101t_3-5_en.py"))
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)

T = {}

T["hi"] = {
    "hook": {
        "title": "वह file जो हर pharmacy के पास पहले से है",
        "md": "हर hospital pharmacy के billing software में एक **Export** button होता है। उसे दबाइए, और आपको `stock.csv` जैसी एक file मिलती है। Excel में खोलें तो साफ़ table है। Notepad में खोलें तो commas वाली text की lines।\n\nयही सादा format, **CSV**, lab instruments, hospital systems और सरकारी health portals के बीच data बाँटने का तरीका है। अब तक आपका data program के अंदर रहता था और program खत्म होते ही गायब हो जाता था। आज आपके programs data को file में **save** करना और वापस **पढ़ना** सीखेंगे: असली datasets के साथ काम का पहला कदम।",
    },
    "learn": [
        "**CSV** file क्या है, और **with open()** से file **खोलना**, **लिखना** और **पढ़ना**",
        "File **modes** \"r\", \"w\" और \"a\" में फ़र्क",
        "**csv.reader** और **csv.DictReader** हर line को list या dictionary कैसे बनाते हैं",
        "**csv.writer** से rows **लिखना**, और maths से पहले values को **convert** करना क्यों ज़रूरी है",
    ],
    "explanation": [
        {
            "heading": "CSV file क्या है, और उसे लिखना",
            "md": "**CSV** मतलब **Comma-Separated Values**। यह सादा text है: पहली line **header** है जिसमें columns के नाम हैं, और उसके बाद हर line एक record है:\n\n" + E.F_STOCK + "\n\nFile बनाने के लिए उसे **write mode**, `\"w\"`, में खोलिए और `write()` से उसमें text लिखिए। हर line `\\n`, यानी newline character, से खत्म होनी चाहिए:\n\n" + E.C_WRITE + "\n\nयह print करता है:\n\n" + E.O_WRITE + "\n\n`with open(...) as f:` file खोलता है और indent वाला block खत्म होते ही उसे **अपने आप बंद** करता है। बिना mode के खोलने का मतलब **read** mode। `line.strip()` हर line के आखिर का `\\n` हटाता है।",
            "callout": {"title": "Champ Lab में files", "md": "Phone पर Champ Lab file को सिर्फ़ program चलने तक रखता है, इसलिए यहाँ हर example पहले अपनी file लिखता है। Computer पर यही code stock.csv को आपके program के बगल में save करता है, और Excel उसे खोल सकता है।"},
        },
        {
            "heading": "csv.reader से rows पढ़ना",
            "md": "आप हर line को खुद commas पर तोड़ सकते हैं, पर **csv** module यह सही तरीके से करता है, quotes के अंदर commas वाली values के लिए भी। `csv.reader` हर line को **list** के रूप में देता है:\n\n" + E.C_READER + "\n\nयह print करता है:\n\n" + E.O_READER + "\n\nदो बातें ध्यान दीजिए। Header पहले आता है, इसलिए सिर्फ़ data चाहिए तो `next(reader)` से उसे छोड़ दीजिए। और **हर value string है**, `'120'` भी।",
            "callout": {"title": "CSV values text हैं", "md": "\"120\" + 5 error है। पहले convert कीजिए: पूरे numbers के लिए int(row[1]), decimals के लिए float(...)।"},
        },
        {
            "heading": "Rows को dictionaries की तरह पढ़ना",
            "md": "`csv.DictReader` header के नामों को **keys** बनाता है, इसलिए हर row एक **dictionary** है और आप values को column के नाम से ढूँढते हैं। यह ज़्यादा साफ़ है और columns का क्रम बदलने पर भी नहीं टूटता:\n\n" + E.C_DICTREADER + "\n\nयह print करता है:\n\n" + E.O_DICTREADER + "\n\nHeader line print नहीं हुई: DictReader ने उसे keys के लिए use किया। `int()` ने हर text value को number बनाया ताकि वह total में जुड़ सके।",
            "callout": {"title": "Header", "md": "CSV file की पहली line, जिसमें columns के नाम हैं, जैसे drug,strips। DictReader इसे हर row की keys के रूप में use करता है।"},
        },
        {
            "heading": "csv.writer से rows लिखना",
            "md": "कई rows लिखनी हों तो उन्हें lists की list में रखिए और commas व newlines `csv.writer` को जोड़ने दीजिए। File को `newline=\"\"` के साथ खोलिए, इससे Windows पर rows के बीच खाली lines नहीं आतीं:\n\n" + E.C_WRITER + "\n\nयह print करता है:\n\n" + E.O_WRITER + "\n\n`writerow(row)` एक row लिखता है; `writerows(rows)` सारी। Numbers अपने आप text के रूप में लिखे जाते हैं।",
        },
        {
            "heading": "File में जोड़ना, और सारी lines पढ़ना",
            "md": "`\"w\"` से खोलने पर file पहले **मिट** जाती है। आखिर में lines जोड़नी हों तो **append mode**, `\"a\"`, use कीजिए। `readlines()` हर line को एक list में पढ़ता है:\n\n" + E.C_APPEND + "\n\nयह print करता है:\n\n" + E.O_APPEND + "\n\nHeader और दो readings मिलाकर 3 lines हैं, और `lines[-1]` latest reading है। इसी तरह program एक चलता हुआ log रख सकता है, हर measurement की एक line।",
            "callout": {"title": "\"w\" मिटा देता है", "md": "मौजूदा file को \"w\" से खोलने पर उसमें जो था सब मिट जाता है। जोड़ने के लिए \"a\", और सिर्फ़ पढ़ने के लिए \"r\" (या कोई mode नहीं) use कीजिए।"},
        },
    ],
    "walkthrough": {
        "intro": "यह program एक छोटा temperature log CSV file में save करता है, DictReader से वापस पढ़ता है और सबसे ऊँची reading ढूँढता है।",
        "keyTerms": [
            {"meaning": "File बनाओ (या मिटाओ) और लिखने के लिए खोलो।"},
            {"meaning": "File को f के रूप में use करो, और बाद में अपने आप बंद करो।"},
            {"meaning": "हर row को header की keys वाली dictionary के रूप में पढ़ो।"},
            {"meaning": "Text value को number में बदलो।"},
        ],
    },
    "errors": {
        "intro": "ये दो errors लगभग हर पहले file program में आती हैं।",
        "examples": [
            {"title": "ऐसी file खोलना जो है ही नहीं", "md": "Read mode के लिए file मौजूद होनी चाहिए। यहाँ नाम गलत लिखा है (`stock` की जगह `stok`)। Spelling और folder check कीजिए; computer पर file आपके program के बगल में होनी चाहिए, या उसका पूरा path दीजिए। (Champ Lab में Errno के बाद का number अलग हो सकता है; message वही है।)"},
            {"title": "Header को number बनाना", "md": "पहली row header है, इसलिए `row[1]` शब्द `strips` है, जो number नहीं बन सकता। पहले `next(reader)` से header छोड़िए, या `csv.DictReader` use कीजिए।"},
        ],
    },
    "mistakes": [
        {"mistake": "Line जोड़नी थी पर `\"w\"` से खोल दिया", "see": "कोई error नहीं, पर file में जो था सब चला गया", "fix": "आखिर में जोड़ने के लिए `\"a\"` (append) use कीजिए।"},
        {"mistake": "हर `write()` के आखिर में `\\n` भूल जाना", "see": "कोई error नहीं, पर सब एक लंबी line में आ जाता है", "fix": "हर line `\\n` से खत्म कीजिए, या `csv.writer` use कीजिए।"},
        {"mistake": "File से आई value से सीधे maths: `row[\"strips\"] + 5`", "see": "TypeError: can only concatenate str (not \"int\") to str", "fix": "पहले convert कीजिए: `int(row[\"strips\"]) + 5`।"},
        {"mistake": "बिना `with` के file खोलना और `close()` भूल जाना", "see": "Data save नहीं हो सकता, या file locked रहती है", "fix": "हमेशा `with open(...) as f:` use कीजिए।"},
    ],
    "tasks": [
        {"title": "File लिखिए", "md": "पहले `with` block के अंदर stock.csv में header `drug,strips` और row `ORS,30` **लिखिए**, हर एक `\\n` से खत्म। पढ़ने वाला हिस्सा आपके लिए तैयार है। Output बिल्कुल यह होना चाहिए:",
         "hints": ["हर f.write() text जोड़ता है; हर line \\n से खत्म कीजिए।", "f.write(\"drug,strips\\n\")\n    f.write(\"ORS,30\\n\")"]},
        {"title": "Header छोड़िए", "md": "**reader** से **next()** लगाकर header row छोड़िए, फिर हर row से सिर्फ़ drug का नाम print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["next(reader) एक row पढ़कर फेंक देता है।", "next(reader)\n    for row in reader:\n        print(row[0])"]},
        {"title": "CSV से total", "md": "stock.csv को **csv.DictReader** से पढ़िए और **strips** column जोड़िए। हर value को **int()** से convert करना याद रखिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["with open(\"stock.csv\") as f:\n    for row in csv.DictReader(f):", "        total += int(row[\"strips\"])"]},
        {"title": "Bug ढूँढिए", "md": "इस program को header रखकर उसके नीचे एक reading जोड़नी है, पर header गायब हो जाता है। **एक mode** बदलिए ताकि output बिल्कुल यह हो:",
         "hints": ["\"w\" लिखने से पहले file मिटा देता है।", "दूसरी बार file को \"a\" से खोलिए ताकि उसमें जुड़े।"],
         "solutionNote": "दूसरे open में \"w\" था, जिसने header मिटा दिया। \"a\" (append) जो है उसे रखता है और नई line आखिर में जोड़ता है।"},
    ],
    "quiz": [
        {"q": "CSV का पूरा नाम क्या है?", "why": "CSV files values को commas से अलग करती हैं।"},
        {"q": "कौन-सा mode file को मिटाए बिना उसके आखिर में lines जोड़ता है?", "why": "\"a\" append mode है।"},
        {"q": "csv.reader से मिलने वाली values किस type की होती हैं?", "why": "Text file से पढ़ी गई हर चीज़ convert करने तक string होती है।"},
        {"q": "हम with open(...) as f: क्यों लिखते हैं?", "why": "with आपके लिए file बंद करता है, error आने पर भी।"},
        {"q": "csv.DictReader से हर row क्या होती है?", "why": "DictReader header के नामों को keys बनाता है।"},
        {"q": "मौजूदा file को \"w\" से खोलने पर क्या होता है?", "why": "Write mode लिखने से पहले file मिटा देता है।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 3.5 · CSV files",
        "children": [
            {"label": "CSV file", "children": [{"label": "सादा text"}, {"label": "Values के बीच commas"}, {"label": "पहली line = header"}]},
            {"label": "खोलना", "children": [{"label": "with open(name, mode)"}, {"label": "\"r\" \"w\" \"a\""}, {"label": "अपने आप बंद"}]},
            {"label": "पढ़ना", "children": [{"label": "csv.reader → lists"}, {"label": "csv.DictReader → dicts"}, {"label": "next() header छोड़ता है"}]},
            {"label": "लिखना", "children": [{"label": "f.write(text + \\n)"}, {"label": "csv.writer"}, {"label": "writerow / writerows"}]},
            {"label": "Convert", "children": [{"label": "Values text हैं"}, {"label": "int() / float()"}, {"label": "फिर हिसाब"}]},
            {"label": "Errors", "children": [{"label": "FileNotFoundError"}, {"label": "ValueError: header"}]},
        ],
    },
    "summary": [
        "**CSV** file सादा text है: एक **header** line, फिर हर line में एक record, values commas से अलग।",
        "`with open(name, mode) as f:` file खोलता है और अपने आप बंद करता है। Modes: **\"r\"** पढ़ना, **\"w\"** लिखना (मिटाकर), **\"a\"** जोड़ना।",
        "**csv.reader** हर row को list देता है; **csv.DictReader** header की keys वाली dictionary। `next(reader)` header छोड़ता है।",
        "**csv.writer** `writerow()` / `writerows()` से rows लिखता है; `newline=\"\"` के साथ खोलिए।",
        "File से पढ़ी हर value **text** है: maths से पहले `int()` या `float()` से convert कीजिए।",
    ],
}

T["hinglish"] = {
    "hook": {
        "title": "Woh file jo har pharmacy ke paas pehle se hai",
        "md": "Har hospital pharmacy ke billing software mein ek **Export** button hota hai. Use dabaaiye, aur aapko `stock.csv` jaisi ek file milti hai. Excel mein kholein to saaf table hai. Notepad mein kholein to commas wali text ki lines.\n\nYahi saada format, **CSV**, lab instruments, hospital systems aur sarkari health portals ke beech data baantne ka tareeka hai. Ab tak aapka data program ke andar rehta tha aur program khatam hote hi gaayab ho jaata tha. Aaj aapke programs data ko file mein **save** karna aur wapas **padhna** seekhenge: asli datasets ke saath kaam ka pehla kadam.",
    },
    "learn": [
        "**CSV** file kya hai, aur **with open()** se file **kholna**, **likhna** aur **padhna**",
        "File **modes** \"r\", \"w\" aur \"a\" mein farq",
        "**csv.reader** aur **csv.DictReader** har line ko list ya dictionary kaise banaate hain",
        "**csv.writer** se rows **likhna**, aur maths se pehle values ko **convert** karna kyun zaroori hai",
    ],
    "explanation": [
        {
            "heading": "CSV file kya hai, aur use likhna",
            "md": "**CSV** matlab **Comma-Separated Values**. Yeh saada text hai: pehli line **header** hai jismein columns ke naam hain, aur uske baad har line ek record hai:\n\n" + E.F_STOCK + "\n\nFile banaane ke liye use **write mode**, `\"w\"`, mein kholiye aur `write()` se usmein text likhiye. Har line `\\n`, yaani newline character, se khatam honi chahiye:\n\n" + E.C_WRITE + "\n\nYeh print karta hai:\n\n" + E.O_WRITE + "\n\n`with open(...) as f:` file kholta hai aur indent wala block khatam hote hi use **apne aap band** karta hai. Bina mode ke kholne ka matlab **read** mode. `line.strip()` har line ke aakhir ka `\\n` hataata hai.",
            "callout": {"title": "Champ Lab mein files", "md": "Phone par Champ Lab file ko sirf program chalne tak rakhta hai, isliye yahaan har example pehle apni file likhta hai. Computer par yahi code stock.csv ko aapke program ke bagal mein save karta hai, aur Excel use khol sakta hai."},
        },
        {
            "heading": "csv.reader se rows padhna",
            "md": "Aap har line ko khud commas par tod sakte hain, par **csv** module yeh sahi tareeke se karta hai, quotes ke andar commas wali values ke liye bhi. `csv.reader` har line ko **list** ke roop mein deta hai:\n\n" + E.C_READER + "\n\nYeh print karta hai:\n\n" + E.O_READER + "\n\nDo baatein dhyaan dijiye. Header pehle aata hai, isliye sirf data chahiye to `next(reader)` se use chhod dijiye. Aur **har value string hai**, `'120'` bhi.",
            "callout": {"title": "CSV values text hain", "md": "\"120\" + 5 error hai. Pehle convert kijiye: poore numbers ke liye int(row[1]), decimals ke liye float(...)."},
        },
        {
            "heading": "Rows ko dictionaries ki tarah padhna",
            "md": "`csv.DictReader` header ke naamon ko **keys** banaata hai, isliye har row ek **dictionary** hai aur aap values ko column ke naam se dhoondhte hain. Yeh zyada saaf hai aur columns ka kram badalne par bhi nahi toot-ta:\n\n" + E.C_DICTREADER + "\n\nYeh print karta hai:\n\n" + E.O_DICTREADER + "\n\nHeader line print nahi hui: DictReader ne use keys ke liye use kiya. `int()` ne har text value ko number banaaya taaki woh total mein jud sake.",
            "callout": {"title": "Header", "md": "CSV file ki pehli line, jismein columns ke naam hain, jaise drug,strips. DictReader ise har row ki keys ke roop mein use karta hai."},
        },
        {
            "heading": "csv.writer se rows likhna",
            "md": "Kai rows likhni hon to unhe lists ki list mein rakhiye aur commas va newlines `csv.writer` ko jodne dijiye. File ko `newline=\"\"` ke saath kholiye, isse Windows par rows ke beech khaali lines nahi aati:\n\n" + E.C_WRITER + "\n\nYeh print karta hai:\n\n" + E.O_WRITER + "\n\n`writerow(row)` ek row likhta hai; `writerows(rows)` saari. Numbers apne aap text ke roop mein likhe jaate hain.",
        },
        {
            "heading": "File mein jodna, aur saari lines padhna",
            "md": "`\"w\"` se kholne par file pehle **mit** jaati hai. Aakhir mein lines jodni hon to **append mode**, `\"a\"`, use kijiye. `readlines()` har line ko ek list mein padhta hai:\n\n" + E.C_APPEND + "\n\nYeh print karta hai:\n\n" + E.O_APPEND + "\n\nHeader aur do readings milaakar 3 lines hain, aur `lines[-1]` latest reading hai. Isi tarah program ek chalta hua log rakh sakta hai, har measurement ki ek line.",
            "callout": {"title": "\"w\" mita deta hai", "md": "Maujooda file ko \"w\" se kholne par usmein jo tha sab mit jaata hai. Jodne ke liye \"a\", aur sirf padhne ke liye \"r\" (ya koi mode nahi) use kijiye."},
        },
    ],
    "walkthrough": {
        "intro": "Yeh program ek chhota temperature log CSV file mein save karta hai, DictReader se wapas padhta hai aur sabse oonchi reading dhoondhta hai.",
        "keyTerms": [
            {"meaning": "File banao (ya mitaao) aur likhne ke liye kholo."},
            {"meaning": "File ko f ke roop mein use karo, aur baad mein apne aap band karo."},
            {"meaning": "Har row ko header ki keys wali dictionary ke roop mein padho."},
            {"meaning": "Text value ko number mein badlo."},
        ],
    },
    "errors": {
        "intro": "Yeh do errors lagbhag har pehle file program mein aati hain.",
        "examples": [
            {"title": "Aisi file kholna jo hai hi nahi", "md": "Read mode ke liye file maujood honi chahiye. Yahaan naam galat likha hai (`stock` ki jagah `stok`). Spelling aur folder check kijiye; computer par file aapke program ke bagal mein honi chahiye, ya uska poora path dijiye. (Champ Lab mein Errno ke baad ka number alag ho sakta hai; message wahi hai.)"},
            {"title": "Header ko number banaana", "md": "Pehli row header hai, isliye `row[1]` shabd `strips` hai, jo number nahi ban sakta. Pehle `next(reader)` se header chhodiye, ya `csv.DictReader` use kijiye."},
        ],
    },
    "mistakes": [
        {"mistake": "Line jodni thi par `\"w\"` se khol diya", "see": "Koi error nahi, par file mein jo tha sab chala gaya", "fix": "Aakhir mein jodne ke liye `\"a\"` (append) use kijiye."},
        {"mistake": "Har `write()` ke aakhir mein `\\n` bhool jaana", "see": "Koi error nahi, par sab ek lambi line mein aa jaata hai", "fix": "Har line `\\n` se khatam kijiye, ya `csv.writer` use kijiye."},
        {"mistake": "File se aayi value se seedhe maths: `row[\"strips\"] + 5`", "see": "TypeError: can only concatenate str (not \"int\") to str", "fix": "Pehle convert kijiye: `int(row[\"strips\"]) + 5`."},
        {"mistake": "Bina `with` ke file kholna aur `close()` bhool jaana", "see": "Data save nahi ho sakta, ya file locked rehti hai", "fix": "Hamesha `with open(...) as f:` use kijiye."},
    ],
    "tasks": [
        {"title": "File likhiye", "md": "Pehle `with` block ke andar stock.csv mein header `drug,strips` aur row `ORS,30` **likhiye**, har ek `\\n` se khatam. Padhne wala hissa aapke liye taiyaar hai. Output bilkul yeh hona chahiye:",
         "hints": ["Har f.write() text jodta hai; har line \\n se khatam kijiye.", "f.write(\"drug,strips\\n\")\n    f.write(\"ORS,30\\n\")"]},
        {"title": "Header chhodiye", "md": "**reader** se **next()** lagaakar header row chhodiye, phir har row se sirf drug ka naam print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["next(reader) ek row padhkar phenk deta hai.", "next(reader)\n    for row in reader:\n        print(row[0])"]},
        {"title": "CSV se total", "md": "stock.csv ko **csv.DictReader** se padhiye aur **strips** column jodiye. Har value ko **int()** se convert karna yaad rakhiye. Output bilkul yeh hona chahiye:",
         "hints": ["with open(\"stock.csv\") as f:\n    for row in csv.DictReader(f):", "        total += int(row[\"strips\"])"]},
        {"title": "Bug dhoondhiye", "md": "Is program ko header rakhkar uske neeche ek reading jodni hai, par header gaayab ho jaata hai. **Ek mode** badaliye taaki output bilkul yeh ho:",
         "hints": ["\"w\" likhne se pehle file mita deta hai.", "Doosri baar file ko \"a\" se kholiye taaki usmein jude."],
         "solutionNote": "Doosre open mein \"w\" tha, jisne header mita diya. \"a\" (append) jo hai use rakhta hai aur nayi line aakhir mein jodta hai."},
    ],
    "quiz": [
        {"q": "CSV ka poora naam kya hai?", "why": "CSV files values ko commas se alag karti hain."},
        {"q": "Kaun-sa mode file ko mitaaye bina uske aakhir mein lines jodta hai?", "why": "\"a\" append mode hai."},
        {"q": "csv.reader se milne wali values kis type ki hoti hain?", "why": "Text file se padhi gayi har cheez convert karne tak string hoti hai."},
        {"q": "Hum with open(...) as f: kyun likhte hain?", "why": "with aapke liye file band karta hai, error aane par bhi."},
        {"q": "csv.DictReader se har row kya hoti hai?", "why": "DictReader header ke naamon ko keys banaata hai."},
        {"q": "Maujooda file ko \"w\" se kholne par kya hota hai?", "why": "Write mode likhne se pehle file mita deta hai."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 3.5 · CSV files",
        "children": [
            {"label": "CSV file", "children": [{"label": "Saada text"}, {"label": "Values ke beech commas"}, {"label": "Pehli line = header"}]},
            {"label": "Kholna", "children": [{"label": "with open(name, mode)"}, {"label": "\"r\" \"w\" \"a\""}, {"label": "Apne aap band"}]},
            {"label": "Padhna", "children": [{"label": "csv.reader → lists"}, {"label": "csv.DictReader → dicts"}, {"label": "next() header chhodta hai"}]},
            {"label": "Likhna", "children": [{"label": "f.write(text + \\n)"}, {"label": "csv.writer"}, {"label": "writerow / writerows"}]},
            {"label": "Convert", "children": [{"label": "Values text hain"}, {"label": "int() / float()"}, {"label": "Phir hisaab"}]},
            {"label": "Errors", "children": [{"label": "FileNotFoundError"}, {"label": "ValueError: header"}]},
        ],
    },
    "summary": [
        "**CSV** file saada text hai: ek **header** line, phir har line mein ek record, values commas se alag.",
        "`with open(name, mode) as f:` file kholta hai aur apne aap band karta hai. Modes: **\"r\"** padhna, **\"w\"** likhna (mitaakar), **\"a\"** jodna.",
        "**csv.reader** har row ko list deta hai; **csv.DictReader** header ki keys wali dictionary. `next(reader)` header chhodta hai.",
        "**csv.writer** `writerow()` / `writerows()` se rows likhta hai; `newline=\"\"` ke saath kholiye.",
        "File se padhi har value **text** hai: maths se pehle `int()` ya `float()` se convert kijiye.",
    ],
}

T["kn"] = {
    "hook": {
        "title": "ಪ್ರತಿ pharmacy ಹತ್ತಿರ ಈಗಾಗಲೇ ಇರುವ file",
        "md": "ಪ್ರತಿ hospital pharmacy ಯ billing software ನಲ್ಲಿ ಒಂದು **Export** button ಇರುತ್ತೆ. ಅದನ್ನು ಒತ್ತಿ, `stock.csv` ತರಹದ ಒಂದು file ಸಿಗುತ್ತೆ. Excel ನಲ್ಲಿ ತೆರೆದರೆ ಅಚ್ಚುಕಟ್ಟಾದ table. Notepad ನಲ್ಲಿ ತೆರೆದರೆ commas ಇರುವ text lines.\n\nಈ ಸರಳ format, **CSV**, lab instruments, hospital systems ಮತ್ತು ಸರ್ಕಾರಿ health portals ನಡುವೆ data ಹಂಚುವ ದಾರಿ. ಇಲ್ಲಿವರೆಗೆ ನಿಮ್ಮ data program ಒಳಗೇ ಇದ್ದು, program ಮುಗಿದಾಗ ಮಾಯವಾಗುತ್ತಿತ್ತು. ಇವತ್ತು ನಿಮ್ಮ programs data ಅನ್ನು file ನಲ್ಲಿ **save** ಮಾಡಿ ಮತ್ತೆ **ಓದಲು** ಕಲಿಯುತ್ತವೆ: ನಿಜವಾದ datasets ಜೊತೆ ಕೆಲಸದ ಮೊದಲ ಹೆಜ್ಜೆ.",
    },
    "learn": [
        "**CSV** file ಅಂದ್ರೆ ಏನು, ಮತ್ತು **with open()** ಇಂದ file **ತೆರೆಯುವುದು**, **ಬರೆಯುವುದು**, **ಓದುವುದು**",
        "File **modes** \"r\", \"w\" ಮತ್ತು \"a\" ನಡುವಿನ ವ್ಯತ್ಯಾಸ",
        "**csv.reader** ಮತ್ತು **csv.DictReader** ಪ್ರತಿ line ಅನ್ನು list ಅಥವಾ dictionary ಆಗಿ ಹೇಗೆ ಬದಲಾಯಿಸುತ್ತವೆ",
        "**csv.writer** ಇಂದ rows **ಬರೆಯುವುದು**, ಮತ್ತು maths ಮುಂಚೆ values **convert** ಮಾಡುವುದು ಯಾಕೆ ಮುಖ್ಯ",
    ],
    "explanation": [
        {
            "heading": "CSV file ಅಂದ್ರೆ ಏನು, ಮತ್ತು ಅದನ್ನು ಬರೆಯುವುದು",
            "md": "**CSV** ಅಂದ್ರೆ **Comma-Separated Values**. ಇದು ಸರಳ text: ಮೊದಲ line **header**, ಅದರಲ್ಲಿ columns ಹೆಸರುಗಳು, ನಂತರದ ಪ್ರತಿ line ಒಂದು record:\n\n" + E.F_STOCK + "\n\nFile ಮಾಡಲು ಅದನ್ನು **write mode**, `\"w\"`, ನಲ್ಲಿ open ಮಾಡಿ `write()` ಇಂದ text ಬರೆಯಿರಿ. ಪ್ರತಿ line `\\n`, ಅಂದ್ರೆ newline character, ಇಂದ ಮುಗಿಯಬೇಕು:\n\n" + E.C_WRITE + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_WRITE + "\n\n`with open(...) as f:` file open ಮಾಡಿ, indent ಮಾಡಿದ block ಮುಗಿದಾಗ ಅದನ್ನು **ತಾನಾಗೇ close** ಮಾಡುತ್ತೆ. Mode ಇಲ್ಲದೆ open ಮಾಡಿದರೆ **read** mode. `line.strip()` ಪ್ರತಿ line ನ ಕೊನೆಯ `\\n` ತೆಗೆಯುತ್ತೆ.",
            "callout": {"title": "Champ Lab ನಲ್ಲಿ files", "md": "Phone ನಲ್ಲಿ Champ Lab file ಅನ್ನು program ಓಡುವವರೆಗೆ ಮಾತ್ರ ಇಡುತ್ತೆ, ಹಾಗಾಗಿ ಇಲ್ಲಿನ ಪ್ರತಿ example ಮೊದಲು ತನ್ನ file ಬರೆಯುತ್ತೆ. Computer ನಲ್ಲಿ ಇದೇ code stock.csv ಅನ್ನು ನಿಮ್ಮ program ಪಕ್ಕದಲ್ಲಿ save ಮಾಡುತ್ತೆ, Excel ಅದನ್ನು ತೆರೆಯಬಹುದು."},
        },
        {
            "heading": "csv.reader ಇಂದ rows ಓದುವುದು",
            "md": "ಪ್ರತಿ line ಅನ್ನು ನೀವೇ commas ಹತ್ತಿರ ಒಡೆಯಬಹುದು, ಆದರೆ **csv** module ಇದನ್ನು ಸರಿಯಾಗಿ ಮಾಡುತ್ತೆ, quotes ಒಳಗೆ commas ಇರುವ values ಗೂ. `csv.reader` ಪ್ರತಿ line ಅನ್ನು **list** ಆಗಿ ಕೊಡುತ್ತೆ:\n\n" + E.C_READER + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_READER + "\n\nಎರಡು ವಿಷಯ ಗಮನಿಸಿ. Header ಮೊದಲು ಬರುತ್ತೆ, data ಮಾತ್ರ ಬೇಕಾದರೆ `next(reader)` ಇಂದ ಅದನ್ನು ಬಿಡಿ. ಮತ್ತು **ಪ್ರತಿ value string**, `'120'` ಕೂಡ.",
            "callout": {"title": "CSV values text", "md": "\"120\" + 5 error. ಮೊದಲು convert ಮಾಡಿ: ಪೂರ್ಣ numbers ಗೆ int(row[1]), decimals ಗೆ float(...)."},
        },
        {
            "heading": "Rows ಅನ್ನು dictionaries ಆಗಿ ಓದುವುದು",
            "md": "`csv.DictReader` header ಹೆಸರುಗಳನ್ನು **keys** ಆಗಿ ಬಳಸುತ್ತೆ, ಹಾಗಾಗಿ ಪ್ರತಿ row ಒಂದು **dictionary**, ನೀವು values ಅನ್ನು column ಹೆಸರಿನಿಂದ ಹುಡುಕುತ್ತೀರಿ. ಇದು ಹೆಚ್ಚು ಸ್ಪಷ್ಟ, columns ಕ್ರಮ ಬದಲಾದರೂ ಮುರಿಯಲ್ಲ:\n\n" + E.C_DICTREADER + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_DICTREADER + "\n\nHeader line print ಆಗಲಿಲ್ಲ: DictReader ಅದನ್ನು keys ಗೆ ಬಳಸಿತು. `int()` ಪ್ರತಿ text value ಅನ್ನು number ಮಾಡಿತು, ಹಾಗಾಗಿ total ಗೆ ಸೇರಿಸಲು ಸಾಧ್ಯವಾಯಿತು.",
            "callout": {"title": "Header", "md": "CSV file ನ ಮೊದಲ line, columns ಹೆಸರುಗಳು ಇರುವುದು, drug,strips ತರಹ. DictReader ಇದನ್ನು ಪ್ರತಿ row ನ keys ಆಗಿ ಬಳಸುತ್ತೆ."},
        },
        {
            "heading": "csv.writer ಇಂದ rows ಬರೆಯುವುದು",
            "md": "ಹಲವು rows ಬರೆಯಲು ಅವನ್ನು lists ನ list ಆಗಿ ಇಡಿ, commas ಮತ್ತು newlines ಅನ್ನು `csv.writer` ಸೇರಿಸಲಿ. File ಅನ್ನು `newline=\"\"` ಜೊತೆ open ಮಾಡಿ, ಇದರಿಂದ Windows ನಲ್ಲಿ rows ನಡುವೆ ಖಾಲಿ lines ಬರಲ್ಲ:\n\n" + E.C_WRITER + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_WRITER + "\n\n`writerow(row)` ಒಂದು row ಬರೆಯುತ್ತೆ; `writerows(rows)` ಎಲ್ಲವನ್ನೂ. Numbers ತಾನಾಗೇ text ಆಗಿ ಬರೆಯಲ್ಪಡುತ್ತವೆ.",
        },
        {
            "heading": "File ಗೆ ಸೇರಿಸುವುದು, ಎಲ್ಲಾ lines ಓದುವುದು",
            "md": "`\"w\"` ಇಂದ open ಮಾಡಿದರೆ file ಮೊದಲು **ಅಳಿಸಿಹೋಗುತ್ತೆ**. ಕೊನೆಗೆ lines ಸೇರಿಸಲು **append mode**, `\"a\"`, ಬಳಸಿ. `readlines()` ಪ್ರತಿ line ಅನ್ನು ಒಂದು list ಗೆ ಓದುತ್ತೆ:\n\n" + E.C_APPEND + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_APPEND + "\n\nHeader ಮತ್ತು ಎರಡು readings ಸೇರಿ 3 lines, `lines[-1]` latest reading. ಹೀಗೆ program ಒಂದು ನಡೆಯುತ್ತಿರುವ log ಇಡಬಹುದು, ಪ್ರತಿ measurement ಗೆ ಒಂದು line.",
            "callout": {"title": "\"w\" ಅಳಿಸುತ್ತೆ", "md": "ಇರುವ file ಅನ್ನು \"w\" ಇಂದ open ಮಾಡಿದರೆ ಅದರಲ್ಲಿದ್ದುದೆಲ್ಲಾ ಅಳಿಸಿಹೋಗುತ್ತೆ. ಸೇರಿಸಲು \"a\", ಓದಲು ಮಾತ್ರ \"r\" (ಅಥವಾ mode ಇಲ್ಲದೆ) ಬಳಸಿ."},
        },
    ],
    "walkthrough": {
        "intro": "ಈ program ಒಂದು ಸಣ್ಣ temperature log ಅನ್ನು CSV file ಆಗಿ save ಮಾಡಿ, DictReader ಇಂದ ಮತ್ತೆ ಓದಿ, ಅತಿ ಹೆಚ್ಚಿನ reading ಹುಡುಕುತ್ತೆ.",
        "keyTerms": [
            {"meaning": "File ಮಾಡು (ಅಥವಾ ಅಳಿಸು), ಬರೆಯಲು open ಮಾಡು."},
            {"meaning": "File ಅನ್ನು f ಆಗಿ ಬಳಸು, ನಂತರ ತಾನಾಗೇ close ಮಾಡು."},
            {"meaning": "ಪ್ರತಿ row ಅನ್ನು header keys ಇರುವ dictionary ಆಗಿ ಓದು."},
            {"meaning": "Text value ಅನ್ನು number ಆಗಿ ಬದಲಾಯಿಸು."},
        ],
    },
    "errors": {
        "intro": "ಈ ಎರಡು errors ಬಹುತೇಕ ಪ್ರತಿ ಮೊದಲ file program ನಲ್ಲೂ ಬರುತ್ತವೆ.",
        "examples": [
            {"title": "ಇಲ್ಲದ file open ಮಾಡುವುದು", "md": "Read mode ಗೆ file ಇರಬೇಕು. ಇಲ್ಲಿ ಹೆಸರು ತಪ್ಪಾಗಿದೆ (`stock` ಬದಲು `stok`). Spelling ಮತ್ತು folder check ಮಾಡಿ; computer ನಲ್ಲಿ file ನಿಮ್ಮ program ಪಕ್ಕದಲ್ಲಿ ಇರಬೇಕು, ಅಥವಾ ಅದರ ಪೂರ್ಣ path ಕೊಡಿ. (Champ Lab ನಲ್ಲಿ Errno ನಂತರದ number ಬೇರೆ ಇರಬಹುದು; message ಅದೇ.)"},
            {"title": "Header ಅನ್ನು number ಮಾಡುವುದು", "md": "ಮೊದಲ row header, ಹಾಗಾಗಿ `row[1]` ಅಂದ್ರೆ `strips` ಪದ, ಅದು number ಆಗಲ್ಲ. ಮೊದಲು `next(reader)` ಇಂದ header ಬಿಡಿ, ಅಥವಾ `csv.DictReader` ಬಳಸಿ."},
        ],
    },
    "mistakes": [
        {"mistake": "Line ಸೇರಿಸಬೇಕಿತ್ತು ಆದರೆ `\"w\"` ಇಂದ open ಮಾಡಿದ್ದು", "see": "Error ಇಲ್ಲ, ಆದರೆ file ನಲ್ಲಿದ್ದುದೆಲ್ಲಾ ಹೋಯಿತು", "fix": "ಕೊನೆಗೆ ಸೇರಿಸಲು `\"a\"` (append) ಬಳಸಿ."},
        {"mistake": "ಪ್ರತಿ `write()` ಕೊನೆಯಲ್ಲಿ `\\n` ಮರೆಯುವುದು", "see": "Error ಇಲ್ಲ, ಆದರೆ ಎಲ್ಲವೂ ಒಂದೇ ಉದ್ದ line ನಲ್ಲಿ", "fix": "ಪ್ರತಿ line ಅನ್ನು `\\n` ಇಂದ ಮುಗಿಸಿ, ಅಥವಾ `csv.writer` ಬಳಸಿ."},
        {"mistake": "File ಇಂದ ಬಂದ value ಮೇಲೆ ನೇರ maths: `row[\"strips\"] + 5`", "see": "TypeError: can only concatenate str (not \"int\") to str", "fix": "ಮೊದಲು convert ಮಾಡಿ: `int(row[\"strips\"]) + 5`."},
        {"mistake": "`with` ಇಲ್ಲದೆ file open ಮಾಡಿ `close()` ಮರೆಯುವುದು", "see": "Data save ಆಗದಿರಬಹುದು, ಅಥವಾ file lock ಆಗಿರುತ್ತೆ", "fix": "ಯಾವಾಗಲೂ `with open(...) as f:` ಬಳಸಿ."},
    ],
    "tasks": [
        {"title": "File ಬರೆಯಿರಿ", "md": "ಮೊದಲ `with` block ಒಳಗೆ stock.csv ಗೆ header `drug,strips` ಮತ್ತು row `ORS,30` **ಬರೆಯಿರಿ**, ಪ್ರತಿಯೊಂದೂ `\\n` ಇಂದ ಮುಗಿಯಲಿ. ಓದುವ ಭಾಗ ನಿಮಗಾಗಿ ಸಿದ್ಧವಿದೆ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["ಪ್ರತಿ f.write() text ಸೇರಿಸುತ್ತೆ; ಪ್ರತಿ line ಅನ್ನು \\n ಇಂದ ಮುಗಿಸಿ.", "f.write(\"drug,strips\\n\")\n    f.write(\"ORS,30\\n\")"]},
        {"title": "Header ಬಿಡಿ", "md": "**reader** ಮೇಲೆ **next()** ಬಳಸಿ header row ಬಿಡಿ, ನಂತರ ಪ್ರತಿ row ಇಂದ drug ಹೆಸರು ಮಾತ್ರ print ಮಾಡಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["next(reader) ಒಂದು row ಓದಿ ಬಿಸಾಡುತ್ತೆ.", "next(reader)\n    for row in reader:\n        print(row[0])"]},
        {"title": "CSV ಇಂದ total", "md": "stock.csv ಅನ್ನು **csv.DictReader** ಇಂದ ಓದಿ **strips** column ಕೂಡಿಸಿ. ಪ್ರತಿ value ಅನ್ನು **int()** ಇಂದ convert ಮಾಡುವುದನ್ನು ಮರೆಯಬೇಡಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["with open(\"stock.csv\") as f:\n    for row in csv.DictReader(f):", "        total += int(row[\"strips\"])"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "ಈ program header ಇಟ್ಟುಕೊಂಡು ಅದರ ಕೆಳಗೆ ಒಂದು reading ಸೇರಿಸಬೇಕು, ಆದರೆ header ಮಾಯವಾಗುತ್ತೆ. **ಒಂದು mode** ಬದಲಾಯಿಸಿ, output ನಿಖರವಾಗಿ ಹೀಗಿರಲಿ:",
         "hints": ["\"w\" ಬರೆಯುವ ಮುಂಚೆ file ಅಳಿಸುತ್ತೆ.", "ಎರಡನೇ ಸಲ file ಅನ್ನು \"a\" ಇಂದ open ಮಾಡಿ, ಸೇರಿಸಲು."],
         "solutionNote": "ಎರಡನೇ open ನಲ್ಲಿ \"w\" ಇತ್ತು, ಅದು header ಅಳಿಸಿತು. \"a\" (append) ಇರುವುದನ್ನು ಉಳಿಸಿ ಹೊಸ line ಅನ್ನು ಕೊನೆಗೆ ಸೇರಿಸುತ್ತೆ."},
    ],
    "quiz": [
        {"q": "CSV ಯ ಪೂರ್ಣ ರೂಪ ಏನು?", "why": "CSV files values ಅನ್ನು commas ಇಂದ ಬೇರ್ಪಡಿಸುತ್ತವೆ."},
        {"q": "File ಅಳಿಸದೆ ಅದರ ಕೊನೆಗೆ lines ಸೇರಿಸುವ mode ಯಾವುದು?", "why": "\"a\" append mode."},
        {"q": "csv.reader ಕೊಡುವ values ಯಾವ type?", "why": "Text file ಇಂದ ಓದಿದ ಎಲ್ಲವೂ convert ಮಾಡುವವರೆಗೆ string."},
        {"q": "ನಾವು with open(...) as f: ಯಾಕೆ ಬರೆಯುತ್ತೇವೆ?", "why": "with ನಿಮಗಾಗಿ file close ಮಾಡುತ್ತೆ, error ಬಂದರೂ."},
        {"q": "csv.DictReader ಇಂದ ಪ್ರತಿ row ಏನು?", "why": "DictReader header ಹೆಸರುಗಳನ್ನು keys ಆಗಿ ಬಳಸುತ್ತೆ."},
        {"q": "ಇರುವ file ಅನ್ನು \"w\" ಇಂದ open ಮಾಡಿದರೆ ಏನಾಗುತ್ತೆ?", "why": "Write mode ಬರೆಯುವ ಮುಂಚೆ file ಅಳಿಸುತ್ತೆ."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 3.5 · CSV files",
        "children": [
            {"label": "CSV file", "children": [{"label": "ಸರಳ text"}, {"label": "Values ನಡುವೆ commas"}, {"label": "ಮೊದಲ line = header"}]},
            {"label": "Open", "children": [{"label": "with open(name, mode)"}, {"label": "\"r\" \"w\" \"a\""}, {"label": "ತಾನಾಗೇ close"}]},
            {"label": "ಓದು", "children": [{"label": "csv.reader → lists"}, {"label": "csv.DictReader → dicts"}, {"label": "next() header ಬಿಡುತ್ತೆ"}]},
            {"label": "ಬರೆ", "children": [{"label": "f.write(text + \\n)"}, {"label": "csv.writer"}, {"label": "writerow / writerows"}]},
            {"label": "Convert", "children": [{"label": "Values text"}, {"label": "int() / float()"}, {"label": "ನಂತರ ಲೆಕ್ಕ"}]},
            {"label": "Errors", "children": [{"label": "FileNotFoundError"}, {"label": "ValueError: header"}]},
        ],
    },
    "summary": [
        "**CSV** file ಸರಳ text: ಒಂದು **header** line, ನಂತರ ಪ್ರತಿ line ನಲ್ಲಿ ಒಂದು record, values commas ಇಂದ ಬೇರೆ.",
        "`with open(name, mode) as f:` file open ಮಾಡಿ ತಾನಾಗೇ close ಮಾಡುತ್ತೆ. Modes: **\"r\"** ಓದು, **\"w\"** ಬರೆ (ಅಳಿಸಿ), **\"a\"** ಸೇರಿಸು.",
        "**csv.reader** ಪ್ರತಿ row ಅನ್ನು list ಆಗಿ; **csv.DictReader** header keys ಇರುವ dictionary ಆಗಿ ಕೊಡುತ್ತೆ. `next(reader)` header ಬಿಡುತ್ತೆ.",
        "**csv.writer** `writerow()` / `writerows()` ಇಂದ rows ಬರೆಯುತ್ತೆ; `newline=\"\"` ಜೊತೆ open ಮಾಡಿ.",
        "File ಇಂದ ಓದಿದ ಪ್ರತಿ value **text**: maths ಮುಂಚೆ `int()` ಅಥವಾ `float()` ಇಂದ convert ಮಾಡಿ.",
    ],
}

NARR = {
    "hi": [
        "यह program एक temperature log को CSV file में save करता है, फिर उसे वापस पढ़कर सबसे ऊँची reading ढूँढता है।",
        "import csv, Python का CSV files वाला module load करता है।",
        "w के साथ open, temps dot csv file को write mode में बनाता है। with उसे अपने आप बंद करेगा।",
        "write file में चार lines डालता है: header, time comma temp, और तीन readings। हर backslash n एक line खत्म करता है।",
        "temps एक खाली list से शुरू होती है, readings को numbers के रूप में जमा करने के लिए तैयार।",
        "अब file फिर से खुलती है, इस बार पढ़ने के लिए।",
        "DictReader पहले header पढ़ता है। फिर हर row एक dictionary बनती है। पहली row में time zero eight hundred है, और temp सैंतीस दशमलव दो, अभी भी text।",
        "float text को number बनाता है, और append उसे temps में जोड़ता है।",
        "Loop बाकी दो rows के लिए भी यही करता है।",
        "print तीनों readings दिखाता है, अब numbers के रूप में।",
        "max सबसे ऊँची ढूँढता है: अड़तीस दशमलव चार, दोपहर में।",
    ],
    "hinglish": [
        "Yeh program ek temperature log ko CSV file mein save karta hai, phir use wapas padhkar sabse oonchi reading dhoondhta hai.",
        "import csv, Python ka CSV files wala module load karta hai.",
        "w ke saath open, temps dot csv file ko write mode mein banata hai. with use apne aap band karega.",
        "write file mein chaar lines daalta hai: header, time comma temp, aur teen readings. Har backslash n ek line khatam karta hai.",
        "temps ek khaali list se shuru hoti hai, readings ko numbers ke roop mein jama karne ke liye taiyaar.",
        "Ab file phir se khulti hai, is baar padhne ke liye.",
        "DictReader pehle header padhta hai. Phir har row ek dictionary banti hai. Pehli row mein time zero eight hundred hai, aur temp saintees dashamlav do, abhi bhi text.",
        "float text ko number banaata hai, aur append use temps mein jodta hai.",
        "Loop baaki do rows ke liye bhi yahi karta hai.",
        "print teenon readings dikhaata hai, ab numbers ke roop mein.",
        "max sabse oonchi dhoondhta hai: adtees dashamlav chaar, dopahar mein.",
    ],
    "kn": [
        "ಈ program ಒಂದು temperature log ಅನ್ನು CSV file ಆಗಿ save ಮಾಡಿ, ಮತ್ತೆ ಓದಿ ಅತಿ ಹೆಚ್ಚಿನ reading ಹುಡುಕುತ್ತೆ.",
        "import csv, Python ನ CSV files module load ಮಾಡುತ್ತೆ.",
        "w ಜೊತೆ open, temps dot csv file ಅನ್ನು write mode ನಲ್ಲಿ ಮಾಡುತ್ತೆ. with ಅದನ್ನು ತಾನಾಗೇ close ಮಾಡುತ್ತೆ.",
        "write file ಗೆ ನಾಲ್ಕು lines ಹಾಕುತ್ತೆ: header, time comma temp, ಮತ್ತು ಮೂರು readings. ಪ್ರತಿ backslash n ಒಂದು line ಮುಗಿಸುತ್ತೆ.",
        "temps ಖಾಲಿ list ಆಗಿ ಶುರು, readings ಅನ್ನು numbers ಆಗಿ ಸಂಗ್ರಹಿಸಲು ಸಿದ್ಧ.",
        "ಈಗ file ಮತ್ತೆ open ಆಗುತ್ತೆ, ಈ ಸಲ ಓದಲು.",
        "DictReader ಮೊದಲು header ಓದುತ್ತೆ. ನಂತರ ಪ್ರತಿ row ಒಂದು dictionary ಆಗುತ್ತೆ. ಮೊದಲ row ನಲ್ಲಿ time zero eight hundred, temp ಮೂವತ್ತೇಳು ಪಾಯಿಂಟ್ ಎರಡು, ಇನ್ನೂ text.",
        "float text ಅನ್ನು number ಮಾಡುತ್ತೆ, append ಅದನ್ನು temps ಗೆ ಸೇರಿಸುತ್ತೆ.",
        "Loop ಉಳಿದ ಎರಡು rows ಗೂ ಇದನ್ನೇ ಮಾಡುತ್ತೆ.",
        "print ಮೂರೂ readings ತೋರಿಸುತ್ತೆ, ಈಗ numbers ಆಗಿ.",
        "max ಅತಿ ಹೆಚ್ಚಿನದನ್ನು ಹುಡುಕುತ್ತೆ: ಮೂವತ್ತೆಂಟು ಪಾಯಿಂಟ್ ನಾಲ್ಕು, ಮಧ್ಯಾಹ್ನ.",
    ],
}

ANIM = {
    "hi": [
        "CSV file सादा text है। पहली line header है। बाकी हर line एक record है, values के बीच commas के साथ।",
        "DictReader पहले header पढ़ता है, और उसके नाम, time और temp, keys के रूप में रखता है।",
        "अगली line एक dictionary बनती है: time zero eight hundred है, और temp सैंतीस दशमलव दो। यह अभी भी text है।",
        "float text को number बनाता है, और append उसे list में जोड़ता है।",
        "हर line के साथ यही होता है। अब max सबसे ऊँची reading ढूँढ सकता है।",
    ],
    "hinglish": [
        "CSV file saada text hai. Pehli line header hai. Baaki har line ek record hai, values ke beech commas ke saath.",
        "DictReader pehle header padhta hai, aur uske naam, time aur temp, keys ke roop mein rakhta hai.",
        "Agli line ek dictionary banti hai: time zero eight hundred hai, aur temp saintees dashamlav do. Yeh abhi bhi text hai.",
        "float text ko number banaata hai, aur append use list mein jodta hai.",
        "Har line ke saath yahi hota hai. Ab max sabse oonchi reading dhoondh sakta hai.",
    ],
    "kn": [
        "CSV file ಸರಳ text. ಮೊದಲ line header. ಉಳಿದ ಪ್ರತಿ line ಒಂದು record, values ನಡುವೆ commas.",
        "DictReader ಮೊದಲು header ಓದಿ, ಅದರ ಹೆಸರುಗಳಾದ time ಮತ್ತು temp ಅನ್ನು keys ಆಗಿ ಇಡುತ್ತೆ.",
        "ಮುಂದಿನ line ಒಂದು dictionary ಆಗುತ್ತೆ: time zero eight hundred, temp ಮೂವತ್ತೇಳು ಪಾಯಿಂಟ್ ಎರಡು. ಇದು ಇನ್ನೂ text.",
        "float text ಅನ್ನು number ಮಾಡುತ್ತೆ, append ಅದನ್ನು list ಗೆ ಸೇರಿಸುತ್ತೆ.",
        "ಪ್ರತಿ line ಗೂ ಇದೇ ಆಗುತ್ತೆ. ಈಗ max ಅತಿ ಹೆಚ್ಚಿನ reading ಹುಡುಕಬಹುದು.",
    ],
}

if __name__ == "__main__":
    build("3-5", "anim-rows", T, NARR, ANIM)

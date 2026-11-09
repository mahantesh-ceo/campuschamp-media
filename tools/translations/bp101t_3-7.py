"""Lesson 3.7 translations (Hindi, Hinglish, Kannada) and voice scripts."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import build  # noqa: E402

_spec = importlib.util.spec_from_file_location("en37", os.path.join(os.path.dirname(__file__), "..", "lessons", "bp101t_3-7_en.py"))
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)

T = {}

T["hi"] = {
    "hook": {
        "title": "Release या reject: फ़ैसला आपका",
        "md": "Pharmaceutical plant में बनी tablets का हर batch factory से निकलने से पहले test होता है। **Assay** check करता है कि हर tablet में drug की सही मात्रा है। **Dissolution test** check करता है कि drug शरीर में सच में tablet से बाहर निकलती है। Quality control lab नतीजे एक file में भेजता है, और हर batch के लिए फ़ैसला करना होता है: **release** या **reject**।\n\nइस project lesson में आप वह फ़ैसला Python में बनाएँगे, Unit III की हर चीज़ से: CSV file पढ़ना, values convert करना, हर batch को specification से check करना, NumPy से सार निकालना, drugs की तुलना करना, और report file लिखना।",
    },
    "learn": [
        "CSV dataset को list of dictionaries में **load** करना, text को numbers में बदलते हुए",
        "Function से हर record को **specification** के against **check** करना",
        "NumPy से column का **सार** निकालना और **groups** की तुलना करना",
        "नतीजों को report file में **लिखना**: एक पूरी छोटी **data pipeline**",
    ],
    "explanation": [
        {
            "heading": "Step 1: dataset load कीजिए",
            "md": "QC lab की file में हर batch की एक row है: batch number, drug, **assay** (label claim का %) और **dissolution** (30 minutes में % घुला):\n\n" + E.F_QC + "\n\nइसे `csv.DictReader` से load कीजिए और numbers को **load करते समय ही** convert कीजिए, ताकि आगे का हर step सीधे maths कर सके:\n\n" + E.C_LOAD + "\n\nयह print करता है:\n\n" + E.O_LOAD + "\n\n`batches` अब पाँच dictionaries की list है, अंदर असली numbers के साथ। अगले steps इसी list से शुरू होते हैं।",
            "callout": {"title": "Specification", "md": "वे limits जो product को release होने के लिए पूरी करनी होती हैं। इस lesson में: assay label claim के 95% से 105% के बीच, और कम से कम 80% घुला हुआ। असली limits pharmacopoeia तय करती है और हर product के लिए अलग होती हैं।"},
        },
        {
            "heading": "Step 2: हर batch check कीजिए",
            "md": "Specification को एक **function** (Lesson 2.5) में रखिए, ताकि नियम एक ही जगह रहे। यह batch के fail हुए tests की list लौटाता है; खाली list मतलब pass:\n\n" + E.C_CHECK + "\n\nयह print करता है:\n\n" + E.O_CHECK + "\n\nList में कुछ भी हो तो `if problems:` True है। B102 में drug कम है; B103 में मात्रा सही है, पर उसका कम हिस्सा घुलता है।",
            "callout": {"title": "एक नियम, एक जगह", "md": "Limits बदलें तो सिर्फ़ check() function बदलिए। Program का हर हिस्सा जो इसे call करता है, नया नियम use करेगा।"},
        },
        {
            "heading": "Step 3: NumPy से सार",
            "md": "एक column को NumPy array (Lesson 3.4) में जमा कीजिए, और सार तीन lines में:\n\n" + E.C_STATS + "\n\nयह print करता है:\n\n" + E.O_STATS + "\n\nAverage 99.78% पर ठीक दिखता है, पर minimum एक batch को limit से नीचे दिखाता है। इसीलिए हमेशा extremes भी देखिए, सिर्फ़ average नहीं।",
        },
        {
            "heading": "Step 4: drugs की तुलना",
            "md": "हर drug का pass rate देखने के लिए Lesson 3.6 का grouping pattern use कीजिए:\n\n" + E.C_GROUP + "\n\nयह print करता है:\n\n" + E.O_GROUP + "\n\nअगर एक product बार-बार एक ही test में fail हो, तो यह process जाँचने का संकेत है: raw material, granulation या compression।",
        },
        {
            "heading": "Step 5: report लिखिए",
            "md": "आखिर में हर batch का फ़ैसला एक **नई** CSV file में लिखिए जिसे QA team Excel में खोल सके:\n\n" + E.C_REPORT + "\n\nयह print करता है:\n\n" + E.O_REPORT + "\n\nReport `qc_report.csv` में जाती है, नया नाम, ताकि `qc.csv` का original data कभी overwrite न हो। पढ़ना → convert → check → सार → report: आपने एक पूरी **data pipeline** बना ली। Unit IV में Pandas इनमें से हर step एक line में करेगा।",
            "callout": {"title": "Raw data कभी overwrite मत कीजिए", "md": "नतीजे हमेशा नई file में लिखिए। qc.csv को \"w\" से खोला तो lab के original नतीजे चले जाएँगे।"},
        },
    ],
    "walkthrough": {
        "intro": "यह program CSV file से तीन batches पढ़ता है, हर एक को specification से check करता है, और बताता है कौन-से batches fail हुए।",
        "keyTerms": [
            {"meaning": "हर batch को dictionary के रूप में पढ़ो।"},
            {"meaning": "File के text को number में बदलो।"},
            {"meaning": "True, अगर batch किसी भी test में fail हो।"},
            {"meaning": "Fail हुए batch का number याद रखो।"},
        ],
    },
    "errors": {
        "intro": "दोनों errors उस data से आती हैं जिसे check से पहले तैयार नहीं किया गया।",
        "examples": [
            {"title": "Text की number से तुलना", "md": "CSV file की values text होती हैं, और Python text की number से तुलना नहीं करता। पहले convert कीजिए: `if float(row[\"assay\"]) < 95:`।"},
            {"title": "File में खाली cell", "md": "B102 का assay cell खाली है, और खाली string number नहीं बन सकती। Lesson 3.6 की तरह पहले check कीजिए: `if row[\"assay\"] == \"\": print(row[\"batch\"], \"assay missing\")`।"},
        ],
    },
    "mistakes": [
        {"mistake": "Fail नियम में `and` लिखना: `assay < 95 and diss < 80`", "see": "कोई error नहीं, पर सिर्फ़ एक test में fail होने वाले batches release हो जाते हैं", "fix": "Batch **किसी भी** test में fail हो तो fail है: `or` use कीजिए।"},
        {"mistake": "Batches की संख्या type करना: `print(3 - len(failed))`", "see": "कोई error नहीं, पर file में ज़्यादा batches होने पर जवाब गलत", "fix": "पढ़ते समय rows गिनिए, या `len(batches)` use कीजिए।"},
        {"mistake": "Report को data file में लिखना: `open(\"qc.csv\", \"w\")`", "see": "कोई error नहीं, पर lab के original नतीजे मिट जाते हैं", "fix": "नतीजे नई file में लिखिए, जैसे `qc_report.csv`।"},
        {"mistake": "सिर्फ़ average देखना", "see": "कोई error नहीं, पर fail batch अच्छे mean के पीछे छिप जाता है", "fix": "`min()`, `max()` और limit से बाहर कितने हैं, यह भी check कीजिए।"},
    ],
    "tasks": [
        {"title": "Batches गिनिए", "md": "qc.csv file आपके लिए पहले से लिख दी गई है। इसे **csv.DictReader** से पढ़िए और rows गिनिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["with open(\"qc.csv\") as f:\n    for row in csv.DictReader(f):", "        count += 1"]},
        {"title": "NumPy से mean assay", "md": "**assay** list से NumPy array बनाइए और उसका mean 1 decimal तक round करके print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["assay = np.array(assay_values)", "print(\"Mean assay:\", round(assay.mean(), 1))"]},
        {"title": "Dissolution failures", "md": "जिन batches की **dissolution** 80 से कम है, उनके numbers की list बनाइए और print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["batches पर loop चलाइए और b[\"dissolution\"] < 80 test कीजिए।", "for b in batches:\n    if b[\"dissolution\"] < 80:\n        low.append(b[\"batch\"])"]},
        {"title": "Bug ढूँढिए", "md": "B201 assay में fail है और B202 dissolution में, इसलिए दोनों reject होने चाहिए। पर यह program कुछ print नहीं करता। नियम ठीक कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["Reject होने के लिए batch को दोनों tests में fail होना है, या सिर्फ़ एक में?", "and को or में बदलिए।"],
         "solutionNote": "and के साथ batch तभी reject होता जब दोनों tests में fail हो, और कोई नहीं हुआ। Batch किसी भी test में fail हो तो reject होना चाहिए, इसलिए नियम में or चाहिए।"},
    ],
    "quiz": [
        {"q": "आपने CSV file से एक row पढ़ी। उसके numbers की तुलना से पहले आमतौर पर क्या करना चाहिए?", "why": "CSV values text हैं; तुलना और maths के लिए numbers चाहिए।"},
        {"q": "Assay की limit 95 से 105 है। Pass होने वाले assay a के लिए कौन-सी condition True है?", "why": "Chained comparison range के दोनों सिरे check करता है।"},
        {"q": "Batch assay OR dissolution test में fail हो तो reject होना चाहिए। दोनों fail conditions को कौन-सा operator जोड़ता है?", "why": "Reject के लिए किसी एक test में fail होना काफ़ी है।"},
        {"q": "qc.csv को \"w\" से खोलने की जगह report qc_report.csv में क्यों लिखें?", "why": "Write mode पहले file मिटाता है; raw data कभी overwrite मत कीजिए।"},
        {"q": "assay = np.array([99.2, 94.1, 101.5])\nprint((assay < 95).sum())\n\nयह क्या print करता है?", "why": "एक value 95 से कम है, और True को 1 गिना जाता है।"},
        {"q": "इस छोटी data pipeline का सही क्रम क्या है?", "why": "जो data पढ़ा और convert नहीं हुआ, उसे check या summarise नहीं कर सकते।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 3.7 · QC dataset project",
        "children": [
            {"label": "पढ़ना", "children": [{"label": "csv.DictReader"}, {"label": "हर batch की dict"}, {"label": "Rows गिनो"}]},
            {"label": "Convert", "children": [{"label": "float() / int()"}, {"label": "खाली cells"}, {"label": "Load करते समय"}]},
            {"label": "Spec check", "children": [{"label": "95 <= assay <= 105"}, {"label": "dissolution >= 80"}, {"label": "कोई भी fail: or"}]},
            {"label": "सार", "children": [{"label": "NumPy mean()"}, {"label": "min() max()"}, {"label": "(arr < 95).sum()"}]},
            {"label": "Group और report", "children": [{"label": "हर drug का pass count"}, {"label": "csv.writer"}, {"label": "नया file name"}]},
            {"label": "Errors", "children": [{"label": "TypeError: str < int"}, {"label": "ValueError: खाली cell"}]},
        ],
    },
    "summary": [
        "**Data pipeline** है: पढ़ना → convert → check → सार → report।",
        "CSV को `csv.DictReader` से list of dictionaries में load कीजिए, numbers को **load करते समय** convert करते हुए।",
        "**Specification** एक function में रखिए; batch **किसी भी** test में fail हो तो fail है, इसलिए fail नियम में `or`।",
        "NumPy से column का सार निकालिए (`mean()`, `min()`, `(arr < 95).sum()`) और गिनती वाले pattern से **groups** की तुलना कीजिए।",
        "नतीजे `csv.writer` से **नई** file में लिखिए; raw data कभी overwrite मत कीजिए।",
    ],
}

T["hinglish"] = {
    "hook": {
        "title": "Release ya reject: faisla aapka",
        "md": "Pharmaceutical plant mein bani tablets ka har batch factory se nikalne se pehle test hota hai. **Assay** check karta hai ki har tablet mein drug ki sahi maatra hai. **Dissolution test** check karta hai ki drug shareer mein sach mein tablet se bahar nikalti hai. Quality control lab nateeje ek file mein bhejta hai, aur har batch ke liye faisla karna hota hai: **release** ya **reject**.\n\nIs project lesson mein aap woh faisla Python mein banaayenge, Unit III ki har cheez se: CSV file padhna, values convert karna, har batch ko specification se check karna, NumPy se saar nikaalna, drugs ki tulna karna, aur report file likhna.",
    },
    "learn": [
        "CSV dataset ko list of dictionaries mein **load** karna, text ko numbers mein badalte hue",
        "Function se har record ko **specification** ke against **check** karna",
        "NumPy se column ka **saar** nikaalna aur **groups** ki tulna karna",
        "Nateejon ko report file mein **likhna**: ek poori chhoti **data pipeline**",
    ],
    "explanation": [
        {
            "heading": "Step 1: dataset load kijiye",
            "md": "QC lab ki file mein har batch ki ek row hai: batch number, drug, **assay** (label claim ka %) aur **dissolution** (30 minutes mein % ghula):\n\n" + E.F_QC + "\n\nIse `csv.DictReader` se load kijiye aur numbers ko **load karte samay hi** convert kijiye, taaki aage ka har step seedhe maths kar sake:\n\n" + E.C_LOAD + "\n\nYeh print karta hai:\n\n" + E.O_LOAD + "\n\n`batches` ab paanch dictionaries ki list hai, andar asli numbers ke saath. Agle steps isi list se shuru hote hain.",
            "callout": {"title": "Specification", "md": "Woh limits jo product ko release hone ke liye poori karni hoti hain. Is lesson mein: assay label claim ke 95% se 105% ke beech, aur kam se kam 80% ghula hua. Asli limits pharmacopoeia tay karti hai aur har product ke liye alag hoti hain."},
        },
        {
            "heading": "Step 2: har batch check kijiye",
            "md": "Specification ko ek **function** (Lesson 2.5) mein rakhiye, taaki niyam ek hi jagah rahe. Yeh batch ke fail hue tests ki list lautaata hai; khaali list matlab pass:\n\n" + E.C_CHECK + "\n\nYeh print karta hai:\n\n" + E.O_CHECK + "\n\nList mein kuch bhi ho to `if problems:` True hai. B102 mein drug kam hai; B103 mein maatra sahi hai, par uska kam hissa ghulta hai.",
            "callout": {"title": "Ek niyam, ek jagah", "md": "Limits badlein to sirf check() function badaliye. Program ka har hissa jo ise call karta hai, naya niyam use karega."},
        },
        {
            "heading": "Step 3: NumPy se saar",
            "md": "Ek column ko NumPy array (Lesson 3.4) mein jama kijiye, aur saar teen lines mein:\n\n" + E.C_STATS + "\n\nYeh print karta hai:\n\n" + E.O_STATS + "\n\nAverage 99.78% par theek dikhta hai, par minimum ek batch ko limit se neeche dikhaata hai. Isiliye hamesha extremes bhi dekhiye, sirf average nahi.",
        },
        {
            "heading": "Step 4: drugs ki tulna",
            "md": "Har drug ka pass rate dekhne ke liye Lesson 3.6 ka grouping pattern use kijiye:\n\n" + E.C_GROUP + "\n\nYeh print karta hai:\n\n" + E.O_GROUP + "\n\nAgar ek product baar-baar ek hi test mein fail ho, to yeh process jaanchne ka sanket hai: raw material, granulation ya compression.",
        },
        {
            "heading": "Step 5: report likhiye",
            "md": "Aakhir mein har batch ka faisla ek **nayi** CSV file mein likhiye jise QA team Excel mein khol sake:\n\n" + E.C_REPORT + "\n\nYeh print karta hai:\n\n" + E.O_REPORT + "\n\nReport `qc_report.csv` mein jaati hai, naya naam, taaki `qc.csv` ka original data kabhi overwrite na ho. Padhna → convert → check → saar → report: aapne ek poori **data pipeline** bana li. Unit IV mein Pandas inmein se har step ek line mein karega.",
            "callout": {"title": "Raw data kabhi overwrite mat kijiye", "md": "Nateeje hamesha nayi file mein likhiye. qc.csv ko \"w\" se khola to lab ke original nateeje chale jaayenge."},
        },
    ],
    "walkthrough": {
        "intro": "Yeh program CSV file se teen batches padhta hai, har ek ko specification se check karta hai, aur batata hai kaun-se batches fail hue.",
        "keyTerms": [
            {"meaning": "Har batch ko dictionary ke roop mein padho."},
            {"meaning": "File ke text ko number mein badlo."},
            {"meaning": "True, agar batch kisi bhi test mein fail ho."},
            {"meaning": "Fail hue batch ka number yaad rakho."},
        ],
    },
    "errors": {
        "intro": "Dono errors us data se aati hain jise check se pehle taiyaar nahi kiya gaya.",
        "examples": [
            {"title": "Text ki number se tulna", "md": "CSV file ki values text hoti hain, aur Python text ki number se tulna nahi karta. Pehle convert kijiye: `if float(row[\"assay\"]) < 95:`."},
            {"title": "File mein khaali cell", "md": "B102 ka assay cell khaali hai, aur khaali string number nahi ban sakti. Lesson 3.6 ki tarah pehle check kijiye: `if row[\"assay\"] == \"\": print(row[\"batch\"], \"assay missing\")`."},
        ],
    },
    "mistakes": [
        {"mistake": "Fail niyam mein `and` likhna: `assay < 95 and diss < 80`", "see": "Koi error nahi, par sirf ek test mein fail hone wale batches release ho jaate hain", "fix": "Batch **kisi bhi** test mein fail ho to fail hai: `or` use kijiye."},
        {"mistake": "Batches ki sankhya type karna: `print(3 - len(failed))`", "see": "Koi error nahi, par file mein zyada batches hone par jawaab galat", "fix": "Padhte samay rows giniye, ya `len(batches)` use kijiye."},
        {"mistake": "Report ko data file mein likhna: `open(\"qc.csv\", \"w\")`", "see": "Koi error nahi, par lab ke original nateeje mit jaate hain", "fix": "Nateeje nayi file mein likhiye, jaise `qc_report.csv`."},
        {"mistake": "Sirf average dekhna", "see": "Koi error nahi, par fail batch achhe mean ke peechhe chhip jaata hai", "fix": "`min()`, `max()` aur limit se bahar kitne hain, yeh bhi check kijiye."},
    ],
    "tasks": [
        {"title": "Batches giniye", "md": "qc.csv file aapke liye pehle se likh di gayi hai. Ise **csv.DictReader** se padhiye aur rows giniye. Output bilkul yeh hona chahiye:",
         "hints": ["with open(\"qc.csv\") as f:\n    for row in csv.DictReader(f):", "        count += 1"]},
        {"title": "NumPy se mean assay", "md": "**assay** list se NumPy array banaiye aur uska mean 1 decimal tak round karke print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["assay = np.array(assay_values)", "print(\"Mean assay:\", round(assay.mean(), 1))"]},
        {"title": "Dissolution failures", "md": "Jin batches ki **dissolution** 80 se kam hai, unke numbers ki list banaiye aur print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["batches par loop chalaaiye aur b[\"dissolution\"] < 80 test kijiye.", "for b in batches:\n    if b[\"dissolution\"] < 80:\n        low.append(b[\"batch\"])"]},
        {"title": "Bug dhoondhiye", "md": "B201 assay mein fail hai aur B202 dissolution mein, isliye dono reject hone chahiye. Par yeh program kuch print nahi karta. Niyam theek kijiye taaki output bilkul yeh ho:",
         "hints": ["Reject hone ke liye batch ko dono tests mein fail hona hai, ya sirf ek mein?", "and ko or mein badaliye."],
         "solutionNote": "and ke saath batch tabhi reject hota jab dono tests mein fail ho, aur koi nahi hua. Batch kisi bhi test mein fail ho to reject hona chahiye, isliye niyam mein or chahiye."},
    ],
    "quiz": [
        {"q": "Aapne CSV file se ek row padhi. Uske numbers ki tulna se pehle aam taur par kya karna chahiye?", "why": "CSV values text hain; tulna aur maths ke liye numbers chahiye."},
        {"q": "Assay ki limit 95 se 105 hai. Pass hone wale assay a ke liye kaun-si condition True hai?", "why": "Chained comparison range ke dono sire check karta hai."},
        {"q": "Batch assay OR dissolution test mein fail ho to reject hona chahiye. Dono fail conditions ko kaun-sa operator jodta hai?", "why": "Reject ke liye kisi ek test mein fail hona kaafi hai."},
        {"q": "qc.csv ko \"w\" se kholne ki jagah report qc_report.csv mein kyun likhein?", "why": "Write mode pehle file mitaata hai; raw data kabhi overwrite mat kijiye."},
        {"q": "assay = np.array([99.2, 94.1, 101.5])\nprint((assay < 95).sum())\n\nYeh kya print karta hai?", "why": "Ek value 95 se kam hai, aur True ko 1 gina jaata hai."},
        {"q": "Is chhoti data pipeline ka sahi kram kya hai?", "why": "Jo data padha aur convert nahi hua, use check ya summarise nahi kar sakte."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 3.7 · QC dataset project",
        "children": [
            {"label": "Padhna", "children": [{"label": "csv.DictReader"}, {"label": "Har batch ki dict"}, {"label": "Rows gino"}]},
            {"label": "Convert", "children": [{"label": "float() / int()"}, {"label": "Khaali cells"}, {"label": "Load karte samay"}]},
            {"label": "Spec check", "children": [{"label": "95 <= assay <= 105"}, {"label": "dissolution >= 80"}, {"label": "Koi bhi fail: or"}]},
            {"label": "Saar", "children": [{"label": "NumPy mean()"}, {"label": "min() max()"}, {"label": "(arr < 95).sum()"}]},
            {"label": "Group aur report", "children": [{"label": "Har drug ka pass count"}, {"label": "csv.writer"}, {"label": "Naya file name"}]},
            {"label": "Errors", "children": [{"label": "TypeError: str < int"}, {"label": "ValueError: khaali cell"}]},
        ],
    },
    "summary": [
        "**Data pipeline** hai: padhna → convert → check → saar → report.",
        "CSV ko `csv.DictReader` se list of dictionaries mein load kijiye, numbers ko **load karte samay** convert karte hue.",
        "**Specification** ek function mein rakhiye; batch **kisi bhi** test mein fail ho to fail hai, isliye fail niyam mein `or`.",
        "NumPy se column ka saar nikaaliye (`mean()`, `min()`, `(arr < 95).sum()`) aur ginti wale pattern se **groups** ki tulna kijiye.",
        "Nateeje `csv.writer` se **nayi** file mein likhiye; raw data kabhi overwrite mat kijiye.",
    ],
}

T["kn"] = {
    "hook": {
        "title": "Release ಅಥವಾ reject: ನಿರ್ಧಾರ ನಿಮ್ಮದು",
        "md": "Pharmaceutical plant ನಲ್ಲಿ ತಯಾರಾದ tablets ನ ಪ್ರತಿ batch factory ಇಂದ ಹೊರಡುವ ಮುಂಚೆ test ಆಗುತ್ತೆ. **Assay** ಪ್ರತಿ tablet ನಲ್ಲಿ ಸರಿಯಾದ ಪ್ರಮಾಣದ drug ಇದೆಯಾ ಅಂತ check ಮಾಡುತ್ತೆ. **Dissolution test** ದೇಹದಲ್ಲಿ drug ನಿಜವಾಗಿ tablet ಇಂದ ಹೊರಬರುತ್ತಾ ಅಂತ check ಮಾಡುತ್ತೆ. Quality control lab ಫಲಿತಾಂಶಗಳನ್ನು file ಆಗಿ ಕಳಿಸುತ್ತೆ, ಪ್ರತಿ batch ಗೆ ನಿರ್ಧಾರ ಮಾಡಬೇಕು: **release** ಅಥವಾ **reject**.\n\nಈ project lesson ನಲ್ಲಿ Unit III ನ ಎಲ್ಲವನ್ನೂ ಬಳಸಿ ಆ ನಿರ್ಧಾರವನ್ನು Python ನಲ್ಲಿ ಕಟ್ಟುತ್ತೀರಿ: CSV file ಓದುವುದು, values convert ಮಾಡುವುದು, ಪ್ರತಿ batch ಅನ್ನು specification ಜೊತೆ check ಮಾಡುವುದು, NumPy ಇಂದ ಸಾರಾಂಶ, drugs ಹೋಲಿಕೆ, ಮತ್ತು report file ಬರೆಯುವುದು.",
    },
    "learn": [
        "CSV dataset ಅನ್ನು list of dictionaries ಗೆ **load** ಮಾಡುವುದು, text ಅನ್ನು numbers ಆಗಿ ಬದಲಾಯಿಸುತ್ತಾ",
        "Function ಇಂದ ಪ್ರತಿ record ಅನ್ನು **specification** ಜೊತೆ **check** ಮಾಡುವುದು",
        "NumPy ಇಂದ column ನ **ಸಾರಾಂಶ** ಮತ್ತು **groups** ಹೋಲಿಕೆ",
        "ಫಲಿತಾಂಶಗಳನ್ನು report file ಗೆ **ಬರೆಯುವುದು**: ಒಂದು ಪೂರ್ಣ ಸಣ್ಣ **data pipeline**",
    ],
    "explanation": [
        {
            "heading": "Step 1: dataset load ಮಾಡಿ",
            "md": "QC lab file ನಲ್ಲಿ ಪ್ರತಿ batch ಗೆ ಒಂದು row: batch number, drug, **assay** (label claim ನ %) ಮತ್ತು **dissolution** (30 minutes ನಲ್ಲಿ ಕರಗಿದ %):\n\n" + E.F_QC + "\n\nಇದನ್ನು `csv.DictReader` ಇಂದ load ಮಾಡಿ, numbers ಅನ್ನು **load ಮಾಡುವಾಗಲೇ** convert ಮಾಡಿ, ಆಗ ಮುಂದಿನ ಪ್ರತಿ step ನೇರವಾಗಿ maths ಮಾಡಬಹುದು:\n\n" + E.C_LOAD + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_LOAD + "\n\n`batches` ಈಗ ಐದು dictionaries ನ list, ಒಳಗೆ ನಿಜವಾದ numbers. ಮುಂದಿನ steps ಈ list ಇಂದಲೇ ಶುರು.",
            "callout": {"title": "Specification", "md": "Release ಆಗಲು product ಪೂರೈಸಬೇಕಾದ limits. ಈ lesson ನಲ್ಲಿ: assay label claim ನ 95% ಇಂದ 105% ನಡುವೆ, ಮತ್ತು ಕನಿಷ್ಠ 80% ಕರಗಬೇಕು. ನಿಜವಾದ limits ಅನ್ನು pharmacopoeia ನಿಗದಿ ಮಾಡುತ್ತೆ, product ಇಂದ product ಗೆ ಬೇರೆ."},
        },
        {
            "heading": "Step 2: ಪ್ರತಿ batch check ಮಾಡಿ",
            "md": "Specification ಅನ್ನು ಒಂದು **function** (Lesson 2.5) ನಲ್ಲಿ ಇಡಿ, ನಿಯಮ ಒಂದೇ ಜಾಗದಲ್ಲಿ ಇರಲಿ. ಇದು batch fail ಆದ tests ನ list ಕೊಡುತ್ತೆ; ಖಾಲಿ list ಅಂದ್ರೆ pass:\n\n" + E.C_CHECK + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_CHECK + "\n\nList ನಲ್ಲಿ ಏನಾದರೂ ಇದ್ದರೆ `if problems:` True. B102 ನಲ್ಲಿ drug ಕಡಿಮೆ; B103 ನಲ್ಲಿ ಪ್ರಮಾಣ ಸರಿ, ಆದರೆ ಕಡಿಮೆ ಭಾಗ ಕರಗುತ್ತೆ.",
            "callout": {"title": "ಒಂದು ನಿಯಮ, ಒಂದು ಜಾಗ", "md": "Limits ಬದಲಾದರೆ check() function ಮಾತ್ರ ಬದಲಾಯಿಸಿ. ಅದನ್ನು call ಮಾಡುವ program ನ ಪ್ರತಿ ಭಾಗ ಹೊಸ ನಿಯಮ ಬಳಸುತ್ತೆ."},
        },
        {
            "heading": "Step 3: NumPy ಇಂದ ಸಾರಾಂಶ",
            "md": "ಒಂದು column ಅನ್ನು NumPy array (Lesson 3.4) ಗೆ ಸಂಗ್ರಹಿಸಿ, ಸಾರಾಂಶ ಮೂರು lines:\n\n" + E.C_STATS + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_STATS + "\n\nAverage 99.78% ನಲ್ಲಿ ಸರಿಯಾಗಿ ಕಾಣುತ್ತೆ, ಆದರೆ minimum ಒಂದು batch limit ಗಿಂತ ಕೆಳಗೆ ಇರುವುದನ್ನು ತೋರಿಸುತ್ತೆ. ಹಾಗಾಗಿ ಯಾವಾಗಲೂ extremes ನೋಡಿ, average ಮಾತ್ರ ಅಲ್ಲ.",
        },
        {
            "heading": "Step 4: drugs ಹೋಲಿಕೆ",
            "md": "ಪ್ರತಿ drug ನ pass rate ನೋಡಲು Lesson 3.6 ನ grouping pattern ಬಳಸಿ:\n\n" + E.C_GROUP + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_GROUP + "\n\nಒಂದು product ಮತ್ತೆ ಮತ್ತೆ ಅದೇ test ನಲ್ಲಿ fail ಆದರೆ, process ಪರಿಶೀಲಿಸಲು ಸೂಚನೆ: raw material, granulation ಅಥವಾ compression.",
        },
        {
            "heading": "Step 5: report ಬರೆಯಿರಿ",
            "md": "ಕೊನೆಯಲ್ಲಿ ಪ್ರತಿ batch ನ ನಿರ್ಧಾರವನ್ನು QA team Excel ನಲ್ಲಿ ತೆರೆಯಬಹುದಾದ **ಹೊಸ** CSV file ಗೆ ಬರೆಯಿರಿ:\n\n" + E.C_REPORT + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_REPORT + "\n\nReport `qc_report.csv` ಗೆ ಹೋಗುತ್ತೆ, ಹೊಸ ಹೆಸರು, ಹಾಗಾಗಿ `qc.csv` ನ original data ಯಾವತ್ತೂ overwrite ಆಗಲ್ಲ. ಓದು → convert → check → ಸಾರಾಂಶ → report: ನೀವು ಒಂದು ಪೂರ್ಣ **data pipeline** ಕಟ್ಟಿದ್ದೀರಿ. Unit IV ನಲ್ಲಿ Pandas ಇವುಗಳ ಪ್ರತಿ step ಅನ್ನು ಒಂದೇ line ನಲ್ಲಿ ಮಾಡುತ್ತೆ.",
            "callout": {"title": "Raw data ಯಾವತ್ತೂ overwrite ಮಾಡಬೇಡಿ", "md": "ಫಲಿತಾಂಶಗಳನ್ನು ಯಾವಾಗಲೂ ಹೊಸ file ಗೆ ಬರೆಯಿರಿ. qc.csv ಅನ್ನು \"w\" ಇಂದ open ಮಾಡಿದರೆ lab ನ original ಫಲಿತಾಂಶಗಳು ಹೋಗುತ್ತವೆ."},
        },
    ],
    "walkthrough": {
        "intro": "ಈ program CSV file ಇಂದ ಮೂರು batches ಓದಿ, ಪ್ರತಿಯೊಂದನ್ನೂ specification ಜೊತೆ check ಮಾಡಿ, ಯಾವ batches fail ಆದವು ಅಂತ ಹೇಳುತ್ತೆ.",
        "keyTerms": [
            {"meaning": "ಪ್ರತಿ batch ಅನ್ನು dictionary ಆಗಿ ಓದು."},
            {"meaning": "File ನ text ಅನ್ನು number ಆಗಿ ಬದಲಾಯಿಸು."},
            {"meaning": "Batch ಯಾವುದಾದರೂ test ನಲ್ಲಿ fail ಆದರೆ True."},
            {"meaning": "Fail ಆದ batch number ನೆನಪಿಡು."},
        ],
    },
    "errors": {
        "intro": "ಎರಡೂ errors check ಮುಂಚೆ ಸಿದ್ಧಪಡಿಸದ data ಇಂದ ಬರುತ್ತವೆ.",
        "examples": [
            {"title": "Text ಅನ್ನು number ಜೊತೆ ಹೋಲಿಸುವುದು", "md": "CSV file ನ values text, ಮತ್ತು Python text ಅನ್ನು number ಜೊತೆ ಹೋಲಿಸಲ್ಲ. ಮೊದಲು convert ಮಾಡಿ: `if float(row[\"assay\"]) < 95:`."},
            {"title": "File ನಲ್ಲಿ ಖಾಲಿ cell", "md": "B102 ನ assay cell ಖಾಲಿ, ಖಾಲಿ string number ಆಗಲ್ಲ. Lesson 3.6 ತರಹ ಮೊದಲು check ಮಾಡಿ: `if row[\"assay\"] == \"\": print(row[\"batch\"], \"assay missing\")`."},
        ],
    },
    "mistakes": [
        {"mistake": "Fail ನಿಯಮದಲ್ಲಿ `and` ಬರೆಯುವುದು: `assay < 95 and diss < 80`", "see": "Error ಇಲ್ಲ, ಆದರೆ ಒಂದೇ test ನಲ್ಲಿ fail ಆದ batches release ಆಗುತ್ತವೆ", "fix": "Batch **ಯಾವುದಾದರೂ** test ನಲ್ಲಿ fail ಆದರೆ fail: `or` ಬಳಸಿ."},
        {"mistake": "Batches ಸಂಖ್ಯೆ type ಮಾಡುವುದು: `print(3 - len(failed))`", "see": "Error ಇಲ್ಲ, ಆದರೆ file ನಲ್ಲಿ ಹೆಚ್ಚು batches ಇದ್ದಾಗ ಉತ್ತರ ತಪ್ಪು", "fix": "ಓದುವಾಗ rows ಎಣಿಸಿ, ಅಥವಾ `len(batches)` ಬಳಸಿ."},
        {"mistake": "Report ಅನ್ನು data file ಗೆ ಬರೆಯುವುದು: `open(\"qc.csv\", \"w\")`", "see": "Error ಇಲ್ಲ, ಆದರೆ lab ನ original ಫಲಿತಾಂಶಗಳು ಅಳಿಸಿಹೋಗುತ್ತವೆ", "fix": "ಫಲಿತಾಂಶಗಳನ್ನು ಹೊಸ file ಗೆ ಬರೆಯಿರಿ, `qc_report.csv` ತರಹ."},
        {"mistake": "Average ಮಾತ್ರ ನೋಡುವುದು", "see": "Error ಇಲ್ಲ, ಆದರೆ fail batch ಒಳ್ಳೆಯ mean ಹಿಂದೆ ಮರೆಯಾಗುತ್ತೆ", "fix": "`min()`, `max()` ಮತ್ತು limit ಹೊರಗೆ ಎಷ್ಟು ಅಂತ ಕೂಡ check ಮಾಡಿ."},
    ],
    "tasks": [
        {"title": "Batches ಎಣಿಸಿ", "md": "qc.csv file ನಿಮಗಾಗಿ ಈಗಾಗಲೇ ಬರೆದಿದೆ. ಅದನ್ನು **csv.DictReader** ಇಂದ ಓದಿ rows ಎಣಿಸಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["with open(\"qc.csv\") as f:\n    for row in csv.DictReader(f):", "        count += 1"]},
        {"title": "NumPy ಇಂದ mean assay", "md": "**assay** list ಇಂದ NumPy array ಮಾಡಿ, ಅದರ mean ಅನ್ನು 1 decimal ಗೆ round ಮಾಡಿ print ಮಾಡಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["assay = np.array(assay_values)", "print(\"Mean assay:\", round(assay.mean(), 1))"]},
        {"title": "Dissolution failures", "md": "**dissolution** 80 ಕ್ಕಿಂತ ಕಡಿಮೆ ಇರುವ batches ನ numbers list ಮಾಡಿ print ಮಾಡಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["batches ಮೇಲೆ loop ಓಡಿಸಿ b[\"dissolution\"] < 80 test ಮಾಡಿ.", "for b in batches:\n    if b[\"dissolution\"] < 80:\n        low.append(b[\"batch\"])"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "B201 assay ನಲ್ಲಿ fail, B202 dissolution ನಲ್ಲಿ fail, ಹಾಗಾಗಿ ಎರಡೂ reject ಆಗಬೇಕು. ಆದರೆ ಈ program ಏನೂ print ಮಾಡಲ್ಲ. ನಿಯಮ ಸರಿ ಮಾಡಿ, output ನಿಖರವಾಗಿ ಹೀಗಿರಲಿ:",
         "hints": ["Reject ಆಗಲು batch ಎರಡೂ tests ನಲ್ಲಿ fail ಆಗಬೇಕಾ, ಅಥವಾ ಒಂದರಲ್ಲಿ ಸಾಕಾ?", "and ಅನ್ನು or ಆಗಿ ಬದಲಾಯಿಸಿ."],
         "solutionNote": "and ಇದ್ದಾಗ batch ಎರಡೂ tests ನಲ್ಲಿ fail ಆದರೆ ಮಾತ್ರ reject ಆಗುತ್ತಿತ್ತು, ಯಾವುದೂ ಹಾಗಾಗಲಿಲ್ಲ. ಯಾವುದಾದರೂ test ನಲ್ಲಿ fail ಆದರೆ reject ಆಗಬೇಕು, ಹಾಗಾಗಿ ನಿಯಮಕ್ಕೆ or ಬೇಕು."},
    ],
    "quiz": [
        {"q": "CSV file ಇಂದ ಒಂದು row ಓದಿದ್ದೀರಿ. ಅದರ numbers ಹೋಲಿಸುವ ಮುಂಚೆ ಸಾಮಾನ್ಯವಾಗಿ ಏನು ಮಾಡಬೇಕು?", "why": "CSV values text; ಹೋಲಿಕೆ ಮತ್ತು maths ಗೆ numbers ಬೇಕು."},
        {"q": "Assay limit 95 ಇಂದ 105. Pass ಆಗುವ assay a ಗೆ ಯಾವ condition True?", "why": "Chained comparison range ನ ಎರಡೂ ತುದಿ check ಮಾಡುತ್ತೆ."},
        {"q": "Batch assay OR dissolution test ನಲ್ಲಿ fail ಆದರೆ reject. ಎರಡು fail conditions ಅನ್ನು ಯಾವ operator ಸೇರಿಸುತ್ತೆ?", "why": "Reject ಗೆ ಯಾವುದಾದರೂ ಒಂದು test fail ಆದರೆ ಸಾಕು."},
        {"q": "qc.csv ಅನ್ನು \"w\" ಇಂದ open ಮಾಡುವ ಬದಲು report ಅನ್ನು qc_report.csv ಗೆ ಯಾಕೆ ಬರೆಯಬೇಕು?", "why": "Write mode ಮೊದಲು file ಅಳಿಸುತ್ತೆ; raw data ಯಾವತ್ತೂ overwrite ಮಾಡಬೇಡಿ."},
        {"q": "assay = np.array([99.2, 94.1, 101.5])\nprint((assay < 95).sum())\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "ಒಂದು value 95 ಕ್ಕಿಂತ ಕಡಿಮೆ, True ಅನ್ನು 1 ಅಂತ ಎಣಿಸುತ್ತಾರೆ."},
        {"q": "ಈ ಸಣ್ಣ data pipeline ನ ಸರಿಯಾದ ಕ್ರಮ ಯಾವುದು?", "why": "ಓದದ, convert ಮಾಡದ data ಅನ್ನು check ಅಥವಾ summarise ಮಾಡಲು ಆಗಲ್ಲ."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 3.7 · QC dataset project",
        "children": [
            {"label": "ಓದು", "children": [{"label": "csv.DictReader"}, {"label": "ಪ್ರತಿ batch ಗೆ dict"}, {"label": "Rows ಎಣಿಸು"}]},
            {"label": "Convert", "children": [{"label": "float() / int()"}, {"label": "ಖಾಲಿ cells"}, {"label": "Load ಮಾಡುವಾಗಲೇ"}]},
            {"label": "Spec check", "children": [{"label": "95 <= assay <= 105"}, {"label": "dissolution >= 80"}, {"label": "ಯಾವುದು fail ಆದರೂ: or"}]},
            {"label": "ಸಾರಾಂಶ", "children": [{"label": "NumPy mean()"}, {"label": "min() max()"}, {"label": "(arr < 95).sum()"}]},
            {"label": "Group ಮತ್ತು report", "children": [{"label": "ಪ್ರತಿ drug pass count"}, {"label": "csv.writer"}, {"label": "ಹೊಸ file ಹೆಸರು"}]},
            {"label": "Errors", "children": [{"label": "TypeError: str < int"}, {"label": "ValueError: ಖಾಲಿ cell"}]},
        ],
    },
    "summary": [
        "**Data pipeline**: ಓದು → convert → check → ಸಾರಾಂಶ → report.",
        "CSV ಅನ್ನು `csv.DictReader` ಇಂದ list of dictionaries ಗೆ load ಮಾಡಿ, numbers ಅನ್ನು **load ಮಾಡುವಾಗಲೇ** convert ಮಾಡಿ.",
        "**Specification** ಅನ್ನು ಒಂದು function ನಲ್ಲಿ ಇಡಿ; batch **ಯಾವುದಾದರೂ** test ನಲ್ಲಿ fail ಆದರೆ fail, ಹಾಗಾಗಿ fail ನಿಯಮದಲ್ಲಿ `or`.",
        "NumPy ಇಂದ column ಸಾರಾಂಶ (`mean()`, `min()`, `(arr < 95).sum()`), ಎಣಿಕೆಯ pattern ಇಂದ **groups** ಹೋಲಿಕೆ.",
        "ಫಲಿತಾಂಶಗಳನ್ನು `csv.writer` ಇಂದ **ಹೊಸ** file ಗೆ ಬರೆಯಿರಿ; raw data ಯಾವತ್ತೂ overwrite ಮಾಡಬೇಡಿ.",
    ],
}

NARR = {
    "hi": [
        "यह program tablets के तीन batches के लिए release का फ़ैसला करता है।",
        "import csv, CSV module load करता है।",
        "ये दो lines lab के नतीजे qc dot csv में save करती हैं: एक header और तीन batches। असली ज़िंदगी में यह file lab से आती।",
        "total batches गिनेगा। यह zero से शुरू होता है।",
        "failed, fail होने वाले batches के numbers जमा करेगा।",
        "DictReader एक बार में एक batch देता है। पहला है B one oh one।",
        "total एक हो जाता है।",
        "Assay और dissolution file में text हैं, इसलिए float उन्हें numbers बनाता है: निन्यानवे दशमलव दो, और बानवे।",
        "यह specification है। Batch fail है अगर assay पचानवे से एक सौ पाँच के बाहर हो, या अस्सी percent से कम घुले। B one oh one दोनों tests pass करता है।",
        "B one oh two का assay चौरानवे दशमलव एक है, limit से नीचे, इसलिए यह failed में जुड़ता है।",
        "B one oh three का assay अच्छा है, पर सिर्फ़ छिहत्तर percent घुलता है। यह भी fail है।",
        "print fail हुए batches की list दिखाता है।",
        "तीन batches घटा दो failures: एक batch release हो सकता है।",
    ],
    "hinglish": [
        "Yeh program tablets ke teen batches ke liye release ka faisla karta hai.",
        "import csv, CSV module load karta hai.",
        "Yeh do lines lab ke nateeje qc dot csv mein save karti hain: ek header aur teen batches. Asli zindagi mein yeh file lab se aati.",
        "total batches ginega. Yeh zero se shuru hota hai.",
        "failed, fail hone wale batches ke numbers jama karega.",
        "DictReader ek baar mein ek batch deta hai. Pehla hai B one oh one.",
        "total ek ho jaata hai.",
        "Assay aur dissolution file mein text hain, isliye float unhe numbers banaata hai: ninyaanve dashamlav do, aur baanve.",
        "Yeh specification hai. Batch fail hai agar assay pachaanve se ek sau paanch ke bahar ho, ya assi percent se kam ghule. B one oh one dono tests pass karta hai.",
        "B one oh two ka assay chauraanve dashamlav ek hai, limit se neeche, isliye yeh failed mein judta hai.",
        "B one oh three ka assay achha hai, par sirf chhihattar percent ghulta hai. Yeh bhi fail hai.",
        "print fail hue batches ki list dikhaata hai.",
        "Teen batches ghata do failures: ek batch release ho sakta hai.",
    ],
    "kn": [
        "ಈ program tablets ನ ಮೂರು batches ಗೆ release ನಿರ್ಧಾರ ಮಾಡುತ್ತೆ.",
        "import csv, CSV module load ಮಾಡುತ್ತೆ.",
        "ಈ ಎರಡು lines lab ಫಲಿತಾಂಶಗಳನ್ನು qc dot csv ಆಗಿ save ಮಾಡುತ್ತವೆ: ಒಂದು header ಮತ್ತು ಮೂರು batches. ನಿಜ ಜೀವನದಲ್ಲಿ ಈ file lab ಇಂದ ಬರುತ್ತೆ.",
        "total batches ಎಣಿಸುತ್ತೆ. ಇದು zero ಇಂದ ಶುರು.",
        "failed, fail ಆದ batches ನ numbers ಸಂಗ್ರಹಿಸುತ್ತೆ.",
        "DictReader ಒಂದು ಸಲಕ್ಕೆ ಒಂದು batch ಕೊಡುತ್ತೆ. ಮೊದಲದು B one oh one.",
        "total ಒಂದು ಆಗುತ್ತೆ.",
        "Assay ಮತ್ತು dissolution file ನಲ್ಲಿ text, ಹಾಗಾಗಿ float ಅವನ್ನು numbers ಮಾಡುತ್ತೆ: ತೊಂಬತ್ತೊಂಬತ್ತು ಪಾಯಿಂಟ್ ಎರಡು, ಮತ್ತು ತೊಂಬತ್ತೆರಡು.",
        "ಇದು specification. Assay ತೊಂಬತ್ತೈದು ಇಂದ ನೂರ ಐದು ಹೊರಗೆ ಇದ್ದರೆ, ಅಥವಾ ಎಂಬತ್ತು percent ಗಿಂತ ಕಡಿಮೆ ಕರಗಿದರೆ batch fail. B one oh one ಎರಡೂ tests pass ಮಾಡುತ್ತೆ.",
        "B one oh two ನ assay ತೊಂಬತ್ತನಾಲ್ಕು ಪಾಯಿಂಟ್ ಒಂದು, limit ಗಿಂತ ಕೆಳಗೆ, ಹಾಗಾಗಿ failed ಗೆ ಸೇರುತ್ತೆ.",
        "B one oh three ನ assay ಚೆನ್ನಾಗಿದೆ, ಆದರೆ ಎಪ್ಪತ್ತಾರು percent ಮಾತ್ರ ಕರಗುತ್ತೆ. ಇದೂ fail.",
        "print fail ಆದ batches list ತೋರಿಸುತ್ತೆ.",
        "ಮೂರು batches ಕಳೆ ಎರಡು failures: ಒಂದು batch release ಆಗಬಹುದು.",
    ],
}

ANIM = {
    "hi": [
        "Quality control के नतीजे CSV file में आते हैं: हर batch की एक row, उसके assay और dissolution के साथ।",
        "Step एक: DictReader हर row को dictionary के रूप में पढ़ता है।",
        "Step दो: values text हैं, इसलिए float उन्हें numbers बनाता है।",
        "Step तीन: हर batch specification से check होता है। B one oh two का assay चौरानवे दशमलव एक है, पचानवे से नीचे, इसलिए यह fail है।",
        "B one oh three सिर्फ़ छिहत्तर percent घुलता है, अस्सी से नीचे। यह भी fail है।",
        "एक batch release हो सकता है, और दो reject होते हैं। यह release का फ़ैसला है, आपके program ने किया।",
    ],
    "hinglish": [
        "Quality control ke nateeje CSV file mein aate hain: har batch ki ek row, uske assay aur dissolution ke saath.",
        "Step ek: DictReader har row ko dictionary ke roop mein padhta hai.",
        "Step do: values text hain, isliye float unhe numbers banaata hai.",
        "Step teen: har batch specification se check hota hai. B one oh two ka assay chauraanve dashamlav ek hai, pachaanve se neeche, isliye yeh fail hai.",
        "B one oh three sirf chhihattar percent ghulta hai, assi se neeche. Yeh bhi fail hai.",
        "Ek batch release ho sakta hai, aur do reject hote hain. Yeh release ka faisla hai, aapke program ne kiya.",
    ],
    "kn": [
        "Quality control ಫಲಿತಾಂಶಗಳು CSV file ಆಗಿ ಬರುತ್ತವೆ: ಪ್ರತಿ batch ಗೆ ಒಂದು row, ಅದರ assay ಮತ್ತು dissolution ಜೊತೆ.",
        "Step ಒಂದು: DictReader ಪ್ರತಿ row ಅನ್ನು dictionary ಆಗಿ ಓದುತ್ತೆ.",
        "Step ಎರಡು: values text, ಹಾಗಾಗಿ float ಅವನ್ನು numbers ಮಾಡುತ್ತೆ.",
        "Step ಮೂರು: ಪ್ರತಿ batch specification ಜೊತೆ check ಆಗುತ್ತೆ. B one oh two ನ assay ತೊಂಬತ್ತನಾಲ್ಕು ಪಾಯಿಂಟ್ ಒಂದು, ತೊಂಬತ್ತೈದಕ್ಕಿಂತ ಕೆಳಗೆ, ಹಾಗಾಗಿ fail.",
        "B one oh three ಎಪ್ಪತ್ತಾರು percent ಮಾತ್ರ ಕರಗುತ್ತೆ, ಎಂಬತ್ತಕ್ಕಿಂತ ಕೆಳಗೆ. ಇದೂ fail.",
        "ಒಂದು batch release ಆಗಬಹುದು, ಎರಡು reject. ಇದು release ನಿರ್ಧಾರ, ನಿಮ್ಮ program ಮಾಡಿದ್ದು.",
    ],
}

if __name__ == "__main__":
    build("3-7", "anim-pipeline", T, NARR, ANIM)

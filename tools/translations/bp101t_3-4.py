"""Lesson 3.4 translations (Hindi, Hinglish, Kannada) and voice scripts."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import build  # noqa: E402

_spec = importlib.util.spec_from_file_location("en34", os.path.join(os.path.dirname(__file__), "..", "lessons", "bp101t_3-4_en.py"))
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)

T = {}

T["hi"] = {
    "hook": {
        "title": "पाँच सौ patients के लिए एक line",
        "md": "एक clinical trial में 500 patients का dose milligrams में दर्ज है, और report में grams चाहिए। List के साथ आप `for` loop लिखकर हर एक को divide करेंगे। **NumPy** के साथ आप `doses / 1000` लिखते हैं, और सभी 500 एक साथ बदल जाते हैं।\n\n**NumPy** (Numerical Python) वह library है जो Python को numbers के साथ तेज़ बनाती है। Unit IV का Pandas और Unit V का Matplotlib इसी पर बने हैं, और आगे course में मिलने वाले machine learning tools भी। सब कुछ एक object से शुरू होता है: **array**।",
    },
    "learn": [
        "**NumPy import** करना और list से **array** बनाना",
        "**Vectorised** maths हर item पर एक साथ कैसे चलता है, और list अलग क्यों बर्ताव करती है",
        "Readings का **mean**, **max**, **min** और **standard deviation** निकालना",
        "Condition से array **filter** करना, जैसे 125 से ऊपर की सारी readings",
    ],
    "explanation": [
        {
            "heading": "Array बनाना",
            "md": "NumPy ऊपर एक बार import होता है, रिवाज़ के मुताबिक छोटे नाम **np** से। `np.array()` list को **array** में बदलता है:\n\n" + E.C_MAKE + "\n\nयह print करता है:\n\n" + E.O_MAKE + "\n\nArray बिना commas के print होता है। `.shape` उसका size देता है: `(3,)` मतलब एक row में 3 items। Indexing और slicing बिल्कुल lists जैसे चलते हैं। List से अलग, array में **एक ही type** की values होती हैं, आमतौर पर numbers।",
            "callout": {"title": "Array", "md": "एक type की values का NumPy grid, np.array() से बनता है। Array पर maths हर item पर एक साथ होता है।"},
        },
        {
            "heading": "पूरे array पर maths",
            "md": "यह है बड़ा idea। Array पर कोई operation **हर item** पर लगता है, बिना loop के। इसे **vectorised** maths कहते हैं:\n\n" + E.C_VEC + "\n\nयह print करता है:\n\n" + E.O_VEC + "\n\nआखिरी line ध्यान से देखिए: **list** पर `* 2` list को दोहराता है, पर **array** पर हर number को दुगुना करता है। इसी फ़र्क की वजह से scientists data के लिए arrays use करते हैं।",
            "callout": {"title": "list * 2, array * 2 नहीं है", "md": "List दोहराती है; array हिसाब लगाता है। Readings पर maths करने से पहले उन्हें np.array() से बदलिए।"},
        },
        {
            "heading": "दो arrays एक साथ",
            "md": "एक ही length के दो arrays **item-दर-item** जुड़ते हैं: पहला पहले से, दूसरा दूसरे से। यहाँ हर बच्चे का dose है weight गुणा mg per kg:\n\n" + E.C_TWO + "\n\nयह print करता है:\n\n" + E.O_TWO + "\n\n12 × 15 = 180, 20 × 15 = 300 और 35 × 10 = 350, एक line में। Lengths न मिलें तो NumPy error देता है।",
        },
        {
            "heading": "एक शब्द में statistics",
            "md": "हर lab report में लगने वाले सार के लिए arrays के पास methods हैं:\n\n" + E.C_STATS + "\n\nयह print करता है:\n\n" + E.O_STATS + "\n\n- `mean()` average है, `max()` और `min()` सबसे बड़ा और सबसे छोटा, `sum()` कुल जोड़।\n- `std()` **standard deviation** है: readings कितनी फैली हुई हैं। छोटी value मतलब readings एक जैसी हैं।\n- `np.median(sugar)` readings sort करने पर बीच की value देता है।",
        },
        {
            "heading": "Condition से filter करना",
            "md": "Array पर comparison से `True` और `False` का array मिलता है, हर item के लिए एक। उसे square brackets के अंदर रखने पर सिर्फ़ `True` वाले items बचते हैं:\n\n" + E.C_MASK + "\n\nयह print करता है:\n\n" + E.O_MASK + "\n\nदो readings 125 से ऊपर थीं। `True` को 1 गिना जाता है, इसलिए `.sum()` उन्हें गिनता है। Conditions जोड़ने के लिए `&` (and) या `|` (or) use कीजिए, **हर condition के चारों ओर brackets** के साथ: `sugar[(sugar > 100) & (sugar < 130)]`।",
            "callout": {"title": "बने-बनाए arrays", "md": "np.arange(0, 25, 6) देता है [0 6 12 18 24], range() जैसा। np.linspace(0, 24, 5) 0 से 24 तक बराबर दूरी के 5 numbers देता है: Unit V में time points के लिए use करेंगे।"},
        },
    ],
    "walkthrough": {
        "intro": "यह program एक batch की छह tablets का वज़न check करता है: average, range, और 490 से 510 mg के बाहर कोई tablet।",
        "keyTerms": [
            {"meaning": "NumPy को छोटे नाम np से load करो।"},
            {"meaning": "List को NumPy array में बदलो।"},
            {"meaning": "सारी values का average।"},
            {"meaning": "सिर्फ़ condition से मेल खाने वाली values रखो।"},
        ],
    },
    "errors": {
        "intro": "NumPy के साथ beginners को सबसे पहले ये दो errors मिलती हैं।",
        "examples": [
            {"title": "Import किए बिना np use करना", "md": "जब तक import न करें, Python `np` को नहीं जानता। Program के ऊपर `import numpy as np` जोड़िए।"},
            {"title": "अलग length के arrays जोड़ना", "md": "Item-दर-item maths के लिए दोनों तरफ़ बराबर items चाहिए: यहाँ 3 weights हैं पर सिर्फ़ 2 doses। Arrays की length बराबर कीजिए।"},
        ],
    },
    "mistakes": [
        {"mistake": "List पर maths करना: `[250, 500] * 2`", "see": "कोई error नहीं, पर `[250, 500, 250, 500]` मिलता है", "fix": "पहले array बनाइए: `np.array([250, 500]) * 2`।"},
        {"mistake": "Filter में `and` / `or` use करना: `w[w > 490 and w < 510]`", "see": "ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()", "fix": "Brackets के साथ `&` और `|` use कीजिए: `w[(w > 490) & (w < 510)]`।"},
        {"mistake": "Brackets छोड़ देना: `w[w > 490 & w < 510]`", "see": "Error या गलत नतीजा, क्योंकि `&` पहले हल होता है", "fix": "हर condition के चारों ओर brackets लगाइए।"},
        {"mistake": "Text और numbers मिलाना: `np.array([250, \"500\"])`", "see": "कोई error नहीं, पर हर item text बन जाता है और maths fail होता है", "fix": "Array में सिर्फ़ numbers रखिए; text को पहले int() या float() से बदलिए।"},
    ],
    "tasks": [
        {"title": "Milligrams से grams", "md": "**doses_mg** को NumPy array में बदलिए और **एक** calculation से हर dose **grams** में print कीजिए (1000 से divide)। Output बिल्कुल यह होना चाहिए:",
         "hints": ["arr = np.array(doses_mg) array बनाता है।", "print(np.array(doses_mg) / 1000)"]},
        {"title": "तीन बच्चों के doses", "md": "Dose है शरीर के वज़न के **हर kg पर 15 mg**। **weight** array को 15 से गुणा करके doses print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["एक गुणा पूरे array पर चलता है।", "print(weight * 15)"]},
        {"title": "Average और सबसे ज़्यादा temperature", "md": "**Mean** temperature 1 decimal तक round करके, और **सबसे ज़्यादा** temperature print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["round(temps.mean(), 1) average को 1 decimal तक round करता है।", "print(\"Max:\", temps.max())"]},
        {"title": "Bug ढूँढिए", "md": "इस program को fever वाली readings (38 से ऊपर और 39.5 से नीचे) दिखानी हैं, पर यह ValueError के साथ crash होता है। Filter ठीक कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["and पूरे arrays पर काम नहीं करता। NumPy उसकी जगह & use करता है।", "fever = temps[(temps > 38) & (temps < 39.5)]"],
         "solutionNote": "and को एक True या False चाहिए, पर temps > 38 उनका पूरा array है। & दोनों arrays को item-दर-item जोड़ता है, और हर condition को अपने brackets चाहिए।"},
    ],
    "quiz": [
        {"q": "import numpy as np\na = np.array([1, 2, 3])\nprint(a * 2)\n\nयह क्या print करता है?", "why": "Array पर maths हर item पर होता है।"},
        {"q": "print([1, 2, 3] * 2)\n\nयह क्या print करता है?", "why": "List पर * list को दोहराता है।"},
        {"q": "import numpy as np क्या करता है?", "why": "यह library को छोटे नाम np से load करता है।"},
        {"q": "a = np.array([10, 20, 30])\nprint(a.mean())\n\nयह क्या print करता है?", "why": "Mean है (10 + 20 + 30) / 3 = 20.0।"},
        {"q": "a = np.array([10, 20, 30]) के लिए a[a > 15] क्या देता है?", "why": "Mask सिर्फ़ वे items रखता है जहाँ condition True है।"},
        {"q": "NumPy filter में दो conditions कैसे जोड़ते हैं?", "why": "& या | use कीजिए और हर condition को brackets में रखिए।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 3.4 · NumPy arrays",
        "children": [
            {"label": "बनाना", "children": [{"label": "import numpy as np"}, {"label": "np.array(list)"}, {"label": ".shape"}]},
            {"label": "Vector maths", "children": [{"label": "arr / 1000"}, {"label": "arr1 * arr2"}, {"label": "Loop नहीं चाहिए"}]},
            {"label": "Statistics", "children": [{"label": "mean()"}, {"label": "max() min() sum()"}, {"label": "std() फैलाव"}]},
            {"label": "Filter", "children": [{"label": "arr > 125 → True/False"}, {"label": "arr[arr > 125]"}, {"label": "& | brackets के साथ"}]},
            {"label": "list से फ़र्क", "children": [{"label": "list * 2 दोहराता है"}, {"label": "array * 2 दुगुना करता है"}, {"label": "Array में एक type"}]},
            {"label": "Errors", "children": [{"label": "NameError: np"}, {"label": "ValueError: shapes"}]},
        ],
    },
    "summary": [
        "**NumPy** `import numpy as np` से load होता है; `np.array(list)` एक type का **array** बनाता है।",
        "Array पर maths **vectorised** है: `doses / 1000` हर item बदलता है, बिना loop के। List पर `* 2` दोहराता है।",
        "बराबर length के दो arrays **item-दर-item** जुड़ते हैं: `weight * mg_per_kg`।",
        "`mean()`, `max()`, `min()`, `sum()` और `std()` एक शब्द में readings का सार देते हैं।",
        "Condition से array filter होता है: `sugar[sugar > 125]`; conditions `&` और `|` से जोड़िए, हर एक brackets में।",
    ],
}

T["hinglish"] = {
    "hook": {
        "title": "Paanch sau patients ke liye ek line",
        "md": "Ek clinical trial mein 500 patients ka dose milligrams mein darj hai, aur report mein grams chahiye. List ke saath aap `for` loop likhkar har ek ko divide karenge. **NumPy** ke saath aap `doses / 1000` likhte hain, aur sabhi 500 ek saath badal jaate hain.\n\n**NumPy** (Numerical Python) woh library hai jo Python ko numbers ke saath tez banaati hai. Unit IV ka Pandas aur Unit V ka Matplotlib isi par bane hain, aur aage course mein milne wale machine learning tools bhi. Sab kuch ek object se shuru hota hai: **array**.",
    },
    "learn": [
        "**NumPy import** karna aur list se **array** banana",
        "**Vectorised** maths har item par ek saath kaise chalta hai, aur list alag kyun bartaav karti hai",
        "Readings ka **mean**, **max**, **min** aur **standard deviation** nikaalna",
        "Condition se array **filter** karna, jaise 125 se upar ki saari readings",
    ],
    "explanation": [
        {
            "heading": "Array banana",
            "md": "NumPy upar ek baar import hota hai, riwaaz ke mutaabik chhote naam **np** se. `np.array()` list ko **array** mein badalta hai:\n\n" + E.C_MAKE + "\n\nYeh print karta hai:\n\n" + E.O_MAKE + "\n\nArray bina commas ke print hota hai. `.shape` uska size deta hai: `(3,)` matlab ek row mein 3 items. Indexing aur slicing bilkul lists jaise chalte hain. List se alag, array mein **ek hi type** ki values hoti hain, aam taur par numbers.",
            "callout": {"title": "Array", "md": "Ek type ki values ka NumPy grid, np.array() se banta hai. Array par maths har item par ek saath hota hai."},
        },
        {
            "heading": "Poore array par maths",
            "md": "Yeh hai bada idea. Array par koi operation **har item** par lagta hai, bina loop ke. Ise **vectorised** maths kehte hain:\n\n" + E.C_VEC + "\n\nYeh print karta hai:\n\n" + E.O_VEC + "\n\nAakhri line dhyaan se dekhiye: **list** par `* 2` list ko dohraata hai, par **array** par har number ko dugna karta hai. Isi farq ki wajah se scientists data ke liye arrays use karte hain.",
            "callout": {"title": "list * 2, array * 2 nahi hai", "md": "List dohraati hai; array hisaab lagaata hai. Readings par maths karne se pehle unhe np.array() se badaliye."},
        },
        {
            "heading": "Do arrays ek saath",
            "md": "Ek hi length ke do arrays **item-dar-item** judte hain: pehla pehle se, doosra doosre se. Yahaan har bachche ka dose hai weight guna mg per kg:\n\n" + E.C_TWO + "\n\nYeh print karta hai:\n\n" + E.O_TWO + "\n\n12 × 15 = 180, 20 × 15 = 300 aur 35 × 10 = 350, ek line mein. Lengths na milein to NumPy error deta hai.",
        },
        {
            "heading": "Ek shabd mein statistics",
            "md": "Har lab report mein lagne wale saar ke liye arrays ke paas methods hain:\n\n" + E.C_STATS + "\n\nYeh print karta hai:\n\n" + E.O_STATS + "\n\n- `mean()` average hai, `max()` aur `min()` sabse bada aur sabse chhota, `sum()` kul jod.\n- `std()` **standard deviation** hai: readings kitni phaili hui hain. Chhoti value matlab readings ek jaisi hain.\n- `np.median(sugar)` readings sort karne par beech ki value deta hai.",
        },
        {
            "heading": "Condition se filter karna",
            "md": "Array par comparison se `True` aur `False` ka array milta hai, har item ke liye ek. Use square brackets ke andar rakhne par sirf `True` wale items bachte hain:\n\n" + E.C_MASK + "\n\nYeh print karta hai:\n\n" + E.O_MASK + "\n\nDo readings 125 se upar thi. `True` ko 1 gina jaata hai, isliye `.sum()` unhe ginta hai. Conditions jodne ke liye `&` (and) ya `|` (or) use kijiye, **har condition ke chaaron or brackets** ke saath: `sugar[(sugar > 100) & (sugar < 130)]`.",
            "callout": {"title": "Bane-banaaye arrays", "md": "np.arange(0, 25, 6) deta hai [0 6 12 18 24], range() jaisa. np.linspace(0, 24, 5) 0 se 24 tak barabar doori ke 5 numbers deta hai: Unit V mein time points ke liye use karenge."},
        },
    ],
    "walkthrough": {
        "intro": "Yeh program ek batch ki chhah tablets ka wazan check karta hai: average, range, aur 490 se 510 mg ke bahar koi tablet.",
        "keyTerms": [
            {"meaning": "NumPy ko chhote naam np se load karo."},
            {"meaning": "List ko NumPy array mein badlo."},
            {"meaning": "Saari values ka average."},
            {"meaning": "Sirf condition se mel khaane wali values rakho."},
        ],
    },
    "errors": {
        "intro": "NumPy ke saath beginners ko sabse pehle yeh do errors milti hain.",
        "examples": [
            {"title": "Import kiye bina np use karna", "md": "Jab tak import na karein, Python `np` ko nahi jaanta. Program ke upar `import numpy as np` jodiye."},
            {"title": "Alag length ke arrays jodna", "md": "Item-dar-item maths ke liye dono taraf barabar items chahiye: yahaan 3 weights hain par sirf 2 doses. Arrays ki length barabar kijiye."},
        ],
    },
    "mistakes": [
        {"mistake": "List par maths karna: `[250, 500] * 2`", "see": "Koi error nahi, par `[250, 500, 250, 500]` milta hai", "fix": "Pehle array banaiye: `np.array([250, 500]) * 2`."},
        {"mistake": "Filter mein `and` / `or` use karna: `w[w > 490 and w < 510]`", "see": "ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()", "fix": "Brackets ke saath `&` aur `|` use kijiye: `w[(w > 490) & (w < 510)]`."},
        {"mistake": "Brackets chhod dena: `w[w > 490 & w < 510]`", "see": "Error ya galat nateeja, kyunki `&` pehle hal hota hai", "fix": "Har condition ke chaaron or brackets lagaiye."},
        {"mistake": "Text aur numbers milaana: `np.array([250, \"500\"])`", "see": "Koi error nahi, par har item text ban jaata hai aur maths fail hota hai", "fix": "Array mein sirf numbers rakhiye; text ko pehle int() ya float() se badaliye."},
    ],
    "tasks": [
        {"title": "Milligrams se grams", "md": "**doses_mg** ko NumPy array mein badaliye aur **ek** calculation se har dose **grams** mein print kijiye (1000 se divide). Output bilkul yeh hona chahiye:",
         "hints": ["arr = np.array(doses_mg) array banata hai.", "print(np.array(doses_mg) / 1000)"]},
        {"title": "Teen bachchon ke doses", "md": "Dose hai shareer ke wazan ke **har kg par 15 mg**. **weight** array ko 15 se guna karke doses print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["Ek guna poore array par chalta hai.", "print(weight * 15)"]},
        {"title": "Average aur sabse zyada temperature", "md": "**Mean** temperature 1 decimal tak round karke, aur **sabse zyada** temperature print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["round(temps.mean(), 1) average ko 1 decimal tak round karta hai.", "print(\"Max:\", temps.max())"]},
        {"title": "Bug dhoondhiye", "md": "Is program ko fever wali readings (38 se upar aur 39.5 se neeche) dikhaani hain, par yeh ValueError ke saath crash hota hai. Filter theek kijiye taaki output bilkul yeh ho:",
         "hints": ["and poore arrays par kaam nahi karta. NumPy uski jagah & use karta hai.", "fever = temps[(temps > 38) & (temps < 39.5)]"],
         "solutionNote": "and ko ek True ya False chahiye, par temps > 38 unka poora array hai. & dono arrays ko item-dar-item jodta hai, aur har condition ko apne brackets chahiye."},
    ],
    "quiz": [
        {"q": "import numpy as np\na = np.array([1, 2, 3])\nprint(a * 2)\n\nYeh kya print karta hai?", "why": "Array par maths har item par hota hai."},
        {"q": "print([1, 2, 3] * 2)\n\nYeh kya print karta hai?", "why": "List par * list ko dohraata hai."},
        {"q": "import numpy as np kya karta hai?", "why": "Yeh library ko chhote naam np se load karta hai."},
        {"q": "a = np.array([10, 20, 30])\nprint(a.mean())\n\nYeh kya print karta hai?", "why": "Mean hai (10 + 20 + 30) / 3 = 20.0."},
        {"q": "a = np.array([10, 20, 30]) ke liye a[a > 15] kya deta hai?", "why": "Mask sirf woh items rakhta hai jahaan condition True hai."},
        {"q": "NumPy filter mein do conditions kaise jodte hain?", "why": "& ya | use kijiye aur har condition ko brackets mein rakhiye."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 3.4 · NumPy arrays",
        "children": [
            {"label": "Banana", "children": [{"label": "import numpy as np"}, {"label": "np.array(list)"}, {"label": ".shape"}]},
            {"label": "Vector maths", "children": [{"label": "arr / 1000"}, {"label": "arr1 * arr2"}, {"label": "Loop nahi chahiye"}]},
            {"label": "Statistics", "children": [{"label": "mean()"}, {"label": "max() min() sum()"}, {"label": "std() phailaav"}]},
            {"label": "Filter", "children": [{"label": "arr > 125 → True/False"}, {"label": "arr[arr > 125]"}, {"label": "& | brackets ke saath"}]},
            {"label": "list se farq", "children": [{"label": "list * 2 dohraata hai"}, {"label": "array * 2 dugna karta hai"}, {"label": "Array mein ek type"}]},
            {"label": "Errors", "children": [{"label": "NameError: np"}, {"label": "ValueError: shapes"}]},
        ],
    },
    "summary": [
        "**NumPy** `import numpy as np` se load hota hai; `np.array(list)` ek type ka **array** banata hai.",
        "Array par maths **vectorised** hai: `doses / 1000` har item badalta hai, bina loop ke. List par `* 2` dohraata hai.",
        "Barabar length ke do arrays **item-dar-item** judte hain: `weight * mg_per_kg`.",
        "`mean()`, `max()`, `min()`, `sum()` aur `std()` ek shabd mein readings ka saar dete hain.",
        "Condition se array filter hota hai: `sugar[sugar > 125]`; conditions `&` aur `|` se jodiye, har ek brackets mein.",
    ],
}

T["kn"] = {
    "hook": {
        "title": "ಐನೂರು patients ಗೆ ಒಂದೇ line",
        "md": "ಒಂದು clinical trial ನಲ್ಲಿ 500 patients ನ dose milligrams ನಲ್ಲಿ ದಾಖಲಾಗಿದೆ, report ಗೆ grams ಬೇಕು. List ಜೊತೆ `for` loop ಬರೆದು ಪ್ರತಿಯೊಂದನ್ನೂ divide ಮಾಡಬೇಕು. **NumPy** ಜೊತೆ `doses / 1000` ಬರೆದರೆ ಸಾಕು, ಎಲ್ಲಾ 500 ಒಂದೇ ಸಲ ಬದಲಾಗುತ್ತವೆ.\n\n**NumPy** (Numerical Python) Python ಅನ್ನು numbers ಜೊತೆ ವೇಗವಾಗಿಸುವ library. Unit IV ನ Pandas ಮತ್ತು Unit V ನ Matplotlib ಇದರ ಮೇಲೆಯೇ ಕಟ್ಟಲಾಗಿದೆ, course ನಲ್ಲಿ ಮುಂದೆ ಸಿಗುವ machine learning tools ಕೂಡ. ಎಲ್ಲವೂ ಒಂದು object ಇಂದ ಶುರು: **array**.",
    },
    "learn": [
        "**NumPy import** ಮಾಡಿ list ಇಂದ **array** ಮಾಡುವುದು",
        "**Vectorised** maths ಪ್ರತಿ item ಮೇಲೆ ಒಂದೇ ಸಲ ಹೇಗೆ ಆಗುತ್ತೆ, list ಯಾಕೆ ಬೇರೆ ತರಹ ವರ್ತಿಸುತ್ತೆ",
        "Readings ನ **mean**, **max**, **min** ಮತ್ತು **standard deviation**",
        "Condition ಇಂದ array **filter** ಮಾಡುವುದು, 125 ಕ್ಕಿಂತ ಹೆಚ್ಚಿನ ಎಲ್ಲಾ readings ತರಹ",
    ],
    "explanation": [
        {
            "heading": "Array ಮಾಡುವುದು",
            "md": "NumPy ಅನ್ನು ಮೇಲೆ ಒಮ್ಮೆ import ಮಾಡುತ್ತಾರೆ, ರೂಢಿಯಂತೆ **np** ಎಂಬ ಸಣ್ಣ ಹೆಸರಿನಲ್ಲಿ. `np.array()` list ಅನ್ನು **array** ಆಗಿ ಬದಲಾಯಿಸುತ್ತೆ:\n\n" + E.C_MAKE + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_MAKE + "\n\nArray commas ಇಲ್ಲದೆ print ಆಗುತ್ತೆ. `.shape` ಅದರ size ಕೊಡುತ್ತೆ: `(3,)` ಅಂದ್ರೆ ಒಂದು row ನಲ್ಲಿ 3 items. Indexing ಮತ್ತು slicing lists ತರಹವೇ. List ಹಾಗಲ್ಲ, array ನಲ್ಲಿ **ಒಂದೇ type** ನ values ಇರುತ್ತವೆ, ಸಾಮಾನ್ಯವಾಗಿ numbers.",
            "callout": {"title": "Array", "md": "ಒಂದೇ type ನ values ಇರುವ NumPy grid, np.array() ಇಂದ ಮಾಡುತ್ತಾರೆ. Array ಮೇಲಿನ maths ಪ್ರತಿ item ಮೇಲೆ ಒಂದೇ ಸಲ ಆಗುತ್ತೆ."},
        },
        {
            "heading": "ಇಡೀ array ಮೇಲೆ maths",
            "md": "ಇದೇ ದೊಡ್ಡ idea. Array ಮೇಲಿನ ಒಂದು operation **ಪ್ರತಿ item** ಗೂ ಅನ್ವಯ ಆಗುತ್ತೆ, loop ಇಲ್ಲದೆ. ಇದನ್ನು **vectorised** maths ಅಂತಾರೆ:\n\n" + E.C_VEC + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_VEC + "\n\nಕೊನೆಯ line ಗಮನಿಸಿ: **list** ಮೇಲೆ `* 2` list ಅನ್ನು ಪುನರಾವರ್ತಿಸುತ್ತೆ, ಆದರೆ **array** ಮೇಲೆ ಪ್ರತಿ number ಅನ್ನು ಎರಡರಷ್ಟು ಮಾಡುತ್ತೆ. ಈ ವ್ಯತ್ಯಾಸದಿಂದಲೇ scientists data ಗೆ arrays ಬಳಸುತ್ತಾರೆ.",
            "callout": {"title": "list * 2, array * 2 ಅಲ್ಲ", "md": "List ಪುನರಾವರ್ತಿಸುತ್ತೆ; array ಲೆಕ್ಕ ಹಾಕುತ್ತೆ. Readings ಮೇಲೆ maths ಮಾಡುವ ಮುಂಚೆ np.array() ಇಂದ ಬದಲಾಯಿಸಿ."},
        },
        {
            "heading": "ಎರಡು arrays ಒಟ್ಟಿಗೆ",
            "md": "ಒಂದೇ length ನ ಎರಡು arrays **item-by-item** ಸೇರುತ್ತವೆ: ಮೊದಲದು ಮೊದಲದರ ಜೊತೆ, ಎರಡನೇದು ಎರಡನೇದರ ಜೊತೆ. ಇಲ್ಲಿ ಪ್ರತಿ ಮಗುವಿನ dose ಅಂದ್ರೆ weight ಗುಣಿಸು mg per kg:\n\n" + E.C_TWO + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_TWO + "\n\n12 × 15 = 180, 20 × 15 = 300 ಮತ್ತು 35 × 10 = 350, ಒಂದೇ line ನಲ್ಲಿ. Lengths ಹೊಂದದಿದ್ದರೆ NumPy error ಕೊಡುತ್ತೆ.",
        },
        {
            "heading": "ಒಂದೇ ಪದದಲ್ಲಿ statistics",
            "md": "ಪ್ರತಿ lab report ಗೆ ಬೇಕಾದ ಸಾರಾಂಶಕ್ಕೆ arrays ಗೆ methods ಇವೆ:\n\n" + E.C_STATS + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_STATS + "\n\n- `mean()` average, `max()` ಮತ್ತು `min()` ಗರಿಷ್ಠ ಮತ್ತು ಕನಿಷ್ಠ, `sum()` ಒಟ್ಟು.\n- `std()` **standard deviation**: readings ಎಷ್ಟು ಹರಡಿವೆ. ಕಡಿಮೆ value ಅಂದ್ರೆ readings ಒಂದೇ ತರಹ.\n- `np.median(sugar)` readings sort ಮಾಡಿದಾಗ ಮಧ್ಯದ value ಕೊಡುತ್ತೆ.",
        },
        {
            "heading": "Condition ಇಂದ filter",
            "md": "Array ಮೇಲಿನ comparison `True` ಮತ್ತು `False` ನ array ಕೊಡುತ್ತೆ, ಪ್ರತಿ item ಗೆ ಒಂದು. ಅದನ್ನು square brackets ಒಳಗೆ ಹಾಕಿದರೆ `True` items ಮಾತ್ರ ಉಳಿಯುತ್ತವೆ:\n\n" + E.C_MASK + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_MASK + "\n\nಎರಡು readings 125 ಕ್ಕಿಂತ ಹೆಚ್ಚು. `True` ಅನ್ನು 1 ಅಂತ ಎಣಿಸುತ್ತಾರೆ, ಹಾಗಾಗಿ `.sum()` ಅವನ್ನು ಎಣಿಸುತ್ತೆ. Conditions ಸೇರಿಸಲು `&` (and) ಅಥವಾ `|` (or) ಬಳಸಿ, **ಪ್ರತಿ condition ಸುತ್ತ brackets** ಜೊತೆ: `sugar[(sugar > 100) & (sugar < 130)]`.",
            "callout": {"title": "ಸಿದ್ಧ arrays", "md": "np.arange(0, 25, 6) ಕೊಡುತ್ತೆ [0 6 12 18 24], range() ತರಹ. np.linspace(0, 24, 5) 0 ಇಂದ 24 ವರೆಗೆ ಸಮ ಅಂತರದ 5 numbers ಕೊಡುತ್ತೆ: Unit V ನಲ್ಲಿ time points ಗೆ ಬಳಸುತ್ತೀರಿ."},
        },
    ],
    "walkthrough": {
        "intro": "ಈ program ಒಂದು batch ನ ಆರು tablets ತೂಕ check ಮಾಡುತ್ತೆ: average, range, ಮತ್ತು 490 ಇಂದ 510 mg ಹೊರಗಿನ tablet.",
        "keyTerms": [
            {"meaning": "NumPy ಅನ್ನು np ಎಂಬ ಸಣ್ಣ ಹೆಸರಿನಲ್ಲಿ load ಮಾಡು."},
            {"meaning": "List ಅನ್ನು NumPy array ಆಗಿ ಬದಲಾಯಿಸು."},
            {"meaning": "ಎಲ್ಲಾ values ನ average."},
            {"meaning": "Condition ಗೆ ಹೊಂದುವ values ಮಾತ್ರ ಇಡು."},
        ],
    },
    "errors": {
        "intro": "NumPy ಜೊತೆ beginners ಗೆ ಮೊದಲು ಸಿಗುವ ಎರಡು errors ಇವು.",
        "examples": [
            {"title": "Import ಮಾಡದೆ np ಬಳಸುವುದು", "md": "Import ಮಾಡುವವರೆಗೆ Python ಗೆ `np` ಗೊತ್ತಿಲ್ಲ. Program ನ ಮೇಲೆ `import numpy as np` ಸೇರಿಸಿ."},
            {"title": "ಬೇರೆ length ನ arrays ಸೇರಿಸುವುದು", "md": "Item-by-item maths ಗೆ ಎರಡೂ ಕಡೆ ಸಮ items ಬೇಕು: ಇಲ್ಲಿ 3 weights ಇವೆ ಆದರೆ 2 doses ಮಾತ್ರ. Arrays ನ length ಸಮ ಮಾಡಿ."},
        ],
    },
    "mistakes": [
        {"mistake": "List ಮೇಲೆ maths: `[250, 500] * 2`", "see": "Error ಇಲ್ಲ, ಆದರೆ `[250, 500, 250, 500]` ಸಿಗುತ್ತೆ", "fix": "ಮೊದಲು array ಮಾಡಿ: `np.array([250, 500]) * 2`."},
        {"mistake": "Filter ನಲ್ಲಿ `and` / `or` ಬಳಸುವುದು: `w[w > 490 and w < 510]`", "see": "ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()", "fix": "Brackets ಜೊತೆ `&` ಮತ್ತು `|` ಬಳಸಿ: `w[(w > 490) & (w < 510)]`."},
        {"mistake": "Brackets ಬಿಡುವುದು: `w[w > 490 & w < 510]`", "see": "Error ಅಥವಾ ತಪ್ಪು ಫಲಿತಾಂಶ, ಯಾಕಂದ್ರೆ `&` ಮೊದಲು ಲೆಕ್ಕ ಆಗುತ್ತೆ", "fix": "ಪ್ರತಿ condition ಸುತ್ತ brackets ಹಾಕಿ."},
        {"mistake": "Text ಮತ್ತು numbers ಬೆರೆಸುವುದು: `np.array([250, \"500\"])`", "see": "Error ಇಲ್ಲ, ಆದರೆ ಪ್ರತಿ item text ಆಗುತ್ತೆ, maths fail ಆಗುತ್ತೆ", "fix": "Array ನಲ್ಲಿ numbers ಮಾತ್ರ ಇಡಿ; text ಅನ್ನು ಮೊದಲು int() ಅಥವಾ float() ಇಂದ ಬದಲಾಯಿಸಿ."},
    ],
    "tasks": [
        {"title": "Milligrams ಇಂದ grams", "md": "**doses_mg** ಅನ್ನು NumPy array ಮಾಡಿ, **ಒಂದೇ** calculation ಇಂದ ಪ್ರತಿ dose ಅನ್ನು **grams** ನಲ್ಲಿ print ಮಾಡಿ (1000 ಇಂದ divide). Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["arr = np.array(doses_mg) array ಮಾಡುತ್ತೆ.", "print(np.array(doses_mg) / 1000)"]},
        {"title": "ಮೂರು ಮಕ್ಕಳ doses", "md": "Dose ದೇಹದ ತೂಕದ **ಪ್ರತಿ kg ಗೆ 15 mg**. **weight** array ಅನ್ನು 15 ಇಂದ ಗುಣಿಸಿ doses print ಮಾಡಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["ಒಂದೇ ಗುಣಾಕಾರ ಇಡೀ array ಮೇಲೆ ಕೆಲಸ ಮಾಡುತ್ತೆ.", "print(weight * 15)"]},
        {"title": "Average ಮತ್ತು ಗರಿಷ್ಠ temperature", "md": "**Mean** temperature ಅನ್ನು 1 decimal ಗೆ round ಮಾಡಿ, ಮತ್ತು **ಗರಿಷ್ಠ** temperature print ಮಾಡಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["round(temps.mean(), 1) average ಅನ್ನು 1 decimal ಗೆ round ಮಾಡುತ್ತೆ.", "print(\"Max:\", temps.max())"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "ಈ program fever readings (38 ಕ್ಕಿಂತ ಹೆಚ್ಚು ಮತ್ತು 39.5 ಕ್ಕಿಂತ ಕಡಿಮೆ) ತೋರಿಸಬೇಕು, ಆದರೆ ValueError ಜೊತೆ crash ಆಗುತ್ತೆ. Filter ಸರಿ ಮಾಡಿ, output ನಿಖರವಾಗಿ ಹೀಗಿರಲಿ:",
         "hints": ["and ಇಡೀ arrays ಮೇಲೆ ಕೆಲಸ ಮಾಡಲ್ಲ. NumPy ಅದರ ಬದಲು & ಬಳಸುತ್ತೆ.", "fever = temps[(temps > 38) & (temps < 39.5)]"],
         "solutionNote": "and ಗೆ ಒಂದು True ಅಥವಾ False ಬೇಕು, ಆದರೆ temps > 38 ಅವುಗಳ ಇಡೀ array. & ಎರಡೂ arrays ಅನ್ನು item-by-item ಸೇರಿಸುತ್ತೆ, ಪ್ರತಿ condition ಗೆ ತನ್ನದೇ brackets ಬೇಕು."},
    ],
    "quiz": [
        {"q": "import numpy as np\na = np.array([1, 2, 3])\nprint(a * 2)\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "Array ಮೇಲಿನ maths ಪ್ರತಿ item ಮೇಲೆ ಆಗುತ್ತೆ."},
        {"q": "print([1, 2, 3] * 2)\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "List ಮೇಲೆ * list ಅನ್ನು ಪುನರಾವರ್ತಿಸುತ್ತೆ."},
        {"q": "import numpy as np ಏನು ಮಾಡುತ್ತೆ?", "why": "ಇದು library ಅನ್ನು np ಎಂಬ ಸಣ್ಣ ಹೆಸರಿನಲ್ಲಿ load ಮಾಡುತ್ತೆ."},
        {"q": "a = np.array([10, 20, 30])\nprint(a.mean())\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "Mean = (10 + 20 + 30) / 3 = 20.0."},
        {"q": "a = np.array([10, 20, 30]) ಗೆ a[a > 15] ಏನು ಕೊಡುತ್ತೆ?", "why": "Mask condition True ಇರುವ items ಮಾತ್ರ ಉಳಿಸುತ್ತೆ."},
        {"q": "NumPy filter ನಲ್ಲಿ ಎರಡು conditions ಹೇಗೆ ಸೇರಿಸುತ್ತೀರಿ?", "why": "& ಅಥವಾ | ಬಳಸಿ, ಪ್ರತಿ condition ಅನ್ನು brackets ನಲ್ಲಿ ಇಡಿ."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 3.4 · NumPy arrays",
        "children": [
            {"label": "ಮಾಡುವುದು", "children": [{"label": "import numpy as np"}, {"label": "np.array(list)"}, {"label": ".shape"}]},
            {"label": "Vector maths", "children": [{"label": "arr / 1000"}, {"label": "arr1 * arr2"}, {"label": "Loop ಬೇಡ"}]},
            {"label": "Statistics", "children": [{"label": "mean()"}, {"label": "max() min() sum()"}, {"label": "std() ಹರಡಿಕೆ"}]},
            {"label": "Filter", "children": [{"label": "arr > 125 → True/False"}, {"label": "arr[arr > 125]"}, {"label": "& | brackets ಜೊತೆ"}]},
            {"label": "list ಇಂದ ವ್ಯತ್ಯಾಸ", "children": [{"label": "list * 2 ಪುನರಾವರ್ತನೆ"}, {"label": "array * 2 ಎರಡರಷ್ಟು"}, {"label": "Array ನಲ್ಲಿ ಒಂದೇ type"}]},
            {"label": "Errors", "children": [{"label": "NameError: np"}, {"label": "ValueError: shapes"}]},
        ],
    },
    "summary": [
        "**NumPy** `import numpy as np` ಇಂದ load ಆಗುತ್ತೆ; `np.array(list)` ಒಂದೇ type ನ **array** ಮಾಡುತ್ತೆ.",
        "Array ಮೇಲಿನ maths **vectorised**: `doses / 1000` ಪ್ರತಿ item ಬದಲಾಯಿಸುತ್ತೆ, loop ಇಲ್ಲದೆ. List ಮೇಲೆ `* 2` ಪುನರಾವರ್ತಿಸುತ್ತೆ.",
        "ಸಮ length ನ ಎರಡು arrays **item-by-item** ಸೇರುತ್ತವೆ: `weight * mg_per_kg`.",
        "`mean()`, `max()`, `min()`, `sum()` ಮತ್ತು `std()` ಒಂದೇ ಪದದಲ್ಲಿ readings ನ ಸಾರಾಂಶ ಕೊಡುತ್ತವೆ.",
        "Condition array ಅನ್ನು filter ಮಾಡುತ್ತೆ: `sugar[sugar > 125]`; conditions ಅನ್ನು `&` ಮತ್ತು `|` ಇಂದ ಸೇರಿಸಿ, ಪ್ರತಿಯೊಂದೂ brackets ನಲ್ಲಿ.",
    ],
}

NARR = {
    "hi": [
        "यह program एक batch की छह tablets की quality जल्दी check करता है।",
        "import numpy as n p, NumPy को छोटे नाम n p से load करता है।",
        "Comment बताता है कि ये tablets के वज़न milligrams में हैं।",
        "n p dot array छह वज़नों की list को NumPy array w में बदलता है।",
        "w dot mean छहों वज़न जोड़कर छह से divide करता है। Average ठीक पाँच सौ है।",
        "min और max सबसे हल्की और सबसे भारी tablet देते हैं: चार सौ अट्ठासी और पाँच सौ दस।",
        "यह mask चार सौ नब्बे से कम, या पाँच सौ दस से ज़्यादा वाली tablets रखता है। हर condition brackets में है, bar के निशान से जुड़ी, जिसका मतलब है or।",
        "सिर्फ़ एक tablet, चार सौ अट्ठासी milligrams, limit से बाहर है।",
    ],
    "hinglish": [
        "Yeh program ek batch ki chhah tablets ki quality jaldi check karta hai.",
        "import numpy as n p, NumPy ko chhote naam n p se load karta hai.",
        "Comment batata hai ki yeh tablets ke wazan milligrams mein hain.",
        "n p dot array chhah wazanon ki list ko NumPy array w mein badalta hai.",
        "w dot mean chhahon wazan jodkar chhah se divide karta hai. Average theek paanch sau hai.",
        "min aur max sabse halki aur sabse bhaari tablet dete hain: chaar sau atthaasi aur paanch sau das.",
        "Yeh mask chaar sau nabbe se kam, ya paanch sau das se zyada wali tablets rakhta hai. Har condition brackets mein hai, bar ke nishaan se judi, jiska matlab hai or.",
        "Sirf ek tablet, chaar sau atthaasi milligrams, limit se bahar hai.",
    ],
    "kn": [
        "ಈ program ಒಂದು batch ನ ಆರು tablets ನ quality ಬೇಗ check ಮಾಡುತ್ತೆ.",
        "import numpy as n p, NumPy ಅನ್ನು n p ಎಂಬ ಸಣ್ಣ ಹೆಸರಿನಲ್ಲಿ load ಮಾಡುತ್ತೆ.",
        "Comment ಇವು tablets ನ ತೂಕ, milligrams ನಲ್ಲಿ ಅಂತ ಹೇಳುತ್ತೆ.",
        "n p dot array ಆರು ತೂಕಗಳ list ಅನ್ನು NumPy array w ಆಗಿ ಬದಲಾಯಿಸುತ್ತೆ.",
        "w dot mean ಆರೂ ತೂಕಗಳನ್ನು ಕೂಡಿಸಿ ಆರರಿಂದ divide ಮಾಡುತ್ತೆ. Average ಸರಿಯಾಗಿ ಐನೂರು.",
        "min ಮತ್ತು max ಅತಿ ಹಗುರ ಮತ್ತು ಅತಿ ಭಾರದ tablets ಕೊಡುತ್ತವೆ: ನಾನೂರ ಎಂಬತ್ತೆಂಟು ಮತ್ತು ಐನೂರ ಹತ್ತು.",
        "ಈ mask ನಾನೂರ ತೊಂಬತ್ತಕ್ಕಿಂತ ಕಡಿಮೆ, ಅಥವಾ ಐನೂರ ಹತ್ತಕ್ಕಿಂತ ಹೆಚ್ಚು ಇರುವ tablets ಉಳಿಸುತ್ತೆ. ಪ್ರತಿ condition brackets ನಲ್ಲಿ, bar ಚಿಹ್ನೆಯಿಂದ ಸೇರಿದೆ, ಅಂದ್ರೆ or.",
        "ಒಂದೇ tablet, ನಾನೂರ ಎಂಬತ್ತೆಂಟು milligrams, limit ಹೊರಗೆ ಇದೆ.",
    ],
}

ANIM = {
    "hi": [
        "Array में तीन doses हैं, milligrams में, एक के बगल में एक।",
        "Array को हज़ार से divide करने पर हर item एक ही समय पर divide होता है। कोई loop नहीं।",
        "print नया array दिखाता है, grams में।",
        "सादी list के साथ यही करने के लिए for loop चाहिए होता। पाँच सौ patients के साथ array कहीं तेज़ है।",
    ],
    "hinglish": [
        "Array mein teen doses hain, milligrams mein, ek ke bagal mein ek.",
        "Array ko hazaar se divide karne par har item ek hi samay par divide hota hai. Koi loop nahi.",
        "print naya array dikhaata hai, grams mein.",
        "Saadi list ke saath yahi karne ke liye for loop chahiye hota. Paanch sau patients ke saath array kahin tez hai.",
    ],
    "kn": [
        "Array ನಲ್ಲಿ ಮೂರು doses, milligrams ನಲ್ಲಿ, ಒಂದರ ಪಕ್ಕ ಒಂದು.",
        "Array ಅನ್ನು ಸಾವಿರದಿಂದ divide ಮಾಡಿದರೆ ಪ್ರತಿ item ಒಂದೇ ಸಮಯದಲ್ಲಿ divide ಆಗುತ್ತೆ. Loop ಇಲ್ಲ.",
        "print ಹೊಸ array ತೋರಿಸುತ್ತೆ, grams ನಲ್ಲಿ.",
        "ಸಾಧಾರಣ list ಜೊತೆ ಇದೇ ಮಾಡಲು for loop ಬೇಕಾಗುತ್ತಿತ್ತು. ಐನೂರು patients ಇದ್ದಾಗ array ತುಂಬಾ ವೇಗ.",
    ],
}

if __name__ == "__main__":
    build("3-4", "anim-vector", T, NARR, ANIM, say_en=lambda t: t.replace("n p", "N P"))

"""Lesson 3.3 translations (Hindi, Hinglish, Kannada) and voice scripts."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import build  # noqa: E402

_spec = importlib.util.spec_from_file_location("en33", os.path.join(os.path.dirname(__file__), "..", "lessons", "bp101t_3-3_en.py"))
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)

T = {}

T["hi"] = {
    "hook": {
        "title": "Pharmacy counter कभी नहीं रुकता",
        "md": "भीड़ वाले pharmacy counter पर patients की queue दिन भर बढ़ती-घटती रहती है। Items cart में जाते हैं और निकलते हैं। Closing time पर कोई पूछता है: आज सबसे ज़्यादा क्या बिका, और क्या reorder करना है?\n\nData भी ऐसा ही है: वह **बदलता** है। आज आप इसके रोज़ के tools सीखेंगे: items जोड़ना और हटाना, sort करना, सबसे छोटा, सबसे बड़ा और average निकालना, और dictionary से गिनती करना। Code की ये कुछ lines pharmacy software दिन में हज़ारों बार चलाता है।",
    },
    "learn": [
        "**append()**, **insert()** और **extend()** से items **जोड़ना**",
        "**remove()** और **pop()** से items **हटाना**",
        "**Sort** करना, और **min()**, **max()**, **sum()** व **count()** से numbers का सार निकालना",
        "Dictionary पर **keys()**, **values()**, **update()** और **pop()**, और dictionary से **गिनती**",
    ],
    "explanation": [
        {
            "heading": "List में items जोड़ना",
            "md": "List के अपने functions होते हैं, जिन्हें **methods** कहते हैं, और ये dot के बाद लिखे जाते हैं। `append()` एक item **आखिर में** जोड़ता है; `insert()` उसे **किसी index पर** जोड़ता है:\n\n" + E.C_ADD + "\n\nयह print करता है:\n\n" + E.O_ADD + "\n\nSita सबसे आगे गई, index 0 पर। दूसरी list से **कई** items एक साथ जोड़ने हों तो `extend()` use कीजिए: `queue.extend([\"Raju\", \"Asha\"])`।",
            "callout": {"title": "Method", "md": "किसी value का अपना function, जो dot के बाद लिखा जाता है: queue.append(\"Anil\")। Lists, strings और dictionaries, सबके अपने methods हैं।"},
        },
        {
            "heading": "Items हटाना",
            "md": "`remove()` **उस value वाला** पहला item हटाता है। `pop()` **आखिरी** item हटाकर आपको वापस देता है; `pop(0)` पहला हटाएगा:\n\n" + E.C_REMOVE + "\n\nयह print करता है:\n\n" + E.O_REMOVE + "\n\n`del cart[0]` भी index से item हटाता है, पर उसे वापस नहीं देता।",
        },
        {
            "heading": "Numbers को sort करना और सार निकालना",
            "md": "Readings के बारे में जो सवाल आप रोज़ पूछते हैं, उनके लिए Python में built-in functions हैं:\n\n" + E.C_SORT + "\n\nयह print करता है:\n\n" + E.O_SORT + "\n\n- `sorted(list)` एक **नई** sorted list देता है और original को वैसा ही छोड़ता है।\n- `list.sort()` list को **खुद** sort करता है और कुछ return नहीं करता। सबसे बड़ा पहले चाहिए तो दोनों में `reverse=True` जोड़िए।\n- `min()`, `max()` और `sum()` numbers की किसी भी list पर चलते हैं; `sum() / len()` average है।\n- `count(x)` बताता है `x` कितनी बार आया; `index(x)` उसकी पहली position देता है।",
            "callout": {"title": "sort() None लौटाता है", "md": "result = sugar.sort() करने पर result None रहता है। sugar.sort() अलग line पर लिखिए, या result = sorted(sugar)।"},
        },
        {
            "heading": "Dictionaries पर operations",
            "md": "`keys()`, `values()` और `items()` keys, values और pairs देते हैं। `pop(key)` एक pair हटाता है, और `update()` कई pairs एक साथ जोड़ता या बदलता है:\n\n" + E.C_DICTOPS + "\n\nयह print करता है:\n\n" + E.O_DICTOPS + "\n\nORS का shelf खाली था, इसलिए उसे stock list से pop किया गया; Ibuprofen `update()` से जुड़ी। `sum(stock.values())` सारी strips जोड़ता है: 120 + 45 + 0 = 165।",
        },
        {
            "heading": "Dictionary से गिनती",
            "md": "चीज़ें **गिनने** का स्वाभाविक तरीका dictionary है: key वह है जो गिन रहे हैं, value कितनी बार। Drug पहली बार आए तो `get(drug, 0)` 0 देता है:\n\n" + E.C_COUNT + "\n\nयह print करता है:\n\n" + E.O_COUNT + "\n\nयह छोटा pattern ऐसे सवालों का जवाब देता है: \"आज सबसे ज़्यादा कौन-सी drug बिकी?\" या \"हर गाँव से कितने patients आए?\"",
            "callout": {"title": "गिनती का pattern", "md": "Loop से पहले counts = {}, फिर उसके अंदर counts[item] = counts.get(item, 0) + 1। इसे याद रखिए; Unit IV में भी काम आएगा।"},
        },
    ],
    "walkthrough": {
        "intro": "यह program stock check करता है और 50 strips से कम वाली हर drug की sorted reorder list बनाता है।",
        "keyTerms": [
            {"meaning": "नतीजे जमा करने के लिए खाली list से शुरू करो।"},
            {"meaning": "हर drug और उसकी quantity, एक-एक pair करके।"},
            {"meaning": "Drug को list के आखिर में जोड़ो।"},
            {"meaning": "List को खुद, alphabetical क्रम में sort करो।"},
        ],
    },
    "errors": {
        "intro": "List methods के साथ ये दो errors सबसे आम हैं।",
        "examples": [
            {"title": "ऐसी value हटाना जो list में नहीं है", "md": "`remove()` तभी चलता है जब value मौजूद हो। पहले check कीजिए: `if \"Aspirin\" in cart: cart.remove(\"Aspirin\")`।"},
            {"title": "sort() के नतीजे को use करना", "md": "`sort()` list को उसी में sort करता है और `None` लौटाता है, इसलिए `lowest` None है। नई list के लिए `sorted(sugar)` use कीजिए, या सीधे `min(sugar)`।"},
        ],
    },
    "mistakes": [
        {"mistake": "`result = data.sort()` लिखकर `result` use करना", "see": "result None है", "fix": "`data.sort()` अलग से call कीजिए, या `result = sorted(data)`।"},
        {"mistake": "append को दो items देना: `cart.append(\"ORS\", \"Zinc\")`", "see": "TypeError: list.append() takes exactly one argument (2 given)", "fix": "एक-एक करके append कीजिए, या `cart.extend([\"ORS\", \"Zinc\"])`।"},
        {"mistake": "दो lists जोड़ने के लिए append: `a.append(b)`", "see": "कोई error नहीं, पर list के अंदर list बनती है: `[1, 2, [3, 4]]`", "fix": "Items एक-एक जोड़ने के लिए `a.extend(b)` use कीजिए।"},
        {"mistake": "खाली list पर `pop()` call करना", "see": "IndexError: pop from empty list", "fix": "पहले check कीजिए: `if queue: queue.pop()`।"},
    ],
    "tasks": [
        {"title": "Queue संभालिए", "md": "Anil अभी आए हैं: उन्हें queue के **आखिर में** जोड़िए। Sita emergency है: उन्हें **सबसे आगे** रखिए। फिर queue print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["append() आखिर में जोड़ता है; insert(0, ...) सबसे आगे।", "queue.append(\"Anil\")\nqueue.insert(0, \"Sita\")"]},
        {"title": "सबसे हल्का, सबसे भारी, average", "md": "ये पाँच patients के वज़न (kg) हैं। **min()**, **max()** और **sum()** से सबसे हल्का, सबसे भारी और average वज़न print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["print(\"Lightest:\", min(weights))", "Average है sum(weights) / len(weights)।"]},
        {"title": "Stock में कुल strips", "md": "Dictionary की **values** जोड़कर shelf पर कुल strips print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["stock.values() सिर्फ़ quantities देता है।", "print(\"Total strips:\", sum(stock.values()))"]},
        {"title": "Bug ढूँढिए", "md": "इस program को गिनना है कि हर drug कितनी बार बिकी, पर यह पहली drug पर ही KeyError के साथ crash हो जाता है। गिनती वाली line ठीक कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["पहली बार drug आने पर counts में उसकी key अभी नहीं है।", "counts[drug] = counts.get(drug, 0) + 1"],
         "solutionNote": "counts[drug] पहली बार fail होता है क्योंकि key अभी है ही नहीं। counts.get(drug, 0) हर नई drug को 0 से शुरू करता है।"},
    ],
    "quiz": [
        {"q": "x = [1, 2]\nx.append(3)\nprint(x)\n\nयह क्या print करता है?", "why": "append item को आखिर में जोड़ता है।"},
        {"q": "कौन-सा method list का आखिरी item हटाकर वापस देता है?", "why": "बिना index के pop() आखिरी item हटाकर लौटाता है।"},
        {"q": "a = [3, 1, 2]\nb = a.sort()\nprint(b)\n\nयह क्या print करता है?", "why": "sort() खुद a को बदलता है और None लौटाता है।"},
        {"q": "d = {\"a\": 1, \"b\": 2}\nprint(sum(d.values()))\n\nयह क्या print करता है?", "why": "values() 1 और 2 देता है, और sum उन्हें जोड़ता है।"},
        {"q": "कौन-सा method दूसरी list का हर item list के आखिर में जोड़ता है?", "why": "extend() items एक-एक करके जोड़ता है; append() पूरी list को एक item बना देगा।"},
        {"q": "counts[d] = counts.get(d, 0) + 1 में get(d, 0) क्या करता है?", "why": "get मौजूदा गिनती देता है, या पहली बार default 0।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 3.3 · Operations",
        "children": [
            {"label": "जोड़ना", "children": [{"label": "append(x)"}, {"label": "insert(i, x)"}, {"label": "extend(list)"}]},
            {"label": "हटाना", "children": [{"label": "remove(x)"}, {"label": "pop() वापस देता है"}, {"label": "del list[i]"}]},
            {"label": "क्रम और सार", "children": [{"label": "sort() उसी में"}, {"label": "sorted() नई list"}, {"label": "min max sum count"}]},
            {"label": "Dictionary", "children": [{"label": "keys() values()"}, {"label": "items()"}, {"label": "update() pop()"}]},
            {"label": "गिनती", "children": [{"label": "counts = {}"}, {"label": "get(k, 0) + 1"}, {"label": "कुछ भी गिनो"}]},
            {"label": "Errors", "children": [{"label": "ValueError: not in list"}, {"label": "sort() से None"}]},
        ],
    },
    "summary": [
        "Methods dot के बाद लिखे जाते हैं। **append()** आखिर में जोड़ता है, **insert(i, x)** किसी index पर, **extend()** कई items।",
        "**remove(x)** एक value हटाता है; **pop()** आखिरी item हटाकर लौटाता है।",
        "**sorted()** नई sorted list देता है; **sort()** उसी में sort करके None लौटाता है। **min()**, **max()**, **sum()** और **count()** सार निकालते हैं।",
        "Dictionaries के पास **keys()**, **values()**, **items()**, **update()** और **pop()** हैं।",
        "चीज़ें गिनने के लिए: loop के अंदर `counts[item] = counts.get(item, 0) + 1`।",
    ],
}

T["hinglish"] = {
    "hook": {
        "title": "Pharmacy counter kabhi nahi rukta",
        "md": "Bheed wale pharmacy counter par patients ki queue din bhar badhti-ghatti rehti hai. Items cart mein jaate hain aur nikalte hain. Closing time par koi poochhta hai: aaj sabse zyada kya bika, aur kya reorder karna hai?\n\nData bhi aisa hi hai: woh **badalta** hai. Aaj aap iske roz ke tools seekhenge: items jodna aur hataana, sort karna, sabse chhota, sabse bada aur average nikaalna, aur dictionary se ginti karna. Code ki yeh kuch lines pharmacy software din mein hazaaron baar chalaata hai.",
    },
    "learn": [
        "**append()**, **insert()** aur **extend()** se items **jodna**",
        "**remove()** aur **pop()** se items **hataana**",
        "**Sort** karna, aur **min()**, **max()**, **sum()** va **count()** se numbers ka saar nikaalna",
        "Dictionary par **keys()**, **values()**, **update()** aur **pop()**, aur dictionary se **ginti**",
    ],
    "explanation": [
        {
            "heading": "List mein items jodna",
            "md": "List ke apne functions hote hain, jinhe **methods** kehte hain, aur yeh dot ke baad likhe jaate hain. `append()` ek item **aakhir mein** jodta hai; `insert()` use **kisi index par** jodta hai:\n\n" + E.C_ADD + "\n\nYeh print karta hai:\n\n" + E.O_ADD + "\n\nSita sabse aage gayi, index 0 par. Doosri list se **kai** items ek saath jodne hon to `extend()` use kijiye: `queue.extend([\"Raju\", \"Asha\"])`.",
            "callout": {"title": "Method", "md": "Kisi value ka apna function, jo dot ke baad likha jaata hai: queue.append(\"Anil\"). Lists, strings aur dictionaries, sabke apne methods hain."},
        },
        {
            "heading": "Items hataana",
            "md": "`remove()` **us value wala** pehla item hataata hai. `pop()` **aakhri** item hatakar aapko wapas deta hai; `pop(0)` pehla hataayega:\n\n" + E.C_REMOVE + "\n\nYeh print karta hai:\n\n" + E.O_REMOVE + "\n\n`del cart[0]` bhi index se item hataata hai, par use wapas nahi deta.",
        },
        {
            "heading": "Numbers ko sort karna aur saar nikaalna",
            "md": "Readings ke baare mein jo sawaal aap roz poochhte hain, unke liye Python mein built-in functions hain:\n\n" + E.C_SORT + "\n\nYeh print karta hai:\n\n" + E.O_SORT + "\n\n- `sorted(list)` ek **nayi** sorted list deta hai aur original ko waisa hi chhodta hai.\n- `list.sort()` list ko **khud** sort karta hai aur kuch return nahi karta. Sabse bada pehle chahiye to dono mein `reverse=True` jodiye.\n- `min()`, `max()` aur `sum()` numbers ki kisi bhi list par chalte hain; `sum() / len()` average hai.\n- `count(x)` batata hai `x` kitni baar aaya; `index(x)` uski pehli position deta hai.",
            "callout": {"title": "sort() None lautaata hai", "md": "result = sugar.sort() karne par result None rehta hai. sugar.sort() alag line par likhiye, ya result = sorted(sugar)."},
        },
        {
            "heading": "Dictionaries par operations",
            "md": "`keys()`, `values()` aur `items()` keys, values aur pairs dete hain. `pop(key)` ek pair hataata hai, aur `update()` kai pairs ek saath jodta ya badalta hai:\n\n" + E.C_DICTOPS + "\n\nYeh print karta hai:\n\n" + E.O_DICTOPS + "\n\nORS ka shelf khaali tha, isliye use stock list se pop kiya gaya; Ibuprofen `update()` se judi. `sum(stock.values())` saari strips jodta hai: 120 + 45 + 0 = 165.",
        },
        {
            "heading": "Dictionary se ginti",
            "md": "Cheezein **ginne** ka swaabhaavik tareeka dictionary hai: key woh hai jo gin rahe hain, value kitni baar. Drug pehli baar aaye to `get(drug, 0)` 0 deta hai:\n\n" + E.C_COUNT + "\n\nYeh print karta hai:\n\n" + E.O_COUNT + "\n\nYeh chhota pattern aise sawaalon ka jawaab deta hai: \"aaj sabse zyada kaun-si drug biki?\" ya \"har gaon se kitne patients aaye?\"",
            "callout": {"title": "Ginti ka pattern", "md": "Loop se pehle counts = {}, phir uske andar counts[item] = counts.get(item, 0) + 1. Ise yaad rakhiye; Unit IV mein bhi kaam aayega."},
        },
    ],
    "walkthrough": {
        "intro": "Yeh program stock check karta hai aur 50 strips se kam wali har drug ki sorted reorder list banata hai.",
        "keyTerms": [
            {"meaning": "Nateeje jama karne ke liye khaali list se shuru karo."},
            {"meaning": "Har drug aur uski quantity, ek-ek pair karke."},
            {"meaning": "Drug ko list ke aakhir mein jodo."},
            {"meaning": "List ko khud, alphabetical kram mein sort karo."},
        ],
    },
    "errors": {
        "intro": "List methods ke saath yeh do errors sabse aam hain.",
        "examples": [
            {"title": "Aisi value hataana jo list mein nahi hai", "md": "`remove()` tabhi chalta hai jab value maujood ho. Pehle check kijiye: `if \"Aspirin\" in cart: cart.remove(\"Aspirin\")`."},
            {"title": "sort() ke nateeje ko use karna", "md": "`sort()` list ko usi mein sort karta hai aur `None` lautaata hai, isliye `lowest` None hai. Nayi list ke liye `sorted(sugar)` use kijiye, ya seedhe `min(sugar)`."},
        ],
    },
    "mistakes": [
        {"mistake": "`result = data.sort()` likhkar `result` use karna", "see": "result None hai", "fix": "`data.sort()` alag se call kijiye, ya `result = sorted(data)`."},
        {"mistake": "append ko do items dena: `cart.append(\"ORS\", \"Zinc\")`", "see": "TypeError: list.append() takes exactly one argument (2 given)", "fix": "Ek-ek karke append kijiye, ya `cart.extend([\"ORS\", \"Zinc\"])`."},
        {"mistake": "Do lists jodne ke liye append: `a.append(b)`", "see": "Koi error nahi, par list ke andar list banti hai: `[1, 2, [3, 4]]`", "fix": "Items ek-ek jodne ke liye `a.extend(b)` use kijiye."},
        {"mistake": "Khaali list par `pop()` call karna", "see": "IndexError: pop from empty list", "fix": "Pehle check kijiye: `if queue: queue.pop()`."},
    ],
    "tasks": [
        {"title": "Queue sambhaaliye", "md": "Anil abhi aaye hain: unhe queue ke **aakhir mein** jodiye. Sita emergency hai: unhe **sabse aage** rakhiye. Phir queue print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["append() aakhir mein jodta hai; insert(0, ...) sabse aage.", "queue.append(\"Anil\")\nqueue.insert(0, \"Sita\")"]},
        {"title": "Sabse halka, sabse bhaari, average", "md": "Yeh paanch patients ke wazan (kg) hain. **min()**, **max()** aur **sum()** se sabse halka, sabse bhaari aur average wazan print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["print(\"Lightest:\", min(weights))", "Average hai sum(weights) / len(weights)."]},
        {"title": "Stock mein kul strips", "md": "Dictionary ki **values** jodkar shelf par kul strips print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["stock.values() sirf quantities deta hai.", "print(\"Total strips:\", sum(stock.values()))"]},
        {"title": "Bug dhoondhiye", "md": "Is program ko ginna hai ki har drug kitni baar biki, par yeh pehli drug par hi KeyError ke saath crash ho jaata hai. Ginti wali line theek kijiye taaki output bilkul yeh ho:",
         "hints": ["Pehli baar drug aane par counts mein uski key abhi nahi hai.", "counts[drug] = counts.get(drug, 0) + 1"],
         "solutionNote": "counts[drug] pehli baar fail hota hai kyunki key abhi hai hi nahi. counts.get(drug, 0) har nayi drug ko 0 se shuru karta hai."},
    ],
    "quiz": [
        {"q": "x = [1, 2]\nx.append(3)\nprint(x)\n\nYeh kya print karta hai?", "why": "append item ko aakhir mein jodta hai."},
        {"q": "Kaun-sa method list ka aakhri item hatakar wapas deta hai?", "why": "Bina index ke pop() aakhri item hatakar lautaata hai."},
        {"q": "a = [3, 1, 2]\nb = a.sort()\nprint(b)\n\nYeh kya print karta hai?", "why": "sort() khud a ko badalta hai aur None lautaata hai."},
        {"q": "d = {\"a\": 1, \"b\": 2}\nprint(sum(d.values()))\n\nYeh kya print karta hai?", "why": "values() 1 aur 2 deta hai, aur sum unhe jodta hai."},
        {"q": "Kaun-sa method doosri list ka har item list ke aakhir mein jodta hai?", "why": "extend() items ek-ek karke jodta hai; append() poori list ko ek item bana dega."},
        {"q": "counts[d] = counts.get(d, 0) + 1 mein get(d, 0) kya karta hai?", "why": "get maujooda ginti deta hai, ya pehli baar default 0."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 3.3 · Operations",
        "children": [
            {"label": "Jodna", "children": [{"label": "append(x)"}, {"label": "insert(i, x)"}, {"label": "extend(list)"}]},
            {"label": "Hataana", "children": [{"label": "remove(x)"}, {"label": "pop() wapas deta hai"}, {"label": "del list[i]"}]},
            {"label": "Kram aur saar", "children": [{"label": "sort() usi mein"}, {"label": "sorted() nayi list"}, {"label": "min max sum count"}]},
            {"label": "Dictionary", "children": [{"label": "keys() values()"}, {"label": "items()"}, {"label": "update() pop()"}]},
            {"label": "Ginti", "children": [{"label": "counts = {}"}, {"label": "get(k, 0) + 1"}, {"label": "Kuch bhi gino"}]},
            {"label": "Errors", "children": [{"label": "ValueError: not in list"}, {"label": "sort() se None"}]},
        ],
    },
    "summary": [
        "Methods dot ke baad likhe jaate hain. **append()** aakhir mein jodta hai, **insert(i, x)** kisi index par, **extend()** kai items.",
        "**remove(x)** ek value hataata hai; **pop()** aakhri item hatakar lautaata hai.",
        "**sorted()** nayi sorted list deta hai; **sort()** usi mein sort karke None lautaata hai. **min()**, **max()**, **sum()** aur **count()** saar nikaalte hain.",
        "Dictionaries ke paas **keys()**, **values()**, **items()**, **update()** aur **pop()** hain.",
        "Cheezein ginne ke liye: loop ke andar `counts[item] = counts.get(item, 0) + 1`.",
    ],
}

T["kn"] = {
    "hook": {
        "title": "Pharmacy counter ಯಾವತ್ತೂ ನಿಲ್ಲಲ್ಲ",
        "md": "ಜನಸಂದಣಿ ಇರುವ pharmacy counter ನಲ್ಲಿ patients queue ದಿನವಿಡೀ ಹೆಚ್ಚು ಕಡಿಮೆ ಆಗುತ್ತಾ ಇರುತ್ತೆ. Items cart ಒಳಗೆ ಹೋಗುತ್ತವೆ, ಹೊರಗೆ ಬರುತ್ತವೆ. Closing time ಗೆ ಯಾರೋ ಕೇಳ್ತಾರೆ: ಇವತ್ತು ಹೆಚ್ಚು ಮಾರಾಟ ಆಗಿದ್ದು ಯಾವುದು, ಏನನ್ನು reorder ಮಾಡಬೇಕು?\n\nData ಕೂಡ ಹಾಗೇ: ಅದು **ಬದಲಾಗುತ್ತೆ**. ಇವತ್ತು ಅದಕ್ಕೆ ದಿನನಿತ್ಯದ tools ಕಲಿಯುತ್ತೀರಿ: items ಸೇರಿಸುವುದು, ತೆಗೆಯುವುದು, sort ಮಾಡುವುದು, ಕನಿಷ್ಠ, ಗರಿಷ್ಠ ಮತ್ತು average ಕಂಡುಹಿಡಿಯುವುದು, dictionary ಇಂದ ಎಣಿಸುವುದು. ಈ ಕೆಲವು lines code ಅನ್ನು pharmacy software ದಿನಕ್ಕೆ ಸಾವಿರಾರು ಸಲ ಓಡಿಸುತ್ತೆ.",
    },
    "learn": [
        "**append()**, **insert()** ಮತ್ತು **extend()** ಇಂದ items **ಸೇರಿಸುವುದು**",
        "**remove()** ಮತ್ತು **pop()** ಇಂದ items **ತೆಗೆಯುವುದು**",
        "**Sort** ಮಾಡುವುದು, **min()**, **max()**, **sum()** ಮತ್ತು **count()** ಇಂದ numbers ಸಾರಾಂಶ",
        "Dictionary ಮೇಲೆ **keys()**, **values()**, **update()** ಮತ್ತು **pop()**, ಮತ್ತು dictionary ಇಂದ **ಎಣಿಕೆ**",
    ],
    "explanation": [
        {
            "heading": "List ಗೆ items ಸೇರಿಸುವುದು",
            "md": "List ಗೆ ತನ್ನದೇ functions ಇವೆ, ಅವನ್ನು **methods** ಅಂತಾರೆ, dot ನಂತರ ಬರೆಯುತ್ತಾರೆ. `append()` ಒಂದು item ಅನ್ನು **ಕೊನೆಗೆ** ಸೇರಿಸುತ್ತೆ; `insert()` ಅದನ್ನು **ಒಂದು index ನಲ್ಲಿ** ಸೇರಿಸುತ್ತೆ:\n\n" + E.C_ADD + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_ADD + "\n\nSita ಮುಂದೆ ಹೋದಳು, index 0 ಗೆ. ಇನ್ನೊಂದು list ಇಂದ **ಹಲವು** items ಒಟ್ಟಿಗೆ ಸೇರಿಸಲು `extend()` ಬಳಸಿ: `queue.extend([\"Raju\", \"Asha\"])`.",
            "callout": {"title": "Method", "md": "ಒಂದು value ಗೆ ಸೇರಿದ function, dot ನಂತರ ಬರೆಯುತ್ತಾರೆ: queue.append(\"Anil\"). Lists, strings ಮತ್ತು dictionaries ಎಲ್ಲಕ್ಕೂ ತಮ್ಮದೇ methods ಇವೆ."},
        },
        {
            "heading": "Items ತೆಗೆಯುವುದು",
            "md": "`remove()` **ಆ value ಇರುವ** ಮೊದಲ item ತೆಗೆಯುತ್ತೆ. `pop()` **ಕೊನೆಯ** item ತೆಗೆದು ನಿಮಗೆ ಹಿಂದೆ ಕೊಡುತ್ತೆ; `pop(0)` ಮೊದಲದನ್ನು ತೆಗೆಯುತ್ತೆ:\n\n" + E.C_REMOVE + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_REMOVE + "\n\n`del cart[0]` ಕೂಡ index ಇಂದ item ತೆಗೆಯುತ್ತೆ, ಆದರೆ ಹಿಂದೆ ಕೊಡಲ್ಲ.",
        },
        {
            "heading": "Numbers sort ಮತ್ತು ಸಾರಾಂಶ",
            "md": "Readings ಬಗ್ಗೆ ನೀವು ಪ್ರತಿದಿನ ಕೇಳುವ ಪ್ರಶ್ನೆಗಳಿಗೆ Python ನಲ್ಲಿ built-in functions ಇವೆ:\n\n" + E.C_SORT + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_SORT + "\n\n- `sorted(list)` **ಹೊಸ** sorted list ಕೊಡುತ್ತೆ, original ಅನ್ನು ಹಾಗೇ ಬಿಡುತ್ತೆ.\n- `list.sort()` list ಅನ್ನು **ಅದರಲ್ಲೇ** sort ಮಾಡುತ್ತೆ, ಏನೂ return ಮಾಡಲ್ಲ. ದೊಡ್ಡದು ಮೊದಲು ಬೇಕಾದರೆ ಎರಡಕ್ಕೂ `reverse=True` ಸೇರಿಸಿ.\n- `min()`, `max()` ಮತ್ತು `sum()` ಯಾವುದೇ numbers list ಮೇಲೆ ಕೆಲಸ ಮಾಡುತ್ತವೆ; `sum() / len()` average.\n- `count(x)` `x` ಎಷ್ಟು ಸಲ ಬಂತು ಅಂತ ಹೇಳುತ್ತೆ; `index(x)` ಅದರ ಮೊದಲ position ಕೊಡುತ್ತೆ.",
            "callout": {"title": "sort() None ಕೊಡುತ್ತೆ", "md": "result = sugar.sort() ಮಾಡಿದರೆ result None. sugar.sort() ಅನ್ನು ಬೇರೆ line ನಲ್ಲಿ ಬರೆಯಿರಿ, ಅಥವಾ result = sorted(sugar)."},
        },
        {
            "heading": "Dictionaries ಮೇಲಿನ operations",
            "md": "`keys()`, `values()` ಮತ್ತು `items()` keys, values ಮತ್ತು pairs ಕೊಡುತ್ತವೆ. `pop(key)` ಒಂದು pair ತೆಗೆಯುತ್ತೆ, `update()` ಹಲವು pairs ಒಟ್ಟಿಗೆ ಸೇರಿಸುತ್ತೆ ಅಥವಾ ಬದಲಾಯಿಸುತ್ತೆ:\n\n" + E.C_DICTOPS + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_DICTOPS + "\n\nORS shelf ಖಾಲಿ ಇತ್ತು, ಹಾಗಾಗಿ ಅದನ್ನು stock list ಇಂದ pop ಮಾಡಲಾಯಿತು; Ibuprofen `update()` ಇಂದ ಸೇರಿತು. `sum(stock.values())` ಎಲ್ಲಾ strips ಕೂಡಿಸುತ್ತೆ: 120 + 45 + 0 = 165.",
        },
        {
            "heading": "Dictionary ಇಂದ ಎಣಿಕೆ",
            "md": "ವಸ್ತುಗಳನ್ನು **ಎಣಿಸಲು** ಸಹಜ ದಾರಿ dictionary: key ನೀವು ಎಣಿಸುತ್ತಿರುವುದು, value ಎಷ್ಟು ಸಲ. ಒಂದು drug ಮೊದಲ ಸಲ ಬಂದಾಗ `get(drug, 0)` 0 ಕೊಡುತ್ತೆ:\n\n" + E.C_COUNT + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_COUNT + "\n\nಈ ಸಣ್ಣ pattern \"ಇವತ್ತು ಹೆಚ್ಚು ಮಾರಾಟ ಆದ drug ಯಾವುದು?\" ಅಥವಾ \"ಪ್ರತಿ ಹಳ್ಳಿಯಿಂದ ಎಷ್ಟು patients ಬಂದರು?\" ಎಂಬ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ಕೊಡುತ್ತೆ.",
            "callout": {"title": "ಎಣಿಕೆಯ pattern", "md": "Loop ಮುಂಚೆ counts = {}, ನಂತರ ಅದರ ಒಳಗೆ counts[item] = counts.get(item, 0) + 1. ಇದನ್ನು ನೆನಪಿಡಿ; Unit IV ನಲ್ಲೂ ಬೇಕಾಗುತ್ತೆ."},
        },
    ],
    "walkthrough": {
        "intro": "ಈ program stock check ಮಾಡಿ, 50 strips ಗಿಂತ ಕಡಿಮೆ ಇರುವ ಪ್ರತಿ drug ನ sorted reorder list ಮಾಡುತ್ತೆ.",
        "keyTerms": [
            {"meaning": "ಫಲಿತಾಂಶ ಸಂಗ್ರಹಿಸಲು ಖಾಲಿ list ಇಂದ ಶುರು ಮಾಡು."},
            {"meaning": "ಪ್ರತಿ drug ಮತ್ತು ಅದರ quantity, ಒಂದೊಂದು pair ಆಗಿ."},
            {"meaning": "Drug ಅನ್ನು list ನ ಕೊನೆಗೆ ಸೇರಿಸು."},
            {"meaning": "List ಅನ್ನು ಅದರಲ್ಲೇ, alphabetical ಕ್ರಮದಲ್ಲಿ sort ಮಾಡು."},
        ],
    },
    "errors": {
        "intro": "List methods ಜೊತೆ ಈ ಎರಡು errors ತುಂಬಾ ಸಾಮಾನ್ಯ.",
        "examples": [
            {"title": "List ನಲ್ಲಿ ಇಲ್ಲದ value ತೆಗೆಯುವುದು", "md": "`remove()` value ಇದ್ದಾಗ ಮಾತ್ರ ಕೆಲಸ ಮಾಡುತ್ತೆ. ಮೊದಲು check ಮಾಡಿ: `if \"Aspirin\" in cart: cart.remove(\"Aspirin\")`."},
            {"title": "sort() ನ ಫಲಿತಾಂಶ ಬಳಸುವುದು", "md": "`sort()` list ಅನ್ನು ಅದರಲ್ಲೇ sort ಮಾಡಿ `None` ಕೊಡುತ್ತೆ, ಹಾಗಾಗಿ `lowest` None. ಹೊಸ list ಗೆ `sorted(sugar)` ಬಳಸಿ, ಅಥವಾ ನೇರವಾಗಿ `min(sugar)`."},
        ],
    },
    "mistakes": [
        {"mistake": "`result = data.sort()` ಬರೆದು `result` ಬಳಸುವುದು", "see": "result None", "fix": "`data.sort()` ಅನ್ನು ಬೇರೆಯಾಗಿ call ಮಾಡಿ, ಅಥವಾ `result = sorted(data)`."},
        {"mistake": "append ಗೆ ಎರಡು items ಕೊಡುವುದು: `cart.append(\"ORS\", \"Zinc\")`", "see": "TypeError: list.append() takes exactly one argument (2 given)", "fix": "ಒಂದೊಂದಾಗಿ append ಮಾಡಿ, ಅಥವಾ `cart.extend([\"ORS\", \"Zinc\"])`."},
        {"mistake": "ಎರಡು lists ಸೇರಿಸಲು append: `a.append(b)`", "see": "Error ಇಲ್ಲ, ಆದರೆ list ಒಳಗೆ list ಬರುತ್ತೆ: `[1, 2, [3, 4]]`", "fix": "Items ಒಂದೊಂದಾಗಿ ಸೇರಿಸಲು `a.extend(b)` ಬಳಸಿ."},
        {"mistake": "ಖಾಲಿ list ಮೇಲೆ `pop()` call ಮಾಡುವುದು", "see": "IndexError: pop from empty list", "fix": "ಮೊದಲು check ಮಾಡಿ: `if queue: queue.pop()`."},
    ],
    "tasks": [
        {"title": "Queue ನಿರ್ವಹಿಸಿ", "md": "Anil ಈಗ ಬಂದಿದ್ದಾರೆ: ಅವರನ್ನು queue ನ **ಕೊನೆಗೆ** ಸೇರಿಸಿ. Sita emergency: ಅವಳನ್ನು **ಎಲ್ಲರ ಮುಂದೆ** ಇಡಿ. ನಂತರ queue print ಮಾಡಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["append() ಕೊನೆಗೆ ಸೇರಿಸುತ್ತೆ; insert(0, ...) ಮುಂದೆ.", "queue.append(\"Anil\")\nqueue.insert(0, \"Sita\")"]},
        {"title": "ಕಡಿಮೆ, ಹೆಚ್ಚು, average ತೂಕ", "md": "ಇವು ಐದು patients ನ ತೂಕ (kg). **min()**, **max()** ಮತ್ತು **sum()** ಇಂದ ಕಡಿಮೆ, ಹೆಚ್ಚು ಮತ್ತು average ತೂಕ print ಮಾಡಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["print(\"Lightest:\", min(weights))", "Average ಅಂದ್ರೆ sum(weights) / len(weights)."]},
        {"title": "Stock ನಲ್ಲಿ ಒಟ್ಟು strips", "md": "Dictionary ನ **values** ಕೂಡಿಸಿ shelf ಮೇಲಿನ ಒಟ್ಟು strips print ಮಾಡಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["stock.values() quantities ಮಾತ್ರ ಕೊಡುತ್ತೆ.", "print(\"Total strips:\", sum(stock.values()))"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "ಈ program ಪ್ರತಿ drug ಎಷ್ಟು ಸಲ ಮಾರಾಟ ಆಯಿತು ಅಂತ ಎಣಿಸಬೇಕು, ಆದರೆ ಮೊದಲ drug ಗೇ KeyError ಜೊತೆ crash ಆಗುತ್ತೆ. ಎಣಿಕೆಯ line ಸರಿ ಮಾಡಿ, output ನಿಖರವಾಗಿ ಹೀಗಿರಲಿ:",
         "hints": ["Drug ಮೊದಲ ಸಲ ಬಂದಾಗ counts ನಲ್ಲಿ ಅದರ key ಇನ್ನೂ ಇಲ್ಲ.", "counts[drug] = counts.get(drug, 0) + 1"],
         "solutionNote": "counts[drug] ಮೊದಲ ಸಲ fail ಆಗುತ್ತೆ ಯಾಕಂದ್ರೆ key ಇನ್ನೂ ಇಲ್ಲ. counts.get(drug, 0) ಪ್ರತಿ ಹೊಸ drug ಅನ್ನು 0 ಇಂದ ಶುರು ಮಾಡುತ್ತೆ."},
    ],
    "quiz": [
        {"q": "x = [1, 2]\nx.append(3)\nprint(x)\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "append item ಅನ್ನು ಕೊನೆಗೆ ಸೇರಿಸುತ್ತೆ."},
        {"q": "List ನ ಕೊನೆಯ item ತೆಗೆದು ಹಿಂದೆ ಕೊಡುವ method ಯಾವುದು?", "why": "Index ಇಲ್ಲದ pop() ಕೊನೆಯ item ತೆಗೆದು ಕೊಡುತ್ತೆ."},
        {"q": "a = [3, 1, 2]\nb = a.sort()\nprint(b)\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "sort() a ಅನ್ನೇ ಬದಲಾಯಿಸಿ None ಕೊಡುತ್ತೆ."},
        {"q": "d = {\"a\": 1, \"b\": 2}\nprint(sum(d.values()))\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "values() 1 ಮತ್ತು 2 ಕೊಡುತ್ತೆ, sum ಅವನ್ನು ಕೂಡಿಸುತ್ತೆ."},
        {"q": "ಇನ್ನೊಂದು list ನ ಪ್ರತಿ item ಅನ್ನು list ನ ಕೊನೆಗೆ ಸೇರಿಸುವ method ಯಾವುದು?", "why": "extend() items ಒಂದೊಂದಾಗಿ ಸೇರಿಸುತ್ತೆ; append() ಇಡೀ list ಅನ್ನು ಒಂದು item ಮಾಡುತ್ತೆ."},
        {"q": "counts[d] = counts.get(d, 0) + 1 ನಲ್ಲಿ get(d, 0) ಏನು ಮಾಡುತ್ತೆ?", "why": "get ಈಗಿನ ಎಣಿಕೆ ಕೊಡುತ್ತೆ, ಅಥವಾ ಮೊದಲ ಸಲ default 0."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 3.3 · Operations",
        "children": [
            {"label": "ಸೇರಿಸು", "children": [{"label": "append(x)"}, {"label": "insert(i, x)"}, {"label": "extend(list)"}]},
            {"label": "ತೆಗೆ", "children": [{"label": "remove(x)"}, {"label": "pop() ಹಿಂದೆ ಕೊಡುತ್ತೆ"}, {"label": "del list[i]"}]},
            {"label": "ಕ್ರಮ ಮತ್ತು ಸಾರ", "children": [{"label": "sort() ಅದರಲ್ಲೇ"}, {"label": "sorted() ಹೊಸ list"}, {"label": "min max sum count"}]},
            {"label": "Dictionary", "children": [{"label": "keys() values()"}, {"label": "items()"}, {"label": "update() pop()"}]},
            {"label": "ಎಣಿಕೆ", "children": [{"label": "counts = {}"}, {"label": "get(k, 0) + 1"}, {"label": "ಏನನ್ನಾದರೂ ಎಣಿಸಿ"}]},
            {"label": "Errors", "children": [{"label": "ValueError: not in list"}, {"label": "sort() ಇಂದ None"}]},
        ],
    },
    "summary": [
        "Methods dot ನಂತರ ಬರೆಯುತ್ತಾರೆ. **append()** ಕೊನೆಗೆ, **insert(i, x)** ಒಂದು index ನಲ್ಲಿ, **extend()** ಹಲವು items ಸೇರಿಸುತ್ತೆ.",
        "**remove(x)** ಒಂದು value ತೆಗೆಯುತ್ತೆ; **pop()** ಕೊನೆಯ item ತೆಗೆದು ಕೊಡುತ್ತೆ.",
        "**sorted()** ಹೊಸ sorted list ಕೊಡುತ್ತೆ; **sort()** ಅದರಲ್ಲೇ sort ಮಾಡಿ None ಕೊಡುತ್ತೆ. **min()**, **max()**, **sum()** ಮತ್ತು **count()** ಸಾರಾಂಶ ಕೊಡುತ್ತವೆ.",
        "Dictionaries ಗೆ **keys()**, **values()**, **items()**, **update()** ಮತ್ತು **pop()** ಇವೆ.",
        "ವಸ್ತುಗಳನ್ನು ಎಣಿಸಲು: loop ಒಳಗೆ `counts[item] = counts.get(item, 0) + 1`.",
    ],
}

NARR = {
    "hi": [
        "यह program हर कम stock वाली drug ढूँढता है, और एक reorder list बनाता है।",
        "Comment नियम बताता है: पचास strips से कम वाली हर चीज़ reorder करो।",
        "stock drug के नामों और shelf पर strips की संख्या की dictionary है।",
        "low एक खाली list से शुरू होती है। Reorder वाली drugs इसमें जोड़ी जाएँगी।",
        "items एक बार में एक pair देता है। पहला है Paracetamol, एक सौ बीस strips के साथ।",
        "एक सौ बीस, पचास से कम नहीं है, इसलिए कुछ नहीं जुड़ता।",
        "अगला है Cetirizine, पैंतालीस के साथ। यह पचास से कम है, इसलिए append इसे low में जोड़ता है।",
        "फिर ORS, बीस के साथ। यह भी जुड़ता है।",
        "sort list को alphabetical क्रम में रखता है, list को खुद बदलकर।",
        "print reorder list दिखाता है।",
        "len उसे गिनता है: reorder के लिए दो items।",
    ],
    "hinglish": [
        "Yeh program har kam stock wali drug dhoondhta hai, aur ek reorder list banata hai.",
        "Comment niyam batata hai: pachaas strips se kam wali har cheez reorder karo.",
        "stock drug ke naamon aur shelf par strips ki sankhya ki dictionary hai.",
        "low ek khaali list se shuru hoti hai. Reorder wali drugs ismein jodi jaayengi.",
        "items ek baar mein ek pair deta hai. Pehla hai Paracetamol, ek sau bees strips ke saath.",
        "Ek sau bees, pachaas se kam nahi hai, isliye kuch nahi judta.",
        "Agla hai Cetirizine, paintaalis ke saath. Yeh pachaas se kam hai, isliye append ise low mein jodta hai.",
        "Phir ORS, bees ke saath. Yeh bhi judta hai.",
        "sort list ko alphabetical kram mein rakhta hai, list ko khud badalkar.",
        "print reorder list dikhaata hai.",
        "len use ginta hai: reorder ke liye do items.",
    ],
    "kn": [
        "ಈ program stock ಕಡಿಮೆ ಇರುವ ಪ್ರತಿ drug ಹುಡುಕಿ, reorder list ಮಾಡುತ್ತೆ.",
        "Comment ನಿಯಮ ಹೇಳುತ್ತೆ: ಐವತ್ತು strips ಗಿಂತ ಕಡಿಮೆ ಇರುವ ಎಲ್ಲವನ್ನೂ reorder ಮಾಡು.",
        "stock, drug ಹೆಸರುಗಳು ಮತ್ತು shelf ಮೇಲಿನ strips ಸಂಖ್ಯೆಯ dictionary.",
        "low ಖಾಲಿ list ಆಗಿ ಶುರು. Reorder ಮಾಡಬೇಕಾದ drugs ಇದಕ್ಕೆ ಸೇರುತ್ತವೆ.",
        "items ಒಂದು ಸಲಕ್ಕೆ ಒಂದು pair ಕೊಡುತ್ತೆ. ಮೊದಲದು Paracetamol, ನೂರ ಇಪ್ಪತ್ತು strips.",
        "ನೂರ ಇಪ್ಪತ್ತು ಐವತ್ತಕ್ಕಿಂತ ಕಡಿಮೆ ಅಲ್ಲ, ಹಾಗಾಗಿ ಏನೂ ಸೇರಲ್ಲ.",
        "ಮುಂದೆ Cetirizine, ನಲವತ್ತೈದು. ಇದು ಐವತ್ತಕ್ಕಿಂತ ಕಡಿಮೆ, ಹಾಗಾಗಿ append ಇದನ್ನು low ಗೆ ಸೇರಿಸುತ್ತೆ.",
        "ನಂತರ ORS, ಇಪ್ಪತ್ತು. ಇದೂ ಸೇರುತ್ತೆ.",
        "sort list ಅನ್ನು alphabetical ಕ್ರಮಕ್ಕೆ ತರುತ್ತೆ, list ಅನ್ನೇ ಬದಲಾಯಿಸಿ.",
        "print reorder list ತೋರಿಸುತ್ತೆ.",
        "len ಅದನ್ನು ಎಣಿಸುತ್ತೆ: reorder ಗೆ ಎರಡು items.",
    ],
}

ANIM = {
    "hi": [
        "low एक खाली list से शुरू होती है, अभी उसमें कुछ नहीं है।",
        "append Cetirizine को आखिर में जोड़ता है। अब list में एक item है, index zero पर।",
        "append उसके बाद ORS जोड़ता है, index एक पर।",
        "pop आखिरी item list से निकालकर वापस देता है, इसलिए print ORS दिखाता है।",
        "List में सिर्फ़ Cetirizine बचा है।",
    ],
    "hinglish": [
        "low ek khaali list se shuru hoti hai, abhi usmein kuch nahi hai.",
        "append Cetirizine ko aakhir mein jodta hai. Ab list mein ek item hai, index zero par.",
        "append uske baad ORS jodta hai, index ek par.",
        "pop aakhri item list se nikaalkar wapas deta hai, isliye print ORS dikhaata hai.",
        "List mein sirf Cetirizine bacha hai.",
    ],
    "kn": [
        "low ಖಾಲಿ list ಆಗಿ ಶುರು, ಇನ್ನೂ ಒಳಗೆ ಏನೂ ಇಲ್ಲ.",
        "append Cetirizine ಅನ್ನು ಕೊನೆಗೆ ಸೇರಿಸುತ್ತೆ. ಈಗ list ನಲ್ಲಿ ಒಂದು item, index zero ನಲ್ಲಿ.",
        "append ಅದರ ನಂತರ ORS ಸೇರಿಸುತ್ತೆ, index ಒಂದರಲ್ಲಿ.",
        "pop ಕೊನೆಯ item ಅನ್ನು list ಇಂದ ತೆಗೆದು ಹಿಂದೆ ಕೊಡುತ್ತೆ, ಹಾಗಾಗಿ print ORS ತೋರಿಸುತ್ತೆ.",
        "List ನಲ್ಲಿ Cetirizine ಮಾತ್ರ ಉಳಿದಿದೆ.",
    ],
}

if __name__ == "__main__":
    build("3-3", "anim-grow", T, NARR, ANIM)

"""Lesson 3.1 translations (Hindi, Hinglish, Kannada) and voice scripts."""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import build  # noqa: E402

_spec = importlib.util.spec_from_file_location("en31", os.path.join(os.path.dirname(__file__), "..", "lessons", "bp101t_3-1_en.py"))
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)

T = {}

T["hi"] = {
    "hook": {
        "title": "सात readings, एक नाम",
        "md": "एक patient का blood pressure हफ़्ते भर हर सुबह check होता है। अब तक जो आप जानते हैं, उससे सात variables चाहिए होंगे: `bp1`, `bp2`, `bp3` वगैरह। अब सोचिए एक महीने की readings, या चालीस patients वाला ward।\n\nPython के पास बेहतर तरीका है: सारी readings, क्रम से, **एक नाम** के नीचे रखो। यह container है **list**। असली data का काम lists से शुरू होता है: इस unit में मिलने वाला हर dataset, stock register से clinical trial तक, lists से बना है।",
    },
    "learn": [
        "Square brackets से **list** बनाना, और **len()** से गिनना",
        "**Indexing** से position के हिसाब से एक item चुनना, **0** से शुरू करके, और आखिर से **-1** से",
        "किसी item को **बदलना**, क्योंकि lists **mutable** हैं",
        "**Slicing** से list का एक हिस्सा लेना, और list पर loop चलाना",
    ],
    "explanation": [
        {
            "heading": "List बनाना",
            "md": "**List** **square brackets** से लिखी जाती है, items commas से अलग:\n\n" + E.C_MAKE + "\n\nयह print करता है:\n\n" + E.O_MAKE + "\n\nList items को **उसी क्रम में** रखती है जिसमें आपने लिखा। `len()` items गिनता है, जैसे Lesson 1.6 में उसने string के letters गिने थे। List में numbers, strings, या दोनों हो सकते हैं, और `[]` खाली list है।",
            "callout": {"title": "List", "md": "Items का क्रम वाला collection, square brackets में, commas से अलग। एक variable सबको रखता है।"},
        },
        {
            "heading": "Indexing: एक item चुनना",
            "md": "हर item का एक position number होता है जिसे **index** कहते हैं। Python गिनती **0** से शुरू करता है, इसलिए पहला item index 0 पर है:\n\n" + E.C_INDEX + "\n\nयह print करता है:\n\n" + E.O_INDEX + "\n\n**Negative indexes** आखिर से गिनते हैं: `-1` आखिरी item है, `-2` उससे पहले वाला। यह तब काम आता है जब आपको latest reading चाहिए और पता नहीं list कितनी लंबी है।",
            "callout": {"title": "पहला item [0] है, [1] नहीं", "md": "4 items वाली list के indexes 0, 1, 2 और 3 हैं। Index 4 माँगने पर IndexError: list index out of range आता है।"},
        },
        {
            "heading": "Item बदलना",
            "md": "String से अलग, list बनने के बाद बदली जा सकती है। किसी item को बदलने के लिए `=` के बाईं ओर index लगाइए:\n\n" + E.C_CHANGE + "\n\nयह print करता है:\n\n" + E.O_CHANGE + "\n\nदूसरा shelf खाली था (0); restock के बाद उसमें 60 हैं। क्योंकि lists बदली जा सकती हैं, इसलिए उन्हें **mutable** कहते हैं।",
        },
        {
            "heading": "Slicing: list का एक हिस्सा लेना",
            "md": "**Slice** `list[start:stop]` index `start` से index `stop` तक की नई list देता है, पर `stop` **शामिल नहीं** होता:\n\n" + E.C_SLICE + "\n\nयह print करता है:\n\n" + E.O_SLICE + "\n\n- `bp[1:4]` indexes 1, 2 और 3 लेता है।\n- पहले item से शुरू करना हो तो `start` छोड़ दीजिए: `bp[:3]`।\n- आखिर तक जाना हो तो `stop` छोड़ दीजिए: `bp[3:]`।\n- `bp[-2:]` आखिरी दो readings देता है।\n- तीसरा number **step** है: `bp[::2]` हर दूसरी reading लेता है।\n\nSlicing original list को कभी नहीं बदलता; वह नई list बनाता है।",
            "callout": {"title": "Slice में items गिनिए", "md": "stop घटा start: bp[1:4] में 4 - 1 = 3 items हैं। Slices strings पर भी बिल्कुल ऐसे ही काम करते हैं।"},
        },
        {
            "heading": "List के हर item से गुज़रना",
            "md": "`for` loop (Lesson 2.3) list के हर item पर क्रम से जाता है, और `in` check करता है कि कोई value list में है या नहीं:\n\n" + E.C_LOOP + "\n\nयह print करता है:\n\n" + E.O_LOOP + "\n\n`\"Aspirin\" in medicines` `False` है क्योंकि इस prescription में Aspirin नहीं है। अगले lessons में आप data रखने के दो और तरीके सीखेंगे, फिर items जोड़ेंगे, हटाएँगे और sort करेंगे।",
        },
    ],
    "walkthrough": {
        "intro": "यह program पाँच दिन की fasting blood sugar readings एक list में रखता है, फिर position से readings निकालता है।",
        "keyTerms": [
            {"meaning": "पाँच readings की list बनाओ, क्रम से।"},
            {"meaning": "Index 0 वाला item: पहली reading।"},
            {"meaning": "आखिरी item, आखिर से गिनकर।"},
            {"meaning": "एक slice: indexes 1, 2 और 3 (stop शामिल नहीं)।"},
        ],
    },
    "errors": {
        "intro": "ये दो errors ऐसा index use करने से आती हैं जो काम नहीं करता।",
        "examples": [
            {"title": "ऐसा index माँगना जो है ही नहीं", "md": "List में 3 items हैं, इसलिए उसके indexes 0, 1 और 2 हैं। Index 3 नहीं है। आखिरी item के लिए `medicines[2]` लिखिए, या उससे बेहतर, `medicines[-1]`।"},
            {"title": "Index में decimal number use करना", "md": "`/` हमेशा float देता है, इसलिए `middle` 1.5 है, और item 1.5 जैसा कुछ नहीं होता। पूरा number पाने के लिए floor division use कीजिए: `middle = len(doses) // 2`।"},
        ],
    },
    "mistakes": [
        {"mistake": "पहले item के लिए `medicines[1]` लिखना", "see": "कोई error नहीं, पर दूसरा item मिलता है", "fix": "Indexes 0 से शुरू होते हैं: पहला item `medicines[0]` है।"},
        {"mistake": "उम्मीद करना कि `bp[1:3]` में index 3 शामिल होगा", "see": "कोई error नहीं, पर slice में उम्मीद से एक item कम है", "fix": "Stop index शामिल नहीं होता: `bp[1:4]` indexes 1, 2 और 3 देता है।"},
        {"mistake": "गोल brackets use करना: `medicines(0)`", "see": "TypeError: 'list' object is not callable", "fix": "Index square brackets में जाता है: `medicines[0]`।"},
        {"mistake": "Text item के quotes भूल जाना: `[\"Paracetamol\", Ibuprofen]`", "see": "NameError: name 'Ibuprofen' is not defined", "fix": "हर text item को quotes चाहिए: `[\"Paracetamol\", \"Ibuprofen\"]`।"},
    ],
    "tasks": [
        {"title": "List बनाइए", "md": "**drugs** नाम की list बनाइए जिसमें `\"Aspirin\"`, `\"Atorvastatin\"` और `\"Amlodipine\"` इसी क्रम में हों। List print कीजिए, फिर उसकी length। Output बिल्कुल यह होना चाहिए:",
         "hints": ["drugs = [\"Aspirin\", \"Atorvastatin\", \"Amlodipine\"]", "print(drugs) list दिखाता है; print(len(drugs)) बताता है उसमें कितने items हैं।"]},
        {"title": "पहली और आखिरी reading", "md": "एक patient का temperature पाँच बार लिया गया। **Indexing** से **पहली** reading और फिर **आखिरी** reading print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["पहला item index 0 पर है।", "आखिरी item index -1 पर है: print(temps[-1])"]},
        {"title": "हफ़्ते के बीच का slice", "md": "ये 7 दिन की pulse readings हैं। **दिन 3, 4 और 5** (indexes 2, 3 और 4) की readings **एक slice** से print कीजिए। Output बिल्कुल यह होना चाहिए:",
         "hints": ["Slice pulse[start:stop] है, और stop शामिल नहीं होता।", "print(pulse[2:5])"]},
        {"title": "Bug ढूँढिए", "md": "Amoxicillin, यानी **दूसरा** item, 200 strips तक restock हुआ। पर यह program तीसरा item बदल देता है। इसे ठीक कीजिए ताकि output बिल्कुल यह हो:",
         "hints": ["दूसरे item का index क्या है?", "Indexes 0 से शुरू होते हैं, इसलिए दूसरा item stock[1] है।"],
         "solutionNote": "Indexes 0 से शुरू होते हैं, इसलिए दूसरा item index 1 पर है। stock[2] तीसरा item था, 300।"},
    ],
    "quiz": [
        {"q": "meds = [\"Aspirin\", \"Insulin\", \"Digoxin\"]\nprint(meds[1])\n\nयह क्या print करता है?", "why": "Indexes 0 से शुरू होते हैं, इसलिए meds[1] दूसरा item है, Insulin।"},
        {"q": "List के पहले item का index क्या है?", "why": "Python list positions हमेशा 0 से गिनता है।"},
        {"q": "x = [10, 20, 30, 40, 50]\nprint(x[1:3])\n\nयह क्या print करता है?", "why": "Slice indexes 1 और 2 लेता है; stop index 3 शामिल नहीं।"},
        {"q": "readings[-1] क्या देता है?", "why": "Negative indexes आखिर से गिनते हैं; -1 आखिरी item है।"},
        {"q": "एक list में 4 items हैं। print(items[4]) से क्या होता है?", "why": "Indexes 0 से 3 हैं, इसलिए index 4 है ही नहीं।"},
        {"q": "Lists के बारे में कौन-सी बात सही है?", "why": "Lists mutable हैं: items बदल, जोड़ और हटा सकते हैं।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 3.1 · Lists",
        "children": [
            {"label": "बनाना", "children": [{"label": "[a, b, c]"}, {"label": "len() गिनता है"}, {"label": "[] खाली है"}]},
            {"label": "Index", "children": [{"label": "0 से शुरू"}, {"label": "-1 आखिरी"}, {"label": "list[i]"}]},
            {"label": "बदलना", "children": [{"label": "list[i] = new"}, {"label": "Mutable"}, {"label": "Strings नहीं"}]},
            {"label": "Slice", "children": [{"label": "[start:stop]"}, {"label": "Stop शामिल नहीं"}, {"label": "[::2] step"}]},
            {"label": "गुज़रना", "children": [{"label": "for item in list"}, {"label": "x in list"}, {"label": "क्रम बना रहता है"}]},
            {"label": "Errors", "children": [{"label": "IndexError: out of range"}, {"label": "TypeError: float index"}]},
        ],
    },
    "summary": [
        "**List** कई items को, क्रम से, एक variable में रखती है: `drugs = [\"Aspirin\", \"Insulin\"]`। `len()` उन्हें गिनता है।",
        "**Indexing** एक item चुनता है: पहला `[0]` है, आखिरी `[-1]`। न होने वाला index **IndexError** देता है।",
        "Lists **mutable** हैं: `stock[1] = 60` एक item बदल देता है।",
        "**Slice** `list[start:stop]` नई list बनाता है, `stop` तक पर उसे शामिल किए बिना; `[::2]` हर दूसरा item लेता है।",
        "`for item in list:` हर item पर जाता है, और `x in list` check करता है कि value मौजूद है या नहीं।",
    ],
}

T["hinglish"] = {
    "hook": {
        "title": "Saat readings, ek naam",
        "md": "Ek patient ka blood pressure hafte bhar har subah check hota hai. Ab tak jo aap jaante hain, usse saat variables chahiye honge: `bp1`, `bp2`, `bp3` wagairah. Ab sochiye ek mahine ki readings, ya chaalis patients wala ward.\n\nPython ke paas behtar tareeka hai: saari readings, kram se, **ek naam** ke neeche rakho. Yeh container hai **list**. Asli data ka kaam lists se shuru hota hai: is unit mein milne wala har dataset, stock register se clinical trial tak, lists se bana hai.",
    },
    "learn": [
        "Square brackets se **list** banana, aur **len()** se ginna",
        "**Indexing** se position ke hisaab se ek item chunna, **0** se shuru karke, aur aakhir se **-1** se",
        "Kisi item ko **badalna**, kyunki lists **mutable** hain",
        "**Slicing** se list ka ek hissa lena, aur list par loop chalana",
    ],
    "explanation": [
        {
            "heading": "List banana",
            "md": "**List** **square brackets** se likhi jaati hai, items commas se alag:\n\n" + E.C_MAKE + "\n\nYeh print karta hai:\n\n" + E.O_MAKE + "\n\nList items ko **usi kram mein** rakhti hai jismein aapne likha. `len()` items ginta hai, jaise Lesson 1.6 mein usne string ke letters gine the. List mein numbers, strings, ya dono ho sakte hain, aur `[]` khaali list hai.",
            "callout": {"title": "List", "md": "Items ka kram wala collection, square brackets mein, commas se alag. Ek variable sabko rakhta hai."},
        },
        {
            "heading": "Indexing: ek item chunna",
            "md": "Har item ka ek position number hota hai jise **index** kehte hain. Python ginti **0** se shuru karta hai, isliye pehla item index 0 par hai:\n\n" + E.C_INDEX + "\n\nYeh print karta hai:\n\n" + E.O_INDEX + "\n\n**Negative indexes** aakhir se ginte hain: `-1` aakhri item hai, `-2` usse pehle wala. Yeh tab kaam aata hai jab aapko latest reading chahiye aur pata nahi list kitni lambi hai.",
            "callout": {"title": "Pehla item [0] hai, [1] nahi", "md": "4 items wali list ke indexes 0, 1, 2 aur 3 hain. Index 4 maangne par IndexError: list index out of range aata hai."},
        },
        {
            "heading": "Item badalna",
            "md": "String se alag, list banne ke baad badli ja sakti hai. Kisi item ko badalne ke liye `=` ke baayin taraf index lagaiye:\n\n" + E.C_CHANGE + "\n\nYeh print karta hai:\n\n" + E.O_CHANGE + "\n\nDoosra shelf khaali tha (0); restock ke baad usmein 60 hain. Kyunki lists badli ja sakti hain, isliye unhe **mutable** kehte hain.",
        },
        {
            "heading": "Slicing: list ka ek hissa lena",
            "md": "**Slice** `list[start:stop]` index `start` se index `stop` tak ki nayi list deta hai, par `stop` **shaamil nahi** hota:\n\n" + E.C_SLICE + "\n\nYeh print karta hai:\n\n" + E.O_SLICE + "\n\n- `bp[1:4]` indexes 1, 2 aur 3 leta hai.\n- Pehle item se shuru karna ho to `start` chhod dijiye: `bp[:3]`.\n- Aakhir tak jaana ho to `stop` chhod dijiye: `bp[3:]`.\n- `bp[-2:]` aakhri do readings deta hai.\n- Teesra number **step** hai: `bp[::2]` har doosri reading leta hai.\n\nSlicing original list ko kabhi nahi badalta; woh nayi list banata hai.",
            "callout": {"title": "Slice mein items giniye", "md": "stop ghata start: bp[1:4] mein 4 - 1 = 3 items hain. Slices strings par bhi bilkul aise hi kaam karte hain."},
        },
        {
            "heading": "List ke har item se guzarna",
            "md": "`for` loop (Lesson 2.3) list ke har item par kram se jaata hai, aur `in` check karta hai ki koi value list mein hai ya nahi:\n\n" + E.C_LOOP + "\n\nYeh print karta hai:\n\n" + E.O_LOOP + "\n\n`\"Aspirin\" in medicines` `False` hai kyunki is prescription mein Aspirin nahi hai. Agle lessons mein aap data rakhne ke do aur tareeke seekhenge, phir items jodenge, hataayenge aur sort karenge.",
        },
    ],
    "walkthrough": {
        "intro": "Yeh program paanch din ki fasting blood sugar readings ek list mein rakhta hai, phir position se readings nikaalta hai.",
        "keyTerms": [
            {"meaning": "Paanch readings ki list banao, kram se."},
            {"meaning": "Index 0 wala item: pehli reading."},
            {"meaning": "Aakhri item, aakhir se ginkar."},
            {"meaning": "Ek slice: indexes 1, 2 aur 3 (stop shaamil nahi)."},
        ],
    },
    "errors": {
        "intro": "Yeh do errors aisa index use karne se aati hain jo kaam nahi karta.",
        "examples": [
            {"title": "Aisa index maangna jo hai hi nahi", "md": "List mein 3 items hain, isliye uske indexes 0, 1 aur 2 hain. Index 3 nahi hai. Aakhri item ke liye `medicines[2]` likhiye, ya usse behtar, `medicines[-1]`."},
            {"title": "Index mein decimal number use karna", "md": "`/` hamesha float deta hai, isliye `middle` 1.5 hai, aur item 1.5 jaisa kuch nahi hota. Poora number paane ke liye floor division use kijiye: `middle = len(doses) // 2`."},
        ],
    },
    "mistakes": [
        {"mistake": "Pehle item ke liye `medicines[1]` likhna", "see": "Koi error nahi, par doosra item milta hai", "fix": "Indexes 0 se shuru hote hain: pehla item `medicines[0]` hai."},
        {"mistake": "Ummeed karna ki `bp[1:3]` mein index 3 shaamil hoga", "see": "Koi error nahi, par slice mein ummeed se ek item kam hai", "fix": "Stop index shaamil nahi hota: `bp[1:4]` indexes 1, 2 aur 3 deta hai."},
        {"mistake": "Gol brackets use karna: `medicines(0)`", "see": "TypeError: 'list' object is not callable", "fix": "Index square brackets mein jaata hai: `medicines[0]`."},
        {"mistake": "Text item ke quotes bhool jaana: `[\"Paracetamol\", Ibuprofen]`", "see": "NameError: name 'Ibuprofen' is not defined", "fix": "Har text item ko quotes chahiye: `[\"Paracetamol\", \"Ibuprofen\"]`."},
    ],
    "tasks": [
        {"title": "List banaiye", "md": "**drugs** naam ki list banaiye jismein `\"Aspirin\"`, `\"Atorvastatin\"` aur `\"Amlodipine\"` isi kram mein hon. List print kijiye, phir uski length. Output bilkul yeh hona chahiye:",
         "hints": ["drugs = [\"Aspirin\", \"Atorvastatin\", \"Amlodipine\"]", "print(drugs) list dikhata hai; print(len(drugs)) batata hai usmein kitne items hain."]},
        {"title": "Pehli aur aakhri reading", "md": "Ek patient ka temperature paanch baar liya gaya. **Indexing** se **pehli** reading aur phir **aakhri** reading print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["Pehla item index 0 par hai.", "Aakhri item index -1 par hai: print(temps[-1])"]},
        {"title": "Hafte ke beech ka slice", "md": "Yeh 7 din ki pulse readings hain. **Din 3, 4 aur 5** (indexes 2, 3 aur 4) ki readings **ek slice** se print kijiye. Output bilkul yeh hona chahiye:",
         "hints": ["Slice pulse[start:stop] hai, aur stop shaamil nahi hota.", "print(pulse[2:5])"]},
        {"title": "Bug dhoondhiye", "md": "Amoxicillin, yaani **doosra** item, 200 strips tak restock hua. Par yeh program teesra item badal deta hai. Ise theek kijiye taaki output bilkul yeh ho:",
         "hints": ["Doosre item ka index kya hai?", "Indexes 0 se shuru hote hain, isliye doosra item stock[1] hai."],
         "solutionNote": "Indexes 0 se shuru hote hain, isliye doosra item index 1 par hai. stock[2] teesra item tha, 300."},
    ],
    "quiz": [
        {"q": "meds = [\"Aspirin\", \"Insulin\", \"Digoxin\"]\nprint(meds[1])\n\nYeh kya print karta hai?", "why": "Indexes 0 se shuru hote hain, isliye meds[1] doosra item hai, Insulin."},
        {"q": "List ke pehle item ka index kya hai?", "why": "Python list positions hamesha 0 se ginta hai."},
        {"q": "x = [10, 20, 30, 40, 50]\nprint(x[1:3])\n\nYeh kya print karta hai?", "why": "Slice indexes 1 aur 2 leta hai; stop index 3 shaamil nahi."},
        {"q": "readings[-1] kya deta hai?", "why": "Negative indexes aakhir se ginte hain; -1 aakhri item hai."},
        {"q": "Ek list mein 4 items hain. print(items[4]) se kya hota hai?", "why": "Indexes 0 se 3 hain, isliye index 4 hai hi nahi."},
        {"q": "Lists ke baare mein kaun-si baat sahi hai?", "why": "Lists mutable hain: items badal, jod aur hata sakte hain."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 3.1 · Lists",
        "children": [
            {"label": "Banana", "children": [{"label": "[a, b, c]"}, {"label": "len() ginta hai"}, {"label": "[] khaali hai"}]},
            {"label": "Index", "children": [{"label": "0 se shuru"}, {"label": "-1 aakhri"}, {"label": "list[i]"}]},
            {"label": "Badalna", "children": [{"label": "list[i] = new"}, {"label": "Mutable"}, {"label": "Strings nahi"}]},
            {"label": "Slice", "children": [{"label": "[start:stop]"}, {"label": "Stop shaamil nahi"}, {"label": "[::2] step"}]},
            {"label": "Guzarna", "children": [{"label": "for item in list"}, {"label": "x in list"}, {"label": "Kram bana rehta hai"}]},
            {"label": "Errors", "children": [{"label": "IndexError: out of range"}, {"label": "TypeError: float index"}]},
        ],
    },
    "summary": [
        "**List** kai items ko, kram se, ek variable mein rakhti hai: `drugs = [\"Aspirin\", \"Insulin\"]`. `len()` unhe ginta hai.",
        "**Indexing** ek item chunta hai: pehla `[0]` hai, aakhri `[-1]`. Na hone wala index **IndexError** deta hai.",
        "Lists **mutable** hain: `stock[1] = 60` ek item badal deta hai.",
        "**Slice** `list[start:stop]` nayi list banata hai, `stop` tak par use shaamil kiye bina; `[::2]` har doosra item leta hai.",
        "`for item in list:` har item par jaata hai, aur `x in list` check karta hai ki value maujood hai ya nahi.",
    ],
}

T["kn"] = {
    "hook": {
        "title": "ಏಳು readings, ಒಂದೇ ಹೆಸರು",
        "md": "ಒಬ್ಬ patient ನ blood pressure ಒಂದು ವಾರ ಪ್ರತಿ ಬೆಳಿಗ್ಗೆ check ಆಗುತ್ತೆ. ಇಲ್ಲಿವರೆಗೆ ಕಲಿತಿರೋದರಿಂದ ಏಳು variables ಬೇಕು: `bp1`, `bp2`, `bp3` ಹೀಗೆ. ಈಗ ಒಂದು ತಿಂಗಳ readings, ಅಥವಾ ನಲವತ್ತು patients ಇರುವ ward ಯೋಚಿಸಿ.\n\nPython ನಲ್ಲಿ ಇದಕ್ಕಿಂತ ಒಳ್ಳೆಯ ದಾರಿ ಇದೆ: ಎಲ್ಲಾ readings ಅನ್ನು, ಕ್ರಮವಾಗಿ, **ಒಂದೇ ಹೆಸರಿನ** ಕೆಳಗೆ ಇಡಿ. ಆ container **list**. ನಿಜವಾದ data ಕೆಲಸ lists ಇಂದ ಶುರು: ಈ unit ನಲ್ಲಿ ಸಿಗುವ ಪ್ರತಿ dataset, stock register ಇಂದ clinical trial ವರೆಗೆ, lists ಇಂದಲೇ ಮಾಡಿದ್ದು.",
    },
    "learn": [
        "Square brackets ಇಂದ **list** ಮಾಡುವುದು, **len()** ಇಂದ ಎಣಿಸುವುದು",
        "**Indexing** ಇಂದ position ಪ್ರಕಾರ ಒಂದು item ಆರಿಸುವುದು, **0** ಇಂದ ಶುರು ಮಾಡಿ, ಕೊನೆಯಿಂದ **-1** ಇಂದ",
        "ಒಂದು item ಅನ್ನು **ಬದಲಾಯಿಸುವುದು**, ಯಾಕಂದ್ರೆ lists **mutable**",
        "**Slicing** ಇಂದ list ನ ಒಂದು ಭಾಗ ತೆಗೆಯುವುದು, ಮತ್ತು list ಮೇಲೆ loop ಓಡಿಸುವುದು",
    ],
    "explanation": [
        {
            "heading": "List ಮಾಡುವುದು",
            "md": "**List** ಅನ್ನು **square brackets** ಇಂದ ಬರೆಯುತ್ತಾರೆ, items commas ಇಂದ ಬೇರೆ:\n\n" + E.C_MAKE + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_MAKE + "\n\nList items ಅನ್ನು **ನೀವು ಬರೆದ ಕ್ರಮದಲ್ಲೇ** ಇಡುತ್ತೆ. `len()` items ಎಣಿಸುತ್ತೆ, Lesson 1.6 ನಲ್ಲಿ string ನ letters ಎಣಿಸಿದ ಹಾಗೆ. List ನಲ್ಲಿ numbers, strings, ಅಥವಾ ಎರಡೂ ಇರಬಹುದು, ಮತ್ತು `[]` ಖಾಲಿ list.",
            "callout": {"title": "List", "md": "Items ನ ಕ್ರಮದ collection, square brackets ಒಳಗೆ, commas ಇಂದ ಬೇರೆ. ಒಂದೇ variable ಎಲ್ಲವನ್ನೂ ಇಡುತ್ತೆ."},
        },
        {
            "heading": "Indexing: ಒಂದು item ಆರಿಸುವುದು",
            "md": "ಪ್ರತಿ item ಗೆ ಒಂದು position number ಇರುತ್ತೆ, ಅದನ್ನು **index** ಅಂತಾರೆ. Python ಎಣಿಕೆ **0** ಇಂದ ಶುರು ಮಾಡುತ್ತೆ, ಹಾಗಾಗಿ ಮೊದಲ item index 0 ನಲ್ಲಿ ಇರುತ್ತೆ:\n\n" + E.C_INDEX + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_INDEX + "\n\n**Negative indexes** ಕೊನೆಯಿಂದ ಎಣಿಸುತ್ತವೆ: `-1` ಕೊನೆಯ item, `-2` ಅದರ ಹಿಂದಿನದು. Latest reading ಬೇಕು ಆದರೆ list ಎಷ್ಟು ಉದ್ದ ಅಂತ ಗೊತ್ತಿಲ್ಲದಿದ್ದಾಗ ಇದು ಉಪಯೋಗ.",
            "callout": {"title": "ಮೊದಲ item [0], [1] ಅಲ್ಲ", "md": "4 items ಇರುವ list ನ indexes 0, 1, 2 ಮತ್ತು 3. Index 4 ಕೇಳಿದರೆ IndexError: list index out of range ಬರುತ್ತೆ."},
        },
        {
            "heading": "Item ಬದಲಾಯಿಸುವುದು",
            "md": "String ಹಾಗಲ್ಲ, list ಮಾಡಿದ ಮೇಲೂ ಬದಲಾಯಿಸಬಹುದು. ಒಂದು item ಬದಲಾಯಿಸಲು `=` ನ ಎಡಕ್ಕೆ index ಹಾಕಿ:\n\n" + E.C_CHANGE + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_CHANGE + "\n\nಎರಡನೇ shelf ಖಾಲಿ ಇತ್ತು (0); restock ಆದ ಮೇಲೆ ಅದರಲ್ಲಿ 60. Lists ಬದಲಾಯಿಸಬಹುದಾದ್ದರಿಂದ, ಅವನ್ನು **mutable** ಅಂತಾರೆ.",
        },
        {
            "heading": "Slicing: list ನ ಒಂದು ಭಾಗ ತೆಗೆಯುವುದು",
            "md": "**Slice** `list[start:stop]` index `start` ಇಂದ index `stop` ವರೆಗಿನ ಹೊಸ list ಕೊಡುತ್ತೆ, ಆದರೆ `stop` **ಸೇರಲ್ಲ**:\n\n" + E.C_SLICE + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_SLICE + "\n\n- `bp[1:4]` indexes 1, 2 ಮತ್ತು 3 ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ.\n- ಮೊದಲ item ಇಂದ ಶುರು ಮಾಡಬೇಕಾದರೆ `start` ಬಿಡಿ: `bp[:3]`.\n- ಕೊನೆಯವರೆಗೆ ಹೋಗಬೇಕಾದರೆ `stop` ಬಿಡಿ: `bp[3:]`.\n- `bp[-2:]` ಕೊನೆಯ ಎರಡು readings ಕೊಡುತ್ತೆ.\n- ಮೂರನೇ number **step**: `bp[::2]` ಪ್ರತಿ ಎರಡನೇ reading ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ.\n\nSlicing original list ಅನ್ನು ಯಾವತ್ತೂ ಬದಲಾಯಿಸಲ್ಲ; ಅದು ಹೊಸ list ಮಾಡುತ್ತೆ.",
            "callout": {"title": "Slice ನಲ್ಲಿ items ಎಣಿಸಿ", "md": "stop ಕಳೆ start: bp[1:4] ನಲ್ಲಿ 4 - 1 = 3 items. Slices strings ಮೇಲೂ ಇದೇ ತರಹ ಕೆಲಸ ಮಾಡುತ್ತವೆ."},
        },
        {
            "heading": "List ನ ಪ್ರತಿ item ಮೂಲಕ ಹೋಗುವುದು",
            "md": "`for` loop (Lesson 2.3) list ನ ಪ್ರತಿ item ಗೆ ಕ್ರಮವಾಗಿ ಹೋಗುತ್ತೆ, ಮತ್ತು `in` ಒಂದು value list ನಲ್ಲಿ ಇದೆಯಾ ಅಂತ check ಮಾಡುತ್ತೆ:\n\n" + E.C_LOOP + "\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n" + E.O_LOOP + "\n\n`\"Aspirin\" in medicines` `False`, ಯಾಕಂದ್ರೆ ಈ prescription ನಲ್ಲಿ Aspirin ಇಲ್ಲ. ಮುಂದಿನ lessons ನಲ್ಲಿ data ಇಡುವ ಇನ್ನೂ ಎರಡು ದಾರಿಗಳನ್ನು ಕಲಿಯುತ್ತೀರಿ, ನಂತರ items ಸೇರಿಸುತ್ತೀರಿ, ತೆಗೆಯುತ್ತೀರಿ, sort ಮಾಡುತ್ತೀರಿ.",
        },
    ],
    "walkthrough": {
        "intro": "ಈ program ಐದು ದಿನದ fasting blood sugar readings ಅನ್ನು ಒಂದು list ನಲ್ಲಿ ಇಡುತ್ತೆ, ನಂತರ position ಪ್ರಕಾರ readings ತೆಗೆಯುತ್ತೆ.",
        "keyTerms": [
            {"meaning": "ಐದು readings ನ list ಮಾಡು, ಕ್ರಮವಾಗಿ."},
            {"meaning": "Index 0 ನ item: ಮೊದಲ reading."},
            {"meaning": "ಕೊನೆಯ item, ಕೊನೆಯಿಂದ ಎಣಿಸಿ."},
            {"meaning": "ಒಂದು slice: indexes 1, 2 ಮತ್ತು 3 (stop ಸೇರಲ್ಲ)."},
        ],
    },
    "errors": {
        "intro": "ಈ ಎರಡು errors ಕೆಲಸ ಮಾಡದ index ಬಳಸಿದಾಗ ಬರುತ್ತವೆ.",
        "examples": [
            {"title": "ಇಲ್ಲದ index ಕೇಳುವುದು", "md": "List ನಲ್ಲಿ 3 items ಇವೆ, ಹಾಗಾಗಿ indexes 0, 1 ಮತ್ತು 2. Index 3 ಇಲ್ಲ. ಕೊನೆಯ item ಗೆ `medicines[2]` ಬರೆಯಿರಿ, ಅಥವಾ ಇನ್ನೂ ಚೆನ್ನಾಗಿ, `medicines[-1]`."},
            {"title": "Index ಆಗಿ decimal number ಬಳಸುವುದು", "md": "`/` ಯಾವಾಗಲೂ float ಕೊಡುತ್ತೆ, ಹಾಗಾಗಿ `middle` 1.5, ಮತ್ತು item 1.5 ಅಂತ ಏನೂ ಇಲ್ಲ. ಪೂರ್ಣ number ಗೆ floor division ಬಳಸಿ: `middle = len(doses) // 2`."},
        ],
    },
    "mistakes": [
        {"mistake": "ಮೊದಲ item ಗೆ `medicines[1]` ಬರೆಯುವುದು", "see": "Error ಇಲ್ಲ, ಆದರೆ ಎರಡನೇ item ಸಿಗುತ್ತೆ", "fix": "Indexes 0 ಇಂದ ಶುರು: ಮೊದಲ item `medicines[0]`."},
        {"mistake": "`bp[1:3]` ನಲ್ಲಿ index 3 ಸೇರುತ್ತೆ ಅಂದುಕೊಳ್ಳುವುದು", "see": "Error ಇಲ್ಲ, ಆದರೆ slice ನಲ್ಲಿ ಅಂದುಕೊಂಡಿದ್ದಕ್ಕಿಂತ ಒಂದು item ಕಡಿಮೆ", "fix": "Stop index ಸೇರಲ್ಲ: `bp[1:4]` indexes 1, 2 ಮತ್ತು 3 ಕೊಡುತ್ತೆ."},
        {"mistake": "ದುಂಡು brackets ಬಳಸುವುದು: `medicines(0)`", "see": "TypeError: 'list' object is not callable", "fix": "Index square brackets ಒಳಗೆ ಹೋಗುತ್ತೆ: `medicines[0]`."},
        {"mistake": "Text item ನ quotes ಮರೆಯುವುದು: `[\"Paracetamol\", Ibuprofen]`", "see": "NameError: name 'Ibuprofen' is not defined", "fix": "ಪ್ರತಿ text item ಗೆ quotes ಬೇಕು: `[\"Paracetamol\", \"Ibuprofen\"]`."},
    ],
    "tasks": [
        {"title": "List ಮಾಡಿ", "md": "`\"Aspirin\"`, `\"Atorvastatin\"` ಮತ್ತು `\"Amlodipine\"` ಇದೇ ಕ್ರಮದಲ್ಲಿ ಇರುವ **drugs** ಎಂಬ list ಮಾಡಿ. List print ಮಾಡಿ, ನಂತರ ಅದರ length. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["drugs = [\"Aspirin\", \"Atorvastatin\", \"Amlodipine\"]", "print(drugs) list ತೋರಿಸುತ್ತೆ; print(len(drugs)) ಎಷ್ಟು items ಅಂತ ಹೇಳುತ್ತೆ."]},
        {"title": "ಮೊದಲ ಮತ್ತು ಕೊನೆಯ reading", "md": "ಒಬ್ಬ patient ನ temperature ಐದು ಸಲ ತೆಗೆದಿದ್ದಾರೆ. **Indexing** ಇಂದ **ಮೊದಲ** reading, ನಂತರ **ಕೊನೆಯ** reading print ಮಾಡಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["ಮೊದಲ item index 0 ನಲ್ಲಿ.", "ಕೊನೆಯ item index -1 ನಲ್ಲಿ: print(temps[-1])"]},
        {"title": "ವಾರದ ಮಧ್ಯದ slice", "md": "ಇವು 7 ದಿನದ pulse readings. **ದಿನ 3, 4 ಮತ್ತು 5** (indexes 2, 3 ಮತ್ತು 4) ರ readings ಅನ್ನು **ಒಂದೇ slice** ಇಂದ print ಮಾಡಿ. Output ನಿಖರವಾಗಿ ಹೀಗಿರಬೇಕು:",
         "hints": ["Slice ಅಂದ್ರೆ pulse[start:stop], ಮತ್ತು stop ಸೇರಲ್ಲ.", "print(pulse[2:5])"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "Amoxicillin, ಅಂದ್ರೆ **ಎರಡನೇ** item, 200 strips ಗೆ restock ಆಯಿತು. ಆದರೆ ಈ program ಮೂರನೇ item ಬದಲಾಯಿಸುತ್ತೆ. Output ನಿಖರವಾಗಿ ಹೀಗಿರುವಂತೆ ಸರಿ ಮಾಡಿ:",
         "hints": ["ಎರಡನೇ item ನ index ಯಾವುದು?", "Indexes 0 ಇಂದ ಶುರು, ಹಾಗಾಗಿ ಎರಡನೇ item stock[1]."],
         "solutionNote": "Indexes 0 ಇಂದ ಶುರು, ಹಾಗಾಗಿ ಎರಡನೇ item index 1 ನಲ್ಲಿ. stock[2] ಮೂರನೇ item ಆಗಿತ್ತು, 300."},
    ],
    "quiz": [
        {"q": "meds = [\"Aspirin\", \"Insulin\", \"Digoxin\"]\nprint(meds[1])\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "Indexes 0 ಇಂದ ಶುರು, ಹಾಗಾಗಿ meds[1] ಎರಡನೇ item, Insulin."},
        {"q": "List ನ ಮೊದಲ item ನ index ಯಾವುದು?", "why": "Python list positions ಅನ್ನು ಯಾವಾಗಲೂ 0 ಇಂದ ಎಣಿಸುತ್ತೆ."},
        {"q": "x = [10, 20, 30, 40, 50]\nprint(x[1:3])\n\nಇದು ಏನು print ಮಾಡುತ್ತೆ?", "why": "Slice indexes 1 ಮತ್ತು 2 ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ; stop index 3 ಸೇರಲ್ಲ."},
        {"q": "readings[-1] ಏನು ಕೊಡುತ್ತೆ?", "why": "Negative indexes ಕೊನೆಯಿಂದ ಎಣಿಸುತ್ತವೆ; -1 ಕೊನೆಯ item."},
        {"q": "ಒಂದು list ನಲ್ಲಿ 4 items ಇವೆ. print(items[4]) ಇಂದ ಏನಾಗುತ್ತೆ?", "why": "Indexes 0 ಇಂದ 3, ಹಾಗಾಗಿ index 4 ಇಲ್ಲವೇ ಇಲ್ಲ."},
        {"q": "Lists ಬಗ್ಗೆ ಯಾವ ಮಾತು ಸರಿ?", "why": "Lists mutable: items ಬದಲಾಯಿಸಬಹುದು, ಸೇರಿಸಬಹುದು, ತೆಗೆಯಬಹುದು."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 3.1 · Lists",
        "children": [
            {"label": "ಮಾಡುವುದು", "children": [{"label": "[a, b, c]"}, {"label": "len() ಎಣಿಸುತ್ತೆ"}, {"label": "[] ಖಾಲಿ"}]},
            {"label": "Index", "children": [{"label": "0 ಇಂದ ಶುರು"}, {"label": "-1 ಕೊನೆಯದು"}, {"label": "list[i]"}]},
            {"label": "ಬದಲಾವಣೆ", "children": [{"label": "list[i] = new"}, {"label": "Mutable"}, {"label": "Strings ಅಲ್ಲ"}]},
            {"label": "Slice", "children": [{"label": "[start:stop]"}, {"label": "Stop ಸೇರಲ್ಲ"}, {"label": "[::2] step"}]},
            {"label": "ಮೂಲಕ ಹೋಗುವುದು", "children": [{"label": "for item in list"}, {"label": "x in list"}, {"label": "ಕ್ರಮ ಉಳಿಯುತ್ತೆ"}]},
            {"label": "Errors", "children": [{"label": "IndexError: out of range"}, {"label": "TypeError: float index"}]},
        ],
    },
    "summary": [
        "**List** ಹಲವು items ಅನ್ನು, ಕ್ರಮವಾಗಿ, ಒಂದೇ variable ನಲ್ಲಿ ಇಡುತ್ತೆ: `drugs = [\"Aspirin\", \"Insulin\"]`. `len()` ಅವನ್ನು ಎಣಿಸುತ್ತೆ.",
        "**Indexing** ಒಂದು item ಆರಿಸುತ್ತೆ: ಮೊದಲದು `[0]`, ಕೊನೆಯದು `[-1]`. ಇಲ್ಲದ index **IndexError** ಕೊಡುತ್ತೆ.",
        "Lists **mutable**: `stock[1] = 60` ಒಂದು item ಬದಲಾಯಿಸುತ್ತೆ.",
        "**Slice** `list[start:stop]` ಹೊಸ list ಮಾಡುತ್ತೆ, `stop` ವರೆಗೆ ಆದರೆ ಅದನ್ನು ಸೇರಿಸದೆ; `[::2]` ಪ್ರತಿ ಎರಡನೇ item.",
        "`for item in list:` ಪ್ರತಿ item ಗೆ ಹೋಗುತ್ತೆ, ಮತ್ತು `x in list` value ಇದೆಯಾ ಅಂತ check ಮಾಡುತ್ತೆ.",
    ],
}

NARR = {
    "hi": [
        "यह program पाँच दिन की blood sugar readings एक list में रखता है, फिर उनकी position से readings निकालता है।",
        "Comment बताता है ये numbers क्या हैं: fasting blood sugar, milligrams per decilitre में।",
        "Square brackets list बनाते हैं। sugar में अब पाँच numbers हैं, उसी क्रम में जिसमें लिखे गए।",
        "sugar of zero पहली reading है। Python positions zero से गिनता है, इसलिए यह एक सौ दस है।",
        "Minus one आखिर से गिनता है, इसलिए sugar of minus one आखिरी reading है: एक सौ पाँच।",
        "Slice one to four, position एक से शुरू होकर position चार से ठीक पहले रुकता है। इससे तीन readings मिलती हैं।",
        "len list के items गिनता है: पाँच readings।",
    ],
    "hinglish": [
        "Yeh program paanch din ki blood sugar readings ek list mein rakhta hai, phir unki position se readings nikaalta hai.",
        "Comment batata hai yeh numbers kya hain: fasting blood sugar, milligrams per decilitre mein.",
        "Square brackets list banaate hain. sugar mein ab paanch numbers hain, usi kram mein jismein likhe gaye.",
        "sugar of zero pehli reading hai. Python positions zero se ginta hai, isliye yeh ek sau das hai.",
        "Minus one aakhir se ginta hai, isliye sugar of minus one aakhri reading hai: ek sau paanch.",
        "Slice one to four, position ek se shuru hokar position chaar se theek pehle rukta hai. Isse teen readings milti hain.",
        "len list ke items ginta hai: paanch readings.",
    ],
    "kn": [
        "ಈ program ಐದು ದಿನದ blood sugar readings ಅನ್ನು ಒಂದು list ನಲ್ಲಿ ಇಡುತ್ತೆ, ನಂತರ ಅವುಗಳ position ಪ್ರಕಾರ readings ತೆಗೆಯುತ್ತೆ.",
        "Comment ಈ numbers ಏನು ಅಂತ ಹೇಳುತ್ತೆ: fasting blood sugar, milligrams per decilitre ನಲ್ಲಿ.",
        "Square brackets list ಮಾಡುತ್ತವೆ. sugar ನಲ್ಲಿ ಈಗ ಐದು numbers, ಬರೆದ ಕ್ರಮದಲ್ಲೇ.",
        "sugar of zero ಮೊದಲ reading. Python positions ಅನ್ನು zero ಇಂದ ಎಣಿಸುತ್ತೆ, ಹಾಗಾಗಿ ಇದು ನೂರ ಹತ್ತು.",
        "Minus one ಕೊನೆಯಿಂದ ಎಣಿಸುತ್ತೆ, ಹಾಗಾಗಿ sugar of minus one ಕೊನೆಯ reading: ನೂರ ಐದು.",
        "Slice one to four, position ಒಂದರಿಂದ ಶುರುವಾಗಿ position ನಾಲ್ಕಕ್ಕೆ ಸ್ವಲ್ಪ ಮುಂಚೆ ನಿಲ್ಲುತ್ತೆ. ಇದರಿಂದ ಮೂರು readings ಸಿಗುತ್ತವೆ.",
        "len list ನ items ಎಣಿಸುತ್ತೆ: ಐದು readings.",
    ],
}

ANIM = {
    "hi": [
        "List sugar में पाँच readings हैं। हर reading अपनी numbered जगह पर है, और numbering zero से शुरू होती है।",
        "sugar of zero पहली जगह है: एक सौ दस।",
        "Minus one आखिर से गिनता है, इसलिए sugar of minus one आखिरी जगह है: एक सौ पाँच।",
        "Slice one to four जगह एक, दो और तीन लेता है। यह जगह चार से पहले रुक जाता है।",
    ],
    "hinglish": [
        "List sugar mein paanch readings hain. Har reading apni numbered jagah par hai, aur numbering zero se shuru hoti hai.",
        "sugar of zero pehli jagah hai: ek sau das.",
        "Minus one aakhir se ginta hai, isliye sugar of minus one aakhri jagah hai: ek sau paanch.",
        "Slice one to four jagah ek, do aur teen leta hai. Yeh jagah chaar se pehle ruk jaata hai.",
    ],
    "kn": [
        "List sugar ನಲ್ಲಿ ಐದು readings ಇವೆ. ಪ್ರತಿ reading ತನ್ನದೇ numbered ಜಾಗದಲ್ಲಿ ಇದೆ, numbering zero ಇಂದ ಶುರು.",
        "sugar of zero ಮೊದಲ ಜಾಗ: ನೂರ ಹತ್ತು.",
        "Minus one ಕೊನೆಯಿಂದ ಎಣಿಸುತ್ತೆ, ಹಾಗಾಗಿ sugar of minus one ಕೊನೆಯ ಜಾಗ: ನೂರ ಐದು.",
        "Slice one to four ಜಾಗ ಒಂದು, ಎರಡು ಮತ್ತು ಮೂರು ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ. ಜಾಗ ನಾಲ್ಕರ ಮುಂಚೆ ನಿಲ್ಲುತ್ತೆ.",
    ],
}

if __name__ == "__main__":
    build("3-1", "anim-index", T, NARR, ANIM)

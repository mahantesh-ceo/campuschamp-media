"""Lesson 1.6 translations (Hindi, Hinglish, Kannada) and voice scripts.

Run to write content/bp101t/1-6/{hi,hinglish,kn}.json and scripts/bp101t/1-6.json.
Lists keep the English order because the website merges by position.
Voices are made with Sarvam (tools/sarvam_lessons.py), which reads English words inside
Hindi and Kannada text naturally, so the voice text is the display text with small fixes.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
LESSON = "1-6"
ANIM_ID = "anim-slice"
SECTIONS = ["hook", "learn", "explanation", "walkthrough", "errors", "mistakes", "tasks",
            "quiz", "exam", "mindmap", "summary", "animations"]

C_WHOLE = "```python\ndrug = \"Paracetamol\"\nprint(drug + \" 500 mg\")\nprint(\"-\" * 12)\nprint(len(drug))\n```"
O_WHOLE = "```\nParacetamol 500 mg\n------------\n11\n```"
C_IDX = "```python\ndrug = \"Aspirin\"\nprint(drug[0])\nprint(drug[3])\nprint(drug[-1])\n```"
C_SLICE = "```python\nbatch = \"AMX-2026-0457\"\nprint(batch[0:3])\nprint(batch[4:8])\nprint(batch[-4:])\n```"
O_SLICE = "```\nAMX\n2026\n0457\n```"
C_METH = "```python\nentry = \"  amoxicillin 250mg  \"\nprint(entry.strip())\nprint(entry.strip().upper())\nprint(entry.strip().capitalize())\nprint(\"250mg\".replace(\"mg\", \" mg\"))\n```"
O_METH = "```\namoxicillin 250mg\nAMOXICILLIN 250MG\nAmoxicillin 250mg\n250 mg\n```"
C_FIND = "```python\nlabel = \"Store below 25 C. Keep away from children.\"\nprint(\"children\" in label)\nprint(label.find(\"25\"))\nprint(label.count(\"e\"))\n```"
C_SPLIT = "```python\nrecord = \"Ravi,45,Amoxicillin\"\nparts = record.split(\",\")\nprint(parts)\nprint(parts[2])\n```"

T = {}

# ======================================================================= Hindi
T["hi"] = {
    "hook": {
        "title": "गड़बड़ drug entry को साफ़ कीजिए",
        "md": "असली records अक्सर गड़बड़ होते हैं। कोई `  amoxicillin 250mg  ` type कर देता है: आगे-पीछे extra spaces, छोटा पहला अक्षर, और unit से पहले space नहीं। Clinical report में यह ऐसे print नहीं हो सकता।\n\nइस lesson के अंत तक आपका program ऐसी entries को साफ़ करेगा, batch code के हिस्से पढ़ेगा, और patient record को उसके हिस्सों में बाँटेगा।",
    },
    "learn": [
        "**+**, **\\*** और **len()** से text को जोड़ना, दोहराना और नापना",
        "**index** से एक character, और **slice** से text का एक हिस्सा कैसे निकालें",
        "**strip()**, **upper()**, **lower()**, **capitalize()** और **replace()** से text कैसे साफ़ करें",
        "**in**, **find()** और **count()** से text में कैसे खोजें, और **split()** से उसे कैसे तोड़ें",
    ],
    "explanation": [
        {"heading": "Strings: जोड़ना, दोहराना, नापना",
         "md": f"**String** quotes के अंदर लिखा text है, जैसा आपने Lesson 1.3 में देखा। तीन tools पूरी string पर काम करते हैं:\n\n{C_WHOLE}\n\nयह print करता है:\n\n{O_WHOLE}\n\n`+` दो strings जोड़ता है, `*` string को दोहराता है, और `len()` उसके characters गिनता है। Spaces भी गिने जाते हैं: `len(\"500 mg\")` है 6।"},
        {"heading": "Indexing: एक बार में एक character",
         "md": f"String के हर character का एक position number होता है, जिसे **index** कहते हैं। Python गिनती **0** से शुरू करता है, 1 से नहीं:\n\n{C_IDX}\n\nयह `A`, `i` और `n` print करता है। `\"Aspirin\"` में A index 0 पर है, s 1 पर, p 2 पर, i 3 पर, और इसी तरह n 6 पर।\n\n**Negative index** आखिर से गिनता है: `drug[-1]` आखिरी character है, `drug[-2]` उससे पहले वाला।",
         "callout": {"title": "गिनती 0 से शुरू होती है", "md": "पहला character drug[0] है। drug[1] दूसरा है।"}},
        {"heading": "Slicing: string का एक हिस्सा",
         "md": f"**Slice** string का एक हिस्सा निकालता है: `text[start:end]`। यह `start` से शुरू होकर `end` से **ठीक पहले** रुकता है।\n\nMedicine strip के batch code में अक्सर काम के हिस्से छुपे होते हैं:\n\n{C_SLICE}\n\nयह print करता है:\n\n{O_SLICE}\n\n`start` छोड़ दें तो शुरुआत से, और `end` छोड़ दें तो आखिर तक: `batch[:3]` है `AMX` और `batch[9:]` है `0457`।",
         "callout": {"title": "Slice", "md": "text[start:end] index start से लेकर index end तक के characters देता है, end को छोड़कर।"}},
        {"heading": "String methods: text साफ़ करना",
         "md": f"**Method** वह function है जो किसी value का अपना होता है। Value के बाद dot लगाकर उसे call करते हैं। ये पाँच text साफ़ करते हैं:\n\n{C_METH}\n\nयह print करता है:\n\n{O_METH}\n\n- **`strip()`** दोनों सिरों से spaces हटाता है।\n- **`upper()`** और **`lower()`** हर अक्षर को capital या small बनाते हैं।\n- **`capitalize()`** सिर्फ़ पहले अक्षर को capital बनाता है।\n- **`replace(old, new)`** हर `old` की जगह `new` रख देता है।\n\nआप इन्हें जोड़कर लिख सकते हैं, जैसे `entry.strip().upper()`। Python इन्हें बाएँ से दाएँ चलाता है।",
         "callout": {"title": "Methods नई string देते हैं", "md": "String को उसी जगह बदला नहीं जा सकता। drug.upper() नई string देता है, इसलिए उसे save कीजिए: drug = drug.upper()।"}},
        {"heading": "खोजना और तोड़ना",
         "md": f"कोई text string के अंदर है या नहीं, यह जानने के लिए **`in`** use कीजिए। यह `True` या `False` देता है:\n\n{C_FIND}\n\nयह `True`, `12` और `5` print करता है। `find()` वह index देता है जहाँ text शुरू होता है (न मिले तो `-1`), और `count()` गिनता है कि वह कितनी बार आया।\n\n**`split()`** जहाँ-जहाँ separator आए, वहाँ string को हिस्सों में तोड़ता है। एक line में save किया गया patient record अलग-अलग values बन जाता है:\n\n{C_SPLIT}\n\nयह `['Ravi', '45', 'Amoxicillin']` और फिर `Amoxicillin` print करता है। Characters की तरह हिस्सों की गिनती भी 0 से होती है। इन lists के बारे में आप Unit III में और सीखेंगे।",
         "callout": {"title": "Search case-sensitive होती है", "md": "\"aspirin\" in \"Aspirin 75 mg\" का जवाब False है। Capitals को ignore करने के लिए दोनों तरफ़ .lower() लगाकर compare कीजिए।"}},
    ],
    "walkthrough": {
        "intro": "यह program record की एक गड़बड़ drug entry को वैसे साफ़ करता है, जैसा clinical report में चाहिए।",
        "keyTerms": [
            {"meaning": "दोनों सिरों से spaces हटाओ।"},
            {"meaning": "पहले अक्षर को capital बनाओ।"},
            {"meaning": "Characters गिनो, spaces समेत।"},
            {"meaning": "पहले चार characters (एक slice)।"},
            {"meaning": "पुराने text की जगह नया text रखो।"},
        ],
    },
    "errors": {
        "intro": "ये दो errors तब आते हैं जब आप string के आखिर से आगे पहुँचते हैं, या उसे उसी जगह बदलने की कोशिश करते हैं।",
        "examples": [
            {"title": "ऐसा index माँगना जो है ही नहीं", "md": "`\"Aspirin\"` में 7 characters हैं, index 0 से 6 तक। Index 7 है ही नहीं। आखिरी character के लिए `drug[6]` या `drug[-1]` use कीजिए।"},
            {"title": "एक character बदलने की कोशिश", "md": "String को उसी जगह बदला नहीं जा सकता। इसकी जगह नई string बनाकर save कीजिए: `drug = drug.capitalize()`, या `drug = \"A\" + drug[1:]`।"},
        ],
    },
    "mistakes": [
        {"mistake": "Method call करके result save न करना, जैसे `drug.upper()` और फिर `print(drug)`", "see": "कोई error नहीं, पर text वैसा ही रहता है", "fix": "Save कीजिए: `drug = drug.upper()`।"},
        {"mistake": "Characters 1 से गिनना, जैसे पहले अक्षर के लिए `drug[1]`", "see": "कोई error नहीं, पर दूसरा अक्षर मिलता है", "fix": "पहला character `drug[0]` है।"},
        {"mistake": "Capitals मिलाए बिना खोजना, जैसे `\"aspirin\" in \"Aspirin 75 mg\"`", "see": "कोई error नहीं, पर जवाब False आता है", "fix": "एक ही case में compare कीजिए: `\"aspirin\" in label.lower()`।"},
        {"mistake": "Text और number को `+` से जोड़ना, जैसे `\"Length: \" + len(drug)`", "see": "TypeError: can only concatenate str (not \"int\") to str", "fix": "f-string use कीजिए: `f\"Length: {len(drug)}\"`।"},
    ],
    "tasks": [
        {"title": "Warning को उभारिए", "md": "Labels पर warnings capital letters में छपती हैं। Warning को capitals में print कीजिए, बिल्कुल ऐसे:", "hints": ["एक string method हर अक्षर को capital बना देता है।", "print(warning.upper())"]},
        {"title": "Extra spaces हटाइए", "md": "Drug का नाम दोनों तरफ़ spaces के साथ type हुआ था। उन्हें हटाइए, ताकि output बिल्कुल यह हो:", "hints": ["strip() दोनों सिरों से spaces हटाता है।", "print(f\"[{entry.strip()}]\")"]},
        {"title": "Batch code से साल पढ़िए", "md": "Batch code **AMX-2026-0457** में साल index 4 से 7 पर है। **Slice** use करके बिल्कुल यह print कीजिए:", "hints": ["Slice अपने end index से ठीक पहले रुकता है।", "print(\"Year:\", batch[4:8])"]},
        {"title": "Bug ढूँढिए", "md": "यह program patient record से drug print करना चाहिए, पर IndexError पर रुक जाता है। इसे ठीक कीजिए ताकि output बिल्कुल यह हो:", "hints": ["Record के कितने हिस्से हैं, और पहला index क्या है?", "हिस्से index 0, 1 और 2 पर हैं।"],
         "solutionNote": "split(\",\") तीन हिस्से देता है, जिनकी गिनती 0, 1 और 2 है। Drug तीसरा हिस्सा है, index 2 पर।"},
    ],
    "quiz": [
        {"q": "len(\"Aspirin\") क्या देता है?", "why": "\"Aspirin\" में 7 characters हैं।"},
        {"q": "drug = \"Paracetamol\"। drug[0] क्या है?", "why": "Index 0 से शुरू होते हैं, इसलिए drug[0] पहला character है।"},
        {"q": "\"Insulin\"[-1] क्या है?", "why": "Negative index आखिर से गिनता है; -1 आखिरी character है।"},
        {"q": "\"BP101T\"[2:5] क्या है?", "why": "Slice index 2, 3 और 4 लेता है, और 5 से ठीक पहले रुकता है।"},
        {"q": "\"  dose  \".strip() क्या देता है?", "why": "strip() दोनों सिरों से spaces हटाता है।"},
        {"q": "\"500,mg\".split(\",\") क्या देता है?", "why": "split(\",\") text को comma पर दो हिस्सों में तोड़ता है।"},
    ],
    "exam": {"note": "Practice के लिए important questions। University के असली questions अलग हो सकते हैं।"},
    "mindmap": {
        "label": "Lesson 1.6 · String operations",
        "children": [
            {"label": "पूरी string", "children": [{"label": "+ जोड़ता है"}, {"label": "* दोहराता है"}, {"label": "len() गिनता है"}]},
            {"label": "Index", "children": [{"label": "0 से शुरू"}, {"label": "[-1] आखिरी"}]},
            {"label": "Slice", "children": [{"label": "[start:end]"}, {"label": "end से पहले रुकता है"}, {"label": "[:3] और [9:]"}]},
            {"label": "साफ़ करना", "children": [{"label": "strip()"}, {"label": "upper() / lower()"}, {"label": "capitalize()"}, {"label": "replace(old, new)"}]},
            {"label": "खोजना और तोड़ना", "children": [{"label": "in → True/False"}, {"label": "find(), count()"}, {"label": "split(\",\")"}]},
            {"label": "Errors", "children": [{"label": "IndexError"}, {"label": "TypeError: बदल नहीं सकते"}]},
        ],
    },
    "summary": [
        "**`+`** strings जोड़ता है, **`*`** उन्हें दोहराता है और **`len()`** उनके characters गिनता है, spaces समेत।",
        "**Index** एक character चुनता है; गिनती **0** से शुरू होती है, और **-1** आखिरी character है।",
        "**Slice** `text[start:end]` एक हिस्सा लेता है, और `end` से **ठीक पहले** रुकता है।",
        "**strip()**, **upper()**, **lower()**, **capitalize()** और **replace()** text साफ़ करते हैं। ये **नई** string देते हैं, इसलिए result save कीजिए।",
        "**in**, **find()** और **count()** text में खोजते हैं; **split()** line को हिस्सों में तोड़ता है, जिनकी गिनती 0 से होती है।",
    ],
}

# ==================================================================== Hinglish
T["hinglish"] = {
    "hook": {
        "title": "Gadbad drug entry ko saaf kijiye",
        "md": "Asli records aksar gadbad hote hain. Koi `  amoxicillin 250mg  ` type kar deta hai: aage-peeche extra spaces, chhota pehla akshar, aur unit se pehle space nahi. Clinical report mein yeh aise print nahi ho sakta.\n\nIs lesson ke ant tak aapka program aisi entries ko saaf karega, batch code ke hisse padhega, aur patient record ko uske hisson mein baantega.",
    },
    "learn": [
        "**+**, **\\*** aur **len()** se text ko jodna, dohrana aur naapna",
        "**index** se ek character, aur **slice** se text ka ek hissa kaise nikaalein",
        "**strip()**, **upper()**, **lower()**, **capitalize()** aur **replace()** se text kaise saaf karein",
        "**in**, **find()** aur **count()** se text mein kaise khojein, aur **split()** se use kaise todein",
    ],
    "explanation": [
        {"heading": "Strings: jodna, dohrana, naapna",
         "md": f"**String** quotes ke andar likha text hai, jaisa aapne Lesson 1.3 mein dekha. Teen tools poori string par kaam karte hain:\n\n{C_WHOLE}\n\nYeh print karta hai:\n\n{O_WHOLE}\n\n`+` do strings jodta hai, `*` string ko dohrata hai, aur `len()` uske characters ginta hai. Spaces bhi gine jaate hain: `len(\"500 mg\")` hai 6."},
        {"heading": "Indexing: ek baar mein ek character",
         "md": f"String ke har character ka ek position number hota hai, jise **index** kehte hain. Python ginti **0** se shuru karta hai, 1 se nahi:\n\n{C_IDX}\n\nYeh `A`, `i` aur `n` print karta hai. `\"Aspirin\"` mein A index 0 par hai, s 1 par, p 2 par, i 3 par, aur isi tarah n 6 par.\n\n**Negative index** aakhir se ginta hai: `drug[-1]` aakhri character hai, `drug[-2]` usse pehle wala.",
         "callout": {"title": "Ginti 0 se shuru hoti hai", "md": "Pehla character drug[0] hai. drug[1] doosra hai."}},
        {"heading": "Slicing: string ka ek hissa",
         "md": f"**Slice** string ka ek hissa nikaalta hai: `text[start:end]`. Yeh `start` se shuru hokar `end` se **theek pehle** rukta hai.\n\nMedicine strip ke batch code mein aksar kaam ke hisse chhupe hote hain:\n\n{C_SLICE}\n\nYeh print karta hai:\n\n{O_SLICE}\n\n`start` chhod dein to shuruaat se, aur `end` chhod dein to aakhir tak: `batch[:3]` hai `AMX` aur `batch[9:]` hai `0457`.",
         "callout": {"title": "Slice", "md": "text[start:end] index start se lekar index end tak ke characters deta hai, end ko chhodkar."}},
        {"heading": "String methods: text saaf karna",
         "md": f"**Method** woh function hai jo kisi value ka apna hota hai. Value ke baad dot lagakar use call karte hain. Yeh paanch text saaf karte hain:\n\n{C_METH}\n\nYeh print karta hai:\n\n{O_METH}\n\n- **`strip()`** dono siron se spaces hatata hai.\n- **`upper()`** aur **`lower()`** har akshar ko capital ya small banate hain.\n- **`capitalize()`** sirf pehle akshar ko capital banata hai.\n- **`replace(old, new)`** har `old` ki jagah `new` rakh deta hai.\n\nAap inhe jodkar likh sakte hain, jaise `entry.strip().upper()`. Python inhe baayein se daayein chalaata hai.",
         "callout": {"title": "Methods nayi string dete hain", "md": "String ko usi jagah badla nahi ja sakta. drug.upper() nayi string deta hai, isliye use save kijiye: drug = drug.upper()."}},
        {"heading": "Khojna aur todna",
         "md": f"Koi text string ke andar hai ya nahi, yeh jaanne ke liye **`in`** use kijiye. Yeh `True` ya `False` deta hai:\n\n{C_FIND}\n\nYeh `True`, `12` aur `5` print karta hai. `find()` woh index deta hai jahan text shuru hota hai (na mile to `-1`), aur `count()` ginta hai ki woh kitni baar aaya.\n\n**`split()`** jahan-jahan separator aaye, wahan string ko hisson mein todta hai. Ek line mein save kiya gaya patient record alag-alag values ban jaata hai:\n\n{C_SPLIT}\n\nYeh `['Ravi', '45', 'Amoxicillin']` aur phir `Amoxicillin` print karta hai. Characters ki tarah hisson ki ginti bhi 0 se hoti hai. In lists ke baare mein aap Unit III mein aur seekhenge.",
         "callout": {"title": "Search case-sensitive hoti hai", "md": "\"aspirin\" in \"Aspirin 75 mg\" ka jawaab False hai. Capitals ko ignore karne ke liye dono taraf .lower() lagaakar compare kijiye."}},
    ],
    "walkthrough": {
        "intro": "Yeh program record ki ek gadbad drug entry ko waise saaf karta hai, jaisa clinical report mein chahiye.",
        "keyTerms": [
            {"meaning": "Dono siron se spaces hatao."},
            {"meaning": "Pehle akshar ko capital banao."},
            {"meaning": "Characters gino, spaces samet."},
            {"meaning": "Pehle chaar characters (ek slice)."},
            {"meaning": "Purane text ki jagah naya text rakho."},
        ],
    },
    "errors": {
        "intro": "Yeh do errors tab aate hain jab aap string ke aakhir se aage pahunchte hain, ya use usi jagah badalne ki koshish karte hain.",
        "examples": [
            {"title": "Aisa index maangna jo hai hi nahi", "md": "`\"Aspirin\"` mein 7 characters hain, index 0 se 6 tak. Index 7 hai hi nahi. Aakhri character ke liye `drug[6]` ya `drug[-1]` use kijiye."},
            {"title": "Ek character badalne ki koshish", "md": "String ko usi jagah badla nahi ja sakta. Iski jagah nayi string banakar save kijiye: `drug = drug.capitalize()`, ya `drug = \"A\" + drug[1:]`."},
        ],
    },
    "mistakes": [
        {"mistake": "Method call karke result save na karna, jaise `drug.upper()` aur phir `print(drug)`", "see": "Koi error nahi, par text waisa hi rehta hai", "fix": "Save kijiye: `drug = drug.upper()`."},
        {"mistake": "Characters 1 se ginna, jaise pehle akshar ke liye `drug[1]`", "see": "Koi error nahi, par doosra akshar milta hai", "fix": "Pehla character `drug[0]` hai."},
        {"mistake": "Capitals milaaye bina khojna, jaise `\"aspirin\" in \"Aspirin 75 mg\"`", "see": "Koi error nahi, par jawaab False aata hai", "fix": "Ek hi case mein compare kijiye: `\"aspirin\" in label.lower()`."},
        {"mistake": "Text aur number ko `+` se jodna, jaise `\"Length: \" + len(drug)`", "see": "TypeError: can only concatenate str (not \"int\") to str", "fix": "f-string use kijiye: `f\"Length: {len(drug)}\"`."},
    ],
    "tasks": [
        {"title": "Warning ko ubhaariye", "md": "Labels par warnings capital letters mein chhapti hain. Warning ko capitals mein print kijiye, bilkul aise:", "hints": ["Ek string method har akshar ko capital bana deta hai.", "print(warning.upper())"]},
        {"title": "Extra spaces hataaiye", "md": "Drug ka naam dono taraf spaces ke saath type hua tha. Unhe hataaiye, taaki output bilkul yeh ho:", "hints": ["strip() dono siron se spaces hatata hai.", "print(f\"[{entry.strip()}]\")"]},
        {"title": "Batch code se saal padhiye", "md": "Batch code **AMX-2026-0457** mein saal index 4 se 7 par hai. **Slice** use karke bilkul yeh print kijiye:", "hints": ["Slice apne end index se theek pehle rukta hai.", "print(\"Year:\", batch[4:8])"]},
        {"title": "Bug dhoondhiye", "md": "Yeh program patient record se drug print karna chahiye, par IndexError par ruk jaata hai. Ise theek kijiye taaki output bilkul yeh ho:", "hints": ["Record ke kitne hisse hain, aur pehla index kya hai?", "Hisse index 0, 1 aur 2 par hain."],
         "solutionNote": "split(\",\") teen hisse deta hai, jinki ginti 0, 1 aur 2 hai. Drug teesra hissa hai, index 2 par."},
    ],
    "quiz": [
        {"q": "len(\"Aspirin\") kya deta hai?", "why": "\"Aspirin\" mein 7 characters hain."},
        {"q": "drug = \"Paracetamol\". drug[0] kya hai?", "why": "Index 0 se shuru hote hain, isliye drug[0] pehla character hai."},
        {"q": "\"Insulin\"[-1] kya hai?", "why": "Negative index aakhir se ginta hai; -1 aakhri character hai."},
        {"q": "\"BP101T\"[2:5] kya hai?", "why": "Slice index 2, 3 aur 4 leta hai, aur 5 se theek pehle rukta hai."},
        {"q": "\"  dose  \".strip() kya deta hai?", "why": "strip() dono siron se spaces hatata hai."},
        {"q": "\"500,mg\".split(\",\") kya deta hai?", "why": "split(\",\") text ko comma par do hisson mein todta hai."},
    ],
    "exam": {"note": "Practice ke liye important questions. University ke asli questions alag ho sakte hain."},
    "mindmap": {
        "label": "Lesson 1.6 · String operations",
        "children": [
            {"label": "Poori string", "children": [{"label": "+ jodta hai"}, {"label": "* dohrata hai"}, {"label": "len() ginta hai"}]},
            {"label": "Index", "children": [{"label": "0 se shuru"}, {"label": "[-1] aakhri"}]},
            {"label": "Slice", "children": [{"label": "[start:end]"}, {"label": "end se pehle rukta hai"}, {"label": "[:3] aur [9:]"}]},
            {"label": "Saaf karna", "children": [{"label": "strip()"}, {"label": "upper() / lower()"}, {"label": "capitalize()"}, {"label": "replace(old, new)"}]},
            {"label": "Khojna aur todna", "children": [{"label": "in → True/False"}, {"label": "find(), count()"}, {"label": "split(\",\")"}]},
            {"label": "Errors", "children": [{"label": "IndexError"}, {"label": "TypeError: badal nahi sakte"}]},
        ],
    },
    "summary": [
        "**`+`** strings jodta hai, **`*`** unhe dohrata hai aur **`len()`** unke characters ginta hai, spaces samet.",
        "**Index** ek character chunta hai; ginti **0** se shuru hoti hai, aur **-1** aakhri character hai.",
        "**Slice** `text[start:end]` ek hissa leta hai, aur `end` se **theek pehle** rukta hai.",
        "**strip()**, **upper()**, **lower()**, **capitalize()** aur **replace()** text saaf karte hain. Yeh **nayi** string dete hain, isliye result save kijiye.",
        "**in**, **find()** aur **count()** text mein khojte hain; **split()** line ko hisson mein todta hai, jinki ginti 0 se hoti hai.",
    ],
}

# ===================================================================== Kannada
T["kn"] = {
    "hook": {
        "title": "ಗೊಂದಲದ drug entry ಅನ್ನು ಸರಿ ಮಾಡಿ",
        "md": "ನಿಜವಾದ records ಹೆಚ್ಚಾಗಿ ಗೊಂದಲವಾಗಿರುತ್ತೆ. ಯಾರೋ `  amoxicillin 250mg  ` ಅಂತ type ಮಾಡ್ತಾರೆ: ಮುಂದೆ-ಹಿಂದೆ extra spaces, ಚಿಕ್ಕ ಮೊದಲ ಅಕ್ಷರ, unit ಮುಂಚೆ space ಇಲ್ಲ. Clinical report ನಲ್ಲಿ ಇದನ್ನು ಹೀಗೇ print ಮಾಡೋಕೆ ಆಗಲ್ಲ.\n\nಈ lesson ಮುಗಿಯುವಷ್ಟರಲ್ಲಿ, ನಿಮ್ಮ program ಇಂಥ entries ಅನ್ನು ಸರಿ ಮಾಡುತ್ತೆ, batch code ನ ಭಾಗಗಳನ್ನು ಓದುತ್ತೆ, ಮತ್ತು patient record ಅನ್ನು ಅದರ ಭಾಗಗಳಾಗಿ ಒಡೆಯುತ್ತೆ.",
    },
    "learn": [
        "**+**, **\\*** ಮತ್ತು **len()** ಇಂದ text ಅನ್ನು ಸೇರಿಸೋದು, ಪುನರಾವರ್ತಿಸೋದು ಮತ್ತು ಅಳೆಯೋದು",
        "**index** ಇಂದ ಒಂದು character, ಮತ್ತು **slice** ಇಂದ text ನ ಒಂದು ಭಾಗ ಹೇಗೆ ತೆಗೆಯೋದು",
        "**strip()**, **upper()**, **lower()**, **capitalize()** ಮತ್ತು **replace()** ಇಂದ text ಅನ್ನು ಹೇಗೆ ಸರಿ ಮಾಡೋದು",
        "**in**, **find()** ಮತ್ತು **count()** ಇಂದ text ನಲ್ಲಿ ಹೇಗೆ ಹುಡುಕೋದು, ಮತ್ತು **split()** ಇಂದ ಅದನ್ನು ಹೇಗೆ ಒಡೆಯೋದು",
    ],
    "explanation": [
        {"heading": "Strings: ಸೇರಿಸೋದು, ಪುನರಾವರ್ತಿಸೋದು, ಅಳೆಯೋದು",
         "md": f"**String** ಅಂದ್ರೆ quotes ಒಳಗೆ ಬರೆದ text, Lesson 1.3 ನಲ್ಲಿ ನೋಡಿದ ಹಾಗೆ. ಮೂರು tools ಪೂರ್ತಿ string ಮೇಲೆ ಕೆಲಸ ಮಾಡುತ್ತವೆ:\n\n{C_WHOLE}\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n{O_WHOLE}\n\n`+` ಎರಡು strings ಸೇರಿಸುತ್ತೆ, `*` string ಅನ್ನು ಪುನರಾವರ್ತಿಸುತ್ತೆ, ಮತ್ತು `len()` ಅದರ characters ಎಣಿಸುತ್ತೆ. Spaces ಕೂಡ ಎಣಿಕೆಗೆ ಬರುತ್ತವೆ: `len(\"500 mg\")` ಅಂದ್ರೆ 6."},
        {"heading": "Indexing: ಒಂದು ಸಲಕ್ಕೆ ಒಂದು character",
         "md": f"String ನ ಪ್ರತಿ character ಗೂ ಒಂದು position number ಇರುತ್ತೆ, ಅದನ್ನು **index** ಅಂತಾರೆ. Python ಎಣಿಕೆಯನ್ನು **0** ಇಂದ ಶುರು ಮಾಡುತ್ತೆ, 1 ಇಂದ ಅಲ್ಲ:\n\n{C_IDX}\n\nಇದು `A`, `i` ಮತ್ತು `n` print ಮಾಡುತ್ತೆ. `\"Aspirin\"` ನಲ್ಲಿ A index 0 ನಲ್ಲಿ, s 1 ನಲ್ಲಿ, p 2 ನಲ್ಲಿ, i 3 ನಲ್ಲಿ, ಹೀಗೇ n 6 ನಲ್ಲಿ ಇದೆ.\n\n**Negative index** ಕೊನೆಯಿಂದ ಎಣಿಸುತ್ತೆ: `drug[-1]` ಕೊನೆಯ character, `drug[-2]` ಅದರ ಹಿಂದಿನದು.",
         "callout": {"title": "ಎಣಿಕೆ 0 ಇಂದ ಶುರು", "md": "ಮೊದಲ character drug[0]. drug[1] ಎರಡನೆಯದು."}},
        {"heading": "Slicing: string ನ ಒಂದು ಭಾಗ",
         "md": f"**Slice** string ನ ಒಂದು ಭಾಗ ತೆಗೆಯುತ್ತೆ: `text[start:end]`. ಇದು `start` ಇಂದ ಶುರು ಆಗಿ, `end` ಗೆ **ಸ್ವಲ್ಪ ಮುಂಚೆ** ನಿಲ್ಲುತ್ತೆ.\n\nMedicine strip ನ batch code ನಲ್ಲಿ ಉಪಯೋಗದ ಭಾಗಗಳು ಅಡಗಿರುತ್ತವೆ:\n\n{C_SLICE}\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n{O_SLICE}\n\n`start` ಬಿಟ್ರೆ ಶುರುವಿನಿಂದ, `end` ಬಿಟ್ರೆ ಕೊನೆಯವರೆಗೆ: `batch[:3]` ಅಂದ್ರೆ `AMX`, `batch[9:]` ಅಂದ್ರೆ `0457`.",
         "callout": {"title": "Slice", "md": "text[start:end] index start ಇಂದ index end ವರೆಗಿನ characters ಕೊಡುತ್ತೆ, end ಅನ್ನು ಬಿಟ್ಟು."}},
        {"heading": "String methods: text ಸರಿ ಮಾಡೋದು",
         "md": f"**Method** ಅಂದ್ರೆ ಒಂದು value ಗೆ ಸೇರಿದ function. Value ನಂತರ dot ಹಾಕಿ ಅದನ್ನು call ಮಾಡುತ್ತೇವೆ. ಈ ಐದು text ಸರಿ ಮಾಡುತ್ತವೆ:\n\n{C_METH}\n\nಇದು print ಮಾಡುತ್ತೆ:\n\n{O_METH}\n\n- **`strip()`** ಎರಡೂ ತುದಿಗಳಿಂದ spaces ತೆಗೆಯುತ್ತೆ.\n- **`upper()`** ಮತ್ತು **`lower()`** ಪ್ರತಿ ಅಕ್ಷರವನ್ನು capital ಅಥವಾ small ಮಾಡುತ್ತವೆ.\n- **`capitalize()`** ಮೊದಲ ಅಕ್ಷರವನ್ನು ಮಾತ್ರ capital ಮಾಡುತ್ತೆ.\n- **`replace(old, new)`** ಪ್ರತಿ `old` ಬದಲು `new` ಹಾಕುತ್ತೆ.\n\nಇವನ್ನು ಸೇರಿಸಿ ಬರೆಯಬಹುದು, ಉದಾ: `entry.strip().upper()`. Python ಇವನ್ನು ಎಡದಿಂದ ಬಲಕ್ಕೆ run ಮಾಡುತ್ತೆ.",
         "callout": {"title": "Methods ಹೊಸ string ಕೊಡುತ್ತವೆ", "md": "String ಅನ್ನು ಅದೇ ಜಾಗದಲ್ಲಿ ಬದಲಾಯಿಸೋಕೆ ಆಗಲ್ಲ. drug.upper() ಹೊಸ string ಕೊಡುತ್ತೆ, ಅದಕ್ಕೇ ಅದನ್ನು save ಮಾಡಿ: drug = drug.upper()."}},
        {"heading": "ಹುಡುಕೋದು ಮತ್ತು ಒಡೆಯೋದು",
         "md": f"ಯಾವುದಾದರೂ text string ಒಳಗೆ ಇದೆಯಾ ಅಂತ ತಿಳಿಯೋಕೆ **`in`** ಬಳಸಿ. ಇದು `True` ಅಥವಾ `False` ಕೊಡುತ್ತೆ:\n\n{C_FIND}\n\nಇದು `True`, `12` ಮತ್ತು `5` print ಮಾಡುತ್ತೆ. `find()` text ಶುರು ಆಗುವ index ಕೊಡುತ್ತೆ (ಸಿಗದಿದ್ರೆ `-1`), ಮತ್ತು `count()` ಅದು ಎಷ್ಟು ಸಲ ಬಂದಿದೆ ಅಂತ ಎಣಿಸುತ್ತೆ.\n\n**`split()`** separator ಬಂದಲ್ಲೆಲ್ಲಾ string ಅನ್ನು ಭಾಗಗಳಾಗಿ ಒಡೆಯುತ್ತೆ. ಒಂದೇ line ನಲ್ಲಿ save ಮಾಡಿದ patient record ಬೇರೆ-ಬೇರೆ values ಆಗುತ್ತೆ:\n\n{C_SPLIT}\n\nಇದು `['Ravi', '45', 'Amoxicillin']` ಮತ್ತು ನಂತರ `Amoxicillin` print ಮಾಡುತ್ತೆ. Characters ತರಹಾನೇ ಭಾಗಗಳ ಎಣಿಕೆಯೂ 0 ಇಂದ. ಈ lists ಬಗ್ಗೆ Unit III ನಲ್ಲಿ ಇನ್ನೂ ಕಲಿಯುತ್ತೀರಿ.",
         "callout": {"title": "ಹುಡುಕಾಟ case-sensitive", "md": "\"aspirin\" in \"Aspirin 75 mg\" ಉತ್ತರ False. Capitals ಬಿಟ್ಟು ಹೋಲಿಸಲು ಎರಡೂ ಕಡೆ .lower() ಹಾಕಿ compare ಮಾಡಿ."}},
    ],
    "walkthrough": {
        "intro": "ಈ program record ನ ಒಂದು ಗೊಂದಲದ drug entry ಅನ್ನು clinical report ಗೆ ಬೇಕಾದ ಹಾಗೆ ಸರಿ ಮಾಡುತ್ತೆ.",
        "keyTerms": [
            {"meaning": "ಎರಡೂ ತುದಿಗಳಿಂದ spaces ತೆಗೆ."},
            {"meaning": "ಮೊದಲ ಅಕ್ಷರವನ್ನು capital ಮಾಡು."},
            {"meaning": "Characters ಎಣಿಸು, spaces ಸೇರಿ."},
            {"meaning": "ಮೊದಲ ನಾಲ್ಕು characters (ಒಂದು slice)."},
            {"meaning": "ಹಳೆಯ text ಬದಲು ಹೊಸ text ಹಾಕು."},
        ],
    },
    "errors": {
        "intro": "String ನ ಕೊನೆಯನ್ನು ದಾಟಿ ಹೋದಾಗ, ಅಥವಾ ಅದನ್ನು ಅದೇ ಜಾಗದಲ್ಲಿ ಬದಲಾಯಿಸೋಕೆ ಪ್ರಯತ್ನಿಸಿದಾಗ ಈ ಎರಡು errors ಬರುತ್ತವೆ.",
        "examples": [
            {"title": "ಇಲ್ಲದ index ಕೇಳೋದು", "md": "`\"Aspirin\"` ನಲ್ಲಿ 7 characters ಇವೆ, index 0 ಇಂದ 6 ವರೆಗೆ. Index 7 ಇಲ್ಲವೇ ಇಲ್ಲ. ಕೊನೆಯ character ಗೆ `drug[6]` ಅಥವಾ `drug[-1]` ಬಳಸಿ."},
            {"title": "ಒಂದು character ಬದಲಾಯಿಸೋಕೆ ಪ್ರಯತ್ನ", "md": "String ಅನ್ನು ಅದೇ ಜಾಗದಲ್ಲಿ ಬದಲಾಯಿಸೋಕೆ ಆಗಲ್ಲ. ಅದರ ಬದಲು ಹೊಸ string ಮಾಡಿ save ಮಾಡಿ: `drug = drug.capitalize()`, ಅಥವಾ `drug = \"A\" + drug[1:]`."},
        ],
    },
    "mistakes": [
        {"mistake": "Method call ಮಾಡಿ result save ಮಾಡದಿರೋದು, ಉದಾ: `drug.upper()` ಆಮೇಲೆ `print(drug)`", "see": "Error ಇಲ್ಲ, ಆದ್ರೆ text ಹಾಗೇ ಇರುತ್ತೆ", "fix": "Save ಮಾಡಿ: `drug = drug.upper()`."},
        {"mistake": "Characters ಅನ್ನು 1 ಇಂದ ಎಣಿಸೋದು, ಉದಾ: ಮೊದಲ ಅಕ್ಷರಕ್ಕೆ `drug[1]`", "see": "Error ಇಲ್ಲ, ಆದ್ರೆ ಎರಡನೇ ಅಕ್ಷರ ಸಿಗುತ್ತೆ", "fix": "ಮೊದಲ character `drug[0]`."},
        {"mistake": "Capitals ಹೊಂದಿಸದೆ ಹುಡುಕೋದು, ಉದಾ: `\"aspirin\" in \"Aspirin 75 mg\"`", "see": "Error ಇಲ್ಲ, ಆದ್ರೆ ಉತ್ತರ False", "fix": "ಒಂದೇ case ನಲ್ಲಿ compare ಮಾಡಿ: `\"aspirin\" in label.lower()`."},
        {"mistake": "Text ಮತ್ತು number ಅನ್ನು `+` ಇಂದ ಸೇರಿಸೋದು, ಉದಾ: `\"Length: \" + len(drug)`", "see": "TypeError: can only concatenate str (not \"int\") to str", "fix": "f-string ಬಳಸಿ: `f\"Length: {len(drug)}\"`."},
    ],
    "tasks": [
        {"title": "Warning ಎದ್ದು ಕಾಣಿಸಲಿ", "md": "Labels ನಲ್ಲಿ warnings capital letters ನಲ್ಲಿ ಇರುತ್ತವೆ. Warning ಅನ್ನು capitals ನಲ್ಲಿ print ಮಾಡಿ, ಹೀಗೇ:", "hints": ["ಒಂದು string method ಪ್ರತಿ ಅಕ್ಷರವನ್ನೂ capital ಮಾಡುತ್ತೆ.", "print(warning.upper())"]},
        {"title": "Extra spaces ತೆಗೆಯಿರಿ", "md": "Drug ಹೆಸರು ಎರಡೂ ಕಡೆ spaces ಜೊತೆ type ಆಗಿತ್ತು. ಅವನ್ನು ತೆಗೆಯಿರಿ, output ಹೀಗೇ ಇರಬೇಕು:", "hints": ["strip() ಎರಡೂ ತುದಿಗಳಿಂದ spaces ತೆಗೆಯುತ್ತೆ.", "print(f\"[{entry.strip()}]\")"]},
        {"title": "Batch code ಇಂದ ವರ್ಷ ಓದಿ", "md": "Batch code **AMX-2026-0457** ನಲ್ಲಿ ವರ್ಷ index 4 ಇಂದ 7 ರಲ್ಲಿ ಇದೆ. **Slice** ಬಳಸಿ ಹೀಗೇ print ಮಾಡಿ:", "hints": ["Slice ತನ್ನ end index ಗೆ ಸ್ವಲ್ಪ ಮುಂಚೆ ನಿಲ್ಲುತ್ತೆ.", "print(\"Year:\", batch[4:8])"]},
        {"title": "Bug ಹುಡುಕಿ", "md": "ಈ program patient record ಇಂದ drug print ಮಾಡಬೇಕು, ಆದ್ರೆ IndexError ನಲ್ಲಿ ನಿಂತುಬಿಡುತ್ತೆ. Output ಹೀಗೇ ಬರುವ ಹಾಗೆ ಸರಿ ಮಾಡಿ:", "hints": ["Record ನಲ್ಲಿ ಎಷ್ಟು ಭಾಗಗಳಿವೆ, ಮತ್ತು ಮೊದಲ index ಯಾವುದು?", "ಭಾಗಗಳು index 0, 1 ಮತ್ತು 2 ರಲ್ಲಿ ಇವೆ."],
         "solutionNote": "split(\",\") ಮೂರು ಭಾಗಗಳನ್ನು ಕೊಡುತ್ತೆ, 0, 1 ಮತ್ತು 2 ಅಂತ ಎಣಿಕೆ. Drug ಮೂರನೇ ಭಾಗ, index 2 ರಲ್ಲಿ."},
    ],
    "quiz": [
        {"q": "len(\"Aspirin\") ಏನು ಕೊಡುತ್ತೆ?", "why": "\"Aspirin\" ನಲ್ಲಿ 7 characters ಇವೆ."},
        {"q": "drug = \"Paracetamol\". drug[0] ಏನು?", "why": "Index 0 ಇಂದ ಶುರು, ಅದಕ್ಕೇ drug[0] ಮೊದಲ character."},
        {"q": "\"Insulin\"[-1] ಏನು?", "why": "Negative index ಕೊನೆಯಿಂದ ಎಣಿಸುತ್ತೆ; -1 ಕೊನೆಯ character."},
        {"q": "\"BP101T\"[2:5] ಏನು?", "why": "Slice index 2, 3 ಮತ್ತು 4 ತೆಗೆದುಕೊಂಡು, 5 ಗೆ ಮುಂಚೆ ನಿಲ್ಲುತ್ತೆ."},
        {"q": "\"  dose  \".strip() ಏನು ಕೊಡುತ್ತೆ?", "why": "strip() ಎರಡೂ ತುದಿಗಳಿಂದ spaces ತೆಗೆಯುತ್ತೆ."},
        {"q": "\"500,mg\".split(\",\") ಏನು ಕೊಡುತ್ತೆ?", "why": "split(\",\") text ಅನ್ನು comma ಬಳಿ ಎರಡು ಭಾಗಗಳಾಗಿ ಒಡೆಯುತ್ತೆ."},
    ],
    "exam": {"note": "Practice ಗಾಗಿ important questions. University ನ ನಿಜವಾದ questions ಬೇರೆ ಇರಬಹುದು."},
    "mindmap": {
        "label": "Lesson 1.6 · String operations",
        "children": [
            {"label": "ಪೂರ್ತಿ string", "children": [{"label": "+ ಸೇರಿಸುತ್ತೆ"}, {"label": "* ಪುನರಾವರ್ತಿಸುತ್ತೆ"}, {"label": "len() ಎಣಿಸುತ್ತೆ"}]},
            {"label": "Index", "children": [{"label": "0 ಇಂದ ಶುರು"}, {"label": "[-1] ಕೊನೆಯದು"}]},
            {"label": "Slice", "children": [{"label": "[start:end]"}, {"label": "end ಗೆ ಮುಂಚೆ ನಿಲ್ಲುತ್ತೆ"}, {"label": "[:3] ಮತ್ತು [9:]"}]},
            {"label": "ಸರಿ ಮಾಡೋದು", "children": [{"label": "strip()"}, {"label": "upper() / lower()"}, {"label": "capitalize()"}, {"label": "replace(old, new)"}]},
            {"label": "ಹುಡುಕು ಮತ್ತು ಒಡೆ", "children": [{"label": "in → True/False"}, {"label": "find(), count()"}, {"label": "split(\",\")"}]},
            {"label": "Errors", "children": [{"label": "IndexError"}, {"label": "TypeError: ಬದಲಾಯಿಸಲು ಆಗಲ್ಲ"}]},
        ],
    },
    "summary": [
        "**`+`** strings ಸೇರಿಸುತ್ತೆ, **`*`** ಅವನ್ನು ಪುನರಾವರ್ತಿಸುತ್ತೆ ಮತ್ತು **`len()`** characters ಎಣಿಸುತ್ತೆ, spaces ಸೇರಿ.",
        "**Index** ಒಂದು character ಆರಿಸುತ್ತೆ; ಎಣಿಕೆ **0** ಇಂದ ಶುರು, ಮತ್ತು **-1** ಕೊನೆಯ character.",
        "**Slice** `text[start:end]` ಒಂದು ಭಾಗ ತೆಗೆಯುತ್ತೆ, `end` ಗೆ **ಸ್ವಲ್ಪ ಮುಂಚೆ** ನಿಲ್ಲುತ್ತೆ.",
        "**strip()**, **upper()**, **lower()**, **capitalize()** ಮತ್ತು **replace()** text ಸರಿ ಮಾಡುತ್ತವೆ. ಇವು **ಹೊಸ** string ಕೊಡುತ್ತವೆ, ಅದಕ್ಕೇ result save ಮಾಡಿ.",
        "**in**, **find()** ಮತ್ತು **count()** text ನಲ್ಲಿ ಹುಡುಕುತ್ತವೆ; **split()** line ಅನ್ನು ಭಾಗಗಳಾಗಿ ಒಡೆಯುತ್ತೆ, ಎಣಿಕೆ 0 ಇಂದ.",
    ],
}

# Walkthrough narration, one line per step (same order as English)
NARR = {
    "hi": [
        "यह program एक गड़बड़ drug entry लेता है और उसे एक-एक string tool से साफ़ करता है।",
        "Comment बताता है कि program क्या करता है।",
        "Entry के दोनों सिरों पर extra spaces हैं, और पहला अक्षर छोटा है। Variables panel देखिए: spaces quotes के अंदर हैं।",
        "strip दोनों सिरों से spaces हटाता है। फिर capitalize पहले अक्षर को capital बनाता है। साफ़ text drug में save हो जाता है।",
        "print साफ़ entry दिखाता है।",
        "len हर character गिनता है, बीच वाले space समेत। कुल सत्रह।",
        "Slice पहले चार characters लेता है, A M O X, और upper उन्हें capitals बना देता है। Label के लिए यह एक छोटा code है।",
        "replace, दो सौ पचास M G की जगह दो सौ पचास, space, M G रखता है। ध्यान दीजिए, drug खुद नहीं बदला: replace ने नई string दी।",
    ],
    "hinglish": [
        "Yeh program ek gadbad drug entry leta hai aur use ek-ek string tool se saaf karta hai.",
        "Comment batata hai ki program kya karta hai.",
        "Entry ke dono siron par extra spaces hain, aur pehla akshar chhota hai. Variables panel dekhiye: spaces quotes ke andar hain.",
        "strip dono siron se spaces hatata hai. Phir capitalize pehle akshar ko capital banata hai. Saaf text drug mein save ho jaata hai.",
        "print saaf entry dikhata hai.",
        "len har character ginta hai, beech wale space samet. Kul satrah.",
        "Slice pehle chaar characters leta hai, A M O X, aur upper unhe capitals bana deta hai. Label ke liye yeh ek chhota code hai.",
        "replace, do sau pachaas M G ki jagah do sau pachaas, space, M G rakhta hai. Dhyaan dijiye, drug khud nahi badla: replace ne nayi string di.",
    ],
    "kn": [
        "ಈ program ಒಂದು ಗೊಂದಲದ drug entry ತೆಗೆದುಕೊಂಡು, ಒಂದೊಂದೇ string tool ಇಂದ ಅದನ್ನು ಸರಿ ಮಾಡುತ್ತೆ.",
        "Comment ಈ program ಏನು ಮಾಡುತ್ತೆ ಅಂತ ಹೇಳುತ್ತೆ.",
        "Entry ನ ಎರಡೂ ತುದಿಗಳಲ್ಲಿ extra spaces ಇವೆ, ಮತ್ತು ಮೊದಲ ಅಕ್ಷರ ಚಿಕ್ಕದು. Variables panel ನೋಡಿ: spaces quotes ಒಳಗೆ ಇವೆ.",
        "strip ಎರಡೂ ತುದಿಗಳಿಂದ spaces ತೆಗೆಯುತ್ತೆ. ಆಮೇಲೆ capitalize ಮೊದಲ ಅಕ್ಷರವನ್ನು capital ಮಾಡುತ್ತೆ. ಸರಿಯಾದ text drug ನಲ್ಲಿ save ಆಗುತ್ತೆ.",
        "print ಸರಿಯಾದ entry ತೋರಿಸುತ್ತೆ.",
        "len ಪ್ರತಿ character ಎಣಿಸುತ್ತೆ, ಮಧ್ಯದ space ಸೇರಿ. ಒಟ್ಟು ಹದಿನೇಳು.",
        "Slice ಮೊದಲ ನಾಲ್ಕು characters ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ, A M O X, ಮತ್ತು upper ಅವನ್ನು capitals ಮಾಡುತ್ತೆ. Label ಗೆ ಇದು ಒಂದು ಚಿಕ್ಕ code.",
        "replace, ಇನ್ನೂರ ಐವತ್ತು M G ಬದಲು ಇನ್ನೂರ ಐವತ್ತು, space, M G ಹಾಕುತ್ತೆ. ಗಮನಿಸಿ, drug ತಾನೇ ಬದಲಾಗಿಲ್ಲ: replace ಹೊಸ string ಕೊಟ್ಟಿದೆ.",
    ],
}

# Animation narration
ANIM = {
    "hi": [
        "यह medicine strip का एक batch code है।",
        "हर character का एक index है, जो zero से शुरू होता है। साल index चार से शुरू होता है।",
        "Slice चार से आठ, index चार, पाँच, छह और सात लेता है। यह आठ से ठीक पहले रुकता है।",
        "ये चार characters मिलकर साल बनाते हैं: दो zero दो छह।",
        "और program इसे label पर print करता है।",
    ],
    "hinglish": [
        "Yeh medicine strip ka ek batch code hai.",
        "Har character ka ek index hai, jo zero se shuru hota hai. Saal index chaar se shuru hota hai.",
        "Slice chaar se aath, index chaar, paanch, chhah aur saat leta hai. Yeh aath se theek pehle rukta hai.",
        "Yeh chaar characters milkar saal banaate hain: do zero do chhah.",
        "Aur program ise label par print karta hai.",
    ],
    "kn": [
        "ಇದು ಒಂದು medicine strip ನ batch code.",
        "ಪ್ರತಿ character ಗೂ ಒಂದು index ಇದೆ, zero ಇಂದ ಶುರು. ವರ್ಷ index ನಾಲ್ಕರಿಂದ ಶುರು ಆಗುತ್ತೆ.",
        "Slice ನಾಲ್ಕರಿಂದ ಎಂಟು, index ನಾಲ್ಕು, ಐದು, ಆರು ಮತ್ತು ಏಳು ತೆಗೆದುಕೊಳ್ಳುತ್ತೆ. ಎಂಟಕ್ಕೆ ಸ್ವಲ್ಪ ಮುಂಚೆ ನಿಲ್ಲುತ್ತೆ.",
        "ಈ ನಾಲ್ಕು characters ಸೇರಿ ವರ್ಷ ಆಗುತ್ತೆ: ಎರಡು zero ಎರಡು ಆರು.",
        "ಮತ್ತು program ಇದನ್ನು label ಮೇಲೆ print ಮಾಡುತ್ತೆ.",
    ],
}


def say_en(text):
    """English voice text: read code names naturally."""
    return text.replace("two fifty M G", "two fifty M G")


def say_native(text, lang):
    """Hindi/Kannada voice text: Sarvam reads English words inside native script; only Python needs native spelling."""
    return text.replace("Python", {"hi": "पाइथन", "kn": "ಪೈಥಾನ್"}[lang])


if __name__ == "__main__":
    en = json.load(open(os.path.join(ROOT, "content", "bp101t", LESSON, "en.json"), encoding="utf-8"))
    n_steps, n_anim = len(en["walkthrough"]["steps"]), len(en["animations"][0]["steps"])
    for lang, data in T.items():
        assert len(NARR[lang]) == n_steps and len(ANIM[lang]) == n_anim, lang
        assert len(data["explanation"]) == len(en["explanation"]) and len(data["tasks"]) == len(en["tasks"]), lang
        assert len(data["quiz"]) == len(en["quiz"]) and len(data["mistakes"]) == len(en["mistakes"]), lang
        doc = dict(data)
        doc["walkthrough"] = dict(doc["walkthrough"], steps=[{"say": s} for s in NARR[lang]])
        doc["animations"] = [{"steps": [{"say": s} for s in ANIM[lang]]}]
        doc["translatedSections"] = SECTIONS
        path = os.path.join(ROOT, "content", "bp101t", LESSON, f"{lang}.json")
        json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("wrote", path)

    narr_en = [s["say"] for s in en["walkthrough"]["steps"]]
    anim_en = [s["say"] for s in en["animations"][0]["steps"]]
    tracks = []
    for tid, prefix, en_lines, native in (("narrator", "step-", narr_en, NARR), (ANIM_ID, ANIM_ID + "-", anim_en, ANIM)):
        tracks.append({"id": tid, "prefix": prefix, "lang": "en", "tts": [say_en(t) for t in en_lines], "display": en_lines})
        tracks.append({"id": tid, "prefix": prefix, "lang": "hi", "tts": [say_native(t, "hi") for t in native["hi"]], "display": native["hi"], "displayHinglish": native["hinglish"]})
        tracks.append({"id": tid, "prefix": prefix, "lang": "kn", "tts": [say_native(t, "kn") for t in native["kn"]], "display": native["kn"]})
    script = {"course": "bp101t", "lesson": LESSON, "voices": {"en": "Ritu", "hi": "Ritu", "kn": "Chaitra"}, "tracks": tracks}
    path = os.path.join(ROOT, "scripts", "bp101t", f"{LESSON}.json")
    json.dump(script, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", path)
    # keep the "Words to know" section after regenerating
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "..", "glossary_bp101t.py")], check=True)

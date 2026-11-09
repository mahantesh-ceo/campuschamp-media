"""Lesson 3.6 (English). Run to write content/bp101t/3-6/en.json."""
import json
import os
import subprocess
import sys

DATA = "patients = [\n    {\"id\": \"P01\", \"age\": 54, \"sex\": \"M\", \"sugar\": 142},\n    {\"id\": \"P02\", \"age\": 61, \"sex\": \"F\", \"sugar\": 118},\n    {\"id\": \"P03\", \"age\": 47, \"sex\": \"F\", \"sugar\": 165},\n]\n"
T_TABLE = "| id | age | sex | sugar (mg/dL) |\n|---|---|---|---|\n| P01 | 54 | M | 142 |\n| P02 | 61 | F | 118 |\n| P03 | 47 | F | 165 |"
C_RECORDS = "```python\n" + DATA + "print(len(patients), \"records\")\nprint(patients[0][\"sugar\"])\nfor p in patients:\n    print(p[\"id\"], p[\"age\"])\n```"
O_RECORDS = "```\n3 records\n142\nP01 54\nP02 61\nP03 47\n```"
C_SELECT = "```python\n" + DATA + "high = []\nfor p in patients:\n    if p[\"sugar\"] >= 126:\n        high.append(p[\"id\"])\nprint(\"High fasting sugar:\", high)\n```"
O_SELECT = "```\nHigh fasting sugar: ['P01', 'P03']\n```"
C_GROUP = "```python\n" + DATA + "totals = {}\ncounts = {}\nfor p in patients:\n    s = p[\"sex\"]\n    totals[s] = totals.get(s, 0) + p[\"sugar\"]\n    counts[s] = counts.get(s, 0) + 1\nfor s in totals:\n    print(s, totals[s] / counts[s])\n```"
O_GROUP = "```\nM 142.0\nF 141.5\n```"
C_CLEAN = "```python\nrecords = [\n    {\"id\": \"P04\", \"age\": 39, \"sugar\": 104},\n    {\"id\": \"P05\", \"age\": None, \"sugar\": 131},\n    {\"id\": \"P06\", \"age\": 540, \"sugar\": 98},\n]\nfor r in records:\n    if r[\"age\"] is None:\n        print(r[\"id\"], \"age missing\")\n    elif not 0 < r[\"age\"] < 120:\n        print(r[\"id\"], \"age looks wrong:\", r[\"age\"])\n```"
O_CLEAN = "```\nP05 age missing\nP06 age looks wrong: 540\n```"
C_ANON = "```python\nvisit = {\"name\": \"Ravi Kumar\", \"phone\": \"98450 12345\", \"age\": 54, \"drug\": \"Metformin\"}\nsafe = {}\nfor key, value in visit.items():\n    if key not in (\"name\", \"phone\"):\n        safe[key] = value\nprint(safe)\n```"
O_ANON = "```\n{'age': 54, 'drug': 'Metformin'}\n```"

L = {
    "id": "3-6",
    "course": "bp101t",
    "unit": "Unit III",
    "unitTitle": "Data Structures & File Handling",
    "number": "3.6",
    "title": "Structured healthcare datasets",
    "minutes": 22,
    "free": False,
    "audioLanguages": ["en", "hi", "kn"],
    "hook": {
        "title": "Every patient visit is a row",
        "md": "When a patient visits the OPD, the hospital records the same things every time: an ID, age, sex, the diagnosis, the drugs prescribed. A pharmacovigilance centre records the same fields for every adverse reaction report. Thousands of visits, all with the **same fields**, make a **structured dataset**.\n\nThis is the kind of data that clinical research, drug safety and hospital planning run on. Today you'll use lists and dictionaries, which you already know, to hold such a dataset, select patients, compare groups, catch bad data, and protect patient privacy.",
    },
    "learn": [
        "What **records**, **fields** and **structured data** are",
        "How to hold a dataset as a **list of dictionaries**, and select records with a condition",
        "How to summarise by **group**, like average sugar for men and women",
        "How to catch **missing** and impossible values, and remove **identifiers** to protect privacy",
    ],
    "explanation": [
        {
            "heading": "Records and fields",
            "md": "Structured data is a **table**. Each **row** is one **record** (one patient, one visit, one report) and each **column** is a **field** (age, sex, sugar):\n\n" + T_TABLE + "\n\nIn Python, the natural way to hold this is a **list of dictionaries**: one dictionary per record, with the field names as keys:\n\n" + C_RECORDS + "\n\nThis prints:\n\n" + O_RECORDS + "\n\n`patients[0]` is the first record; `patients[0][\"sugar\"]` is one field of it. A `for` loop visits every record.",
            "callout": {"type": "definition", "title": "Structured data", "md": "Data organised as records that all have the same fields, like a table. Spreadsheets, CSV files and hospital registers are structured; doctors' free-text notes are not."},
        },
        {
            "heading": "Selecting records",
            "md": "To pick out the records that match a condition, loop through the dataset and keep the ones you want. A fasting blood sugar of 126 mg/dL or more suggests diabetes:\n\n" + C_SELECT + "\n\nThis prints:\n\n" + O_SELECT + "\n\nThis is exactly what a filter in Excel does, and in Unit IV Pandas will do it in one line.",
        },
        {
            "heading": "Summaries by group",
            "md": "Often you want to compare groups: men and women, wards, age groups. Use the counting pattern from Lesson 3.3 twice, once for the totals and once for the counts:\n\n" + C_GROUP + "\n\nThis prints:\n\n" + O_GROUP + "\n\nThe two women's readings average (118 + 165) / 2 = 141.5. With three patients this is easy by hand; with three thousand, the same seven lines still work.",
        },
        {
            "heading": "Missing and impossible values",
            "md": "Real datasets are never perfect. A field may be **missing** (Python uses `None`, Excel shows a blank) or **impossible**, like an age of 540 that was meant to be 54. Check before you calculate:\n\n" + C_CLEAN + "\n\nThis prints:\n\n" + O_CLEAN + "\n\n`is None` tests for a missing value. `0 < age < 120` checks a range in one go. Finding these problems is called **data cleaning**, and it takes more time than the analysis itself in most real projects.",
            "callout": {"type": "warning", "title": "Never guess a missing value", "md": "Don't silently put 0 for a missing age or dose: the average will be wrong. Flag it, ask the source, or leave the record out and say so in your report."},
        },
        {
            "heading": "Privacy: remove what identifies a patient",
            "md": "Names, phone numbers, addresses and Aadhaar numbers **identify** a patient. Under India's **Digital Personal Data Protection Act, 2023**, health data must be protected. Before analysis, keep only the fields you need and use a code like `P01` instead of the name:\n\n" + C_ANON + "\n\nThis prints:\n\n" + O_ANON + "\n\nThe analysis still works, and nobody reading the file can tell who the patient is. This is called **de-identification** (or anonymisation).",
            "callout": {"type": "tip", "title": "Keep a data dictionary", "md": "A data dictionary lists every field: its name, type, unit and allowed values (age: int, years, 0 to 120). It keeps a dataset consistent when many people enter data."},
        },
    ],
    "walkthrough": {
        "intro": "This program reads three adverse drug reaction (ADR) reports, counts the reports for each drug and counts the serious ones.",
        "filename": "adr_reports.py",
        "code": "# Adverse drug reaction (ADR) reports\nreports = [\n    {\"drug\": \"Amoxicillin\", \"reaction\": \"Rash\", \"serious\": False},\n    {\"drug\": \"Ibuprofen\", \"reaction\": \"Gastric pain\", \"serious\": False},\n    {\"drug\": \"Amoxicillin\", \"reaction\": \"Anaphylaxis\", \"serious\": True},\n]\nby_drug = {}\nserious = 0\nfor r in reports:\n    by_drug[r[\"drug\"]] = by_drug.get(r[\"drug\"], 0) + 1\n    if r[\"serious\"]:\n        serious += 1\nprint(\"Reports per drug:\", by_drug)\nprint(\"Serious reactions:\", serious)",
        "output": "Reports per drug: {'Amoxicillin': 2, 'Ibuprofen': 1}\nSerious reactions: 1",
        "steps": [
            {"line": None, "say": "This program summarises adverse drug reaction reports, the kind pharmacists send to the national pharmacovigilance programme.", "output": None, "audio": "step-01.mp3"},
            {"line": 1, "say": "The comment says what the data is: A D R reports.", "output": None, "audio": "step-02.mp3"},
            {"line": 2, "say": "reports is a list of dictionaries. Each dictionary is one record, with the same three fields: drug, reaction and serious.", "output": None, "audio": "step-03.mp3", "vars": {"reports": "[3 records]"}},
            {"line": 7, "say": "by_drug will count the reports for each drug. It starts empty.", "output": None, "audio": "step-04.mp3", "vars": {"by_drug": "{}"}},
            {"line": 8, "say": "serious will count the serious reactions. It starts at zero.", "output": None, "audio": "step-05.mp3", "vars": {"serious": "0"}},
            {"line": 9, "say": "The loop takes one record at a time. The first is Amoxicillin, with a rash.", "output": None, "audio": "step-06.mp3", "vars": {"r": "{'drug': 'Amoxicillin', ...}"}},
            {"line": 10, "say": "This is the counting pattern. Amoxicillin is new, so get gives zero, and its count becomes one.", "output": None, "audio": "step-07.mp3", "vars": {"by_drug": "{'Amoxicillin': 1}"}},
            {"line": 11, "say": "A rash isn't marked serious, so the serious count stays at zero.", "output": None, "audio": "step-08.mp3"},
            {"line": 10, "say": "The second record is Ibuprofen. It gets a count of one.", "output": None, "audio": "step-09.mp3", "vars": {"by_drug": "{'Amoxicillin': 1, 'Ibuprofen': 1}"}},
            {"line": 12, "say": "The third is Amoxicillin again, now two. And anaphylaxis is serious, so serious goes up to one.", "output": None, "audio": "step-10.mp3", "vars": {"by_drug": "{'Amoxicillin': 2, 'Ibuprofen': 1}", "serious": "1"}},
            {"line": 13, "say": "print shows the number of reports for each drug.", "output": "Reports per drug: {'Amoxicillin': 2, 'Ibuprofen': 1}", "audio": "step-11.mp3"},
            {"line": 14, "say": "And one serious reaction, which in real practice must be reported quickly.", "output": "Serious reactions: 1", "audio": "step-12.mp3"},
        ],
        "keyTerms": [
            {"term": "reports = [{...}, {...}]", "meaning": "A dataset: a list with one dictionary per record."},
            {"term": "r[\"drug\"]", "meaning": "One field of the current record."},
            {"term": "by_drug.get(r[\"drug\"], 0) + 1", "meaning": "Count the records for each drug."},
            {"term": "if r[\"serious\"]:", "meaning": "Runs only for records where serious is True."},
        ],
    },
    "errors": {
        "intro": "Both errors come from records that don't look the way the program expects.",
        "examples": [
            {
                "title": "A field name spelled differently",
                "code": "patients = [{\"id\": \"P01\", \"age\": 54, \"sugar\": 142}]\nprint(patients[0][\"Sugar\"])",
                "output": "KeyError: 'Sugar'",
                "errorLine": 2,
                "md": "The field is `\"sugar\"` with a small s. Field names must match exactly. A data dictionary that fixes the spelling of every field prevents this when many people enter data.",
            },
            {
                "title": "Comparing a missing value",
                "code": "records = [{\"id\": \"P04\", \"age\": 39}, {\"id\": \"P05\", \"age\": None}]\nfor r in records:\n    if r[\"age\"] < 40:\n        print(r[\"id\"], \"is under 40\")",
                "output": "TypeError: '<' not supported between instances of 'NoneType' and 'int'",
                "errorLine": 3,
                "md": "P05 has no age, so Python is asked whether None is less than 40, which makes no sense. Check for missing values first: `if r[\"age\"] is not None and r[\"age\"] < 40:`.",
            },
        ],
    },
    "mistakes": [
        {"mistake": "Spelling a field differently in some records: `\"Age\"` and `\"age\"`", "see": "KeyError for some records", "fix": "Agree on field names in a data dictionary and use them everywhere."},
        {"mistake": "Mixing units: some doses in mg, some in g", "see": "No error, but averages and totals are wrong", "fix": "Store every value in one unit; convert when the data is entered."},
        {"mistake": "Converting a blank or \"NA\" value: `int(\"NA\")`", "see": "ValueError: invalid literal for int() with base 10: 'NA'", "fix": "Check for missing values before converting them."},
        {"mistake": "Keeping names and phone numbers in files used for analysis", "see": "No error, but a privacy breach if the file is shared", "fix": "Remove identifiers and use patient codes like P01."},
    ],
    "tasks": [
        {
            "id": "t1",
            "title": "List every record",
            "md": "Loop through **patients** and print each patient's id and sugar reading. The output must be exactly:",
            "expectedOutput": "P01 142\nP02 118\nP03 165",
            "starterCode": DATA + "\n# Print each id and sugar reading\n",
            "hints": ["for p in patients: visits each record.", "for p in patients:\n    print(p[\"id\"], p[\"sugar\"])"],
            "solution": DATA + "\n# Print each id and sugar reading\nfor p in patients:\n    print(p[\"id\"], p[\"sugar\"])",
            "check": {"type": "exactOutput", "mustContain": ["for "]},
        },
        {
            "id": "t2",
            "title": "Count the women",
            "md": "Count how many records have sex **\"F\"**. The output must be exactly:",
            "expectedOutput": "Female patients: 2",
            "starterCode": DATA + "\ncount = 0\n# Count the records where sex is \"F\"\n\nprint(\"Female patients:\", count)",
            "hints": ["Loop through the records and test p[\"sex\"] == \"F\".", "for p in patients:\n    if p[\"sex\"] == \"F\":\n        count += 1"],
            "solution": DATA + "\ncount = 0\n# Count the records where sex is \"F\"\nfor p in patients:\n    if p[\"sex\"] == \"F\":\n        count += 1\nprint(\"Female patients:\", count)",
            "check": {"type": "exactOutput", "mustContain": ["sex"]},
        },
        {
            "id": "t3",
            "title": "Average age",
            "md": "Add up the **age** field of every record and print the average age. The output must be exactly:",
            "expectedOutput": "Average age: 54.0",
            "starterCode": DATA + "\ntotal = 0\n# Add up the ages, then print the average\n",
            "hints": ["total += p[\"age\"] inside a loop.", "print(\"Average age:\", total / len(patients))"],
            "solution": DATA + "\ntotal = 0\n# Add up the ages, then print the average\nfor p in patients:\n    total += p[\"age\"]\nprint(\"Average age:\", total / len(patients))",
            "check": {"type": "exactOutput", "mustContain": ["age"]},
        },
        {
            "id": "t4",
            "title": "Find the bug",
            "md": "This program should list patients over 60, but it crashes on P05, whose age is missing. Fix the condition so missing ages are skipped and the output is exactly:",
            "expectedOutput": "P06 is a senior",
            "starterCode": "records = [{\"id\": \"P04\", \"age\": 39}, {\"id\": \"P05\", \"age\": None}, {\"id\": \"P06\", \"age\": 72}]\nfor r in records:\n    if r[\"age\"] > 60:\n        print(r[\"id\"], \"is a senior\")",
            "hints": ["None can't be compared with a number. Check for it first.", "if r[\"age\"] is not None and r[\"age\"] > 60:"],
            "solution": "records = [{\"id\": \"P04\", \"age\": 39}, {\"id\": \"P05\", \"age\": None}, {\"id\": \"P06\", \"age\": 72}]\nfor r in records:\n    if r[\"age\"] is not None and r[\"age\"] > 60:\n        print(r[\"id\"], \"is a senior\")",
            "solutionNote": "and checks the left side first: for P05, r[\"age\"] is not None is False, so Python never tries None > 60.",
            "check": {"type": "exactOutput", "mustContain": ["None"]},
        },
    ],
    "quiz": [
        {"q": "In a dataset table, what is one row?", "options": ["A field", "A record", "A file", "A header"], "answer": 1, "why": "Each row is one record: one patient, visit or report.", "code": False},
        {"q": "In a dataset table, what is one column?", "options": ["A record", "A field", "A dataset", "A key error"], "answer": 1, "why": "Each column is a field, like age or sugar.", "code": False},
        {"q": "Which Python structure best holds a dataset of patient records?", "options": ["A single string", "A list of dictionaries", "A tuple of numbers", "A set"], "answer": 1, "why": "One dictionary per record, all inside a list.", "code": False},
        {"q": "How do you test whether a field is missing (None)?", "options": ["if x == 0:", "if x is None:", "if x == \"\":", "if not x > 0:"], "answer": 1, "why": "is None checks for Python's missing value.", "code": True},
        {"q": "Which of these directly identifies a patient?", "options": ["Age", "Blood group", "Phone number", "Fasting sugar"], "answer": 2, "why": "A phone number points to one person; remove it before analysis.", "code": False},
        {"q": "What is a data dictionary for?", "options": ["Translating drug names", "Listing each field's name, type, unit and allowed values", "Storing passwords", "Sorting records"], "answer": 1, "why": "It keeps everyone entering data consistent.", "code": False},
    ],
    "exam": {
        "note": "Important questions for practice. Actual university questions may differ.",
        "short": [
            {"q": "What is structured data? Give two examples of structured healthcare datasets.", "marks": 2,
             "md": "**Structured data** is data organised into **records** (rows) that all have the same **fields** (columns), like a table.\n\nExamples:\n- **Patient/OPD register**: patient ID, age, sex, diagnosis, drugs prescribed.\n- **Adverse drug reaction (ADR) reports**: drug, reaction, seriousness, outcome.\n\nOthers: lab results, prescription records, pharmacy stock registers, clinical trial case report forms."},
            {"q": "What are missing values? How can they be detected in Python?", "marks": 2,
             "md": "A **missing value** is a field with no data recorded (blank in Excel, `None` in Python, often \"NA\").\n\n```python\nfor r in records:\n    if r[\"age\"] is None:\n        print(r[\"id\"], \"age missing\")\n```\n\nMissing values must be detected before calculation; otherwise comparisons give `TypeError` and averages are wrong."},
        ],
        "long": [
            {"q": "Explain how structured healthcare data can be represented and processed in Python using lists and dictionaries. Include selecting records, grouping, handling missing values and protecting patient privacy.", "marks": 5,
             "md": "**1. Representation**: a dataset is a **list of dictionaries**; each dictionary is one record and the keys are the field names.\n\n```python\npatients = [\n    {\"id\": \"P01\", \"age\": 54, \"sex\": \"M\", \"sugar\": 142},\n    {\"id\": \"P02\", \"age\": 61, \"sex\": \"F\", \"sugar\": 118},\n]\nprint(patients[0][\"sugar\"])   # one field of one record\n```\n\n**2. Selecting records** (filtering):\n\n```python\nhigh = []\nfor p in patients:\n    if p[\"sugar\"] >= 126:\n        high.append(p[\"id\"])\n```\n\n**3. Grouping and summarising**: totals and counts per group with `get()`.\n\n```python\ntotals, counts = {}, {}\nfor p in patients:\n    s = p[\"sex\"]\n    totals[s] = totals.get(s, 0) + p[\"sugar\"]\n    counts[s] = counts.get(s, 0) + 1\n```\n\n**4. Data quality**: detect missing (`is None`) and impossible values (`not 0 < age < 120`), use consistent units and field names (a **data dictionary**).\n\n**5. Privacy**: remove direct identifiers (name, phone, address, Aadhaar) and use codes like `P01` (**de-identification**), as required for health data under the Digital Personal Data Protection Act, 2023.\n\n**Uses**: pharmacovigilance (ADR report counts), clinical studies, hospital drug utilisation, stock planning. In Unit IV the same operations are done with Pandas."},
        ],
    },
    "mindmap": {
        "label": "Lesson 3.6 · Healthcare datasets",
        "children": [
            {"label": "Dataset", "children": [{"label": "Table of records"}, {"label": "Row = record"}, {"label": "Column = field"}]},
            {"label": "In Python", "children": [{"label": "List of dicts"}, {"label": "records[0][\"age\"]"}, {"label": "for r in records"}]},
            {"label": "Select & group", "children": [{"label": "if condition → append"}, {"label": "Count with get()"}, {"label": "Average per group"}]},
            {"label": "Data quality", "children": [{"label": "Missing: None"}, {"label": "Out-of-range values"}, {"label": "Same units & names"}]},
            {"label": "Privacy", "children": [{"label": "Remove names, phones"}, {"label": "Use patient IDs"}, {"label": "DPDP Act 2023"}]},
            {"label": "Errors", "children": [{"label": "KeyError: field name"}, {"label": "TypeError: None compare"}]},
        ],
    },
    "summary": [
        "**Structured data** is a table: each **row** is a **record**, each **column** a **field**.",
        "In Python a dataset is a **list of dictionaries**: `patients[0][\"sugar\"]` is one field of one record.",
        "Select records with a loop and `if`; summarise **by group** with totals and counts using `get()`.",
        "Check for **missing** (`is None`) and **impossible** values before calculating; never guess a missing value.",
        "Protect privacy: remove **identifiers** (name, phone, Aadhaar) and use codes like `P01`, as the DPDP Act 2023 requires.",
    ],
    "video": {"videoUrl": None, "searchTerms": ["structured data healthcare dataset python list of dictionaries", "data cleaning missing values python beginners"]},
    "animations": [
        {
            "id": "table",
            "title": "Counting through a dataset",
            "afterExplanation": 2,
            "canvas": {"desktop": {"w": 800, "h": 460}, "mobile": {"w": 360, "h": 600}},
            "actors": [
                {"id": "data", "type": "card", "title": "ADR reports", "icon": "🩺", "color": "indigo", "mono": True,
                 "lines": ["drug, reaction, serious", "Amoxicillin, Rash, False", "Ibuprofen, Gastric pain, False", "Amoxicillin, Anaphylaxis, True"],
                 "desktop": {"x": 40, "y": 30, "w": 480, "h": 170}, "mobile": {"x": 8, "y": 12, "w": 344, "h": 160}},
                {"id": "amox", "type": "box", "label": "Amoxicillin", "value": "0", "color": "amber",
                 "desktop": {"x": 40, "y": 225, "w": 220, "h": 80}, "mobile": {"x": 16, "y": 190, "w": 156, "h": 80}},
                {"id": "ibu", "type": "box", "label": "Ibuprofen", "value": "0", "color": "amber",
                 "desktop": {"x": 280, "y": 225, "w": 220, "h": 80}, "mobile": {"x": 188, "y": 190, "w": 156, "h": 80}},
                {"id": "ser", "type": "box", "label": "serious", "value": "0", "color": "rose",
                 "desktop": {"x": 540, "y": 225, "w": 220, "h": 80}, "mobile": {"x": 16, "y": 285, "w": 328, "h": 70}},
                {"id": "out", "type": "terminal", "title": "Output",
                 "desktop": {"x": 40, "y": 325, "w": 720, "h": 115}, "mobile": {"x": 16, "y": 375, "w": 328, "h": 160}},
            ],
            "steps": [
                {"say": "A structured dataset is a table. Each row is one report, and each column is a field.", "audio": "anim-table-01.mp3",
                 "actions": [{"do": "show", "target": "data"}, {"do": "show", "target": "out"}, {"do": "highlightLine", "target": "data", "line": 0},
                             {"do": "show", "target": "amox"}, {"do": "show", "target": "ibu"}, {"do": "show", "target": "ser"}]},
                {"say": "The first report is for Amoxicillin. Its count becomes one.", "audio": "anim-table-02.mp3",
                 "actions": [{"do": "highlightLine", "target": "data", "line": 1}, {"do": "setValue", "target": "amox", "value": "1"}, {"do": "pulse", "target": "amox"}]},
                {"say": "The second is for Ibuprofen, so Ibuprofen's count becomes one.", "audio": "anim-table-03.mp3",
                 "actions": [{"do": "highlightLine", "target": "data", "line": 2}, {"do": "setValue", "target": "ibu", "value": "1"}, {"do": "pulse", "target": "ibu"}]},
                {"say": "The third is Amoxicillin again, and it is serious: anaphylaxis. Amoxicillin goes to two, and serious to one.", "audio": "anim-table-04.mp3",
                 "actions": [{"do": "highlightLine", "target": "data", "line": 3}, {"do": "setValue", "target": "amox", "value": "2"}, {"do": "setValue", "target": "ser", "value": "1"},
                             {"do": "pulse", "target": "amox"}, {"do": "pulse", "target": "ser"}]},
                {"say": "Three rows, one pass. The same loop would summarise thirty thousand reports.", "audio": "anim-table-05.mp3",
                 "actions": [{"do": "appendOutput", "target": "out", "text": "{'Amoxicillin': 2, 'Ibuprofen': 1}"}, {"do": "appendOutput", "target": "out", "text": "Serious reactions: 1"}]},
            ],
        }
    ],
}

if __name__ == "__main__":
    root = os.path.join(os.path.dirname(__file__), "..", "..")
    out = os.path.join(root, "content", "bp101t", "3-6", "en.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(L, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", out)
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "..", "glossary_bp101t.py")], check=True, stdout=subprocess.DEVNULL)

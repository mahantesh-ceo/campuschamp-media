"""Lesson 3.5 (English). Run to write content/bp101t/3-5/en.json."""
import json
import os
import subprocess
import sys

F_STOCK = "```\ndrug,strips,price\nParacetamol,120,25.5\nCetirizine,45,18.0\n```"
C_WRITE = "```python\nwith open(\"stock.csv\", \"w\") as f:\n    f.write(\"drug,strips\\n\")\n    f.write(\"Paracetamol,120\\n\")\n    f.write(\"Cetirizine,45\\n\")\n\nwith open(\"stock.csv\") as f:\n    for line in f:\n        print(line.strip())\n```"
O_WRITE = "```\ndrug,strips\nParacetamol,120\nCetirizine,45\n```"
C_READER = "```python\nimport csv\n\nwith open(\"stock.csv\", \"w\") as f:\n    f.write(\"drug,strips\\nParacetamol,120\\nCetirizine,45\\n\")\n\nwith open(\"stock.csv\") as f:\n    for row in csv.reader(f):\n        print(row)\n```"
O_READER = "```\n['drug', 'strips']\n['Paracetamol', '120']\n['Cetirizine', '45']\n```"
C_DICTREADER = "```python\nimport csv\n\nwith open(\"stock.csv\", \"w\") as f:\n    f.write(\"drug,strips\\nParacetamol,120\\nCetirizine,45\\n\")\n\ntotal = 0\nwith open(\"stock.csv\") as f:\n    for row in csv.DictReader(f):\n        print(row[\"drug\"], row[\"strips\"])\n        total += int(row[\"strips\"])\nprint(\"Total:\", total)\n```"
O_DICTREADER = "```\nParacetamol 120\nCetirizine 45\nTotal: 165\n```"
C_WRITER = "```python\nimport csv\n\nrows = [[\"patient\", \"dose_mg\"], [\"Ravi\", 500], [\"Meena\", 250]]\nwith open(\"doses.csv\", \"w\", newline=\"\") as f:\n    csv.writer(f).writerows(rows)\n\nwith open(\"doses.csv\") as f:\n    for line in f:\n        print(line.strip())\n```"
O_WRITER = "```\npatient,dose_mg\nRavi,500\nMeena,250\n```"
C_APPEND = "```python\nwith open(\"log.csv\", \"w\") as f:\n    f.write(\"time,temp\\n\")\n\nwith open(\"log.csv\", \"a\") as f:\n    f.write(\"08:00,37.2\\n\")\n    f.write(\"12:00,38.1\\n\")\n\nwith open(\"log.csv\") as f:\n    lines = f.readlines()\nprint(len(lines), \"lines\")\nprint(lines[-1].strip())\n```"
O_APPEND = "```\n3 lines\n12:00,38.1\n```"

L = {
    "id": "3-5",
    "course": "bp101t",
    "unit": "Unit III",
    "unitTitle": "Data Structures & File Handling",
    "number": "3.5",
    "title": "Reading and writing CSV files",
    "minutes": 22,
    "free": False,
    "audioLanguages": ["en", "hi", "kn"],
    "hook": {
        "title": "The file every pharmacy already has",
        "md": "Every hospital pharmacy's billing software has an **Export** button. Press it, and you get a file called something like `stock.csv`. Open it in Excel and it's a neat table. Open it in Notepad and it's just lines of text with commas.\n\nThat simple format, **CSV**, is how lab instruments, hospital systems and government health portals share data. So far your data lived inside the program and vanished when it ended. Today your programs learn to **save** data to a file and **read** it back: the first step to working with real datasets.",
    },
    "learn": [
        "What a **CSV** file is, and how to **open**, **write** and **read** a file with **with open()**",
        "How the file **modes** \"r\", \"w\" and \"a\" differ",
        "How **csv.reader** and **csv.DictReader** turn each line into a list or a dictionary",
        "How to **write** rows with **csv.writer**, and why values must be **converted** before maths",
    ],
    "explanation": [
        {
            "heading": "What a CSV file is, and writing one",
            "md": "**CSV** means **Comma-Separated Values**. It's plain text: the first line is the **header** with the column names, and each line after it is one record:\n\n" + F_STOCK + "\n\nTo create a file, open it in **write mode**, `\"w\"`, and `write()` text into it. Each line must end with `\\n`, the newline character:\n\n" + C_WRITE + "\n\nThis prints:\n\n" + O_WRITE + "\n\n`with open(...) as f:` opens the file and **closes it automatically** when the indented block ends. Opening without a mode means **read** mode. `line.strip()` removes the `\\n` at the end of each line.",
            "callout": {"type": "tip", "title": "Files in Champ Lab", "md": "On your phone, Champ Lab keeps a file only while the program runs, so every example here writes its file first. On a computer, the same code saves stock.csv next to your program, and Excel can open it."},
        },
        {
            "heading": "Reading rows with csv.reader",
            "md": "You could split each line at the commas yourself, but the **csv** module does it properly, even for values that contain commas inside quotes. `csv.reader` gives each line as a **list**:\n\n" + C_READER + "\n\nThis prints:\n\n" + O_READER + "\n\nTwo things to notice. The header comes first, so skip it with `next(reader)` when you only want the data. And **every value is a string**, even `'120'`.",
            "callout": {"type": "warning", "title": "CSV values are text", "md": "\"120\" + 5 is an error. Convert first: int(row[1]) for whole numbers, float(...) for decimals."},
        },
        {
            "heading": "Reading rows as dictionaries",
            "md": "`csv.DictReader` uses the header names as **keys**, so each row is a **dictionary** and you look values up by column name, which is clearer and doesn't break if the columns change order:\n\n" + C_DICTREADER + "\n\nThis prints:\n\n" + O_DICTREADER + "\n\nThe header line isn't printed: DictReader used it for the keys. `int()` turned each text value into a number so it could be added to the total.",
            "callout": {"type": "definition", "title": "Header", "md": "The first line of a CSV file, holding the column names, like drug,strips. DictReader uses it as the keys of each row."},
        },
        {
            "heading": "Writing rows with csv.writer",
            "md": "To write many rows, put them in a list of lists and let `csv.writer` add the commas and newlines. Open the file with `newline=\"\"`, which stops blank lines appearing between rows on Windows:\n\n" + C_WRITER + "\n\nThis prints:\n\n" + O_WRITER + "\n\n`writerow(row)` writes one row; `writerows(rows)` writes them all. Numbers are written as text automatically.",
        },
        {
            "heading": "Adding to a file, and reading all lines",
            "md": "Opening with `\"w\"` **erases** the file first. To add lines at the end, use **append mode**, `\"a\"`. `readlines()` reads every line into a list:\n\n" + C_APPEND + "\n\nThis prints:\n\n" + O_APPEND + "\n\nThe header plus two readings make 3 lines, and `lines[-1]` is the latest reading. This is how a program can keep a running log, one line per measurement.",
            "callout": {"type": "warning", "title": "\"w\" erases", "md": "Opening an existing file with \"w\" deletes what was in it. Use \"a\" to add to it, and \"r\" (or no mode) to only read it."},
        },
    ],
    "walkthrough": {
        "intro": "This program saves a small temperature log as a CSV file, reads it back with DictReader and finds the highest reading.",
        "filename": "temp_log.py",
        "code": "import csv\n# A small temperature log, saved as a CSV file\nwith open(\"temps.csv\", \"w\") as f:\n    f.write(\"time,temp\\n08:00,37.2\\n12:00,38.4\\n18:00,37.8\\n\")\ntemps = []\nwith open(\"temps.csv\") as f:\n    for row in csv.DictReader(f):\n        temps.append(float(row[\"temp\"]))\nprint(\"Readings:\", temps)\nprint(\"Highest:\", max(temps))",
        "output": "Readings: [37.2, 38.4, 37.8]\nHighest: 38.4",
        "steps": [
            {"line": None, "say": "This program saves a temperature log as a CSV file, then reads it back and finds the highest reading.", "output": None, "audio": "step-01.mp3"},
            {"line": 1, "say": "import csv loads Python's module for CSV files.", "output": None, "audio": "step-02.mp3"},
            {"line": 3, "say": "open with w creates the file temps dot csv in write mode. with will close it automatically.", "output": None, "audio": "step-03.mp3"},
            {"line": 4, "say": "write puts four lines into the file: the header, time comma temp, and three readings. Each backslash n ends a line.", "output": None, "audio": "step-04.mp3"},
            {"line": 5, "say": "temps starts as an empty list, ready to collect the readings as numbers.", "output": None, "audio": "step-05.mp3", "vars": {"temps": "[]"}},
            {"line": 6, "say": "Now the file is opened again, this time for reading.", "output": None, "audio": "step-06.mp3"},
            {"line": 7, "say": "DictReader reads the header first. Then each row becomes a dictionary. The first row has time zero eight hundred, and temp thirty seven point two, still as text.", "output": None, "audio": "step-07.mp3", "vars": {"row": "{'time': '08:00', 'temp': '37.2'}"}},
            {"line": 8, "say": "float turns the text into a number, and append adds it to temps.", "output": None, "audio": "step-08.mp3", "vars": {"temps": "[37.2]"}},
            {"line": 8, "say": "The loop does the same for the other two rows.", "output": None, "audio": "step-09.mp3", "vars": {"temps": "[37.2, 38.4, 37.8]"}},
            {"line": 9, "say": "print shows all three readings, now as numbers.", "output": "Readings: [37.2, 38.4, 37.8]", "audio": "step-10.mp3"},
            {"line": 10, "say": "max finds the highest: thirty eight point four, at noon.", "output": "Highest: 38.4", "audio": "step-11.mp3"},
        ],
        "keyTerms": [
            {"term": "open(\"temps.csv\", \"w\")", "meaning": "Create (or erase) the file and open it for writing."},
            {"term": "with ... as f:", "meaning": "Use the file as f, and close it automatically afterwards."},
            {"term": "csv.DictReader(f)", "meaning": "Read each row as a dictionary keyed by the header."},
            {"term": "float(row[\"temp\"])", "meaning": "Turn the text value into a number."},
        ],
    },
    "errors": {
        "intro": "These two errors come up in almost every first file program.",
        "examples": [
            {
                "title": "Opening a file that doesn't exist",
                "code": "with open(\"stok.csv\") as f:\n    print(f.read())",
                "output": "FileNotFoundError: [Errno 2] No such file or directory: 'stok.csv'",
                "errorLine": 1,
                "md": "Read mode needs the file to exist. Here the name is misspelt (`stok` for `stock`). Check the spelling and the folder; on a computer the file must be next to your program, or you give its full path. (In Champ Lab the number after Errno may differ; the message is the same.)",
            },
            {
                "title": "Converting the header as a number",
                "code": "import csv\nwith open(\"stock.csv\", \"w\") as f:\n    f.write(\"drug,strips\\nORS,30\\n\")\nwith open(\"stock.csv\") as f:\n    for row in csv.reader(f):\n        print(int(row[1]))",
                "output": "ValueError: invalid literal for int() with base 10: 'strips'",
                "errorLine": 6,
                "md": "The first row is the header, so `row[1]` is the word `strips`, which can't become a number. Skip the header with `next(reader)` first, or use `csv.DictReader`.",
            },
        ],
    },
    "mistakes": [
        {"mistake": "Opening with `\"w\"` when you meant to add a line", "see": "No error, but everything that was in the file is gone", "fix": "Use `\"a\"` (append) to add at the end."},
        {"mistake": "Forgetting `\\n` at the end of each `write()`", "see": "No error, but everything ends up on one long line", "fix": "End each line with `\\n`, or use `csv.writer`."},
        {"mistake": "Doing maths with a value straight from the file: `row[\"strips\"] + 5`", "see": "TypeError: can only concatenate str (not \"int\") to str", "fix": "Convert first: `int(row[\"strips\"]) + 5`."},
        {"mistake": "Opening a file without `with` and forgetting `close()`", "see": "Data may not be saved, or the file stays locked", "fix": "Always use `with open(...) as f:`."},
    ],
    "tasks": [
        {
            "id": "t1",
            "title": "Write a file",
            "md": "Inside the first `with` block, **write** the header `drug,strips` and the row `ORS,30` into stock.csv, each ending with `\\n`. The reading part is done for you. The output must be exactly:",
            "expectedOutput": "drug,strips\nORS,30",
            "starterCode": "# Write the two lines into stock.csv\nwith open(\"stock.csv\", \"w\") as f:\n    pass  # replace with f.write(...)\n\nwith open(\"stock.csv\") as f:\n    for line in f:\n        print(line.strip())",
            "hints": ["Each f.write() adds text; end each line with \\n.", "f.write(\"drug,strips\\n\")\n    f.write(\"ORS,30\\n\")"],
            "solution": "# Write the two lines into stock.csv\nwith open(\"stock.csv\", \"w\") as f:\n    f.write(\"drug,strips\\n\")\n    f.write(\"ORS,30\\n\")\n\nwith open(\"stock.csv\") as f:\n    for line in f:\n        print(line.strip())",
            "check": {"type": "exactOutput", "mustContain": ["f.write("]},
        },
        {
            "id": "t2",
            "title": "Skip the header",
            "md": "Use the **reader** to skip the header row with **next()**, then print only the drug name from each row. The output must be exactly:",
            "expectedOutput": "Paracetamol\nCetirizine",
            "starterCode": "import csv\nwith open(\"stock.csv\", \"w\") as f:\n    f.write(\"drug,strips\\nParacetamol,120\\nCetirizine,45\\n\")\n\nwith open(\"stock.csv\") as f:\n    reader = csv.reader(f)\n    # Skip the header, then print each drug name\n",
            "hints": ["next(reader) reads and throws away one row.", "next(reader)\n    for row in reader:\n        print(row[0])"],
            "solution": "import csv\nwith open(\"stock.csv\", \"w\") as f:\n    f.write(\"drug,strips\\nParacetamol,120\\nCetirizine,45\\n\")\n\nwith open(\"stock.csv\") as f:\n    reader = csv.reader(f)\n    # Skip the header, then print each drug name\n    next(reader)\n    for row in reader:\n        print(row[0])",
            "check": {"type": "exactOutput", "mustContain": ["next(", "row[0]"]},
        },
        {
            "id": "t3",
            "title": "Total from a CSV",
            "md": "Read stock.csv with **csv.DictReader** and add up the **strips** column. Remember to convert each value with **int()**. The output must be exactly:",
            "expectedOutput": "Total strips: 200",
            "starterCode": "import csv\nwith open(\"stock.csv\", \"w\") as f:\n    f.write(\"drug,strips\\nParacetamol,120\\nCetirizine,45\\nORS,35\\n\")\n\ntotal = 0\n# Read the file and add up the strips column\n\nprint(\"Total strips:\", total)",
            "hints": ["with open(\"stock.csv\") as f:\n    for row in csv.DictReader(f):", "        total += int(row[\"strips\"])"],
            "solution": "import csv\nwith open(\"stock.csv\", \"w\") as f:\n    f.write(\"drug,strips\\nParacetamol,120\\nCetirizine,45\\nORS,35\\n\")\n\ntotal = 0\n# Read the file and add up the strips column\nwith open(\"stock.csv\") as f:\n    for row in csv.DictReader(f):\n        total += int(row[\"strips\"])\nprint(\"Total strips:\", total)",
            "check": {"type": "exactOutput", "mustContain": ["DictReader", "int("]},
        },
        {
            "id": "t4",
            "title": "Find the bug",
            "md": "This program should keep the header and add a reading below it, but the header disappears. Change **one mode** so the output is exactly:",
            "expectedOutput": "time,temp\n08:00,37.2",
            "starterCode": "with open(\"log.csv\", \"w\") as f:\n    f.write(\"time,temp\\n\")\n\nwith open(\"log.csv\", \"w\") as f:\n    f.write(\"08:00,37.2\\n\")\n\nwith open(\"log.csv\") as f:\n    for line in f:\n        print(line.strip())",
            "hints": ["\"w\" erases the file before writing.", "Open the file the second time with \"a\" to add to it."],
            "solution": "with open(\"log.csv\", \"w\") as f:\n    f.write(\"time,temp\\n\")\n\nwith open(\"log.csv\", \"a\") as f:\n    f.write(\"08:00,37.2\\n\")\n\nwith open(\"log.csv\") as f:\n    for line in f:\n        print(line.strip())",
            "solutionNote": "The second open used \"w\", which erased the header. \"a\" (append) keeps what's there and adds the new line at the end.",
            "check": {"type": "exactOutput", "mustContain": ["log.csv"]},
        },
    ],
    "quiz": [
        {"q": "What does CSV stand for?", "options": ["Computer Stored Values", "Comma-Separated Values", "Column Sorted Variables", "Coded Sheet View"], "answer": 1, "why": "CSV files separate values with commas.", "code": False},
        {"q": "Which mode adds lines to the end of a file without erasing it?", "options": ["\"r\"", "\"w\"", "\"a\"", "\"x\""], "answer": 2, "why": "\"a\" is append mode.", "code": True},
        {"q": "What type are the values that csv.reader gives you?", "options": ["int", "float", "str", "It depends on the value"], "answer": 2, "why": "Everything read from a text file is a string until you convert it.", "code": False},
        {"q": "Why do we write with open(...) as f:?", "options": ["It's faster", "The file is closed automatically at the end of the block", "It makes the file a CSV", "It skips the header"], "answer": 1, "why": "with closes the file for you, even if an error happens.", "code": True},
        {"q": "What is each row from csv.DictReader?", "options": ["A list", "A string", "A dictionary keyed by the header", "A tuple"], "answer": 2, "why": "DictReader uses the header names as keys.", "code": False},
        {"q": "What happens if you open an existing file with \"w\"?", "options": ["Lines are added at the end", "It is erased and starts empty", "An error", "It opens read-only"], "answer": 1, "why": "Write mode erases the file before writing.", "code": True},
    ],
    "exam": {
        "note": "Important questions for practice. Actual university questions may differ.",
        "short": [
            {"q": "What is a CSV file? Give an example.", "marks": 2,
             "md": "A **CSV (Comma-Separated Values)** file is a plain-text file that stores a table: each line is a record and the values are separated by commas. The first line is usually the **header** with column names.\n\n```\ndrug,strips,price\nParacetamol,120,25.5\nCetirizine,45,18.0\n```\n\nIt can be opened in Excel and read by Python's `csv` module."},
            {"q": "Explain the file modes \"r\", \"w\" and \"a\".", "marks": 2,
             "md": "- `\"r\"` (read, default): opens an existing file for reading; `FileNotFoundError` if it doesn't exist.\n- `\"w\"` (write): creates the file, or **erases** an existing one, and opens it for writing.\n- `\"a\"` (append): opens for writing at the **end** of the file, keeping existing content; creates it if needed.\n\n```python\nwith open(\"log.csv\", \"a\") as f:\n    f.write(\"08:00,37.2\\n\")\n```"},
        ],
        "long": [
            {"q": "Explain how to read and write CSV files in Python using the csv module, with examples of csv.reader, csv.DictReader and csv.writer.", "marks": 5,
             "md": "Python's built-in **csv** module reads and writes comma-separated files. Files are opened with `with open(filename, mode) as f:`, which closes them automatically.\n\n**1. Writing with csv.writer**\n\n```python\nimport csv\nrows = [[\"patient\", \"dose_mg\"], [\"Ravi\", 500], [\"Meena\", 250]]\nwith open(\"doses.csv\", \"w\", newline=\"\") as f:\n    writer = csv.writer(f)\n    writer.writerows(rows)      # or writer.writerow(row) for one row\n```\n\n**2. Reading with csv.reader**: each row is a **list of strings**.\n\n```python\nwith open(\"doses.csv\") as f:\n    reader = csv.reader(f)\n    header = next(reader)        # skip the header\n    for row in reader:\n        print(row[0], int(row[1]))\n```\n\n**3. Reading with csv.DictReader**: each row is a **dictionary** keyed by the header.\n\n```python\ntotal = 0\nwith open(\"doses.csv\") as f:\n    for row in csv.DictReader(f):\n        total += int(row[\"dose_mg\"])\nprint(total)   # 750\n```\n\n**Points to remember**\n- All values read are strings; convert with `int()` / `float()` before calculations.\n- `\"w\"` erases an existing file; `\"a\"` appends.\n- Use `newline=\"\"` when writing to avoid blank lines on Windows.\n- A missing file in read mode gives `FileNotFoundError`.\n\nCSV files are used to exchange stock registers, lab results and patient data between hospital systems and analysis programs."},
        ],
    },
    "mindmap": {
        "label": "Lesson 3.5 · CSV files",
        "children": [
            {"label": "CSV file", "children": [{"label": "Plain text"}, {"label": "Commas between values"}, {"label": "First line = header"}]},
            {"label": "Open", "children": [{"label": "with open(name, mode)"}, {"label": "\"r\" \"w\" \"a\""}, {"label": "Closes by itself"}]},
            {"label": "Read", "children": [{"label": "csv.reader → lists"}, {"label": "csv.DictReader → dicts"}, {"label": "next() skips header"}]},
            {"label": "Write", "children": [{"label": "f.write(text + \\n)"}, {"label": "csv.writer"}, {"label": "writerow / writerows"}]},
            {"label": "Convert", "children": [{"label": "Values are text"}, {"label": "int() / float()"}, {"label": "Then calculate"}]},
            {"label": "Errors", "children": [{"label": "FileNotFoundError"}, {"label": "ValueError: header"}]},
        ],
    },
    "summary": [
        "A **CSV** file is plain text: a **header** line, then one record per line with values separated by commas.",
        "`with open(name, mode) as f:` opens a file and closes it automatically. Modes: **\"r\"** read, **\"w\"** write (erases), **\"a\"** append.",
        "**csv.reader** gives each row as a list; **csv.DictReader** gives a dictionary keyed by the header. `next(reader)` skips the header.",
        "**csv.writer** with `writerow()` / `writerows()` writes rows; open with `newline=\"\"`.",
        "Every value read from a file is **text**: convert with `int()` or `float()` before doing maths.",
    ],
    "video": {"videoUrl": None, "searchTerms": ["python read write csv file csv module", "python csv dictreader beginners"]},
    "animations": [
        {
            "id": "rows",
            "title": "From a line of text to a dictionary",
            "afterExplanation": 2,
            "canvas": {"desktop": {"w": 800, "h": 460}, "mobile": {"w": 360, "h": 600}},
            "actors": [
                {"id": "file", "type": "card", "title": "temps.csv", "icon": "📄", "color": "indigo", "mono": True,
                 "lines": ["time,temp", "08:00,37.2", "12:00,38.4", "18:00,37.8"],
                 "desktop": {"x": 40, "y": 30, "w": 440, "h": 170}, "mobile": {"x": 16, "y": 12, "w": 328, "h": 160}},
                {"id": "temps", "type": "box", "label": "temps", "value": "[]", "color": "emerald",
                 "desktop": {"x": 510, "y": 30, "w": 250, "h": 100}, "mobile": {"x": 16, "y": 185, "w": 328, "h": 80}},
                {"id": "row", "type": "pill", "text": "row = {'time': '08:00', 'temp': '37.2'}", "color": "amber",
                 "desktop": {"x": 40, "y": 215, "w": 440, "h": 30}, "mobile": {"x": 16, "y": 280, "w": 328, "h": 30}},
                {"id": "out", "type": "terminal", "title": "Output",
                 "desktop": {"x": 40, "y": 270, "w": 720, "h": 160}, "mobile": {"x": 16, "y": 330, "w": 328, "h": 200}},
            ],
            "steps": [
                {"say": "A CSV file is plain text. The first line is the header. Every other line is one record, with commas between the values.", "audio": "anim-rows-01.mp3",
                 "actions": [{"do": "show", "target": "file"}, {"do": "show", "target": "out"}, {"do": "show", "target": "temps"}]},
                {"say": "DictReader reads the header first, and keeps its names, time and temp, as the keys.", "audio": "anim-rows-02.mp3",
                 "actions": [{"do": "highlightLine", "target": "file", "line": 0}]},
                {"say": "The next line becomes a dictionary: time is zero eight hundred, and temp is thirty seven point two. It is still text.", "audio": "anim-rows-03.mp3",
                 "actions": [{"do": "highlightLine", "target": "file", "line": 1}, {"do": "show", "target": "row"}, {"do": "pulse", "target": "row"}]},
                {"say": "float turns the text into a number, and append adds it to the list.", "audio": "anim-rows-04.mp3",
                 "actions": [{"do": "setValue", "target": "temps", "value": "[37.2]"}, {"do": "pulse", "target": "temps"}]},
                {"say": "The same happens for every line. Now max can find the highest reading.", "audio": "anim-rows-05.mp3",
                 "actions": [{"do": "highlightLine", "target": "file", "line": 3}, {"do": "setValue", "target": "temps", "value": "[37.2, 38.4, 37.8]"}, {"do": "pulse", "target": "temps"},
                             {"do": "appendOutput", "target": "out", "text": "Highest: 38.4"}]},
            ],
        }
    ],
}

if __name__ == "__main__":
    root = os.path.join(os.path.dirname(__file__), "..", "..")
    out = os.path.join(root, "content", "bp101t", "3-5", "en.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(L, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", out)
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "..", "glossary_bp101t.py")], check=True, stdout=subprocess.DEVNULL)

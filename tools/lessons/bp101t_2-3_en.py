"""Lesson 2.3 (English). Run to write content/bp101t/2-3/en.json."""
import json
import os
import subprocess
import sys

C_FIRST = "```python\nfor day in range(1, 4):\n    print(f\"Day {day}: 1 tablet\")\nprint(\"Course complete\")\n```"
O_FIRST = "```\nDay 1: 1 tablet\nDay 2: 1 tablet\nDay 3: 1 tablet\nCourse complete\n```"
C_RANGE = "```python\nfor hour in range(0, 24, 8):\n    print(f\"Dose at {hour}:00\")\n```"
O_RANGE = "```\nDose at 0:00\nDose at 8:00\nDose at 16:00\n```"
C_SEQ = "```python\nfor letter in \"DOSE\":\n    print(letter)\n\ndrugs = [\"Paracetamol\", \"Amoxicillin\", \"Cetirizine\"]\nfor drug in drugs:\n    print(drug.upper())\n```"
O_SEQ = "```\nD\nO\nS\nE\nPARACETAMOL\nAMOXICILLIN\nCETIRIZINE\n```"
C_TOTAL = "```python\ndoses = [500, 500, 650, 500]\ntotal = 0\nfor dose in doses:\n    total += dose\nprint(\"Total today:\", total, \"mg\")\nif total > 4000:\n    print(\"Above the daily limit!\")\n```"
C_COUNT = "```python\ntemps = [36.8, 38.4, 37.1, 39.6]\nfevers = 0\nfor temp in temps:\n    if temp >= 38.0:\n        print(temp, \"is a fever\")\n        fevers += 1\nprint(\"Readings with fever:\", fevers)\n```"
O_COUNT = "```\n38.4 is a fever\n39.6 is a fever\nReadings with fever: 2\n```"

L = {
    "id": "2-3",
    "course": "bp101t",
    "unit": "Unit II",
    "unitTitle": "Control Structures & Functions",
    "number": "2.3",
    "title": "for loops",
    "minutes": 15,
    "free": False,
    "audioLanguages": ["en", "hi", "kn"],
    "hook": {
        "title": "A dosing chart for 30 days",
        "md": "A patient leaves with a 30-day course, and you want to print a chart: **Day 1, Day 2, ... Day 30**. Writing 30 `print()` lines would be slow, boring and easy to get wrong.\n\nComputers are brilliant at repeating things. In this lesson, you'll write **one** line that repeats as many times as you need: a **for loop**.",
    },
    "learn": [
        "How a **for loop** repeats a block once for each item",
        "How **range()** makes a run of numbers, and why the stop number is left out",
        "How to loop over the letters of a **string** and the items of a **list**",
        "How to **add up** or **count** things with a loop",
    ],
    "explanation": [
        {
            "heading": "Repeating without copying",
            "md": "A **for loop** runs the same block again and again, once for each value it is given:\n\n" + C_FIRST + "\n\nThis prints:\n\n" + O_FIRST + "\n\nEach time round, the **loop variable** `day` takes the next value: first 1, then 2, then 3. One run of the block is called an **iteration**.\n\nThe rules you know from `if` apply here too: the `for` line ends with a **colon**, and the block is **indented with 4 spaces**. `print(\"Course complete\")` is not indented, so it runs **once**, after the loop has finished.",
            "callout": {"type": "definition", "title": "Loop", "md": "A block of code that runs again and again. A for loop runs it once for each value; each run is one iteration."},
        },
        {
            "heading": "range(): a run of numbers",
            "md": "**range()** makes the numbers a loop goes through. It has three forms:\n\n| You write | You get |\n|---|---|\n| `range(5)` | 0, 1, 2, 3, 4 |\n| `range(1, 6)` | 1, 2, 3, 4, 5 |\n| `range(0, 24, 8)` | 0, 8, 16 |\n\nThe third number is the **step**: how much to add each time. A medicine taken every 8 hours:\n\n" + C_RANGE + "\n\nThis prints:\n\n" + O_RANGE,
            "callout": {"type": "warning", "title": "The stop number is never included", "md": "range(1, 6) stops just before 6, like a slice. For days 1 to 30, write range(1, 31)."},
        },
        {
            "heading": "Looping over text and lists",
            "md": "A `for` loop can go through more than numbers. It can visit each character of a **string**, or each item of a **list**: a set of values inside square brackets, separated by commas.\n\n" + C_SEQ + "\n\nThis prints:\n\n" + O_SEQ + "\n\nThe loop variable takes each item in turn, from the first to the last. You'll learn much more about lists in Unit III.",
        },
        {
            "heading": "Adding up with a loop",
            "md": "To add up values, start a **total** at 0 **before** the loop, and add to it **inside** the loop. This is called an **accumulator**.\n\nAn adult's paracetamol doses for one day:\n\n" + C_TOTAL + "\n\nThis prints `Total today: 2150 mg`. Nothing else prints, because 2150 is not above 4000 mg, the usual daily limit for adults.\n\n`total += dose` is the shortcut from Lesson 1.4: it means `total = total + dose`.",
            "callout": {"type": "tip", "title": "Start the total outside the loop", "md": "If total = 0 is inside the loop, it goes back to 0 every time round, and you only get the last value."},
        },
        {
            "heading": "An if inside a loop",
            "md": "A loop and an `if` work well together: the loop visits every value, and the `if` picks out the ones that matter. Here, a nurse's temperature readings are checked for fever, and counted:\n\n" + C_COUNT + "\n\nThis prints:\n\n" + O_COUNT + "\n\nThe `if` block has 8 spaces, because it is inside the loop. The last `print` has none, so it runs once, after all the readings are checked.",
        },
    ],
    "walkthrough": {
        "intro": "This program prints a 3-day tablet chart and counts how many tablets the patient needs.",
        "filename": "tablet_chart.py",
        "code": "# 3-day course: 2 tablets a day\ntotal = 0\nfor day in range(1, 4):\n    total += 2\n    print(f\"Day {day}: 2 tablets\")\nprint(\"Tablets needed:\", total)",
        "output": "Day 1: 2 tablets\nDay 2: 2 tablets\nDay 3: 2 tablets\nTablets needed: 6",
        "steps": [
            {"line": None, "say": "This program repeats two lines, once for each day of the course, and keeps a running total.", "output": None, "audio": "step-01.mp3"},
            {"line": 1, "say": "The comment says what the program does.", "output": None, "audio": "step-02.mp3"},
            {"line": 2, "say": "total starts at zero, before the loop.", "output": None, "audio": "step-03.mp3", "vars": {"total": "0"}},
            {"line": 3, "say": "range one to four gives one, two and three. The loop starts, and day is one.", "output": None, "audio": "step-04.mp3", "vars": {"day": "1"}},
            {"line": 4, "say": "Two tablets are added to total, so total is two.", "output": None, "audio": "step-05.mp3", "vars": {"total": "2"}},
            {"line": 5, "say": "print shows day one.", "output": "Day 1: 2 tablets", "audio": "step-06.mp3"},
            {"line": 3, "say": "The block is finished, so Python goes back to the top of the loop. day becomes two.", "output": None, "audio": "step-07.mp3", "vars": {"day": "2"}},
            {"line": 5, "say": "total becomes four, and print shows day two.", "output": "Day 2: 2 tablets", "audio": "step-08.mp3", "vars": {"total": "4"}},
            {"line": 5, "say": "Once more for day three. total becomes six.", "output": "Day 3: 2 tablets", "audio": "step-09.mp3", "vars": {"day": "3", "total": "6"}},
            {"line": 6, "say": "range has no numbers left, so the loop ends. The last line is not indented, so it runs once, and shows the total.", "output": "Tablets needed: 6", "audio": "step-10.mp3"},
        ],
        "keyTerms": [
            {"term": "for day in ...:", "meaning": "Repeat the block once for each value, stored in day."},
            {"term": "range(1, 4)", "meaning": "The numbers 1, 2 and 3 (4 is left out)."},
            {"term": "total = 0", "meaning": "Start the running total before the loop."},
            {"term": "total += 2", "meaning": "Add 2 to the total, every time round."},
        ],
    },
    "errors": {
        "intro": "These two errors come from the for line itself.",
        "examples": [
            {
                "title": "Forgetting the colon",
                "code": "for day in range(1, 4)\n    print(day)",
                "output": "SyntaxError: expected ':'",
                "errorLine": 1,
                "md": "Like `if`, the `for` line must end with a colon: `for day in range(1, 4):`.",
            },
            {
                "title": "Giving range() text instead of a number",
                "code": "days = \"5\"\nfor day in range(days):\n    print(day)",
                "output": "TypeError: 'str' object cannot be interpreted as an integer",
                "errorLine": 2,
                "md": "`\"5\"` is a string, for example from `input()`. `range()` needs an integer. Convert it first: `range(int(days))`.",
            },
        ],
    },
    "mistakes": [
        {"mistake": "Expecting `range(1, 30)` to include 30", "see": "No error, but the chart stops at Day 29", "fix": "The stop is left out, so write `range(1, 31)`."},
        {"mistake": "Putting `total = 0` inside the loop", "see": "No error, but the total is only the last value", "fix": "Start the total once, before the loop."},
        {"mistake": "Indenting the final `print` by mistake", "see": "No error, but the total prints after every iteration", "fix": "Lines that should run once go after the loop, with no indentation."},
        {"mistake": "Using `range()` with a decimal, e.g. `range(1, 7.5)`", "see": "TypeError: 'float' object cannot be interpreted as an integer", "fix": "`range()` only takes whole numbers. Use `int()` or a whole number."},
    ],
    "tasks": [
        {
            "id": "t1",
            "title": "Number the doses",
            "md": "Use a **for loop** with **range()** to print the three doses of the day, exactly:",
            "expectedOutput": "Dose 1\nDose 2\nDose 3",
            "starterCode": "# Print Dose 1, Dose 2 and Dose 3 with a for loop\n",
            "hints": ["range(1, 4) gives 1, 2 and 3.", "for n in range(1, 4):\n    print(f\"Dose {n}\")"],
            "solution": "# Print Dose 1, Dose 2 and Dose 3 with a for loop\nfor n in range(1, 4):\n    print(f\"Dose {n}\")",
            "check": {"type": "exactOutput", "mustContain": ["for", "range("]},
        },
        {
            "id": "t2",
            "title": "Every 6 hours",
            "md": "An antibiotic is given every 6 hours, starting at midnight. Use **range() with a step** so the output is exactly:",
            "expectedOutput": "Dose at 0:00\nDose at 6:00\nDose at 12:00\nDose at 18:00",
            "starterCode": "# Print the dose times for one day, every 6 hours\n",
            "hints": ["The third number in range() is the step: range(0, 24, 6).", "for hour in range(0, 24, 6):\n    print(f\"Dose at {hour}:00\")"],
            "solution": "# Print the dose times for one day, every 6 hours\nfor hour in range(0, 24, 6):\n    print(f\"Dose at {hour}:00\")",
            "check": {"type": "exactOutput", "mustContain": ["range(", "6)"]},
        },
        {
            "id": "t3",
            "title": "Add up the doses",
            "md": "Add up the doses in the list with a loop, and print the total exactly:",
            "expectedOutput": "Total: 1000 mg",
            "starterCode": "doses = [250, 500, 250]\ntotal = 0\n# Add each dose to total, then print the total\n",
            "hints": ["Inside the loop: total += dose", "for dose in doses:\n    total += dose\nprint(\"Total:\", total, \"mg\")"],
            "solution": "doses = [250, 500, 250]\ntotal = 0\n# Add each dose to total, then print the total\nfor dose in doses:\n    total += dose\nprint(\"Total:\", total, \"mg\")",
            "check": {"type": "exactOutput", "mustContain": ["for"]},
        },
        {
            "id": "t4",
            "title": "Find the bug",
            "md": "A patient takes 3 tablets a day for 7 days, so they need 21 tablets. This program says 3, and there is no error. Fix it so the output is exactly:",
            "expectedOutput": "Tablets for 7 days: 21",
            "starterCode": "total = 0\nfor day in range(1, 8):\n    total = 0\n    total += 3\nprint(\"Tablets for 7 days:\", total)",
            "hints": ["What happens to total at the start of every iteration?", "Remove the total = 0 inside the loop. The one before the loop is enough."],
            "solution": "total = 0\nfor day in range(1, 8):\n    total += 3\nprint(\"Tablets for 7 days:\", total)",
            "solutionNote": "total = 0 inside the loop reset the total every day, so only the last 3 was left. Starting it once, before the loop, lets it grow to 21.",
            "check": {"type": "exactOutput", "mustContain": ["for"]},
        },
    ],
    "quiz": [
        {"q": "Which numbers does range(1, 4) give?", "options": ["1, 2, 3, 4", "1, 2, 3", "0, 1, 2, 3", "1 and 4"], "answer": 1, "why": "range stops just before the stop number, 4.", "code": True},
        {"q": "for i in range(3):\n    print(\"Shake well\")\n\nHow many times is \"Shake well\" printed?", "options": ["2", "3", "4", "Once"], "answer": 1, "why": "range(3) gives 0, 1 and 2: three values, so three iterations.", "code": True},
        {"q": "What does range(0, 10, 5) give?", "options": ["0, 5", "0, 5, 10", "5, 10", "0 to 10"], "answer": 0, "why": "Start at 0, add 5 each time, and stop before 10.", "code": True},
        {"q": "total = 0\nfor n in range(1, 4):\n    total += n\nprint(total)\n\nWhat does this print?", "options": ["3", "4", "6", "10"], "answer": 2, "why": "1 + 2 + 3 = 6.", "code": True},
        {"q": "for ch in \"ABC\":\n    print(ch)\n\nWhat is printed?", "options": ["ABC on one line", "A, B and C on separate lines", "3", "Error"], "answer": 1, "why": "The loop visits each character, and each print starts a new line.", "code": True},
        {"q": "Which line runs only once, after the loop ends?", "options": ["The for line", "An indented line under for", "The next line with no indentation", "Every line"], "answer": 2, "why": "Lines that are not indented are outside the loop, so they run once, after it finishes.", "code": False},
    ],
    "exam": {
        "note": "Important questions for practice. Actual university questions may differ.",
        "short": [
            {"q": "Explain the range() function with its three forms.", "marks": 2,
             "md": "**range()** generates a sequence of integers, mostly used with a `for` loop.\n\n1. `range(stop)`: 0 up to stop - 1. `range(5)` gives 0, 1, 2, 3, 4.\n2. `range(start, stop)`: start up to stop - 1. `range(1, 6)` gives 1, 2, 3, 4, 5.\n3. `range(start, stop, step)`: start, start + step, ... before stop. `range(0, 24, 8)` gives 0, 8, 16.\n\nThe stop value is never included, and all arguments must be integers."},
            {"q": "Write a program to print the multiplication table of a number using a for loop.", "marks": 2,
             "md": "```python\nn = int(input(\"Enter a number: \"))\nfor i in range(1, 11):\n    print(n, \"x\", i, \"=\", n * i)\n```\n\nFor n = 5 this prints `5 x 1 = 5` up to `5 x 10 = 50`. `range(1, 11)` gives 1 to 10, and the loop runs the print once for each value."},
        ],
        "long": [
            {"q": "Explain the for loop in Python with syntax, flow and examples. Write a program to find the sum of the first n natural numbers.", "marks": 5,
             "md": "A **for loop** repeats a block of statements once for **each item** of a sequence (a `range()`, a string, a list, etc.).\n\n**Syntax:**\n\n```python\nfor variable in sequence:\n    statements\n```\n\n**Flow:** Python takes the first item and stores it in the loop variable, runs the indented block (one **iteration**), then takes the next item, and repeats until no items are left. Statements after the loop (not indented) run once.\n\n**Example 1: range()**\n\n```python\nfor hour in range(0, 24, 8):\n    print(f\"Dose at {hour}:00\")\n```\n\nOutput: `Dose at 0:00`, `Dose at 8:00`, `Dose at 16:00`.\n\n**Example 2: a list**\n\n```python\nfor drug in [\"Paracetamol\", \"Cetirizine\"]:\n    print(drug.upper())\n```\n\n**Program: sum of the first n natural numbers**\n\n```python\nn = int(input(\"Enter n: \"))\ntotal = 0\nfor i in range(1, n + 1):\n    total += i\nprint(\"Sum =\", total)\n```\n\nFor n = 10, the output is `Sum = 55`. `total` is an **accumulator**: it starts at 0 before the loop, and each iteration adds the current number."},
        ],
    },
    "mindmap": {
        "label": "Lesson 2.3 · for loops",
        "children": [
            {"label": "for loop", "children": [{"label": "Repeat for each value"}, {"label": "Loop variable"}, {"label": "Iteration = one run"}]},
            {"label": "range()", "children": [{"label": "range(5) → 0-4"}, {"label": "range(1, 6) → 1-5"}, {"label": "range(0, 24, 8) → step"}]},
            {"label": "Sequences", "children": [{"label": "Characters of a string"}, {"label": "Items of a list"}]},
            {"label": "Patterns", "children": [{"label": "total = 0 before"}, {"label": "total += value inside"}, {"label": "Count with an if"}]},
            {"label": "Syntax", "children": [{"label": "Colon :"}, {"label": "4-space block"}, {"label": "After loop runs once"}]},
            {"label": "Errors", "children": [{"label": "SyntaxError: expected ':'"}, {"label": "TypeError: str/float in range"}]},
        ],
    },
    "summary": [
        "A **for loop** runs its indented block once for **each value**; the **loop variable** holds the current value, and each run is an **iteration**.",
        "**range(stop)**, **range(start, stop)** and **range(start, stop, step)** make runs of whole numbers; the **stop is never included**.",
        "A for loop can also visit each **character of a string** or each **item of a list**.",
        "To add up, start `total = 0` **before** the loop and use `total += value` **inside** it.",
        "An **if inside a loop** picks out or counts the values that matter. Lines after the loop, with no indentation, run once.",
    ],
    "video": {"videoUrl": None, "searchTerms": ["python for loop range for beginners", "python for loop sum of numbers"]},
    "animations": [
        {
            "id": "loop",
            "title": "How a for loop goes round",
            "afterExplanation": 0,
            "canvas": {"desktop": {"w": 800, "h": 460}, "mobile": {"w": 360, "h": 600}},
            "actors": [
                {"id": "code", "type": "card", "title": "tablet_chart.py", "icon": "💊", "color": "indigo", "mono": True,
                 "lines": ["total = 0", "for day in range(1, 4):", "    total += 2", "    print(f\"Day {day}: 2 tablets\")", "print(\"Tablets needed:\", total)"],
                 "desktop": {"x": 40, "y": 40, "w": 440, "h": 220}, "mobile": {"x": 16, "y": 120, "w": 328, "h": 200}},
                {"id": "day", "type": "box", "label": "day", "value": "1", "color": "amber",
                 "desktop": {"x": 520, "y": 40, "w": 240, "h": 90}, "mobile": {"x": 16, "y": 12, "w": 156, "h": 96}},
                {"id": "total", "type": "box", "label": "total", "value": "0", "color": "emerald",
                 "desktop": {"x": 520, "y": 150, "w": 240, "h": 90}, "mobile": {"x": 188, "y": 12, "w": 156, "h": 96}},
                {"id": "out", "type": "terminal", "title": "Output",
                 "desktop": {"x": 40, "y": 280, "w": 720, "h": 150}, "mobile": {"x": 16, "y": 336, "w": 328, "h": 200}},
            ],
            "steps": [
                {"say": "total starts at zero. The loop will go round three times, for days one, two and three.", "audio": "anim-loop-01.mp3",
                 "actions": [{"do": "show", "target": "code"}, {"do": "show", "target": "total"}, {"do": "show", "target": "out"}, {"do": "highlightLine", "target": "code", "line": 0}]},
                {"say": "First time round, day is one. Two tablets are added, and day one is printed.", "audio": "anim-loop-02.mp3",
                 "actions": [{"do": "show", "target": "day"}, {"do": "highlightLine", "target": "code", "line": 3}, {"do": "setValue", "target": "total", "value": "2"}, {"do": "appendOutput", "target": "out", "text": "Day 1: 2 tablets"}]},
                {"say": "Back to the top. day is two, and total grows to four.", "audio": "anim-loop-03.mp3",
                 "actions": [{"do": "highlightLine", "target": "code", "line": 1}, {"do": "setValue", "target": "day", "value": "2"}, {"do": "setValue", "target": "total", "value": "4"}, {"do": "appendOutput", "target": "out", "text": "Day 2: 2 tablets"}]},
                {"say": "Once more: day three, total six.", "audio": "anim-loop-04.mp3",
                 "actions": [{"do": "setValue", "target": "day", "value": "3"}, {"do": "setValue", "target": "total", "value": "6"}, {"do": "appendOutput", "target": "out", "text": "Day 3: 2 tablets"}, {"do": "pulse", "target": "total"}]},
                {"say": "No numbers are left, so the loop ends, and the last line runs just once.", "audio": "anim-loop-05.mp3",
                 "actions": [{"do": "highlightLine", "target": "code", "line": 4}, {"do": "appendOutput", "target": "out", "text": "Tablets needed: 6"}]},
            ],
        }
    ],
}

if __name__ == "__main__":
    root = os.path.join(os.path.dirname(__file__), "..", "..")
    out = os.path.join(root, "content", "bp101t", "2-3", "en.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(L, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", out)
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "..", "glossary_bp101t.py")], check=True, stdout=subprocess.DEVNULL)

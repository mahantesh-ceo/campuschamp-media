"""Lesson 2.1 (English). Run to write content/bp101t/2-1/en.json."""
import json
import os
import subprocess
import sys

C_IF = "```python\ntemp = 38.6\nif temp >= 38.0:\n    print(\"Fever\")\nprint(\"Check done\")\n```"
C_ELSE = "```python\nstock = 12\nreorder_level = 20\nif stock < reorder_level:\n    print(\"Reorder now\")\nelse:\n    print(\"Stock OK\")\n```"
C_ELIF = "```python\nsystolic = 134\nif systolic < 120:\n    print(\"Normal\")\nelif systolic < 130:\n    print(\"Elevated\")\nelif systolic < 140:\n    print(\"High BP, stage 1\")\nelse:\n    print(\"High BP, stage 2\")\n```"
C_AND = "```python\nage = 70\nif age < 12 or age >= 65:\n    print(\"Extra care: check the dose\")\nelse:\n    print(\"Standard adult dose\")\n```"

L = {
    "id": "2-1",
    "course": "bp101t",
    "unit": "Unit II",
    "unitTitle": "Control Structures & Functions",
    "number": "2.1",
    "title": "if, if-else and if-elif-else",
    "minutes": 15,
    "free": False,
    "audioLanguages": ["en", "hi", "kn"],
    "hook": {
        "title": "Is it a fever?",
        "md": "A nurse reads a thermometer: **38.6 °C**. Is that a fever? A high fever? Or normal?\n\nA pharmacist makes decisions like this all day: is the stock low, is the dose too high, is the patient a child? Until now, your programs ran every line, top to bottom. In this lesson, your program will **decide** which lines to run.",
    },
    "learn": [
        "How **if** runs some lines only when a condition is **True**",
        "Why the **colon** and **indentation** matter in Python",
        "How **if-else** chooses between two paths",
        "How **if-elif-else** chooses one path out of many, and why the order matters",
    ],
    "explanation": [
        {
            "heading": "if: run some lines only when needed",
            "md": "An **if statement** asks a yes-or-no question. If the answer is `True`, Python runs the lines under it. If it is `False`, Python skips them.\n\n" + C_IF + "\n\nThis prints:\n\n```\nFever\nCheck done\n```\n\nThe question `temp >= 38.0` is called a **condition**. You met these comparison operators in Lesson 1.4: `==`, `!=`, `<`, `>`, `<=` and `>=`. Each one gives `True` or `False`.\n\nTry it with `temp = 37.0`. The condition is `False`, so `Fever` is skipped, and only `Check done` prints.",
            "callout": {"type": "definition", "title": "Condition", "md": "An expression that is either True or False, like temp >= 38.0. It decides whether the lines under if run."},
        },
        {
            "heading": "The colon and the indentation",
            "md": "Two small things tell Python what belongs to the `if`:\n\n1. A **colon** `:` at the end of the `if` line.\n2. **Indentation**: the lines that belong to the `if` start with **4 spaces**.\n\nThe indented lines are called a **block**. The block ends where the indentation ends. In the example above, `print(\"Fever\")` is inside the block, and `print(\"Check done\")` is outside it, so it always runs.\n\nMost IDEs add the 4 spaces for you when you press Enter after the colon.",
            "callout": {"type": "warning", "title": "Indentation is not decoration", "md": "In Python, spaces at the start of a line change what the program does. Use 4 spaces, and keep every line of a block lined up."},
        },
        {
            "heading": "if-else: one of two paths",
            "md": "Often you want something to happen in both cases. **else** gives the second path: it runs when the condition is `False`.\n\nA pharmacy reorders a medicine when its stock falls below the reorder level:\n\n" + C_ELSE + "\n\nThis prints `Reorder now`, because 12 is less than 20. With `stock = 35`, it would print `Stock OK`.\n\nExactly one of the two blocks runs, never both and never neither. `else` has no condition of its own; it ends with a colon too.",
        },
        {
            "heading": "if-elif-else: one of many paths",
            "md": "When there are more than two cases, use **elif**, short for \"else if\". Here is a simplified blood pressure check using the top number (systolic, in mmHg):\n\n" + C_ELIF + "\n\nThis prints `High BP, stage 1`.\n\nPython checks the conditions **from top to bottom** and runs the **first** block whose condition is `True`. Then it skips everything else in the chain. 134 is not below 120, not below 130, but it is below 140, so the third block runs.\n\nYou can have as many `elif` parts as you need. The `else` at the end is optional; it catches everything the conditions above did not.",
            "callout": {"type": "tip", "title": "The order matters", "md": "Because Python stops at the first True condition, check the narrowest case first. If systolic < 140 came first, 110 would also print stage 1."},
        },
        {
            "heading": "Combining conditions with and, or, not",
            "md": "The logical operators from Lesson 1.4 join conditions into one:\n\n- **`and`** is `True` only when **both** sides are `True`.\n- **`or`** is `True` when **at least one** side is `True`.\n- **`not`** flips `True` to `False` and back.\n\nChildren and older patients often need extra care with doses:\n\n" + C_AND + "\n\nThis prints `Extra care: check the dose`, because `age >= 65` is `True`, and `or` needs only one side to be `True`.",
        },
    ],
    "walkthrough": {
        "intro": "This program reads a body temperature and prints the right message. Only one of the three messages can print.",
        "filename": "fever_check.py",
        "code": "# Classify a body temperature\ntemp = 38.6\nif temp >= 39.5:\n    print(\"High fever: refer to a doctor\")\nelif temp >= 38.0:\n    print(\"Fever\")\nelse:\n    print(\"No fever\")\nprint(\"Temperature:\", temp, \"C\")",
        "output": "Fever\nTemperature: 38.6 C",
        "steps": [
            {"line": None, "say": "This program reads a temperature and decides which message to show. Only one of the three messages will print.", "output": None, "audio": "step-01.mp3"},
            {"line": 1, "say": "The comment says what the program does.", "output": None, "audio": "step-02.mp3"},
            {"line": 2, "say": "temp stores thirty-eight point six.", "output": None, "audio": "step-03.mp3", "vars": {"temp": "38.6"}},
            {"line": 3, "say": "The if asks: is temp at least thirty-nine point five? Thirty-eight point six is not, so the condition is False. Python skips the indented line under it.", "output": None, "audio": "step-04.mp3"},
            {"line": 5, "say": "Now elif asks the next question: is temp at least thirty-eight? Yes. This condition is True.", "output": None, "audio": "step-05.mp3"},
            {"line": 6, "say": "So Python runs the block under elif, and prints Fever.", "output": "Fever", "audio": "step-06.mp3"},
            {"line": 7, "say": "One block has already run, so Python skips else and the line under it.", "output": None, "audio": "step-07.mp3"},
            {"line": 9, "say": "The last line is not indented. It is outside the if chain, so it always runs.", "output": "Temperature: 38.6 C", "audio": "step-08.mp3"},
        ],
        "keyTerms": [
            {"term": "if", "meaning": "Run the block only when the condition is True."},
            {"term": "elif", "meaning": "\"Else if\": check another condition when the ones above were False."},
            {"term": "else", "meaning": "Run this block when no condition above was True."},
            {"term": ":", "meaning": "Ends every if, elif and else line."},
            {"term": "4 spaces", "meaning": "Mark the lines that belong to a block."},
        ],
    },
    "errors": {
        "intro": "Most if errors come from a missing colon or missing indentation.",
        "examples": [
            {
                "title": "Forgetting the colon",
                "code": "temp = 38.6\nif temp >= 38.0\n    print(\"Fever\")",
                "output": "SyntaxError: expected ':'",
                "errorLine": 2,
                "md": "Every `if`, `elif` and `else` line must end with a colon. Write `if temp >= 38.0:`.",
            },
            {
                "title": "Forgetting to indent the block",
                "code": "temp = 38.6\nif temp >= 38.0:\nprint(\"Fever\")",
                "output": "IndentationError: expected an indented block after 'if' statement on line 2",
                "errorLine": 3,
                "md": "Python needs at least one indented line after the colon. Add 4 spaces before `print(\"Fever\")`.",
            },
        ],
    },
    "mistakes": [
        {"mistake": "Using `=` instead of `==` in a condition, e.g. `if dose = 500:`", "see": "SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?", "fix": "`=` stores a value; `==` compares. Write `if dose == 500:`."},
        {"mistake": "Putting the wider condition first, e.g. `if temp >= 38.0` before `elif temp >= 39.5`", "see": "No error, but a high fever prints only \"Fever\"", "fix": "Check the narrowest case first: `temp >= 39.5`, then `temp >= 38.0`."},
        {"mistake": "Giving `else` a condition, e.g. `else temp < 38.0:`", "see": "SyntaxError: expected ':'", "fix": "`else` takes no condition. Use `elif temp < 38.0:` or just `else:`."},
        {"mistake": "Comparing text with different capitals, e.g. `if drug == \"aspirin\"` when drug is \"Aspirin\"", "see": "No error, but the condition is False", "fix": "Compare in one case: `if drug.lower() == \"aspirin\":`."},
    ],
    "tasks": [
        {
            "id": "t1",
            "title": "Reorder or not?",
            "md": "Stock below 10 strips means the pharmacy must reorder. Use **if-else** so the output is exactly:",
            "expectedOutput": "Reorder",
            "starterCode": "stock = 8\n# Print \"Reorder\" if stock is below 10, otherwise print \"In stock\"\n",
            "hints": ["Start with: if stock < 10:", "if stock < 10:\n    print(\"Reorder\")\nelse:\n    print(\"In stock\")"],
            "solution": "stock = 8\n# Print \"Reorder\" if stock is below 10, otherwise print \"In stock\"\nif stock < 10:\n    print(\"Reorder\")\nelse:\n    print(\"In stock\")",
            "check": {"type": "exactOutput", "mustContain": ["if", "else"]},
        },
        {
            "id": "t2",
            "title": "Check the dose limit",
            "md": "The prescribed single dose is higher than the limit. Print a warning with the dose, exactly:",
            "expectedOutput": "Too high: 1200 mg",
            "starterCode": "dose = 1200\nmax_dose = 1000\n# If dose is more than max_dose, print \"Too high: <dose> mg\". Otherwise print \"Dose OK\".\n",
            "hints": ["Compare with >: if dose > max_dose:", "Use an f-string: print(f\"Too high: {dose} mg\")"],
            "solution": "dose = 1200\nmax_dose = 1000\n# If dose is more than max_dose, print \"Too high: <dose> mg\". Otherwise print \"Dose OK\".\nif dose > max_dose:\n    print(f\"Too high: {dose} mg\")\nelse:\n    print(\"Dose OK\")",
            "check": {"type": "exactOutput", "mustContain": ["if"]},
        },
        {
            "id": "t3",
            "title": "Class of the result",
            "md": "Use **if-elif-else**: 75 or more is \"Distinction\", 60 or more is \"First class\", 50 or more is \"Second class\", and anything lower is \"Fail\". For 72 marks, the output must be exactly:",
            "expectedOutput": "First class",
            "starterCode": "marks = 72\n# Print the class of the result\n",
            "hints": ["Check the highest limit first: if marks >= 75:", "if marks >= 75:\n    print(\"Distinction\")\nelif marks >= 60:\n    print(\"First class\")\nelif marks >= 50:\n    print(\"Second class\")\nelse:\n    print(\"Fail\")"],
            "solution": "marks = 72\n# Print the class of the result\nif marks >= 75:\n    print(\"Distinction\")\nelif marks >= 60:\n    print(\"First class\")\nelif marks >= 50:\n    print(\"Second class\")\nelse:\n    print(\"Fail\")",
            "check": {"type": "exactOutput", "mustContain": ["elif"]},
        },
        {
            "id": "t4",
            "title": "Find the bug",
            "md": "A temperature of 40.1 should print \"High fever\", but this program prints \"Fever\". There is no error message. Fix it so the output is exactly:",
            "expectedOutput": "High fever",
            "starterCode": "temp = 40.1\nif temp >= 38.0:\n    print(\"Fever\")\nelif temp >= 39.5:\n    print(\"High fever\")\nelse:\n    print(\"No fever\")",
            "hints": ["Python runs the first block whose condition is True. Is 40.1 >= 38.0?", "Check temp >= 39.5 first, then temp >= 38.0."],
            "solution": "temp = 40.1\nif temp >= 39.5:\n    print(\"High fever\")\nelif temp >= 38.0:\n    print(\"Fever\")\nelse:\n    print(\"No fever\")",
            "solutionNote": "40.1 >= 38.0 is True, so the first block ran and the rest were skipped. Putting the narrower check (39.5) first fixes it.",
            "check": {"type": "exactOutput", "mustContain": ["elif"]},
        },
    ],
    "quiz": [
        {"q": "x = 5\nif x > 3:\n    print(\"A\")\nelse:\n    print(\"B\")\n\nWhat does this print?", "options": ["A", "B", "A and B", "Nothing"], "answer": 0, "why": "5 > 3 is True, so the if block runs and else is skipped.", "code": True},
        {"q": "What must come at the end of an if line?", "options": ["A semicolon ;", "A colon :", "A full stop .", "Nothing"], "answer": 1, "why": "if, elif and else lines all end with a colon.", "code": False},
        {"q": "In an if-elif-else chain, how many blocks run?", "options": ["All the True ones", "Exactly one", "At least two", "None"], "answer": 1, "why": "Python runs the first block whose condition is True (or else), then skips the rest.", "code": False},
        {"q": "temp = 37.0\nif temp >= 38.0:\n    print(\"Fever\")\nelse:\n    print(\"Normal\")\n\nWhat does this print?", "options": ["Fever", "Normal", "Fever Normal", "Error"], "answer": 1, "why": "37.0 >= 38.0 is False, so the else block runs.", "code": True},
        {"q": "What does elif mean?", "options": ["End if", "Else if", "Either if", "Exit if"], "answer": 1, "why": "elif is short for \"else if\": check another condition.", "code": False},
        {"q": "Which error do you get when the line after if: is not indented?", "options": ["SyntaxError: expected ':'", "IndentationError", "TypeError", "NameError"], "answer": 1, "why": "Python expects an indented block after the colon.", "code": False},
    ],
    "exam": {
        "note": "Important questions for practice. Actual university questions may differ.",
        "short": [
            {"q": "Write the syntax of the if-elif-else statement with an example.", "marks": 2,
             "md": "**Syntax:**\n\n```python\nif condition1:\n    block1\nelif condition2:\n    block2\nelse:\n    block3\n```\n\nPython checks the conditions from top to bottom and runs only the first block whose condition is True; else runs if none is True.\n\n**Example:**\n\n```python\nsystolic = 134\nif systolic < 120:\n    print(\"Normal\")\nelif systolic < 140:\n    print(\"High BP, stage 1\")\nelse:\n    print(\"High BP, stage 2\")\n```\n\nOutput: `High BP, stage 1`."},
            {"q": "What is indentation in Python? Why is it important?", "marks": 2,
             "md": "**Indentation** is the space at the start of a line. Python uses it to group statements into a **block**, for example the lines that belong to an `if`, `elif` or `else`. The standard is **4 spaces**.\n\nIt is important because, unlike languages that use braces `{ }`, Python decides which statements belong to a block only from the indentation. Missing or uneven indentation gives an **IndentationError**, or makes the program run the wrong lines."},
        ],
        "long": [
            {"q": "Explain the decision-making statements in Python (if, if-else and if-elif-else) with syntax, flow and examples.", "marks": 5,
             "md": "**Decision-making statements** let a program choose which statements to run, based on a **condition** (an expression that is True or False, usually built with comparison operators such as `>=` and logical operators such as `and`, `or`, `not`).\n\n**1. if statement:** runs a block only when the condition is True.\n\n```python\ntemp = 38.6\nif temp >= 38.0:\n    print(\"Fever\")\n```\n\nFlow: condition True → run block → continue; condition False → skip block.\n\n**2. if-else statement:** chooses between two blocks.\n\n```python\nstock = 12\nif stock < 20:\n    print(\"Reorder now\")\nelse:\n    print(\"Stock OK\")\n```\n\nExactly one of the two blocks runs.\n\n**3. if-elif-else ladder:** chooses one block out of many.\n\n```python\nsystolic = 134\nif systolic < 120:\n    print(\"Normal\")\nelif systolic < 130:\n    print(\"Elevated\")\nelif systolic < 140:\n    print(\"High BP, stage 1\")\nelse:\n    print(\"High BP, stage 2\")\n```\n\nOutput: `High BP, stage 1`. Conditions are checked from top to bottom; the first True one runs and the rest are skipped, so the order of conditions matters.\n\n**Rules:** each `if`, `elif` and `else` line ends with a colon; the block under it is indented (4 spaces); `else` has no condition and is optional."},
        ],
    },
    "mindmap": {
        "label": "Lesson 2.1 · if, if-else, if-elif-else",
        "children": [
            {"label": "Condition", "children": [{"label": "True or False"}, {"label": "== != < > <= >="}, {"label": "and / or / not"}]},
            {"label": "if", "children": [{"label": "Runs block when True"}, {"label": "Skips when False"}]},
            {"label": "if-else", "children": [{"label": "Two paths"}, {"label": "Exactly one runs"}]},
            {"label": "if-elif-else", "children": [{"label": "Many paths"}, {"label": "Top to bottom"}, {"label": "First True wins"}]},
            {"label": "Syntax", "children": [{"label": "Colon :"}, {"label": "4-space indent"}, {"label": "Block"}]},
            {"label": "Errors", "children": [{"label": "SyntaxError: expected ':'"}, {"label": "IndentationError"}]},
        ],
    },
    "summary": [
        "An **if statement** runs its block only when its **condition** is `True`.",
        "Every `if`, `elif` and `else` line ends with a **colon**, and the block under it is **indented with 4 spaces**.",
        "**if-else** chooses one of two paths; exactly one block runs.",
        "**if-elif-else** checks conditions **from top to bottom** and runs only the **first** `True` one, so put the narrowest check first.",
        "**and**, **or** and **not** combine several conditions into one.",
    ],
    "video": {"videoUrl": None, "searchTerms": ["python if elif else for beginners", "python indentation explained"]},
    "animations": [
        {
            "id": "branch",
            "title": "How Python picks one branch",
            "afterExplanation": 3,
            "canvas": {"desktop": {"w": 800, "h": 460}, "mobile": {"w": 360, "h": 600}},
            "actors": [
                {"id": "code", "type": "card", "title": "fever_check.py", "icon": "🌡️", "color": "indigo", "mono": True,
                 "lines": ["if temp >= 39.5:", "    print(\"High fever\")", "elif temp >= 38.0:", "    print(\"Fever\")", "else:", "    print(\"No fever\")"],
                 "desktop": {"x": 40, "y": 40, "w": 400, "h": 250}, "mobile": {"x": 16, "y": 120, "w": 328, "h": 230}},
                {"id": "temp", "type": "box", "label": "temp", "value": "38.6", "color": "amber",
                 "desktop": {"x": 500, "y": 40, "w": 240, "h": 100}, "mobile": {"x": 100, "y": 10, "w": 160, "h": 96}},
                {"id": "q1", "type": "pill", "text": "38.6 >= 39.5 → False", "color": "rose",
                 "desktop": {"x": 480, "y": 165, "w": 280, "h": 30}, "mobile": {"x": 40, "y": 362, "w": 280, "h": 30}},
                {"id": "q2", "type": "pill", "text": "38.6 >= 38.0 → True", "color": "emerald",
                 "desktop": {"x": 480, "y": 210, "w": 280, "h": 30}, "mobile": {"x": 40, "y": 400, "w": 280, "h": 30}},
                {"id": "out", "type": "terminal", "title": "Output",
                 "desktop": {"x": 40, "y": 320, "w": 720, "h": 110}, "mobile": {"x": 16, "y": 444, "w": 328, "h": 120}},
            ],
            "steps": [
                {"say": "Here is the temperature, thirty-eight point six, and a chain of three branches.", "audio": "anim-branch-01.mp3",
                 "actions": [{"do": "show", "target": "temp"}, {"do": "show", "target": "code"}, {"do": "show", "target": "out"}]},
                {"say": "Python asks the first question. Is it at least thirty-nine point five? No, so it skips this branch.", "audio": "anim-branch-02.mp3",
                 "actions": [{"do": "highlightLine", "target": "code", "line": 0}, {"do": "show", "target": "q1"}]},
                {"say": "It moves to elif. Is it at least thirty-eight? Yes.", "audio": "anim-branch-03.mp3",
                 "actions": [{"do": "highlightLine", "target": "code", "line": 2}, {"do": "show", "target": "q2"}, {"do": "pulse", "target": "q2"}]},
                {"say": "So it runs this block, and prints Fever.", "audio": "anim-branch-04.mp3",
                 "actions": [{"do": "highlightLine", "target": "code", "line": 3}, {"do": "appendOutput", "target": "out", "text": "Fever"}]},
                {"say": "One branch has run, so else is skipped. Only one branch ever runs.", "audio": "anim-branch-05.mp3",
                 "actions": [{"do": "highlightLine", "target": "code", "line": 4}]},
            ],
        }
    ],
}

if __name__ == "__main__":
    root = os.path.join(os.path.dirname(__file__), "..", "..")
    out = os.path.join(root, "content", "bp101t", "2-1", "en.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(L, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", out)
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "..", "glossary_bp101t.py")], check=True)

"""Lesson 1.7 (English). Run to write content/bp101t/1-7/en.json."""
import json
import os

L = {
    "id": "1-7",
    "course": "bp101t",
    "unit": "Unit I",
    "unitTitle": "Introduction to Python programming",
    "number": "1.7",
    "title": "Libraries and pip",
    "minutes": 15,
    "free": True,
    "audioLanguages": ["en", "hi", "kn"],
    "hook": {
        "title": "Don't make every tablet from scratch",
        "md": "A pharmacy doesn't manufacture every tablet it dispenses. It uses ready-made medicines from trusted makers.\n\nPython works the same way. Instead of writing every tool yourself, you use **libraries**: ready-made code written and tested by others. By the end of this lesson, you'll use Python's built-in libraries, and know how to install new ones with **pip**.",
    },
    "learn": [
        "What a **module** and a **library** are",
        "How to use the **standard library**, which comes with Python, such as **math**",
        "Three ways to **import**: `import math`, `from math import sqrt` and `import numpy as np`",
        "What **third-party** libraries are, and how to install and uninstall them with **pip**",
    ],
    "explanation": [
        {
            "heading": "Modules and libraries",
            "md": "A **module** is a Python file full of ready-made code, such as functions and values. A **library** is a collection of modules for one kind of job.\n\nTo use one, you **import** it at the top of your program:\n\n```python\nimport math\nprint(math.sqrt(49))\nprint(math.pi)\n```\n\nThis prints:\n\n```\n7.0\n3.141592653589793\n```\n\n`import math` brings in the **math** module. Then you use its tools with a dot: `math.sqrt()` finds a square root, and `math.pi` is the value of pi.",
            "callout": {"type": "definition", "title": "Library", "md": "Ready-made, tested code you can import into your program instead of writing it yourself."},
        },
        {
            "heading": "The standard library: already inside Python",
            "md": "Python comes with a large **standard library**. You don't install anything; you just import it. A few you'll meet in pharmacy work:\n\n- **math**: square roots, pi, rounding up and down\n- **statistics**: averages and spread of data\n- **random**: random numbers, for example to pick a sample\n- **datetime**: dates and times, such as expiry dates\n\nRounding up is common when dispensing. 45 tablets, 10 per strip:\n\n```python\nimport math\nprint(45 / 10)\nprint(math.ceil(45 / 10))\n```\n\nThis prints `4.5` and then `5`. You can't give half a strip, so `math.ceil()` rounds **up** to the next whole number. `math.floor()` rounds **down**.",
        },
        {
            "heading": "Three ways to import",
            "md": "**1. Import the whole module**, then use the module name with a dot:\n\n```python\nimport math\nprint(math.ceil(4.5))\n```\n\n**2. Import only what you need**, then use it without the dot:\n\n```python\nfrom math import sqrt\nprint(sqrt(81))\n```\n\n**3. Import with a short name** (an **alias**), using `as`:\n\n```python\nimport statistics as st\nprint(st.mean([250, 500, 375]))\n```\n\nThe three programs print `5`, `9.0` and `375`. Big libraries have standard aliases that everyone uses, like `import numpy as np` and `import pandas as pd`.",
            "callout": {"type": "tip", "title": "Imports go at the top", "md": "Put your import lines at the start of the program, so every line below can use them."},
        },
        {
            "heading": "Third-party libraries",
            "md": "**Third-party** libraries are written by people outside the Python team and shared for free on **PyPI**, the Python Package Index. Three of them are in your syllabus:\n\n- **NumPy**: fast calculations on lots of numbers (Unit IV)\n- **Pandas**: tables of data, like a spreadsheet of patient results (Unit IV)\n- **Matplotlib**: graphs, such as a drug concentration curve (Unit V)\n\nThese don't come with Python. You **install** them once on your computer, and then import them like any other library.\n\n**In Champ Lab:** NumPy, Pandas and Matplotlib are already installed, so you can import them straight away.",
        },
        {
            "heading": "Installing and uninstalling with pip",
            "md": "**pip** is Python's installer. It downloads a library from PyPI and sets it up. You type pip **commands** in the **terminal** (Command Prompt on Windows), not inside a Python program:\n\n```\npip install numpy\npip uninstall numpy\npip list\npip show numpy\npip install --upgrade numpy\n```\n\n- **`pip install`** downloads and installs a library.\n- **`pip uninstall`** removes it (type `y` to confirm).\n- **`pip list`** shows every library installed.\n- **`pip show`** shows details of one library, such as its version.\n- **`pip install --upgrade`** updates a library to its newest version.\n\nIn **Jupyter Notebook**, run it inside a cell with a percent sign: `%pip install numpy`.",
            "callout": {"type": "warning", "title": "pip is not Python code", "md": "Typing pip install numpy inside a .py file or at the >>> prompt gives a SyntaxError. Type it in the terminal."},
        },
    ],
    "walkthrough": {
        "intro": "A patient needs 45 tablets, and each strip has 10. This program works out how many strips the pharmacist should give.",
        "filename": "strips.py",
        "code": "# How many strips should the pharmacist give?\nimport math\ntablets_needed = 45\nper_strip = 10\nprint(\"Exact:\", tablets_needed / per_strip)\nprint(\"Strips:\", math.ceil(tablets_needed / per_strip))\nfrom math import sqrt\nprint(\"Square root of 81:\", sqrt(81))",
        "output": "Exact: 4.5\nStrips: 5\nSquare root of 81: 9.0",
        "steps": [
            {"line": None, "say": "This program uses Python's math library to work out how many strips to give.", "output": None, "audio": "step-01.mp3"},
            {"line": 1, "say": "The comment says what the program does.", "output": None, "audio": "step-02.mp3"},
            {"line": 2, "say": "import math brings in Python's math module. It comes with Python, so there's nothing to install.", "output": None, "audio": "step-03.mp3"},
            {"line": 3, "say": "The patient needs forty-five tablets.", "output": None, "audio": "step-04.mp3", "vars": {"tablets_needed": "45"}},
            {"line": 4, "say": "Each strip has ten tablets.", "output": None, "audio": "step-05.mp3", "vars": {"per_strip": "10"}},
            {"line": 5, "say": "Forty-five divided by ten is four point five. But you can't give half a strip.", "output": "Exact: 4.5", "audio": "step-06.mp3"},
            {"line": 6, "say": "math dot ceil rounds up to the next whole number. So the pharmacist gives five strips.", "output": "Strips: 5", "audio": "step-07.mp3"},
            {"line": 7, "say": "This line imports only the square root tool, so it can be used without writing math and a dot.", "output": None, "audio": "step-08.mp3"},
            {"line": 8, "say": "The square root of eighty-one is nine. Python shows it as nine point zero.", "output": "Square root of 81: 9.0", "audio": "step-09.mp3"},
        ],
        "keyTerms": [
            {"term": "import math", "meaning": "Bring in the math module; use its tools with math and a dot."},
            {"term": "math.ceil(x)", "meaning": "Round up to the next whole number."},
            {"term": "from math import sqrt", "meaning": "Bring in one tool, to use without the module name."},
            {"term": "pip install numpy", "meaning": "Install a library. Typed in the terminal, not in Python."},
        ],
    },
    "errors": {
        "intro": "These two errors happen when Python can't find a library, or can't find a tool inside it.",
        "examples": [
            {
                "title": "The library isn't installed, or its name is misspelt",
                "code": "import numpi",
                "output": "ModuleNotFoundError: No module named 'numpi'",
                "errorLine": 1,
                "md": "Python looked for a library called `numpi` and couldn't find one. Check the spelling (`numpy`). If the spelling is right, the library isn't installed yet: run `pip install numpy` in the terminal.",
            },
            {
                "title": "Using a tool without its module name",
                "code": "import math\nprint(sqrt(16))",
                "output": "NameError: name 'sqrt' is not defined",
                "errorLine": 2,
                "md": "`import math` brings in the module, so its tools need the module name: `math.sqrt(16)`. Or import the tool itself first: `from math import sqrt`.",
            },
        ],
    },
    "mistakes": [
        {"mistake": "Typing `pip install numpy` inside a Python program or at the `>>>` prompt", "see": "SyntaxError: invalid syntax", "fix": "Type it in the terminal. In Jupyter, use `%pip install numpy`."},
        {"mistake": "Using a module before importing it, e.g. `math.ceil(4.5)` with no import", "see": "NameError: name 'math' is not defined", "fix": "Add `import math` at the top."},
        {"mistake": "Importing with an alias, then using the full name, e.g. `import numpy as np` then `numpy.mean(...)`", "see": "NameError: name 'numpy' is not defined", "fix": "Use the alias: `np.mean(...)`."},
        {"mistake": "Saving your own file as `math.py` or `numpy.py`", "see": "Import errors, because Python imports your file instead of the library", "fix": "Rename your file, for example `strips.py`."},
    ],
    "tasks": [
        {
            "id": "t1",
            "title": "Round up the strips",
            "md": "A patient needs **23 tablets**, and each strip has **10**. Use **math.ceil()** to print the number of strips, exactly:",
            "expectedOutput": "Strips: 3",
            "starterCode": "import math\n# 23 tablets, 10 per strip\n",
            "hints": ["23 / 10 is 2.3. Round it up.", "print(\"Strips:\", math.ceil(23 / 10))"],
            "solution": "import math\n# 23 tablets, 10 per strip\nprint(\"Strips:\", math.ceil(23 / 10))",
            "check": {"type": "exactOutput", "mustContain": ["math.ceil("]},
        },
        {
            "id": "t2",
            "title": "Import just one tool",
            "md": "Import only **sqrt** from the math module, and print the square root of 144, exactly:",
            "expectedOutput": "12.0",
            "starterCode": "# Import sqrt from math, then print the square root of 144\n",
            "hints": ["The import line starts with from math import ...", "from math import sqrt, then print(sqrt(144))"],
            "solution": "# Import sqrt from math, then print the square root of 144\nfrom math import sqrt\nprint(sqrt(144))",
            "check": {"type": "exactOutput", "mustContain": ["from math import sqrt"]},
        },
        {
            "id": "t3",
            "title": "Use pi",
            "md": "A round tablet has a radius of **4 mm**. Its face area is pi × radius × radius. Use **math.pi** and an f-string with two decimal places to print exactly:",
            "expectedOutput": "Area: 50.27 sq mm",
            "starterCode": "import math\nradius_mm = 4\n# Print the area with two decimal places\n",
            "hints": ["The area is math.pi * radius_mm * radius_mm.", "print(f\"Area: {math.pi * radius_mm * radius_mm:.2f} sq mm\")"],
            "solution": "import math\nradius_mm = 4\n# Print the area with two decimal places\nprint(f\"Area: {math.pi * radius_mm * radius_mm:.2f} sq mm\")",
            "check": {"type": "exactOutput", "mustContain": ["math.pi"]},
        },
        {
            "id": "t4",
            "title": "Find the bug",
            "md": "This program should print the number of strips for 45 tablets, but it stops with a NameError. Fix it so the output is exactly:",
            "expectedOutput": "Strips: 5",
            "starterCode": "import math\nprint(\"Strips:\", ceil(45 / 10))",
            "hints": ["The program imported math, not ceil.", "Write math.ceil instead of ceil."],
            "solution": "import math\nprint(\"Strips:\", math.ceil(45 / 10))",
            "solutionNote": "import math brings in the module, so its tools need the module name and a dot: math.ceil.",
            "check": {"type": "exactOutput", "mustContain": ["math.ceil("]},
        },
    ],
    "quiz": [
        {"q": "Which command installs NumPy?", "options": ["import numpy", "pip install numpy", "install numpy", "python numpy"], "answer": 1, "why": "pip install downloads and installs a library. import only uses one that is already installed."},
        {"q": "Which of these comes with Python, with nothing to install?", "options": ["math", "numpy", "pandas", "matplotlib"], "answer": 0, "why": "math is part of the standard library. The others are third-party libraries."},
        {"q": "import math. What does print(math.ceil(4.1)) show?", "options": ["4", "5", "4.1", "Error"], "answer": 1, "why": "ceil rounds up to the next whole number.", "code": True},
        {"q": "After import numpy as np, how do you use NumPy?", "options": ["numpy.mean()", "np.mean()", "as.mean()", "import.mean()"], "answer": 1, "why": "The alias np replaces the name numpy.", "code": True},
        {"q": "Which command removes a library?", "options": ["pip delete", "pip remove", "pip uninstall", "pip clear"], "answer": 2, "why": "pip uninstall removes a library."},
        {"q": "Where do you type pip install numpy?", "options": ["In a terminal or command prompt", "Inside print()", "At the top of a .py file", "At the >>> prompt"], "answer": 0, "why": "pip is a command for the terminal, not Python code."},
    ],
    "exam": {
        "note": "Important questions for practice. Actual university questions may differ.",
        "short": [
            {"q": "What is pip? Write the commands to install and uninstall a library.", "marks": 2,
             "md": "**pip** is the package installer for Python. It downloads libraries from the Python Package Index (**PyPI**) and installs them. Commands are typed in the terminal / command prompt:\n- Install: `pip install numpy`\n- Uninstall: `pip uninstall numpy`\n- List installed libraries: `pip list`"},
            {"q": "Differentiate between the standard library and third-party libraries with examples.", "marks": 2,
             "md": "The **standard library** comes with Python and needs no installation; it is used directly with `import`. Examples: `math`, `statistics`, `random`, `datetime`.\n\n**Third-party libraries** are developed outside the core Python team, shared on PyPI, and must be installed with **pip** before use. Examples: `numpy`, `pandas`, `matplotlib`."},
        ],
        "long": [
            {"q": "Explain modules and libraries in Python. Describe the ways to import a library, and how libraries are installed and uninstalled using pip, with examples.", "marks": 5,
             "md": "**Module:** a Python file containing ready-made functions, variables and classes. **Library:** a collection of related modules. Libraries save time because tested code is reused instead of written again.\n\n**Types of libraries:**\n1. **Standard library:** comes with Python; no installation. Examples: `math`, `statistics`, `random`, `datetime`.\n2. **Third-party libraries:** shared on PyPI; installed with pip. Examples: `numpy` (numerical computing), `pandas` (data tables), `matplotlib` (graphs).\n\n**Ways to import:**\n1. `import math` and then `math.sqrt(49)` gives `7.0`.\n2. `from math import sqrt` and then `sqrt(81)` gives `9.0`.\n3. With an alias: `import numpy as np`, then `np.mean(...)`.\n\n**pip commands (typed in the terminal / command prompt):**\n- `pip install numpy`: installs a library.\n- `pip uninstall numpy`: removes a library.\n- `pip list`: lists installed libraries.\n- `pip show numpy`: shows details such as the version.\n- `pip install --upgrade numpy`: upgrades to the latest version.\n- In Jupyter Notebook: `%pip install numpy`.\n\n**Example program:**\n\n```python\nimport math\ntablets_needed = 45\nper_strip = 10\nprint(\"Strips:\", math.ceil(tablets_needed / per_strip))\n```\n\n**Output:**\n\n```\nStrips: 5\n```"},
        ],
    },
    "mindmap": {
        "label": "Lesson 1.7 · Libraries & pip",
        "children": [
            {"label": "Library", "children": [{"label": "Ready-made, tested code"}, {"label": "Module = one file"}]},
            {"label": "Standard", "children": [{"label": "math, statistics"}, {"label": "random, datetime"}, {"label": "Nothing to install"}]},
            {"label": "Third-party", "children": [{"label": "NumPy, Pandas, Matplotlib"}, {"label": "From PyPI"}]},
            {"label": "import", "children": [{"label": "import math"}, {"label": "from math import sqrt"}, {"label": "import numpy as np"}]},
            {"label": "pip (terminal)", "children": [{"label": "pip install"}, {"label": "pip uninstall"}, {"label": "pip list / show"}]},
            {"label": "Errors", "children": [{"label": "ModuleNotFoundError"}, {"label": "NameError: sqrt"}]},
        ],
    },
    "summary": [
        "A **library** is ready-made, tested code; a **module** is one file of it. You bring it in with **import**.",
        "The **standard library** comes with Python, such as **math**: `math.ceil()` rounds up, `math.sqrt()` finds a square root.",
        "Import a whole module (`import math`), one tool (`from math import sqrt`), or use a short **alias** (`import numpy as np`).",
        "**Third-party** libraries such as **NumPy**, **Pandas** and **Matplotlib** come from **PyPI** and are installed with **pip**.",
        "**pip install**, **pip uninstall**, **pip list** and **pip show** are typed in the **terminal**, not inside Python.",
    ],
    "video": {"videoUrl": None, "searchTerms": ["python modules and import for beginners", "how to use pip install python"]},
    "animations": [
        {
            "id": "pip",
            "title": "From PyPI to your program",
            "afterExplanation": 4,
            "canvas": {"desktop": {"w": 800, "h": 460}, "mobile": {"w": 360, "h": 600}},
            "actors": [
                {"id": "term", "type": "terminal", "title": "Terminal",
                 "desktop": {"x": 40, "y": 30, "w": 730, "h": 120}, "mobile": {"x": 16, "y": 16, "w": 328, "h": 140}},
                {"id": "pypi", "type": "box", "label": "PyPI (online)", "value": "numpy", "color": "amber",
                 "desktop": {"x": 80, "y": 200, "w": 240, "h": 110}, "mobile": {"x": 16, "y": 190, "w": 156, "h": 100}},
                {"id": "pc", "type": "box", "label": "Your computer", "value": "not installed", "color": "emerald",
                 "desktop": {"x": 480, "y": 200, "w": 240, "h": 110}, "mobile": {"x": 188, "y": 190, "w": 156, "h": 100}},
                {"id": "t_dl", "type": "text", "text": "pip downloads and installs", "size": 18,
                 "desktop": {"x": 200, "y": 330, "w": 400, "h": 28}, "mobile": {"x": 16, "y": 310, "w": 328, "h": 26}},
            ],
            "steps": [
                {"say": "In the terminal, the student types: pip install numpy.", "audio": "anim-pip-01.mp3",
                 "actions": [{"do": "show", "target": "term"}, {"do": "appendOutput", "target": "term", "text": "pip install numpy"}]},
                {"say": "pip finds NumPy on PyPI, the online library of Python packages.", "audio": "anim-pip-02.mp3",
                 "actions": [{"do": "show", "target": "pypi"}, {"do": "pulse", "target": "pypi"}]},
                {"say": "It downloads NumPy and installs it on the computer.", "audio": "anim-pip-03.mp3",
                 "actions": [{"do": "show", "target": "pc"}, {"do": "show", "target": "t_dl"}, {"do": "setValue", "target": "pc", "value": "numpy installed"}, {"do": "pulse", "target": "pc"}]},
                {"say": "Now any program on this computer can use it, with import numpy as np.", "audio": "anim-pip-04.mp3",
                 "actions": [{"do": "appendOutput", "target": "term", "text": "Successfully installed numpy"}]},
                {"say": "And pip uninstall numpy removes it again.", "audio": "anim-pip-05.mp3",
                 "actions": [{"do": "appendOutput", "target": "term", "text": "pip uninstall numpy"}, {"do": "setValue", "target": "pc", "value": "not installed"}]},
            ],
        }
    ],
}

if __name__ == "__main__":
    root = os.path.join(os.path.dirname(__file__), "..", "..")
    out = os.path.join(root, "content", "bp101t", "1-7", "en.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(L, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", out)
    # keep the "Words to know" section after regenerating
    import subprocess, sys
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "..", "glossary_bp101t.py")], check=True)
